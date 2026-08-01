import json


def load_context():
    with open("data/context.json", "r") as file:
        return json.load(file)


def generate_response(question):
    context = load_context()

    response = f"""
Based on the robotics knowledge base:

{context}

Student question:
{question}

Answer:
This is a placeholder response. The Hugging Face model will be connected here.
"""

    return response
