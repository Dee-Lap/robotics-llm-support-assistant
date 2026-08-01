import json
import csv
from datetime import datetime


def load_context():
    with open("data/context.json", "r") as file:
        return json.load(file)


def load_prompt_template():
    with open("prompts/prompt_template.txt", "r") as file:
        return file.read()


def build_prompt(question):
    context = load_context()
    template = load_prompt_template()

    prompt = template.format(
        context=context,
        question=question
    )

    return prompt


def validate_response(response):
    """
    Basic validation step.
    Later this can become an LLM evaluation step.
    """

    if len(response.strip()) < 20:
        return False

    return True


def save_conversation(question, response):
    with open("data/conversations.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            question,
            response
        ])


def generate_response(question):

    prompt = build_prompt(question)

    # Placeholder until Hugging Face is connected
    response = f"""
Generated response using prompt:

{prompt}

[LLM RESPONSE WILL GO HERE]
"""

    if validate_response(response):
        save_conversation(question, response)

    return response