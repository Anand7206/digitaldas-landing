export interface TestimonialItem {
  id: string;
  videoUrl: string;
  thumbnailUrl: string;
  clientName: string;
  companyName: string;
  designation: string;
}

export interface CampaignItem {
  id: string;
  imageUrl: string;
  title: string;
  platform: 'Meta Ads' | 'Google Ads' | 'SEO' | 'Performance Marketing' | 'Analytics';
  description: string;
}

export interface CaseStudyItem {
  id: string;
  clientName: string;
  serviceProvided: string;
  description: string;
  logoUrl?: string;
  badge?: string;
}

export interface LeadFormData {
  fullName: string;
  phone: string;
  businessName: string;
  email: string;
  industry: string;
  serviceNeeded: string;
  budget: string;
  preferredContact: string;
}
