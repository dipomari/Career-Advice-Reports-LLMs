from api_commands import create_thread, send_message, wait_for_completion, retrieve_answer
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')


def personal_assessment_part(content: str) -> dict:
    """
    This function takes the content and genereates a dictionary
        {
            "personal_assessment": {
                "skills": ,
                "interests": ,
                "personality_traits": ,
                "career_values":,
                "long_term_goals": 
            }
        }
    """


    assistant_id = os.getenv('ASSISTANTS.personal_assessment')
    thread_id_personal_assessment_= create_thread()

    send_message(thread_id=thread_id_personal_assessment_, content="content")
    wait_for_completion(thread_id=thread_id_personal_assessment_, assistant_id=assistant_id)

    personal_assessment_answer = retrieve_answer(thread_id=thread_id_personal_assessment_)
    personal_assessment_json = json.loads(personal_assessment_answer)

    return personal_assessment_json

def career_options_part(content: str) -> dict:
    """
    This function takes the content and genereates a dictionary
        {
            "career_options": {
                "insustry_overview": ,
                "potential_roles":{
                    "role_1": ,
                    "role_2": ,
                    "role_3": ,
                },
                "growth_opportunities": , 
                 "justification": ,
            }
        }
    """

    assistant_id = os.getenv('ASSISTANTS.career_options')
    thread_id_career_options = create_thread()

    send_message(thread_id=thread_id_career_options, content="content")
    wait_for_completion(thread_id=thread_id_career_options, assistant_id=assistant_id)

    career_options_answer = retrieve_answer(thread_id=thread_id_career_options)
    career_options_json = json.loads(career_options_answer)

    return career_options_json

def educational_requirements_part(content: str) -> dict:
    """
    This function takes the content from Career Options and genereates a dictionary
        {
            "educational_requirements": {
                "necessary_education": ,
                "training_programs": ,
                "continuing_education": ,
            }
        }
    """

    assistant_id = os.getenv('ASSISTANTS.educational_requirements')
    thread_id_educational_requirements = create_thread()

    send_message(thread_id=thread_id_educational_requirements, content="content")
    wait_for_completion(thread_id=thread_id_educational_requirements, assistant_id=assistant_id)

    educational_requirements_answer = retrieve_answer(thread_id=thread_id_educational_requirements)
    educational_requirements_json = json.loads(educational_requirements_answer)

    return educational_requirements_json

def market_analysis_part(content: str) -> dict:
    """
    This function takes the content and genereates a dictionary
        {
            "market_analysis": {
                "job_market": ,
                "salary_range": 
                "job_growth": ,
            }
        }
    """

    assistant_id = os.getenv('ASSISTANTS.market_analysis')
    thread_id_market_analysis = create_thread()

    send_message(thread_id=thread_id_market_analysis, content="content")
    wait_for_completion(thread_id=thread_id_market_analysis, assistant_id=assistant_id)

    market_analysis_answer = retrieve_answer(thread_id=thread_id_market_analysis)
    market_analysis_json = json.loads(market_analysis_answer)

    return market_analysis_json

def action_plan_part(content: str) -> dict:
    """
    This function takes the content and genereates a dictionary
        {
            "action_plan": {
                "short_term_goals": ,
                "long_term_goals": ,
                "next_steps": ,
            }
        }
    """

    assistant_id = os.getenv('ASSISTANTS.action_plan')
    thread_id_action_plan = create_thread()

    send_message(thread_id=thread_id_action_plan, content="content")
    wait_for_completion(thread_id=thread_id_action_plan, assistant_id=assistant_id)
    
    action_plan_answer = retrieve_answer(thread_id=thread_id_action_plan)
    action_plan_json = json.loads(action_plan_answer)

    return action_plan_json


def question_assistant() -> list:
    assistant_id = os.getenv('ASSISTANTS.question_assistant')

    thread_id_question_assistant = create_thread()

    q_and_a = []
    q_and_a_pairs = ""
    while True:
        wait_for_completion(thread_id=thread_id_question_assistant, assistant_id=assistant_id)
        next_question = "Queston: " + retrieve_answer(thread_id=thread_id_question_assistant)
        
        if "TERMINATE" in next_question:
            break
        
        print(next_question)

        answer = input("Answer: ")
        q_and_a.append((next_question, answer))
        send_message(thread_id=thread_id_question_assistant, content=answer)
    
    for pair in q_and_a:

        question = pair[0]
        answer = pair[1]

        q_and_a_pairs += f"{question} Answer: {answer} "

        q_and_a_pairs = q_and_a_pairs.strip()
        
    return q_and_a_pairs
