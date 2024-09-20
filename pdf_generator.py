import pdfkit
import tempfile
import os


def competencies_assessment_short_term_goal(profile: dict, competencies_assessment: dict) -> str:

    key_competencies = competencies_assessment['Competency Framework']['Key Competencies']
    behavioral_competencies = competencies_assessment['Competency Framework']['Behavioral Competencies']
    short_term_goal = profile['short_term_goal']
    # Start constructing the HTML content
    html_str = f"""
    <div style="page-break-inside: avoid;">
        <h1>Skill Baseline for: {short_term_goal}</h1>
        
        <h2>Key Skills</h2>
        <div>
    """

    for competency, details in key_competencies.items():
        html_str += f"""
            <h3>{competency}</h3>
            <p><strong>Description:</strong> {details['Description']}</p>
            <p><strong>Justification:</strong> {details['Justification']}</p>
        """

    html_str += "</div><h2>Key Behavioral Competencies</h2><div>"

    for competency, details in behavioral_competencies.items():
        html_str += f"""
            <h3>{competency}</h3>
            <p><strong>Description:</strong> {details['Description']}</p>
            <p><strong>Justification:</strong> {details['Justification']}</p>
        """

    html_str += "</div></div>"

    return html_str

def competencies_assessment_long_term_goal(profile: dict, competencies_assessment: dict) -> str:

    key_competencies = competencies_assessment['Competency Framework']['Key Competencies']
    behavioral_competencies = competencies_assessment['Competency Framework']['Behavioral Competencies']
    long_term_goal = profile['long_term_goal']
    # Start constructing the HTML content
    html_str = f"""
    <div style="page-break-inside: avoid;">
        <h1>Skills Baseline for {long_term_goal}</h1>
        
        <h2>Key Skills</h2>
        <div>
    """

    for competency, details in key_competencies.items():
        html_str += f"""
            <h3>{competency}</h3>
            <p><strong>Description:</strong> {details['Description']}</p>
            <p><strong>Importance:</strong> {details['Justification']}</p>
        """

    html_str += "</div><h2>Key Behavioral Competencies</h2><div>"

    for competency, details in behavioral_competencies.items():
        html_str += f"""
            <h3>{competency}</h3>
            <p><strong>Description:</strong> {details['Description']}</p>
            <p><strong>Importance:</strong> {details['Justification']}</p>
        """

    html_str += "</div></div>"

    return html_str

def short_term_skill_gap_analysis_html(profile: dict, skill_gap_analysis: dict) -> str:
    
    identified_gaps = skill_gap_analysis['SkillGapAnalysis']['IdentifiedGaps']

    short_term_goal = profile['short_term_goal']

    html_str = f"""
    <div style="page-break-inside: avoid;">
        <h1>Skill Gap Analysis between Baseline and Profile's Current Skills</h1>
        <div>
    """
    for gap in identified_gaps:
        html_str += f"""
            <h2>{gap['Skill']}</h2>
            <p><strong>Current Level:</strong> {gap['CurrentLevel']}</p>
            <p><strong>Required Level:</strong> {gap['RequiredLevel']}</p>
            <p><strong>Gap Description:</strong> {gap['GapDescription']}</p>
            <h3>Strategies to Narrow the Gap:</h3>
            <ul>
        """
        for strategy in gap['StrategiesToNarrowGap']:
            html_str += f"<li>{strategy}</li>"

        html_str += "</ul>"

    html_str += "</div></div>"

    return html_str

def long_term_skill_gap_analysis_html(profile: dict, skill_gap_analysis: dict) -> str:
        
    identified_gaps = skill_gap_analysis['SkillGapAnalysis']['IdentifiedGaps']

    long_term_goal = profile['long_term_goal']

    html_str = f"""
    <div style="page-break-inside: avoid;">
        <h1>Skill Gap Analysis for {long_term_goal}</h1>
        <div>
    """
    for gap in identified_gaps:
        html_str += f"""
            <h2>{gap['Skill']}</h2>
            <p><strong>Current Level:</strong> {gap['CurrentLevel']}</p>
            <p><strong>Required Level:</strong> {gap['RequiredLevel']}</p>
            <p><strong>Gap Description:</strong> {gap['GapDescription']}</p>
            <h3>Strategies to Narrow the Gap:</h3>
            <ul>
        """
        for strategy in gap['StrategiesToNarrowGap']:
            html_str += f"<li>{strategy}</li>"

        html_str += "</ul>"

    html_str += "</div></div>"

    return html_str

def pathway_to_short_term_goal_html(profile: dict, career_pathway: dict) -> str:
        
    milestones = career_pathway['career_pathway']['key_milestones']
    current_occupation = profile['current_occupation']
    short_term_goal = profile['short_term_goal']

    html_str = f"""
    <div style="page-break-inside: avoid;">
        <h1>Career Pathway</h1>
        <h2>From {current_occupation} to {short_term_goal}</h2>

        <h2>Key Milestones</h2>
        <div>
    """

    for milestone in milestones:
        html_str += f"""
            <h3>{milestone['milestone']}</h3>
            <h4>Actions:</h4>
            <ul>
        """
        for action in milestone['actions']:
            html_str += f"<li>{action}</li>"
        html_str += "</ul>"

    html_str += "</div></div>"

    return html_str

def pathway_to_long_term_goal_html(profile: dict, career_pathway: dict) -> str:

    milestones = career_pathway['career_pathway']['key_milestones']

    long_term_goal = profile['long_term_goal']

    html_str = f"""
    <div style="page-break-inside: avoid;">
        <h1>Career Pathway for {long_term_goal}</h1>

        <h2>Key Milestones</h2>
        <div>
    """

    for milestone in milestones:
        html_str += f"""
            <h3>{milestone['milestone']}</h3>
            <h4>Actions:</h4>
            <ul>
        """
        for action in milestone['actions']:
            html_str += f"<li>{action}</li>"
        html_str += "</ul>"

    html_str += "</div></div>"

    return html_str 

def short_term_educational_requirements_html(profile: dict, educational_requirements: dict) -> str:
    
    educational_content = educational_requirements['SkillGapRecommendations']['EducationalContent']

    short_term_goal = profile['short_term_goal']

    html_str = f"""
    <div style="page-break-inside: avoid;">
        <h1>Educational Content Recommendations for Filling the Gaps</h1>
        <div>
    """
    for skill in educational_content:
        html_str += f"<h2>{skill['Skill']}</h2>"
        
        for recommendation in skill['Recommendations']:
            html_str += f"""
                <h3>{recommendation['Type']}: {recommendation['Title']}</h3>
                <p><strong>Provider:</strong> {recommendation['Provider']}</p>
                <p><strong>Description:</strong> {recommendation['Description']}</p>
                <p><strong>Link:</strong> <a href="{recommendation['Link']}">{recommendation['Link']}</a></p>
            """

    html_str += "</div></div>"

    return html_str

def long_term_educational_requirements_html(profile: dict, educational_requirements: dict) -> str:
    
    educational_content = educational_requirements['SkillGapRecommendations']['EducationalContent']

    long_term_goal = profile['long_term_goal']

    html_str = f"""
    <div style="page-break-inside: avoid;">
        <h1>Skill Gap Recommendations for {long_term_goal}</h1>
        <div>
    """
    for skill in educational_content:
        html_str += f"<h2>{skill['Skill']}</h2>"
        
        for recommendation in skill['Recommendations']:
            html_str += f"""
                <h3>{recommendation['Type']}: {recommendation['Title']}</h3>
                <p><strong>Provider:</strong> {recommendation['Provider']}</p>
                <p><strong>Description:</strong> {recommendation['Description']}</p>
                <p><strong>Link:</strong> <a href="{recommendation['Link']}">{recommendation['Link']}</a></p>
            """

    html_str += "</div></div>"

    return html_str


def generate_pdf(profile:dict, short_term_skills_json: dict, long_term_skills_json: dict,
                short_term_skill_gap_json: dict, long_term_skill_gap_json: dict,
                pathway_to_short_term_goal_json: dict, pathway_to_long_term_goal_json: dict,
                educational_suggestions_for_short_term_json: dict, educational_suggestions_for_long_term_json: dict,
                file_name: str = "Career_Exploration_Report.pdf") -> str:
    
    short_term_skills_html_str = competencies_assessment_short_term_goal(profile, short_term_skills_json)
    long_term_skills_html_str = competencies_assessment_long_term_goal(profile, long_term_skills_json)
    short_term_skill_gap_html_str = short_term_skill_gap_analysis_html(profile, short_term_skill_gap_json)
    long_term_skill_gap_html_str = long_term_skill_gap_analysis_html(profile, long_term_skill_gap_json)
    pathway_to_short_term_goal_html_str = pathway_to_short_term_goal_html(profile, pathway_to_short_term_goal_json)
    pathway_to_long_term_goal_html_str = pathway_to_long_term_goal_html(profile, pathway_to_long_term_goal_json)
    educational_suggestions_for_short_term_html_str = short_term_educational_requirements_html(profile, educational_suggestions_for_short_term_json)
    educational_suggestions_for_long_term_html_str = long_term_educational_requirements_html(profile, educational_suggestions_for_long_term_json)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{ size: A4; }}
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Arial', sans-serif;
                font-size: 12pt; /* Increased base font size for better readability */
                color: #333333; /* Darker color for better contrast */
            }}
            h1 {{
                font-size: 20pt; /* Significantly larger to stand out as the main title */
                font-weight: bold;
                color: #0056b3; /* Added a distinct color for primary headers */
                margin-bottom: 24px; /* More space below the header */
                padding-bottom: 6px; /* Added padding for visual space */
                border-bottom: 2px solid #0056b3; /* Underline effect for emphasis */
            }}
            h2 {{
                font-size: 16pt; /* Larger than h3 but smaller than h1 */
                font-weight: bold;
                color: #006600; /* Different color to distinguish from h1 */
                margin-top: 20px; /* Space above h2 for separation */
                margin-bottom: 12px; /* Increased space below the header */
            }}
            h3 {{
                font-size: 14pt; /* Smaller than h2, yet distinguishable from body text */
                font-weight: bold;
                color: #cc5200; /* Unique color for tertiary headers */
                margin-bottom: 8px; /* Smaller margin to keep sections compact */
            }}
            strong {{
                color: #737373; /* Keeping the strong tag subtle */
                font-weight: bold; /* Ensure it's bolded */
            }}
            a {{
                color: #0056b3; /* Link color matches h1 for consistency */
                text-decoration: none; /* Optional: removes underline from links */
            }}
            a:hover {{
                text-decoration: underline; /* Underline on hover for better interaction */
            }}
            .avoid-break {{
                page-break-after: always;
            }}
        </style>
        <title>Career Exploration Report</title>
    </head>
    <body>
        {short_term_skills_html_str}
        {long_term_skills_html_str}
        {short_term_skill_gap_html_str}
        {long_term_skill_gap_html_str}
        {pathway_to_short_term_goal_html_str}
        {pathway_to_long_term_goal_html_str}
        {educational_suggestions_for_short_term_html_str}
        {educational_suggestions_for_long_term_html_str}
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

def generate_short_pdf(profile:dict, short_term_skills_json: dict, 
                short_term_skill_gap_json: dict,
                pathway_to_short_term_goal_json: dict, 
                educational_suggestions_for_short_term_json: dict,
                file_name: str = "Career_Exploration_Report.pdf") -> str:
    
    short_term_skills_html_str = competencies_assessment_short_term_goal(profile, short_term_skills_json)

    short_term_skill_gap_html_str = short_term_skill_gap_analysis_html(profile, short_term_skill_gap_json)

    pathway_to_short_term_goal_html_str = pathway_to_short_term_goal_html(profile, pathway_to_short_term_goal_json)

    educational_suggestions_for_short_term_html_str = short_term_educational_requirements_html(profile, educational_suggestions_for_short_term_json)


    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{ size: A4; }}
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Arial', sans-serif;
                font-size: 12pt; /* Increased base font size for better readability */
                color: #333333; /* Darker color for better contrast */
            }}
            h1 {{
                font-size: 20pt; /* Significantly larger to stand out as the main title */
                font-weight: bold;
                color: #0056b3; /* Added a distinct color for primary headers */
                margin-bottom: 24px; /* More space below the header */
                padding-bottom: 6px; /* Added padding for visual space */
                border-bottom: 2px solid #0056b3; /* Underline effect for emphasis */
            }}
            h2 {{
                font-size: 16pt; /* Larger than h3 but smaller than h1 */
                font-weight: bold;
                color: #006600; /* Different color to distinguish from h1 */
                margin-top: 20px; /* Space above h2 for separation */
                margin-bottom: 12px; /* Increased space below the header */
            }}
            h3 {{
                font-size: 14pt; /* Smaller than h2, yet distinguishable from body text */
                font-weight: bold;
                color: #cc5200; /* Unique color for tertiary headers */
                margin-bottom: 8px; /* Smaller margin to keep sections compact */
            }}
            strong {{
                color: #737373; /* Keeping the strong tag subtle */
                font-weight: bold; /* Ensure it's bolded */
            }}
            a {{
                color: #0056b3; /* Link color matches h1 for consistency */
                text-decoration: none; /* Optional: removes underline from links */
            }}
            a:hover {{
                text-decoration: underline; /* Underline on hover for better interaction */
            }}
            .avoid-break {{
                page-break-after: always;
            }}

        </style>
        <h1>From {profile["current_occupation"]} to {profile["short_term_goal"]}</h1>
        <h2>Profile Information</h2>
        <ul>
            <li><strong>Education:</strong> {profile['education']}</li>
            <li><strong>Current Occupation:</strong> {profile['current_occupation']}</li>
            <li><strong>Years of Experience:</strong> {profile['years_of_experience']}</li>
            <li><strong>Industry:</strong> {profile['industry']}</li>
            <li><strong>Goal:</strong> {profile['short_term_goal']}</li>
            <li><strong>Current Skills:</strong> {', '.join(profile['current_skills'])}</li>
        </ul>
    </head>
    <body>
        {short_term_skills_html_str}

        {short_term_skill_gap_html_str}

        {pathway_to_short_term_goal_html_str}

        {educational_suggestions_for_short_term_html_str}

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