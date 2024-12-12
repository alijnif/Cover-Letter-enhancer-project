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
THE JOB DESCRIPTION :
X is Europe's leading freelancing platform with one clear mission: to give people the freedom to choose who they work with. Co-founded in 2013, X is a tech company with a human approach that helps companies and freelancers make the perfect match.

It is a marketplace that embraces a community of over 700,000 freelancers and over 70,000 clients, ranging from small and medium-sized enterprises to large corporations. More than just a connector, our marketplace streamlines freelancer-client communications, simplifies administrative and legal tasks, expedites invoicing and payments, and so much more.
We are all about giving both freelancers and companies choice and added peace of mind, so that every experience on X is nothing less than (inter)stellar.

✨ X is also…
- a tech company with a human approach
- a company with a strong culture fueled by 700 employees from 40+ nationalities, working from 9 countries all around Europe - Germany, Belgium, United Arab Emirates, Spain, France, Netherlands, Nordic countries, United Kingdom, and Switzerland.
- committed to creating a safe and inclusive space where every employee can thrive both personally and professionally
- committed to equality and diversity (50% of People managers are women)
- a company with strong career path policies allowing all employees to develop and grow equally

Join us on Planet, we need you to help us write this next chapter! 🪐

At X we believe that Ambition is the Way, so all lists of missions and responsibilities are non-exhaustive.
Explore your future career  🔭
As the CRM & Marketing Ops Lead, you will be responsible for leading a team to manage and optimize our marketing operations and CRM processes. Your role will involve empowering sales teams, enhancing activation and retention strategies, and ensuring teams operational excellence.

Key responsibilities ✨

CRM databases cleaning, enrichment and segmentation:
Identify and implement strategies to enrich our clients databases with relevant data points using 3rd party tools like Clay, FullEnrich, Lusha…
Works closely with the Growth & Data Engineering team to design, develop, and maintain data pipelines, automations and integrations.
Activation and Retention Strategies:
Set up and improve activation and retention workflows for clients and freelancers through tests and experiments.
Collaborate with Sales, Marketing, and Freelance teams to implement new business solutions.
KPIs: number of tests deployed, Customer activation rate, retention rate, email campaign performance.
Sales Teams Empowerment and Lead Management:
Manage inbound processes: Define MQL criteria, funnel steps, and harmonize processes.
Develop and optimize lead generation strategies, including automatic database enrichment, lead scoring, etc.
KPIs: Lead conversion rate, lead qualification accuracy, database enrichment rate.
Tool Administration and Reporting:
Own the marketing tools stack and serve as the point of contact for Data/Ops on technical topics, manage and optimize Hubspot properties, and provide training on marketing tools usage.
Create dashboards on Hubspot and Excel for marketing and freelancer teams.
Conduct regular performance analysis on email performance, deliverability, and inbound performance.
KPIs: Report accuracy, tool utilization rate, bug resolution time.
About you 🧑‍🚀

5-8 years of experience in marketing, growth, or operations within a tech company or startup.
Proficient in CRM tools (Hubspot, Salesforce).
Familiarity with technical tools (API, data, NoCode automation platforms like Zapier or Make, scripting languages like Python)
Strong collaboration skills with the ability to work with multiple teams.
Demonstrated leadership and ability to drive internal change.
Rigorous and committed to implementing reliable and sustainable processes.
Languages: Fluency in English and French as you will work in both languages


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
