import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from todo_service import get_tasks, add_task, update_task, delete_task

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FUNCTIONS = [
    {
        "name": "get_tasks",
        "description": "שליפת משימות עם אפשרות סינון",
        "parameters": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["pending", "in_progress", "done"]
                },
                "task_type": {
                    "type": "string",
                    "enum": ["personal", "work", "other"]
                }
            }
        }
    },
    {
        "name": "add_task",
        "description": "הוספת משימה חדשה",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "type": {
                    "type": "string",
                    "enum": ["personal", "work", "other"]
                },
                "start_date": {"type": "string"},
                "end_date": {"type": "string"}
            },
            "required": ["title", "type"]
        }
    },
    {
        "name": "update_task",
        "description": "עדכון משימה קיימת",
        "parameters": {
            "type": "object",
            "properties": {
                "task_id": {"type": "integer"},
                "updates": {"type": "object"}
            },
            "required": ["task_id", "updates"]
        }
    },
    {
        "name": "delete_task",
        "description": "מחיקת משימה",
        "parameters": {
            "type": "object",
            "properties": {
                "task_id": {"type": "integer"}
            },
            "required": ["task_id"]
        }
    }
]

def agent(query: str) -> str:
    first_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "אתה Agent לניהול משימות. "
                    "קבל טקסט חופשי והחלט איזו פונקציה יש להפעיל."
                )
            },
            {"role": "user", "content": query}
        ],
        functions=FUNCTIONS,
        function_call="auto"
    )

    message = first_response.choices[0].message

    if not message.function_call:
        return message.content

    func_name = message.function_call.name
    args = json.loads(message.function_call.arguments)

    if func_name == "get_tasks":
        result = get_tasks(**args)

    elif func_name == "add_task":
        result = add_task(args)

    elif func_name == "update_task":
        result = update_task(**args)

    elif func_name == "delete_task":
        result = delete_task(**args)

    else:
        result = "Unknown function"

    second_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query},
            message.model_dump(),
            {
                "role": "function",
                "name": func_name,
                "content": json.dumps(result, default=str, ensure_ascii=False)
            }
        ]
    )

    return second_response.choices[0].message.content