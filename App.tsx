import React from 'react';
import { Header } from './components/Header';
import { Hero } from './components/Hero';
import { TrustProof } from './components/TrustProof';
import { PainPoints } from './components/PainPoints';
import { Services } from './components/Services';
import { WhyDigitalDas } from './components/WhyDigitalDas';
import { CaseStudies } from './components/CaseStudies';
import { Testimonials } from './components/Testimonials';
import { CampaignProof } from './components/CampaignProof';
import { WorkProcess } from './components/WorkProcess';
import { Industries } from './components/Industries';
import { LeadForm } from './components/LeadForm';
import { FinalCTA } from './components/FinalCTA';
import { Footer } from './components/Footer';
import { StickyMobileCTA } from './components/StickyMobileCTA';

export const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans text-slate-900 selection:bg-das-orange selection:text-white pb-14 sm:pb-0">
      
      {/* 1. Mobile-First Header */}
      <Header />

      {/* Main Content Sections */}
      <main className="flex-grow">
        {/* 2. Hero Section */}
        <Hero />

        {/* 3. Trust & Proof Bar */}
        <TrustProof />

        {/* 4. Problem / Pain Points */}
        <PainPoints />

        {/* 5. Services */}
        <Services />

        {/* 6. Why Digital Das */}
        <WhyDigitalDas />

        {/* 7. Work / Case Studies */}
        <CaseStudies />

        {/* 8. Client Testimonial Video Section */}
        <Testimonials />

        {/* 9. Campaign Performance Screenshots */}
        <CampaignProof />

        {/* 10. 4-Step Work Process */}
        <WorkProcess />

        {/* 11. Target Industries */}
        <Industries />

        {/* 12. Lead Generation Form */}
        <LeadForm />

        {/* 13. Final CTA */}
        <FinalCTA />
      </main>

      {/* 14. Footer */}
      <Footer />

      {/* Sticky Mobile Bar */}
      <StickyMobileCTA />

    </div>
  );
};

export default App;
