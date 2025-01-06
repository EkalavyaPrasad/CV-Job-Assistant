import streamlit as st
from langchain_ollama import ChatOllama
import json
import ollama
from openai import OpenAI


client = OpenAI(base_url='http://localhost:11434/v1', 
                api_key = 'ollama')



def get_industry(jd):
    prompt = """You are a helpful assistant that does what it is told to do.\
          Find out the top three matches of the Job Area (such as, finance, digital marketing, accounting, Chemical engineering, etc.) that matches the user profile\
          Based on the User Info provided to you,You have to return a json object where the keys are given below:\
        - name: return ONLY the first name of the user. \
        - ind1: first Job Area
        - ind2: second Job Area
        - ind3: third Job Area"""
    
    llm = ChatOllama(
        model="phi3:latest",
        temperature=0, format='json'
    )
    messages = [
    ("system", prompt),
    ("human", jd),
    ]
    response = llm.invoke(messages).content
    return json.loads(response)





user_info = """Ekalavya Prasad

• +44 7774732797 • ekalavyaprasad2709@gmail.com • www.linkedin.com/in/ekalavya-prasad •

Credit risk Analyst with strong financial modelling, forecasting, and cross-functional collaboration expertise. Expertise in financial modelling, forecasting, and report generation using Excel, Python, and SQL, with hands-on experience leveraging data for strategic decision-making. Top academic performance in Financial Management MSc at the University of Birmingham with a distinction grade and practical experience in credit risk modelling and automated reporting processes using AI. Part-qualified CIMA with a proven ability to deliver insights in high-level meetings and contribute to process improvements in dynamic, multi-national environments.

TECHNICAL SKILLS
Python: Applied Python for data analysis, developing AI models, and LLM-based software, demonstrating advanced proficiency.
MS Excel: Advanced proficiency with Macros, and functions. Used for preparing financial reports and modeling cashflows.
MS Word and PowerPoint: Prepared numerous reports, presentations and memos using the tools. Advanced proficiency. 
SQL: Utilised to extract, manipulate, and analyse large datasets during internships.
Project Management: Coordinated AI research workshops using Agile methodology, managed cross-functional teams to deliver projects on time, and presented strategic insights to stakeholders using PowerPoint and data dashboards. 

EDUCATION
MSc Financial Management (Distinction) • University of Birmingham                                                        2023 - 2024
Key Modules
•	International Treasury Management: Assessed International Forex and Credit risks. prepared IFRS-compliant reports. 
•	Risk Analysis and Management: Applied statistical methods for risk modelling and forecasting using Python and Stata.
Dissertation: "Credit Risk Modelling using Deep Learning & AI" – Achieved top marks in the class with a 1st rank for this dissertation.
•	Developed and implemented credit risk deep learning models; skilled in automating processes to streamline financial insights and reporting for strategic decision-making.  Live Demo
Research Project: Worked Autonomously to Develop a web application that fully automates Moody’s Credit Rating process using a combination of machine learning and natural language processing (NLP) techniques.
•	Certifications: Studying towards CIMA (Part-qualified), Certificate of Treasury (Part-qualified)
Bachelor of Commerce (First Class Honors) •   Sri Sathya Sai Institute of Higher Learning                     2020-2023
Key Modules:
•	Advanced Accounting: Mastered advanced global accounting standards and applied advanced Excel skills and financial modelling to business scenarios.
Research Project: Portfolio Management and Risk modelling using Python, excel and Quantopian.

EXPERIENCE & EXTRACURRICULAR
Corporate Analyst Development Program • J.P Morgan Chase & Co.  (Virtual Experience )   Aug 2024 – Oct 2024
•	Led data analysis and validation on a 1,500-row M&A dataset, assessing potential acquisition leads and presenting key findings to stakeholders to support strategic decision-making. 
•	Crafted a storytelling-driven presentation using PowerPoint to communicate process improvements to stakeholders.
Library Shaper • University of Birmingham                                                                                   Nov 2023 – Aug 2024
•	Managed cross-functional teams, Coordinating with student volunteers and staff to ensure successful campaign execution.
•	Coordinated an AI research workshop project using Agile principles, overseeing all stages from planning and content development to execution. Experience using tools like PowerPoint and data dashboards to present strategic insights.
LANGUAGES 
English: Fluent
Hindi: Fluent
French: Intermediate Proficiency, achieved a triple diploma (awarded by the Alliance française)	
"""




st.title('AI Job Assistant.')

required_models = ['llama3.2:latest', 'phi3:latest' ]
def check_models(models):
    available_models = ollama.list()

    for model in models:
        if model not in available_models:
            ollama.pull(model)
            models_availiable = False  
        else:
            models_availiable = True


    return models_availiable


with st.sidebar:
    if check_models(required_models) == False:
        st.spinner('Downloading models..')
        
    cv_info = st.text_area('Paste your CV...',user_info, height=500)
    st.info('According to your CV these are your top 3 industries, Feel free to change them.')
    info = get_industry(cv_info)
    ind_1 = st.text_input('1st Job area', info['ind1'])
    ind_2 = st.text_input('2nd Job area', info['ind2'])
    ind_3 = st.text_input('3rd Job area', info['ind3'])
    
    

st.divider()
job_description = st.text_area('Paste the Job description here...')
st.divider()

def ai_report(jd):
    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0
    )
    messages = [
    ("system", f"""You are a seasoned recruiter with expertise in hiring for {ind_1}, {ind_2}, and {ind_3}. With over 10 years of experience, you excel in understanding the nuances of job \
descriptions and crafting tailored CVs. I am sharing a job description with you for analysis. Once you confirm \
you're ready, I’ll provide my resume for further customisation. Please review the Job Description and let me know your insights."""
),
    ("human", f'provide insights for  <<<{jd}>>>'),
    ]
    response = llm.stream(messages) 
    for chunk in response:
        yield chunk.content



def cv_review(analysis, user_cv_info):
    prompt = f"""
    Job description analysis: "{analysis}".\n
    Here’s my resume for your review <<<{user_cv_info}>>>. Based on the job description analysis, please provide 
    the following:
    - Professional Summary: A professional summary that highlights my analytical skills, and relevant 
    experience ensuring it aligns with the job description.
    - Key Bullet Points: Four to five tailored bullet points for my work at [insert recent role, e.g., 
    current/recent company name/project] and [insert previous role/project name], ensuring these points 
    highlight skills and accomplishments relevant to the target job title and JD requirements.
    - ATS Optimisation: A list of 10 keywords or skills critical for passing Applicant Tracking Systems (ATS), 
    based on the job description."""
        
         
    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0,
    )
    messages = [
    ("human", prompt),
    ]
    response = llm.stream(messages) 
    for chunk in response:
        yield chunk.content

def identify_skill_gaps(cv, jd, cv_report):
    prompt = f"""
    The following text provides key information for analysis:
    - CV of the User: "{cv}"
    - Job Description (JD): "{jd}"
    - CV Analysis Report based on the Job Description: "{cv_report}"

    Task:
    Read the Job description carefully. 
    Review the provided CV and Job Description, along with the analysis report. Identify any skills or qualifications mentioned in the Job Description that are missing or insufficiently emphasized in the CV. List these missing skills explicitly.\
    Do not mention skills that are not mentioned in the Job description. 

    Additionally, suggest specific content revisions or additions to the CV to incorporate these skills effectively while maintaining clarity and relevance. Ensure the suggested changes align with the tone and structure of the existing CV.

    Lastly, consider everything and provide a score out of 10, on how likely the CV is to be shortlisted.
    """

        
    
    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0.2,
    )
    messages = [
    ("human", prompt),
    ]
    response = llm.stream(messages) 
    for chunk in response:
        yield chunk.content


def update_cv(cv, jd, analysis, gaps):
    prompt = f"""
    The following text provides key information for analysis:
    - Job Description (JD): "{jd}"
    - CV Analysis and Personal Summary based on the Job Description: "{analysis}"
    - Gaps in skills, qualifications etc. that are either absent or not represented properly: "{gaps}"

    Task:
    Read the Job description carefully. 
    Review the provided CV provided below and Job Description, along with the analysis reports. 
    Incorporate the ATS friendly words mentioned. 

    Your task is to take all the information and update the CV mentioned below. 
    Format:
    - Name \n
    - Contact | email | linkedin\n
    - Personal Summary (As mentioned in the CV Analysis.)\n
    - Technical Skills (Each skill separated by a new line.)\n
    - Experience and Extra-curricular. \n
    - Education. \n

    Rules:
    - Write in Markdown format.
    - Under the Name and contact information, Use the personal summary mentioned in the CV analysis. 
    - Please adjust the CV content to British English, changing terms like "optimize" to "optimise" and any other 
    relevant variations.
    - Make the CV stand out by telling your story.
    - Try to stick to the base format of the CV as much as possible. 
    - Highlight quantifiable achievements. Employers love numbers!
    - Use action verbs like 'developed,' 'implemented,' and 'optimised.'
    - Use a consistent format and structure.
    - Omit any information that is irrelevant to the Job description. 
    - Demonstrate how skills and experiences from previous roles can be applied to the new position. 
    
    Now make the necessary changes to the cv below. <<{cv}>>
    """
    
    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0.1,
    )
    messages = [
    ("human", prompt),
    ]
    response = llm.stream(messages) 
    for chunk in response:
        yield chunk.content


tailor_cv = st.button('Initialise Model')

report_text = ''
cv_report_text = ''
skill_gap_text = ''
updated_cv_text = ''

if tailor_cv:
    if cv_info.strip() == '':
        st.warning('Paste your CV to continue...')
    else:
        with st.spinner('Initialising AI model...'):
            st.subheader("Summary of Job Description")
            report_placeholder = st.empty() 
            for chunk in ai_report(job_description):
                report_text += chunk 
                report_placeholder.markdown(report_text) 

        st.divider()
        with st.spinner('Analysing your CV...'):
            st.subheader('Analysis of CV')
            cv_analysis_placeholder = st.empty()
            for a_chunk in cv_review(report_text, cv_info):
                cv_report_text += a_chunk
                cv_analysis_placeholder.markdown(cv_report_text)

        st.divider()
        with st.spinner('Identifying skill gaps...'):
            st.subheader('Skill Gaps')
            skill_gap_placeholder = st.empty()
            for b_chunk in identify_skill_gaps(cv_info, job_description, report_text):
                skill_gap_text += b_chunk
                skill_gap_placeholder.markdown(skill_gap_text)


