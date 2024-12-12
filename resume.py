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

## Expérience Professionnelle

### Consultant CRM, Société de Conseil International (Industrie Pharmaceutique)  
**Jan 2024 – Sep 2024**  
- **Ateliers de découverte et collecte de besoins** : Animation d’ateliers avec les parties prenantes pour définir les processus métiers et recueillir les besoins fonctionnels et techniques.  
- **Conception et déploiement de solutions CRM** : Mise en place d'un environnement CRM pour plusieurs pays afin de répondre aux besoins des utilisateurs.  
- **Documentation des exigences** : Rédaction des exigences fonctionnelles et intégration des données pour assurer la livraison du projet.  
- **Collaboration technique et métier** : Coordination avec les équipes métier et technique pour garantir des configurations conformes aux attentes.  
- **Démo des solutions** : Présentation des solutions développées aux parties prenantes pour valider leur adéquation aux besoins.  
- **Suivi des formations** : Accompagnement des utilisateurs finaux lors du déploiement du CRM dans différents pays.  

### Consultant CRM, Cabinet de Conseil en Transformation Digitale (Assurance)  
**Nov 2022 – Dec 2023**  
- **Analyse des besoins et user stories** : Identification des besoins métiers et traduction en user stories pour les équipes techniques.  
- **Ateliers de collecte des besoins** : Animation d’ateliers pour définir les processus métiers et recueillir les besoins fonctionnels.  
- **Développement de solutions CRM** : Conception de parcours utilisateurs et déploiement de fonctionnalités CRM adaptées (gestion commerciale, parrainage, etc.).  
- **Gestion Agile** : Suivi des projets via des réunions régulières (daily, weekly, copil, coproj).  
- **Collaboration technique** : Coordination avec les développeurs pour garantir la qualité des livrables.  
- **Contrôle qualité** : Validation des livrables techniques avant mise en production.  

### Chef de projet digital, Agence Digitale  
**Sep 2020 – Juin 2022**  
- **Support client** : Participation à l’avant-vente et préparation de supports pour les prospects.  
- **Développement web** : Conception et optimisation de solutions web (frameworks modernes).  
- **Développement applicatif** : Conception d’applications utilisant des technologies back-end et bases de données relationnelles.  
- **Marketing automation** : Déploiement de campagnes CRM (emailing, SMS) adaptées aux cycles de vie client.  

### Administrateur CRM, Secteur Hôtellerie  
**Nov 2018 – Sep 2020**  
- **Intégration de solutions de gestion** : Déploiement et configuration de systèmes de gestion spécifiques à l'industrie.  
- **Formation utilisateurs** : Formation des équipes commerciales à l’utilisation d’outils CRM et omnicanaux.  
- **Gestion de campagnes marketing** : Conception et envoi de communications ciblées pour maximiser l’engagement des clients.  
- **Analyse et reporting** : Suivi des indicateurs de performance et recommandations pour optimiser les campagnes.

---
## Langues et Compétences IT
- **Langues** : Français (courant), Arabe (langue maternelle), Anglais (courant)
- **Compétences IT** : SOQL, HTML, CSS, PHP
---
## Expérience et Réalisations Complémentaires
- **5x Certifications Salesforce** : Associate, Admin, App Builder, Sales Cloud, IA Associate
- **+12 projets numériques réalisés** 

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
