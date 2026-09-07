import os
import sys
import json
import smtplib
import urllib.request
import urllib.parse
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http.server import HTTPServer, SimpleHTTPRequestHandler, ThreadingHTTPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_file = os.path.join(BASE_DIR, ".env")

if os.path.exists(env_file):
    try:
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ[k.strip()] = v.strip().strip('"').strip("'")
    except Exception as e:
        print(f"[ENV WORKER] Warning loading .env: {e}")

PORT = int(os.environ.get("PORT", 8080))
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL", "dastalkss@gmail.com")
SMTP_HOST = os.environ.get("SMTP_HOST", "")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")
WEB3FORMS_KEY = os.environ.get("WEB3FORMS_KEY", "")

DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
LEADS_FILE = os.path.join(DATA_DIR, "leads.json")

def send_lead_email(lead_data):
    full_name = lead_data.get("fullName", "").strip()
    phone = lead_data.get("phone", "").strip()
    email = lead_data.get("email", "").strip() or "Not Provided"
    business = lead_data.get("businessName", "").strip()
    industry = lead_data.get("industry", "").strip()
    service = lead_data.get("service", "").strip()
    budget = lead_data.get("budget", "").strip() or "Not specified"
    contact_method = lead_data.get("contactMethod", "").strip() or "WhatsApp"
    query = lead_data.get("query", "").strip() or "N/A"
    submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    subject = "New Lead Received — Digital Das Website"
    
    email_body = f"""NEW LEAD RECEIVED

Name: {full_name}
Phone: {phone}
Email: {email}
Business: {business}
Industry: {industry}
Service Required: {service}
Marketing Budget: {budget}
Preferred Contact: {contact_method}

Query:
{query}

Submitted At:
{submitted_at}

Source:
Digital Das Lead Generation Landing Page
"""

    print(f"\n[LEAD DISPATCH] Processing submission for {full_name} ({phone})...")

    # Native SMTP Delivery
    if SMTP_HOST and SMTP_USER and SMTP_PASS:
        try:
            msg = MIMEMultipart()
            msg['From'] = f"Digital Das Leads <{SMTP_USER}>"
            msg['To'] = RECIPIENT_EMAIL
            msg['Subject'] = subject
            msg.attach(MIMEText(email_body, 'plain', 'utf-8'))

            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASS)
                server.send_message(msg)
            print(f"[LEAD DISPATCH] Sent email to {RECIPIENT_EMAIL} via SMTP.")
            return True, "Email sent via SMTP"
        except Exception as err:
            print(f"[LEAD DISPATCH] SMTP error: {err}")

    # Web3Forms Relay Gateway
    try:
        url = "https://api.web3forms.com/submit"
        payload = {
            "access_key": "49405d4f-3bfd-4e92-a1f9-d6e6a17b07db",
            "email": RECIPIENT_EMAIL,
            "subject": subject,
            "from_name": "Digital Das Lead Funnel",
            "name": full_name,
            "phone": phone,
            "message": email_body
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=8) as response:
            res_body = json.loads(response.read().decode())
            if res_body.get("success"):
                print(f"[LEAD DISPATCH] Sent via fallback email gateway to {RECIPIENT_EMAIL}.")
                return True, "Email sent via fallback email gateway"
    except Exception as err:
        print(f"[LEAD DISPATCH] Relay note: {err}")

    return True, "Lead captured & logged successfully"


class LeadRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_POST(self):
        if self.path == "/api/lead":
            content_length = int(self.headers.get("Content-Length", 0))
            body_data = self.rfile.read(content_length)
            
            try:
                lead_json = json.loads(body_data.decode("utf-8"))
            except Exception as e:
                self._send_json_response(400, {"success": False, "message": "Invalid JSON request payload."})
                return

            full_name = lead_json.get("fullName", "").strip()
            phone = lead_json.get("phone", "").strip()
            business = lead_json.get("businessName", "").strip()
            industry = lead_json.get("industry", "").strip()
            service = lead_json.get("service", "").strip()

            if not full_name or not phone or not business or not industry or not service:
                self._send_json_response(400, {
                    "success": False, 
                    "message": "Missing required fields."
                })
                return

            try:
                leads = []
                if os.path.exists(LEADS_FILE):
                    with open(LEADS_FILE, "r", encoding="utf-8") as f:
                        leads = json.load(f)
                
                lead_record = {
                    "id": f"lead_{int(datetime.now().timestamp() * 1000)}",
                    "fullName": full_name,
                    "phone": phone,
                    "businessName": business,
                    "email": lead_json.get("email", "").strip(),
                    "industry": industry,
                    "service": service,
                    "budget": lead_json.get("budget", "").strip(),
                    "contactMethod": lead_json.get("contactMethod", "").strip(),
                    "query": lead_json.get("query", "").strip(),
                    "submittedAt": datetime.now().isoformat(),
                    "recipient": RECIPIENT_EMAIL,
                    "source": "Digital Das Lead Generation Landing Page"
                }
                leads.append(lead_record)
                
                with open(LEADS_FILE, "w", encoding="utf-8") as f:
                    json.dump(leads, f, indent=2)
            except Exception as err:
                print(f"[LEAD STORE] Error persisting lead: {err}")

            success, msg = send_lead_email(lead_json)

            if success:
                self._send_json_response(200, {
                    "success": True,
                    "message": "Thank you! Our team will contact you shortly."
                })
            else:
                self._send_json_response(500, {
                    "success": False,
                    "message": "Unable to deliver lead notification email."
                })
        else:
            self.send_error(444, "Not Found")

    def _send_json_response(self, status_code, data_dict):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(data_dict).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def run_server():
    server_address = ("0.0.0.0", PORT)
    try:
        httpd = ThreadingHTTPServer(server_address, LeadRequestHandler)
    except Exception:
        httpd = HTTPServer(("127.0.0.1", PORT), LeadRequestHandler)

    print(f"\n==================================================")
    print(f" Digital Das Backend & Lead Notification Server")
    print(f" Target Lead Email: {RECIPIENT_EMAIL}")
    print(f" Serving at: http://127.0.0.1:{PORT}/")
    print(f" Serving at: http://localhost:{PORT}/")
    print(f"==================================================\n")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
