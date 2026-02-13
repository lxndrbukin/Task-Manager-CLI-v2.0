from config import load_config
import anthropic

config = load_config()

client = anthropic.Anthropic(api_key=config["ai"]["api_key"])

message = client.messages.create(
    model=config["ai"]["model"],
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content)