#from assistants import 
from assistants import *
from pdf_generator import *


# make up another profile starting from education and ending with current skills
profile = {
    "education":"Bachelor’s International Business Management",
    "current_occupation":"Intern at a Financial Services Firm",
    "years_of_experience":"2",
    "industry":"Finance",
    "short_term_goal":"Transitioning to a Data Scientist role within the next 2 years",
    "long_term_goal":"Establish a career in AI research and development",
    "current_skills":["Financial analysis", "Excel modeling", "Market research", "Basic Python programming"],
    }
profile_1 = {
    "docname": "Profile 1",
    "education": "Bachelor's in Marketing",
    "current_occupation": "Social Media Coordinator at a Tech Startup",
    "years_of_experience": "1.5",
    "industry": "Technology",
    "short_term_goal": "Transitioning to a Brand Strategist role within the next year",
    "long_term_goal": "Become a Marketing Director for a global tech company",
    "current_skills": ["Social media management", "Content creation", "Google Analytics", "Basic SEO"]
}

profile_2 = {
    "docname": "Profile 2",
    "education": "Bachelor's in Business Administration",
    "current_occupation": "Junior Business Analyst at a Retail Company",
    "years_of_experience": "3",
    "industry": "Retail",
    "short_term_goal": "Move into a Product Manager role within the next 1.5 years",
    "long_term_goal": "Launch a consultancy firm specializing in retail innovation",
    "current_skills": ["Data analysis", "Market research", "Project management", "Basic SQL"]
}

profile_3 = {
    "docname": "Profile 3",
    "education": "Bachelor's in Data Science",
    "current_occupation": "Data Analyst Intern at a Healthcare Firm",
    "years_of_experience": "1",
    "industry": "Healthcare",
    "short_term_goal": "Transitioning to a Data Scientist role in a healthcare AI team",
    "long_term_goal": "Become a leading AI researcher in predictive healthcare models",
    "current_skills": ["Python programming", "Data visualization", "SQL", "Basic machine learning"]
}

profile_4 = {
    "docname": "Profile 4",
    "education": "Bachelor's in Business Administration",
    "current_occupation": "Sales Operations Analyst at a Consumer Goods Company",
    "years_of_experience": "2",
    "industry": "Consumer Goods",
    "short_term_goal": "Become a Business Development Manager within the next 2 years",
    "long_term_goal": "Lead the sales strategy for a Fortune 500 company",
    "current_skills": ["Salesforce management", "CRM tools", "Sales forecasting", "Market analysis"]
}

profile_5 = {
    "docname": "Profile 5",
    "education": "Bachelor's in Marketing",
    "current_occupation": "Content Marketing Intern at a Fashion Brand",
    "years_of_experience": "1",
    "industry": "Fashion",
    "short_term_goal": "Move into a Digital Marketing role focusing on SEO and PPC campaigns",
    "long_term_goal": "Become the Chief Marketing Officer of a luxury fashion house",
    "current_skills": ["Content writing", "SEO", "Email marketing", "Basic Google Ads"]
}

profile_6 = {
    "docname": "Profile 6",
    "education": "Bachelor's in Data Science",
    "current_occupation": "Data Analyst at a Logistics Firm",
    "years_of_experience": "2",
    "industry": "Logistics",
    "short_term_goal": "Transition to a Senior Data Scientist role in supply chain optimization",
    "long_term_goal": "Lead a data-driven transformation in logistics and automation",
    "current_skills": ["Python programming", "Data cleaning", "Logistics modeling", "Basic R programming"]
}

profile_7 = {
    "docname": "Profile 7",
    "education": "Bachelor's in Business Administration",
    "current_occupation": "Operations Analyst at a Manufacturing Company",
    "years_of_experience": "3",
    "industry": "Manufacturing",
    "short_term_goal": "Become a Supply Chain Manager within the next 1.5 years",
    "long_term_goal": "Lead global supply chain operations for a multinational company",
    "current_skills": ["Process improvement", "Lean management", "Inventory optimization", "Basic ERP systems"]
}

profile_8 = {
    "docname": "Profile 8",
    "education": "Bachelor's in Marketing",
    "current_occupation": "Email Marketing Specialist at a SaaS Company",
    "years_of_experience": "2",
    "industry": "Software as a Service (SaaS)",
    "short_term_goal": "Transition into a Growth Marketing role within 1 year",
    "long_term_goal": "Lead growth and customer retention strategies for a tech unicorn",
    "current_skills": ["Email automation", "A/B testing", "Campaign analysis", "Basic CRM tools"]
}

profile_9 = {
    "docname": "Profile 9",
    "education": "Bachelor's in Data Science",
    "current_occupation": "Machine Learning Intern at a Financial Services Firm",
    "years_of_experience": "1",
    "industry": "Finance",
    "short_term_goal": "Move into a full-time Machine Learning Engineer role",
    "long_term_goal": "Lead AI innovation in risk assessment for financial institutions",
    "current_skills": ["Python", "Machine learning", "Data preprocessing", "Basic TensorFlow"]
}

profile_10 = {
    "docname": "Profile 10",
    "education": "Bachelor's in Business Administration",
    "current_occupation": "Junior Marketing Analyst at an E-commerce Company",
    "years_of_experience": "2",
    "industry": "E-commerce",
    "short_term_goal": "Become a Marketing Manager with a focus on digital transformation",
    "long_term_goal": "Lead marketing strategy for a top e-commerce platform",
    "current_skills": ["Google Analytics", "Social media strategy", "Digital advertising", "Basic HTML/CSS"]
}

peding_profiles = [profile_3]

for profile in peding_profiles:
    print(f"run for {profile['docname']}")

    short_term_str = f"Industry:{profile["industry"]}, goal: {profile['short_term_goal']}"
    short_term_skills = competency_framework_part(short_term_str)

    print("SHORT TERM SKILLS MESSAGE:\n\n",short_term_skills)


    """
    Step 2: Skill Gap Analysis
    """

    skills = profile["current_skills"]
    skills_for_short_term = f"Current Skills: {skills}\n\n Skills needed for {profile['short_term_goal']}: {short_term_skills["Competency Framework"]["Key Competencies"]}\n Bahavioral Skills{short_term_skills["Competency Framework"]["Behavioral Competencies"]} "


    #iterate over the competencies to add them into a string to be sent to the assistant
    skill_gap_short_term_message = "Make your Skill Gap Analysis HIGHLIGHT MORE THAN 3 SKILLS GAPS AND GIVE MORE THAN 2 STRATEGIES FOR EACH SKILL GAP:\n\n INDUSTRY NEEDS:\n\n"
    for competency in short_term_skills["Competency Framework"]["Key Competencies"]:
        skill_gap_short_term_message += f"Competency: {competency}\n"
        skill_gap_short_term_message += f"Description: {short_term_skills['Competency Framework']['Key Competencies'][competency]['Description']}\n"
        skill_gap_short_term_message += f"Importance: {short_term_skills['Competency Framework']['Key Competencies'][competency]['Justification']}\n\n"

    for competency in short_term_skills["Competency Framework"]["Behavioral Competencies"]:
        skill_gap_short_term_message += f"Competency: {competency}\n"
        skill_gap_short_term_message += f"Description: {short_term_skills['Competency Framework']['Behavioral Competencies'][competency]['Description']}\n"
        skill_gap_short_term_message += f"Importance: {short_term_skills['Competency Framework']['Behavioral Competencies'][competency]['Justification']}\n\n"

    skill_gap_short_term_message += f"\n Current SKills: {skills}"


    print("📊📈📉SKILL SHORT TERM GAP MESSAGE:\n\n",skill_gap_short_term_message)

    short_term_skill_gap = skill_gap_part(skill_gap_short_term_message)
    print("IDENTIFIED SKILLGAPS :\n\n",short_term_skill_gap)


    """
    step 3: Career Pathway
    """

    identified_gaps = short_term_skill_gap['SkillGapAnalysis']['IdentifiedGaps']

    short_term_skill_gap_prompt = "Here are the strategies to narrow the identified skill gaps :\n\n"

    # Iterate over each gap and extract strategies
    for gap in identified_gaps:
        short_term_skill_gap_prompt += f"SkillGap: {gap['Skill']}\n"
        for strategy in gap['StrategiesToNarrowGap']:
            short_term_skill_gap_prompt += f"- {strategy}\n"
        short_term_skill_gap_prompt += "\n"  # Add a newline for spacing between skills
        
    client_info_prompt = f"""
    Give at least 5 well defined milestones, and give a career path using the following information:

    Goal: {profile['short_term_goal']}

    Current Ocuppation: {profile['current_occupation']}
    """ 

    client_info_prompt += short_term_skill_gap_prompt

    pathway_to_short_term_goal = career_pathway_part(client_info_prompt)

    print("🎒🎓🏫PathWAY from today to short term:\n\n", pathway_to_short_term_goal)


    """
    RECOMMENDED EDUCATIONAL OPTIONS
    """


    for gap in short_term_skill_gap["SkillGapAnalysis"]["IdentifiedGaps"]:
        skill_gap_prompt = f"SKILL GAPS ANALYSIS:\n\n" \
                f"Skillgap: {gap['Skill']}\n" \
                f"Current Level: {gap['CurrentLevel']}\n" \
                f"Required Level: {gap['RequiredLevel']}\n" \
                f"Gap Description: {gap['GapDescription']}\n" \

    for milestone in pathway_to_short_term_goal["career_pathway"]["key_milestones"]:
        for action in milestone["actions"]:
            skill_gap_prompt += f"Recommended actions for client: - {action}\n"

    short_term_educational_options_message = f"Make your Educational Recommendations to help the client achieve the recommended actions:\n\n{skill_gap_prompt}"


    educational_suggestions_for_short_term = educational_recommendation_part(short_term_educational_options_message)
    print("📈📊💹EDUCATIONAL SUGGESTIONS FOR FILLING SHORT TERM SKILL GAPS:\n\n",educational_suggestions_for_short_term)


    pdf = generate_short_pdf(profile=profile,
        short_term_skills_json=short_term_skills,
        short_term_skill_gap_json=short_term_skill_gap,
        pathway_to_short_term_goal_json=pathway_to_short_term_goal,
        educational_suggestions_for_short_term_json=educational_suggestions_for_short_term,
        file_name=f"{profile["docname"]}_careeradvice.pdf"
    )
