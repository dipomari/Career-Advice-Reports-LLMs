from api_commands import create_thread, send_message, wait_for_completion, retrieve_answer
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')


def competency_framework_part(content: str) -> dict:
    assistant_id = os.getenv('ASSISTANTS.competency_framework')
    thread_id_personal_assessment_= create_thread()

    message = send_message(thread_id=thread_id_personal_assessment_, content=content)
    print("MESSAGE", message)
    wait_for_completion(thread_id=thread_id_personal_assessment_, assistant_id=assistant_id)

    personal_assessment_answer = retrieve_answer(thread_id=thread_id_personal_assessment_)
    #print("RAW ANSWER", personal_assessment_answer)
    personal_assessment_json = json.loads(personal_assessment_answer)

    return personal_assessment_json

def skill_gap_part(content: str) -> dict:
    assistant_id = os.getenv('ASSISTANTS.skill_gap')
    thread_id_career_options = create_thread()

    send_message(thread_id=thread_id_career_options, content=content)
    wait_for_completion(thread_id=thread_id_career_options, assistant_id=assistant_id)

    career_options_answer = retrieve_answer(thread_id=thread_id_career_options)
    career_options_json = json.loads(career_options_answer)

    return career_options_json

def career_pathway_part(content: str) -> dict:
    assistant_id = os.getenv('ASSISTANTS.career_pathway')
    thread_id_educational_requirements = create_thread()

    send_message(thread_id=thread_id_educational_requirements, content=content)
    wait_for_completion(thread_id=thread_id_educational_requirements, assistant_id=assistant_id)

    educational_requirements_answer = retrieve_answer(thread_id=thread_id_educational_requirements)
    educational_requirements_json = json.loads(educational_requirements_answer)

    return educational_requirements_json

def educational_recommendation_part(content: str) -> dict:
    assistant_id = os.getenv('ASSISTANTS.educational_recommendation')
    thread_id_market_analysis = create_thread()

    send_message(thread_id=thread_id_market_analysis, content=content)
    wait_for_completion(thread_id=thread_id_market_analysis, assistant_id=assistant_id)

    market_analysis_answer = retrieve_answer(thread_id=thread_id_market_analysis)
    market_analysis_json = json.loads(market_analysis_answer)

    return market_analysis_json

def action_plan_part(content: str) -> dict:
    assistant_id = os.getenv('ASSISTANTS.action_plan')
    thread_id_action_plan = create_thread()

    send_message(thread_id=thread_id_action_plan, content=content)
    wait_for_completion(thread_id=thread_id_action_plan, assistant_id=assistant_id)
    
    action_plan_answer = retrieve_answer(thread_id=thread_id_action_plan)
    action_plan_json = json.loads(action_plan_answer)

    return action_plan_json

