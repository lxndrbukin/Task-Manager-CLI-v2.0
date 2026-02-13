from ai.claude import claude_client
import json

def clean_json_response(text):
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def extract_task_from_text(user_input, config):
    try:
        prompt = f"""Extract task information from this input and return ONLY valid JSON.

            User input: "{user_input}"
            
            Return JSON with these EXACT fields:
            - title: Concise task title (string)
            - desc: Additional details (string, empty if none)
            - priority: Must be "High", "Medium", or "Low"  
            - status: Must be "Pending", "In Progress", or "Completed"
            
            Rules:
            - Default priority: "Medium" if not specified
            - Default status: "Pending" if not specified
            - Return ONLY the JSON, no other text
            
            JSON:"""

        if config["ai"]["provider"] == "anthropic":
            message = claude_client(prompt, config)
            response_text = message.content[0].text
        else:
            print(f"Unsupported AI provider: {config['ai']['provider']}")
            return None

        task_data = json.loads(clean_json_response(response_text))

        required_fields = ["title", "desc", "priority", "status"]
        if all(field in task_data for field in required_fields):
            return task_data
        else:
            return None

    except Exception as e:
        print(f"AI extraction error: {e}")
        return None