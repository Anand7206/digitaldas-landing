/**
 * Digital Das Lead Generation Landing Page Engine
 * Handles Video Lightbox, Extensible Testimonials Data, Lead Form Validation & Pixel Event Hooks
 * Real-Time Lead Email Submission to dastalkss@gmail.com
 * Meta Pixel Integration & Thank You Page Redirection
 */

// ==========================================
// 1. EXTENSIBLE TESTIMONIAL VIDEO DATA STRUCTURE
// ==========================================
const testimonialVideos = [
  {
    id: "v1",
    clientName: "Rahul Verma",
    companyName: "Shivaay Properties",
    designation: "Managing Director",
    title: "Revolutionized Our Real Estate Lead Pipeline & Website Conversion",
    videoUrl: "https://lightslategray-marten-148391.hostingersite.com/wp-content/uploads/2025/08/Nothing-makes-us-prouder-than-happy-clients-Thank-you-for-sharing-your-journey-with-us-%E2%9D%A4%EF%B8%8F-1.mp4",
    thumbnailUrl: "https://digitaldas.in/wp-content/uploads/2025/11/1st-reel.jpg",
    result: "3.2X Increase in High-Intent Buyer Enquiries",
    tags: ["Real Estate", "Meta Ads", "Website Revamp"]
  },
  {
    id: "v2",
    clientName: "Priya Sharma",
    companyName: "Pick N Play",
    designation: "Founder & CEO",
    title: "Seamless Social Media Marketing & High ROI Performance Campaigns",
    videoUrl: "https://lightslategray-marten-148391.hostingersite.com/wp-content/uploads/2025/08/When-clients-speak-the-world-listens-%F0%9F%8E%AFGrateful-for-the-kind-words-%E2%80%94-your-trust-keeps-us-going-1.mp4",
    thumbnailUrl: "https://digitaldas.in/wp-content/uploads/2025/11/2nd-reel.jpg",
    result: "Scalable Growth & 45% Lower Customer Acquisition Cost",
    tags: ["E-Commerce", "Performance Ads", "Branding"]
  },
  {
    id: "v3",
    clientName: "Vikram Singh",
    companyName: "Rakshak Security",
    designation: "Head of Operations",
    title: "Stunning Digital Presence & Consistent B2B Enterprise Inquiries",
    videoUrl: "https://lightslategray-marten-148391.hostingersite.com/wp-content/uploads/2025/08/Honest-reviews-happy-clients-Your-feedback-helps-us-grow-and-serve-you-better-%F0%9F%8C%9F.-1-1.mp4",
    thumbnailUrl: "https://digitaldas.in/wp-content/uploads/2025/11/3rd-reel.jpg",
    result: "Expanded Corporate Footprint across North India",
    tags: ["B2B Services", "Google Ads", "SEO"]
  },
  {
    id: "v4",
    clientName: "Ankit Gupta",
    companyName: "Growth Partner",
    designation: "Co-Founder",
    title: "Transparent Reporting & High-Converting Paid Funnel Architecture",
    videoUrl: "https://digitaldas.in/wp-content/uploads/2025/10/Video-625.mp4",
    thumbnailUrl: "https://digitaldas.in/wp-content/uploads/2025/11/4th-reel.jpg",
    result: "40% Higher Conversion Rate on Paid Search Traffic",
    tags: ["Google Ads", "Conversion Optimization"]
  }
];

// ==========================================
// 2. TRACKING-READY EVENT HOOKS SYSTEM
// ==========================================
function trackEvent(eventName, payload = {}) {
  const timestamp = new Date().toISOString();
  const eventData = { eventName, timestamp, ...payload };
  
  console.log(`[Tracking Hook] ${eventName}:`, eventData);

  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push(eventData);
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
  renderTestimonialVideos();
  setupMobileMenu();
  setupFormHandlers();
  setupTrackingHooks();
});

// ==========================================
// 4. RENDER VIDEO TESTIMONIALS DYNAMICALLY
// ==========================================
function renderTestimonialVideos() {
  const container = document.getElementById('testimonial-video-grid');
  if (!container) return;

  container.innerHTML = testimonialVideos.map((video) => `
    <div class="glass-card rounded-2xl overflow-hidden flex flex-col h-full group hover:border-amber-500/50 transition-all duration-300">
      <!-- Thumbnail & Play Button Overlay -->
      <div class="relative aspect-video w-full overflow-hidden bg-slate-900 cursor-pointer video-card-thumb" onclick="openVideoModal('${video.videoUrl}', '${encodeURIComponent(video.title)}', '${video.clientName}')">
        <img 
          src="${video.thumbnailUrl}" 
          alt="${video.clientName} Testimonial - ${video.companyName}"
          loading="lazy" 
          class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 opacity-90 group-hover:opacity-100"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/20 to-transparent flex items-center justify-center">
          <div class="w-16 h-16 rounded-full bg-amber-500 text-slate-950 flex items-center justify-center shadow-lg shadow-amber-500/30 play-btn-circle transition-all duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 ml-1" fill="currentColor" viewBox="0 0 24 24">
              <path d="M8 5v14l11-7z"/>
            </svg>
          </div>
        </div>
        <span class="absolute top-3 left-3 bg-slate-900/80 backdrop-blur-md border border-amber-500/30 text-amber-400 text-xs font-semibold px-3 py-1 rounded-full">
          🎥 Success Story
        </span>
      </div>

      <!-- Content -->
      <div class="p-6 flex flex-col flex-grow justify-between">
        <div>
          <h4 class="text-lg font-bold text-white mb-2 line-clamp-2 group-hover:text-amber-400 transition-colors">
            "${video.title}"
          </h4>
          ${video.result ? `
            <p class="text-xs font-semibold text-emerald-400 bg-emerald-950/50 border border-emerald-800/40 rounded-lg px-3 py-1.5 inline-block mb-4">
              ✓ ${video.result}
            </p>
          ` : ''}
        </div>

        <div class="pt-4 border-t border-slate-800/80 flex items-center justify-between">
          <div>
            <h5 class="font-bold text-white text-sm">${video.clientName}</h5>
            <p class="text-xs text-amber-500 font-medium">${video.companyName} <span class="text-slate-400">(${video.designation})</span></p>
          </div>
          <button 
            onclick="openVideoModal('${video.videoUrl}', '${encodeURIComponent(video.title)}', '${video.clientName}')"
            class="text-xs font-bold text-amber-400 hover:text-amber-300 flex items-center gap-1 group-hover:translate-x-1 transition-transform"
          >
            Watch <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
          </button>
        </div>
      </div>
    </div>
  `).join('');
}

// ==========================================
// 5. VIDEO LIGHTBOX MODAL HANDLER
// ==========================================
function openVideoModal(videoUrl, titleEncoded, clientName) {
  const modal = document.getElementById('videoModal');
  const videoPlayer = document.getElementById('modalVideoPlayer');
  const modalTitle = document.getElementById('modalVideoTitle');
  const modalSubtitle = document.getElementById('modalVideoSubtitle');

  if (!modal || !videoPlayer) return;

  const title = decodeURIComponent(titleEncoded);
  modalTitle.textContent = title;
  modalSubtitle.textContent = `Client Testimonial: ${clientName}`;
  
  videoPlayer.src = videoUrl;
  modal.classList.remove('hidden');
  modal.classList.add('flex');
  document.body.style.overflow = 'hidden';

  videoPlayer.play().catch(e => console.log('Autoplay blocked or user gesture required:', e));

  trackEvent('testimonial_video_play', { clientName, videoUrl });
}

function closeVideoModal() {
  const modal = document.getElementById('videoModal');
  const videoPlayer = document.getElementById('modalVideoPlayer');

  if (!modal || !videoPlayer) return;

  videoPlayer.pause();
  videoPlayer.src = "";
  modal.classList.add('hidden');
  modal.classList.remove('flex');
  document.body.style.overflow = 'auto';
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeVideoModal();
});

// ==========================================
// 6. SERVICE SELECT & SCROLL HANDLER
// ==========================================
function selectServiceAndScroll(serviceName) {
  const serviceSelect = document.getElementById('formService');
  const leadSection = document.getElementById('lead-form');

  if (serviceSelect && serviceName) {
    for (let i = 0; i < serviceSelect.options.length; i++) {
      if (serviceSelect.options[i].value.toLowerCase().includes(serviceName.toLowerCase()) || 
          serviceName.toLowerCase().includes(serviceSelect.options[i].value.toLowerCase())) {
        serviceSelect.selectedIndex = i;
        break;
      }
    }
  }

  if (leadSection) {
    leadSection.scrollIntoView({ behavior: 'smooth' });
  }

  trackEvent('case_study_click', { serviceRequested: serviceName });
}

// ==========================================
// 7. LEAD FORM SUBMISSION & THANK-YOU REDIRECT
// ==========================================
function setupFormHandlers() {
  const form = document.getElementById('leadForm');
  const errorAlert = document.getElementById('formErrorAlert');
  const errorText = document.getElementById('formErrorText');
  const submitBtn = document.getElementById('leadSubmitBtn');
  const submitBtnText = document.getElementById('leadSubmitBtnText');
  const submitBtnSpinner = document.getElementById('leadSubmitBtnSpinner');

  if (!form) return;

  let formStarted = false;
  let isSubmitting = false;

  form.querySelectorAll('input, select, textarea').forEach(input => {
    input.addEventListener('focus', () => {
      if (!formStarted) {
        formStarted = true;
        trackEvent('lead_form_start');
      }
    });
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (isSubmitting) return;

    if (errorAlert) errorAlert.classList.add('hidden');

    const fullName = document.getElementById('fullName').value.trim();
    const phone = document.getElementById('phoneNumber').value.trim();
    const businessName = document.getElementById('businessName').value.trim();
    const email = document.getElementById('emailAddress').value.trim();
    const industry = document.getElementById('industry').value.trim();
    const service = document.getElementById('formService').value;
    const budget = document.getElementById('marketingBudget').value;
    const contactMethod = document.querySelector('input[name="contactMethod"]:checked')?.value || 'WhatsApp';
    const query = document.getElementById('userQuery')?.value.trim() || '';

    if (!fullName || !phone || !businessName || !industry || !service) {
      showError('Please complete all required fields marked with *');
      return;
    }

    const phoneClean = phone.replace(/[^0-9+]/g, '');
    if (phoneClean.length < 8) {
      showError('Please enter a valid phone or WhatsApp number.');
      return;
    }

    isSubmitting = true;
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.classList.add('opacity-75', 'cursor-not-allowed');
    }
    if (submitBtnText) submitBtnText.textContent = "Submitting Strategy Call Request...";
    if (submitBtnSpinner) submitBtnSpinner.classList.remove('hidden');

    const leadPayload = {
      fullName,
      phone,
      businessName,
      email,
      industry,
      service,
      budget,
      contactMethod,
      query,
      recipient: "dastalkss@gmail.com"
    };

    try {
      let isSuccess = false;

      // Method 1: Local backend API endpoint (/api/lead)
      if (window.location.protocol.startsWith('http')) {
        try {
          const response = await fetch('/api/lead', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(leadPayload)
          });
          const result = await response.json();
          if (response.ok && result.success) {
            isSuccess = true;
          }
        } catch (apiErr) {
          console.warn('[Local API Note]:', apiErr);
        }
      }

      // Method 2: Direct Web3Forms Secure Gateway fallback to dastalkss@gmail.com
      if (!isSuccess) {
        const formattedMessage = `NEW LEAD RECEIVED\n\nName: ${fullName}\nPhone: ${phone}\nEmail: ${email || 'Not Provided'}\nBusiness: ${businessName}\nIndustry: ${industry}\nService Required: ${service}\nMarketing Budget: ${budget}\nPreferred Contact: ${contactMethod}\n\nQuery:\n${query || 'N/A'}\n\nSubmitted At:\n${new Date().toLocaleString()}\n\nSource:\nDigital Das Lead Generation Landing Page`;

        const res = await fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            access_key: '49405d4f-3bfd-4e92-a1f9-d6e6a17b07db',
            email: 'dastalkss@gmail.com',
            subject: 'New Lead Received — Digital Das Website',
            from_name: 'Digital Das Lead Funnel',
            name: fullName,
            phone: phone,
            message: formattedMessage
          })
        });

        const resData = await res.json();
        if (resData.success) {
          isSuccess = true;
        }
      }

      if (isSuccess) {
        trackEvent('lead_form_submit', leadPayload);
        form.reset();
        // Redirect to Thank-You Page (Single source of truth for form Contact conversion)
        window.location.href = 'thank-you.html';
      } else {
        throw new Error('Email delivery failed. Please check your internet connection or contact us via WhatsApp.');
      }

    } catch (err) {
      console.error('[Lead Form Error]:', err);
      showError(err.message || 'Submission could not be delivered. Please check your connection or contact us via WhatsApp.');
    } finally {
      isSubmitting = false;
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.classList.remove('opacity-75', 'cursor-not-allowed');
      }
      if (submitBtnText) submitBtnText.textContent = "GET MY FREE STRATEGY CALL";
      if (submitBtnSpinner) submitBtnSpinner.classList.add('hidden');
    }
  });

  function showError(msg) {
    if (errorText) errorText.textContent = msg;
    if (errorAlert) errorAlert.classList.remove('hidden');
  }
}

// ==========================================
// 8. MOBILE MENU & GLOBAL CLICK TRACKERS
// ==========================================
function setupMobileMenu() {
  const menuBtn = document.getElementById('mobileMenuBtn');
  const menuDrawer = document.getElementById('mobileMenuDrawer');
  const menuClose = document.getElementById('mobileMenuClose');

  if (menuBtn && menuDrawer) {
    menuBtn.addEventListener('click', () => {
      menuDrawer.classList.remove('translate-x-full');
    });
  }

  if (menuClose && menuDrawer) {
    menuClose.addEventListener('click', () => {
      menuDrawer.classList.add('translate-x-full');
    });
  }
}

function closeMobileMenu() {
  const menuDrawer = document.getElementById('mobileMenuDrawer');
  if (menuDrawer) {
    menuDrawer.classList.add('translate-x-full');
  }
}

function setupTrackingHooks() {
  document.querySelectorAll('[data-track]').forEach(el => {
    el.addEventListener('click', () => {
      const eventName = el.getAttribute('data-track');
      const label = el.getAttribute('data-track-label') || el.innerText.trim();
      trackEvent(eventName, { label });
    });
  });
}
