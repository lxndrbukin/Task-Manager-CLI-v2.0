from anthropic import Anthropic

def claude_client(prompt, config):
    client = Anthropic(api_key=config["ai"]["api_key"])

    message = client.messages.create(
        model=config["ai"]["model"],
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text