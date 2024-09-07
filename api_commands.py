from openai import OpenAI
import json
import os
from dotenv import load_dotenv
import time

# Load the API key from a file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def create_thread() -> str:
    thread = client.beta.threads.create()
    thread_id = thread.id
    return thread_id

def send_message(thread_id:str ,content:str) -> None:
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
        )

def wait_for_completion(thread_id, assistant_id) -> None:
    run = client.beta.threads.runs.create_and_poll(thread_id=thread_id, assistant_id=assistant_id)
    while run.status != 'completed':
        time.sleep(0.5)

    return run

def retrieve_answer(thread_id) -> str:
    response = client.beta.threads.messages.list(thread_id=thread_id)
    messages = response.data
    latest_message = messages[0]
    answer = latest_message.content[0].text.value
    
    return answer
