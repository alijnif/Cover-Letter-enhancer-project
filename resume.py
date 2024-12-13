from dotenv import load_dotenv
import os
import openai

# Load environment variables from the .env file
load_dotenv()

# Load API KEY from .env file
api_key = os.getenv("OPENAI_API_KEY")

# prompt (assuming that you entered below your resume and job desciption)
prompt = f"""
I am looking for an application mentioning one of the following titles: "Business Analyst Salesforce or CRM, CRM Project Manager, CRM Product Owner, CRM Consultant."
Below, I have included the details of the job offer as well as my CV, and I would like you to analyze how my experience and skills align with the requirements of the position, as well as what I need to demonstrate during interviews to prove my ability to fulfill this role.
Please identify the key qualifications and responsibilities in the job description and assess how my background supports them. Highlight the specific skills, achievements, or experiences from my CV that are most relevant to the role.
Also, write me a concise cover letter (maximum 30 lines) to support my application for this position, considering that my name is "Add your name here".
---


### Here is the job description to analyze and identify all relevant requirements and skills for the application:
Job Title: Senior Salesforce Consultant – Digital Transformation Specialist
Company Name: Fiction Solutions
Location: Paris, France (Hybrid)
Type: Full-Time

About Us
Fiction Solutions is a boutique consultancy specializing in Salesforce implementation, CRM optimization, and digital transformation for enterprises in healthcare, insurance, and hospitality sectors. With a focus on delivering value-driven solutions, we empower businesses to enhance customer experiences and streamline operations through innovative technology and tailored strategies.

At Fiction Solutions, we pride ourselves on fostering a collaborative environment where expertise, passion, and ambition drive exceptional results.

About the Role
As a Senior Salesforce Consultant at Fiction Solutions, you will play a pivotal role in designing and delivering Salesforce solutions across diverse industries. You will work closely with clients to understand their business needs, lead implementation projects, and drive digital transformation strategies.

Responsibilities

Discovery & Requirements Gathering:

Lead discovery workshops to identify client needs, define business processes, and gather technical and functional requirements.
Salesforce Implementation & Customization:

Design, configure, and deploy Salesforce solutions, ensuring alignment with client objectives.
Oversee CRM deployments across multiple countries and business units, adapting to localized requirements.
Project Management & Agile Delivery:

Manage end-to-end project lifecycles, including sprint planning, task delegation, and progress tracking.
Host daily stand-ups, sprint reviews, and retrospectives to ensure timely delivery.
Data Integration & Reporting:

Define data models, manage integrations with external systems, and ensure data accuracy.
Develop and present dashboards, KPIs, and reports tailored to client requirements.
Training & Change Management:

Facilitate user training sessions to ensure smooth adoption of Salesforce tools.
Provide ongoing support and documentation to empower client teams.
Collaboration:

Coordinate with technical teams, developers, and business stakeholders to guarantee successful implementations.
Key Qualifications

5+ years of experience as a Salesforce Consultant or CRM specialist in industries like healthcare, insurance, or hospitality.
Proven expertise in Salesforce implementation across multiple modules (e.g., Sales Cloud, Service Cloud).
Strong knowledge of Agile project management methodologies and tools.
Technical proficiency with CRM tools, SOQL, APIs, and automation platforms like Zapier or Make.
Demonstrated ability to analyze business needs and translate them into actionable solutions.
Strong collaboration and communication skills, with experience in managing diverse teams and stakeholders.
Salesforce certifications (e.g., Admin, App Builder, Sales Cloud, or equivalent).
Preferred Skills

Experience in marketing automation tools and customer journey mapping.
Familiarity with NoCode tools and scripting languages like Python.
Multilingual capabilities (Fluent in French, English, and Arabic preferred).
Perks & Benefits

Competitive salary with performance-based bonuses.
Flexible working environment (hybrid setup).
Opportunity to lead impactful projects for top-tier clients.
Professional development budget and Salesforce certification sponsorship.
A vibrant, inclusive company culture with regular team-building events.
How to Apply
Submit your CV and a cover letter showcasing how your expertise aligns with Fiction Solutions’ mission and the responsibilities of this role.



---

### Here is my CV Markdown:

## Professional Experience

### CRM Consultant, International Consulting Firm (Pharma Industry)  
**Jan 2024 – Sep 2024**  
- **Workshops and requirements gathering**: Led workshops with stakeholders to define business processes and gather functional and technical requirements.  
- **CRM design and deployment**: Implemented CRM environments for multiple countries (Poland, Romania, Greece) to meet user needs.  
- **Requirements documentation**: Authored functional specifications and integrated data to ensure project delivery.  
- **Technical and business collaboration**: Coordinated with business and technical teams to ensure configurations met requirements.  
- **Solution demonstrations**: Presented developed solutions to stakeholders to validate alignment with needs.  
- **Training support**: Supported CRM training for users in five countries (Poland, Romania, Greece, Brazil, and Mexico).  

### CRM Consultant, Digital Transformation Firm (Insurance Sector)  
**Nov 2022 – Dec 2023**  
- **Needs analysis and user stories**: Translated business needs into functional and technical specifications as user stories.  
- **Workshops and requirements gathering**: Conducted workshops to define business processes and collect functional requirements.  
- **CRM and marketing solutions design**: Designed Salesforce solutions tailored to client needs (e.g., sales journeys, lead conversion, referral programs).  
- **Agile project management**: Managed daily stand-ups, weekly reviews, and project governance meetings (copil, coproj).  
- **Team collaboration**: Worked closely with developers to ensure accurate solution configurations.  
- **Quality control**: Verified technical deliverables to ensure quality and compliance before deployment.  

### Digital Project Manager, Digital Agency  
**Sep 2020 – Jun 2022**  
- **Client engagement**: Prepared presales materials for prospective clients.  
- **Web development**: Designed and optimized web tools (mainly WordPress).  
- **App development**: Built applications using frameworks like Laravel and MySQL.  
- **Customer engagement campaigns**: Executed CRM campaigns (email, SMS, automation) aligned with customer segmentation and lifecycle.  

### CRM Administrator, Hospitality Sector  
**Nov 2018 – Sep 2020**  
- **System integration**: Deployed and configured hotel management systems (e.g., Cloudbeds).  
- **Training**: Trained sales and customer service teams on CRM usage.  
- **Marketing campaign management**: Planned and executed targeted promotions via email and tracked user interactions.  
- **Analysis and reporting**: Monitored campaign KPIs and developed recommendations to improve engagement and performance.


---
## Languages and IT Skills  
- **Languages**: French (fluent), Arabic (native), English (fluent)  
- **IT Skills**: SOQL, HTML, CSS, PHP  

---

## Additional Experience and Achievements  
- **5x Salesforce Certifications**: Associate, Admin, App Builder, Sales Cloud, IA Associate  
- **12+ Digital Projects Delivered**  
"""

# make api call
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ], 
    temperature = 0.25
)
    
# extract response
resume = response.choices[0].message.content
print(resume)
