from openai import AsyncOpenAI
from config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def analyze_promise(text: str) -> str:
    prompt = f"""
    Проаналізуй цей діалог і визнач, чи є тут обіцянка менеджера зробити прорахунок до кінця дня,
    і чи вона виконана (так/ні). Поясни коротко.

    Текст:
    {text}
    """

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return ""
