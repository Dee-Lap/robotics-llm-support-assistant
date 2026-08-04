# Robotics Support Assistant

An AI-powered troubleshooting assistant that helps robotics students diagnose hardware and software issues through natural language interaction.

<img width="423" height="127" alt="image" src="https://github.com/user-attachments/assets/dcedef75-f5bb-44d1-8526-7b053ab0917b" />


---

## Overview

During robotics competitions, students frequently need quick access to technical guidance while debugging hardware, software, and system integration issues. This project explores how large language models can support technical problem-solving by providing conversational troubleshooting assistance.

This repository is a clean-room reconstruction inspired by an LLM-powered conversational system I developed during my research experience. It recreates the core engineering concepts involved in building an AI assistant, including:

- Structured prompt engineering
- Hugging Face transformer-based inference
- Context-augmented generation
- Response processing
- Interaction logging
- Basic evaluation workflows

The goal of this project is to demonstrate an end-to-end LLM application pipeline while exploring practical challenges in AI reliability and usability.

---

## Demo

<img width="422" height="111" alt="image" src="https://github.com/user-attachments/assets/0626f66b-cae0-4734-8906-ffa85baeeb42" />


Example interaction:

**User:**
> My robot is moving slower than expected.

**Assistant:**
> We'll need to check the code execution logs, power connections, and the motors and sensors to see if there's anything wrong.

---

## Features

### Conversational AI Interface

- Chat-based interface for robotics troubleshooting questions
- Natural language interaction between students and the assistant
- Clean user/assistant message formatting

### Large Language Model Integration

The assistant uses Hugging Face Transformers for language generation.

The inference pipeline includes:

- Tokenization using `AutoTokenizer`
- Text generation using `AutoModelForCausalLM`
- Response decoding and cleanup

Workflow:

```
User Question
      |
      v
Prompt Construction
      |
      v
    Tokenizer
      |
      v
Transformer Model
      |
      v
Generated Response
      |
      v
Response Processing
```

### Context-Augmented Prompting

The assistant uses a structured robotics knowledge base to provide relevant troubleshooting information.

The prompt combines:

- Assistant instructions
- Robotics troubleshooting context
- Student question

Example:

```
Assistant Role:
You are a robotics support assistant.

Context:
- Check power connections
- Verify motors and sensors
- Review code execution logs

Question:
My robot sensor is not working.
```

This helps guide responses and reduces unsupported answers.

### Conversation Logging and Evaluation

The system records chatbot interactions for analysis.

Logged information includes:

- Timestamp
- User question
- Generated response
- Response length

Example:

```
2026-08-04 15:30:49.108988,My robot's motor is not spinning even though the code runs,"""Let me check the power connections first."" I will check the power connections and the motor is spinning now.",109.
```

The evaluation pipeline analyzes:

- Number of conversations
- Average response length
- Empty or failed responses

This provides a foundation for measuring chatbot behavior and improving reliability.

---

## System Architecture

```
              User
                |
                v
        Flask Web Application
                |
                v
        Prompt Construction
                |
                v
       Context Injection Layer
                |
                v
    Hugging Face Transformer Model
                |
                v
        Response Processing
                |
                v
       Conversation Logging
                |
                v
        Evaluation Pipeline
```

---

## Technology Stack

**Backend**
- Python
- Flask

**Artificial Intelligence / Machine Learning**
- Hugging Face Transformers
- PyTorch
- Large Language Models
- Prompt Engineering
- Natural Language Processing

**Frontend**
- HTML
- CSS
- JavaScript

**Data Processing**
- JSON
- CSV
- Pandas

---

## Project Structure

```
robotics-llm-support-assistant/
├── app.py                     # Flask application entry point
├── chatbot.py                 # LLM inference pipeline and chatbot logic
├── evaluation.py              # Conversation analysis and evaluation tools
├── requirements.txt
├── data/
│   ├── context.json           # Robotics troubleshooting knowledge base
│   └── conversations.csv      # Logged chatbot interactions
├── prompts/
│   └── prompt_template.txt    # Structured prompt design
├── templates/
│   └── index.html             # Web interface
└── static/
    └── style.css               # Interface styling
```

---

## How It Works

### 1. User Submits a Question

A student enters a robotics troubleshooting question through the web interface.

Example: `"My robot motor is not spinning."`

### 2. Context Retrieval

The system loads robotics troubleshooting information from a structured JSON knowledge base.

Example topics:

- Hardware connections
- Sensor troubleshooting
- Software debugging

### 3. Prompt Construction

The chatbot builds a structured prompt containing:

- Assistant behavior guidelines
- Relevant robotics context
- User question

### 4. Model Inference

The prompt is converted into tokens and passed to a Hugging Face language model.

The generated tokens are decoded into a natural language response.

### 5. Response Processing

Generated responses are cleaned before being displayed.

Processing includes:

- Removing prompt repetition
- Removing unnecessary formatting
- Improving conversational output

### 6. Logging and Evaluation

Each interaction is saved for later analysis.

Evaluation scripts provide basic measurements of chatbot usage and response characteristics.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd robotics-llm-support-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate (Windows):

```bash
venv\Scripts\activate
```

Activate (macOS/Linux):

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Example Questions

Try asking:

```
My servo motor is not moving.
```

```
My sensors are giving incorrect readings.
```

```
My robot code runs but the motors do not respond.
```

```
My robot loses power during competition.
```

---

## Design Decisions

**Why use an open-source Hugging Face model?**
Using open-source models provides transparency and flexibility while allowing experimentation with different model architectures.

**Why include context injection?**
General language models may produce unreliable technical advice. Providing robotics-specific context helps guide responses toward relevant troubleshooting information.

**Why log conversations?**
Interaction logging enables analysis of chatbot behavior and provides a foundation for improving response quality.

---

## Future Improvements

- Retrieval-Augmented Generation (RAG)
- Vector database integration
- Embedding-based document search
- Automated LLM evaluation metrics
- Improved safety and reliability checks
- Cloud deployment
- Larger instruction-tuned models

---

## Author

**Dalima Lappia**
Computer Science Student, Penn State University (Graduation: August 2026)

Interested in:
- Human-AI Interaction
- Responsible AI
- Large Language Models
- AI Systems Engineering
