import asyncio
import logging
from datetime import datetime
from itertools import cycle
from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE, RECIPIENT_USERNAME, MESSAGE_TEMPLATE

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

WORDS = ["любимая", "жена", "девочка", "принцесса", "королева"]
word_cycle = cycle(WORDS)


async def send_message(client):
    try:
        word = next(word_cycle)
        message = MESSAGE_TEMPLATE.format(word)
        await client.send_message(RECIPIENT_USERNAME, message)
        logger.info(f'Сообщение "{message}" успешно отправлено пользователю {RECIPIENT_USERNAME} в {datetime.now()}')
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения: {e}")


async def main():
    client = TelegramClient('session', API_ID, API_HASH)

    await client.start(phone=PHONE)
    logger.info("Клиент успешно запущен!")
    logger.info(f"Сообщения будут отправляться пользователю {RECIPIENT_USERNAME} каждый час")
    logger.info(f"Слова будут меняться по циклу: {', '.join(WORDS)}")

    while True:
        await send_message(client)
        logger.info("Ожидание 1 час до следующей отправки...")
        await asyncio.sleep(3600)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Программа остановлена пользователем")
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
