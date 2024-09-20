#from assistants import 
from assistants import *
from pdf_generator import *

profile = {
    "name":"Alex Martinez",
    "age":"28",
    "location":"San Francisco, CA",
    "education":"Bachelor’s Degree in Business Administration",
    "current_occupation":"Marketing Coordinator",
    "years_of_experience":"5",
    "industry":"Digital Marketing",
    "short_term_goal":"Become a Marketing Manager within the next 2 years",
    "long_term_goal":"Aim to be a Chief Marketing Officer (CMO) of a tech startup",
    "current_skills":["Social Media Marketing", "SEO and SEM", "Content Creation and Strategy", "Data Analysis (Basic)"],
    "preferred_learning_mode":"Online self-paced courses", 
    "time_commitment":"Able to dedicate 6-8 hours per week",
    "learning_style":"Visual and Kinesthetic",
    "professional_interests":["Technology trends", "startup culture", "innovative marketing strategies"],
    "personal_interests":["Hiking", "reading science fiction", "podcasting"]
    }

profile2 = {
    "name":"Priya Singh",
    "age":"32",
    "location":"Austin, TX",
    "education":"Master’s Degree in Computer Science",
    "current_occupation":"Software Developer",
    "years_of_experience":"7",
    "industry":"Software Development",
    "short_term_goal":"Transition to a Software Architect role within the next 3 years",
    "long_term_goal":"Leading a development team at a major tech company, focusing on innovative software solutions",
    "current_skills":["Expertise in Java and Python", "Experience with Agile and Scrum methodologies", "Strong background in developing SaaS products", "Proficient in cloud platforms like AWS and Azure"],
    "preferred_learning_mode":"Blended learning (online with occasional in-person workshops)",
    "time_commitment":"Willing to dedicate 10 hours per week",
    "learning_style":"Analytical and Practical",
    "professional_interests":["Emerging technologies", "AI", "cybersecurity"],
    "personal_interests":["Coding competitions", "blogging about tech trends", "cycling"]
    }


short_term_str = f"Industry:{profile["industry"]}, goal: {profile['short_term_goal']}"
short_term_skills = competency_framework_part(short_term_str)

long_term_str = f"Industry:{profile["industry"]}, goal: {profile['long_term_goal']}"
long_term_skills = competency_framework_part(long_term_str)


print("SHORT TERM SKILLS MESSAGE:\n\n",short_term_skills)
print("LONGTERM SKILLS MESSAGE:\n\n",long_term_skills)

"""
Step 2: Skill Gap Analysis
"""

skills = profile["current_skills"]
skills_for_short_term = f"Current Skills: {skills}\n\n Skills needed for {profile['short_term_goal']}: {short_term_skills["Competency Framework"]["Key Competencies"]}\n Bahavioral Skills{short_term_skills["Competency Framework"]["Behavioral Competencies"]} "

skills_for_long_term = f"""Achieved Skills: {short_term_skills["Competency Framework"]["Key Competencies"]}\n
Bahavioral Skills{short_term_skills["Competency Framework"]["Behavioral Competencies"]}\n\n SKILLS NEEDED for {profile['long_term_goal']}: 
{long_term_skills["Competency Framework"]["Key Competencies"]}\n Bahavioral Skills{long_term_skills["Competency Framework"]["Behavioral Competencies"]} """


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

skill_gap_long_term_message = "Make your Skill Gap Analysis HIGHLIGHT MORE THAN 3 SKILLS GAPS AND GIVE MORE THAN 2 STRATEGIES FOR EACH SKILL GAP:\n\n INDUSTRY NEEDS:\n\n"
for competency in long_term_skills["Competency Framework"]["Key Competencies"]:
    skill_gap_long_term_message += f"Competency: {competency}\n"
    skill_gap_long_term_message += f"Description: {long_term_skills['Competency Framework']['Key Competencies'][competency]['Description']}\n"
    skill_gap_long_term_message += f"Importance: {long_term_skills['Competency Framework']['Key Competencies'][competency]['Justification']}\n\n"

for competency in long_term_skills["Competency Framework"]["Behavioral Competencies"]:
    skill_gap_long_term_message += f"Competency: {competency}\n"
    skill_gap_long_term_message += f"Description: {long_term_skills['Competency Framework']['Behavioral Competencies'][competency]['Description']}\n"
    skill_gap_long_term_message += f"Importance: {long_term_skills['Competency Framework']['Behavioral Competencies'][competency]['Justification']}\n\n"

achieved_skills = ""
for competency in short_term_skills["Competency Framework"]["Key Competencies"]:
    achieved_skills += f"Skill: {competency}\n"
    achieved_skills += f"{short_term_skills['Competency Framework']['Key Competencies'][competency]['Description']}\n"

for competency in short_term_skills["Competency Framework"]["Behavioral Competencies"]:
    achieved_skills += f"Skill: {competency}\n"
    achieved_skills += f"{short_term_skills['Competency Framework']['Behavioral Competencies'][competency]['Description']}\n"


skill_gap_short_term_message += f"\n Current SKills: {skills} {achieved_skills}"

print("📊📈📉SKILL LONG TERM GAP MESSAGE:\n\n",skill_gap_long_term_message)

long_term_skill_gap = skill_gap_part(skill_gap_long_term_message)
print("IDENTIFIED SKILLGAPS :\n\n",long_term_skill_gap)


"""
step 3: Career Pathway
"""

identified_gaps = short_term_skill_gap['SkillGapAnalysis']['IdentifiedGaps']

short_term_skill_gap_prompt = "Here are the strategies to narrow the skill gaps identified:\n\n"

# Iterate over each gap and extract strategies
for gap in identified_gaps:
    short_term_skill_gap_prompt += f"SkillGap: {gap['Skill']}\n"
    for strategy in gap['StrategiesToNarrowGap']:
        short_term_skill_gap_prompt += f"- {strategy}\n"
    short_term_skill_gap_prompt += "\n"  # Add a newline for spacing between skills
    
client_info_prompt = f"""
Make a 10 milestone career path using the following information:

Goal: {profile['short_term_goal']}

Professional Background
Current Ocuppation: {profile['current_occupation']}
- Years of Experience: {profile['years_of_experience']}
- Industry: {profile['industry']}
""" 

short_term_skill_gap_prompt += client_info_prompt

pathway_to_short_term_goal = career_pathway_part(short_term_skill_gap_prompt)

print("🎒🎓🏫PathWAY from today to short term:\n\n", pathway_to_short_term_goal)

identified_gaps = long_term_skill_gap['SkillGapAnalysis']['IdentifiedGaps']

long_term_skill_gap_prompt = "Here are the strategies to narrow the skill gaps identified:\n\n"

# Iterate over each gap and extract strategies
for gap in identified_gaps:
    long_term_skill_gap_prompt += f"SkillGap: {gap['Skill']}\n"
    for strategy in gap['StrategiesToNarrowGap']:
        long_term_skill_gap_prompt += f"- {strategy}\n"
    long_term_skill_gap_prompt += "\n"  # Add a newline for spacing between skills

client_info_prompt = f"""
Make a 10 milestone career path using the following information:

Goal: {profile['long_term_goal']}
Professional Background
Current Ocuppation: {profile['current_occupation']}
- Years of Experience: {profile['years_of_experience']}
- Industry: {profile['industry']}
"""

long_term_skill_gap_prompt += client_info_prompt

pathway_to_long_term_goal = career_pathway_part(long_term_skill_gap_prompt)

print("🎒🎓🏫PathWAY to long term goal from short term:\n\n", pathway_to_long_term_goal)


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

for gap in long_term_skill_gap["SkillGapAnalysis"]["IdentifiedGaps"]:
    skill_gap_prompt = f"SKILL GAPS ANALYSIS:\n\n" \
             f"Skillgap: {gap['Skill']}\n" \
             f"Current Level: {gap['CurrentLevel']}\n" \
             f"Required Level: {gap['RequiredLevel']}\n" \
             f"Gap Description: {gap['GapDescription']}\n" \

for milestone in pathway_to_long_term_goal["career_pathway"]["key_milestones"]:
    for action in milestone["actions"]:
        skill_gap_prompt += f"Recommended actions for client: - {action}\n"

long_term_educational_options_message = f"Make your Educational Recommendations to help the client achieve the recommended actions:\n\n{skill_gap_prompt}"

educational_suggestions_for_long_term = educational_recommendation_part(long_term_educational_options_message)
print("📈📊💹EDUCATIONAL SUGGESTIONS FOR FILLING LONG TERM SKILL GAPS:\n\n",educational_suggestions_for_long_term)




"""
action_plan_message = f"Q&A:\n\n{questionare} Career Options:\n\n {career_options} Educational Requirements:\n\n {educational_options} Market Analysis:\n\n {market_analysis}"
action_plan = action_plan_part(action_plan_message)
print("🛫🗓️👍ACTION PLAN:\n\n",action_plan)

"""
pdf = generate_pdf(profile=profile,
    short_term_skills_json=short_term_skills,
    long_term_skills_json=long_term_skills,
    short_term_skill_gap_json=short_term_skill_gap,
    long_term_skill_gap_json=long_term_skill_gap,
    pathway_to_short_term_goal_json=pathway_to_short_term_goal,
    pathway_to_long_term_goal_json=pathway_to_long_term_goal,
    educational_suggestions_for_short_term_json=educational_suggestions_for_short_term,
    educational_suggestions_for_long_term_json=educational_suggestions_for_long_term,
    file_name="Tech_test.pdf"
)
