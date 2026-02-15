from openai import OpenAI

def grok_client(prompt, config):
    client = OpenAI(api_key=config["ai"]["api_key"], base_url="https://api.x.ai/v1")

    message = client.chat.completions.create(
        model=config["ai"]["model"],
        max_completion_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.choices[0].message.content