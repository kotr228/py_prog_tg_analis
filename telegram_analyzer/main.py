import asyncio
from datetime import datetime, timedelta

from telegram_client import client, start_client
from analyzer import analyze_promise

async def main():
    await start_client()

    dialogs = await client.get_dialogs(limit=20)
    user_dialogs = [d for d in dialogs if d.is_user][:10]

    since_date = datetime.now() - timedelta(days=30)

    for dialog in user_dialogs:
        print(f"\nОбробка чату з: {dialog.name}")

        messages = []
        async for message in client.iter_messages(dialog.id, offset_date=since_date, reverse=True):
            if message.text:
                messages.append(message.text)

        full_text = "\n".join(messages)
        if not full_text.strip():
            print("Немає текстових повідомлень за останній місяць.")
            continue

        print("Відправляю текст на аналіз в OpenAI...")
        analysis_result = await analyze_promise(full_text)
        print(f"Аналіз:\n{analysis_result}")

if __name__ == "__main__":
    asyncio.run(main())
