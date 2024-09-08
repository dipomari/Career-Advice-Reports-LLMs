#from assistants import 
from assistants import *
from pdf_generator import *

questionare = question_assistant()

personal_assessment = personal_assessment_part(questionare)
print(personal_assessment)

career_message = f"Q&A:\n\n {questionare} Personal Assessment:\n\n {personal_assessment}"
career_options = career_options_part(career_message)
print(career_options)

educational_options_message = f"Q&A:\n\n{questionare} Career Options:\n\n {career_options}"
educational_options = educational_requirements_part(educational_options_message)
print(educational_options)


market_analysis = market_analysis_part(educational_options_message)
print(market_analysis)

action_plan_message = f"Q&A:\n\n{questionare} Career Options:\n\n {career_options} Educational Requirements:\n\n {educational_options} Market Analysis:\n\n {market_analysis}"
action_plan = action_plan_part(action_plan_message)
print(action_plan)

pdf = generate_pdf(
    personality_json=personal_assessment,
    career_json=career_options,
    educational_json=educational_options,
    market_json=market_analysis,
    action_json=action_plan,
    file_name="test.pdf"
)