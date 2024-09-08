import pdfkit
import tempfile
import os

def personal_assessment_html(personal_assessment: dict) -> str:

    skills = personal_assessment['personal_assessment']['skills']
    interests = personal_assessment['personal_assessment']['interests']
    personality_traits = personal_assessment['personal_assessment']['personality_traits']
    career_values = personal_assessment['personal_assessment']['career_values']
    long_term_goals = personal_assessment['personal_assessment']['long_term_goals']

    personal_assessment_html_str = f"""
    <div style=page-break-inside: avoid;">
        <h1>Personal Assessment</h1>
        <h2>Skills</h2>
        <p>{skills}</p>
        <h2>Interests</h2>
        <p>{interests}</p>
        <h2>Personality Traits</h2>
        <p>{personality_traits}</p>
        <h2>Career Values</h2>
        <p>{career_values}</p>
        <h2>Long Term Goals</h2>
        <p>{long_term_goals}</p>
    </div>
    """
    return personal_assessment_html_str

def career_options_html(career_options: dict) -> str:

    industry_overview = career_options['career_options']['industry_overview']
    potential_roles = career_options['career_options']['potential_roles']
    growth_opportunities = career_options['career_options']['growth_opportunities']
    
    career_options_html_str = f"""
    <div style=page-break-inside: avoid;">
        <h1>Career Options</h1>
        <h2>Industry Overview</h2>
        <p>{industry_overview}</p>
        <h2>Potential Roles</h2>
        {potential_roles}
        <h2>Growth Opportunities</h2>
        <p>{growth_opportunities}</p>
    </div>
    """
    return career_options_html_str

def educational_requirements_html(educational_requirements: dict) -> str:
    """Example Dictionary:
    {'educational_and_training_requirements': {'necessary_education': "A bachelor's degree in Computer Science or related field is necessary for roles such as Software Developer or Data Analyst. A master's degree may be required for positions like Data Scientist or Machine Learning Engineer.", 'training_programs': 'To enhance technical skills, consider enrolling in online courses or bootcamps focusing on programming languages (e.g., Python, R), data analysis tools (e.g., SQL, Tableau), and machine learning techniques. Completion of a coding bootcamp can also be beneficial for roles in software development.', 'continuing_education': 'For continuous learning and career growth, participation in workshops, conferences, and hackathons can help stay updated with the latest industry trends. Pursuing certifications such as AWS Certified Solutions Architect or Google Professional Data Engineer can also add value to your resume and open up advanced career opportunities.'}}
    """
    necessary_education = educational_requirements['educational_and_training_requirements']['necessary_education']
    training_programs = educational_requirements['educational_and_training_requirements']['training_programs']
    continuing_education = educational_requirements['educational_and_training_requirements']['continuing_education']

    educational_requirements_html_str = f"""
    <div style=page-break-inside: avoid;">
    
        <h1>Educational Requirements</h1>
        <h2>Necessary Education</h2>
        <p>{necessary_education}</p>
        <h2>Training Programs</h2>
        <p>{training_programs}</p>
        <h2>Continuing Education</h2>
        <p>{continuing_education}</p>
    </div>
    """
    return educational_requirements_html_str

def market_analysis_html(market_analysis: dict) -> str:
    job_market_trends = market_analysis['market_analysis']['job_market_trends']
    geographical_factors = market_analysis['market_analysis']['geographical_factors']
    salary_expectations = market_analysis['market_analysis']['salary_expectations']
    
    market_analysis_html_str = f"""
    <div style=page-break-inside: avoid;">
        <h1>Market Analysis</h1>
        <h2>Job Market Trends</h2>
        <p>{job_market_trends}</p>
        <h2>Geographical Factors</h2>
        <p>{geographical_factors}</p>
        <h2>Salary Expectations</h2>
        <p>{salary_expectations}</p>
    </div>
    """
    return market_analysis_html_str

def action_plan_html(action_plan: dict) -> str:
    short_term_goals = action_plan['action_plan']['short_term_goals']
    long_term_strategy = action_plan['action_plan']['long_term_strategy']
    networking_strategies = action_plan['action_plan']['networking_strategies']

    action_plan_html_str = f"""
    <div style=page-break-inside: avoid;">
        <h1>Action Plan</h1>
        <h2>Short Term Goals</h2>
        <p>{short_term_goals}</p>
        <h2>Long Term Strategy</h2>
        <p>{long_term_strategy}</p>
        <h2>Networking Strategies</h2>
        <p>{networking_strategies}</p>
    </div>
    """
    return action_plan_html_str


def generate_pdf(personality_json: dict, career_json: dict, educational_json: dict, market_json: dict, action_json: dict, file_name: str = "Career_Exploration_Report.pdf") -> str:
    personal_assessment_html_str = personal_assessment_html(personality_json)
    career_options_html_str = career_options_html(career_json)
    educational_requirements_html_str = educational_requirements_html(educational_json)
    market_analysis_html_str = market_analysis_html(market_json)
    action_plan_html_str = action_plan_html(action_json)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{ size: A4; }}
            body {{ margin: 0; padding: 0; font-family: Arial, sans-serif; font-size: 10.5pt; color: #737373; }}
            h1, h2, h3, strong {{ color: #737373; }}
            h1 {{ font-size: 12.5pt; font-weight: bold; margin-bottom: 20px; }}
            h2, h3 {{ font-size: 11.5pt; font-weight: bold; margin-bottom: 10px; }}
            .avoid-break {{ page-break-after: always; }}
        </style>
        <title>Career Exploration Report</title>
    </head>
    <body>
        {personal_assessment_html_str}
        {career_options_html_str}
        {educational_requirements_html_str}
        {market_analysis_html_str}
        {action_plan_html_str}
    </body>
    </html>
    """
    options = {
        "page-size": "A4",
        "margin-top": "1.400in",
        "margin-right": "0.75in",
        "margin-bottom": "1.200in",
        "margin-left": "0.45in",
        "encoding": "UTF-8",
        "no-outline": None,
        "dpi": 300,
    }

    # Determine the path to the user's Downloads folder
    home = os.path.expanduser("~")
    downloads_path = os.path.join(home, "Downloads", file_name)

    # Use pdfkit to create the PDF directly at the specified location
    pdfkit.from_string(html_content, downloads_path, options=options)

    return downloads_path