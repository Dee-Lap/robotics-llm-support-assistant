import json
import csv
from datetime import datetime

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "HuggingFaceTB/SmolLM2-360M-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def load_context():
    with open("data/context.json", "r") as file:
        return json.load(file)


def load_prompt_template():
    with open("prompts/prompt_template.txt", "r") as file:
        return file.read()


def build_prompt(question):
    context = format_context(load_context())
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
            response,
            len(response)
        ])


def generate_response(question):

    prompt = build_prompt(question)

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.7,
        do_sample=True
    )

    generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]

    response = tokenizer.decode(
    generated_tokens,
    skip_special_tokens=True
)
    response = clean_response(response)

    if validate_response(response):
        save_conversation(question, response)

    return response

def format_context(context):
    lines = []

    competition = context["robotics_competition"]["description"]
    lines.append(f"Competition: {competition}\n")

    lines.append("Hardware Tips:")
    for item in context["hardware"]:
        lines.append(f"- {item}")

    lines.append("\nSoftware Tips:")
    for item in context["software"]:
        lines.append(f"- {item}")

    return "\n".join(lines)

def clean_response(response):

    remove_patterns = [
        "Response:",
        "Answer:",
        "Assistant:"
    ]

    for pattern in remove_patterns:
        response = response.replace(pattern, "")

    return response.strip()