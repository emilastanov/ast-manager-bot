from openai import OpenAI

from config import OPENAI_BASE_URL, OPENAI_API_KEY


def make_request(messages, model, temperature=0.7, max_tokens=256, stream=False, n=1):

    client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)

    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=stream,
        n=n
    )
