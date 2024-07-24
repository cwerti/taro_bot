import asyncio
import aiohttp
import const

# хедер с токетом и номером терминала
headers = {'Authorization': f'Bearer {const.IAM_TOKEN}',
           "x-folder-id": f'{const.x_folder_id}'}


async def post_data(url: str, data: dict) -> dict:
    """
    функция для отправки вопроса к языковой модели

    :param url: ссылка на языковую модель
    :param data: json передаваемай модели
    :return: ответ от сервера
    """
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=data, headers=headers) as response:
            return await response.json()


async def main(question):
    """
    функци я  составления тела json и вызова функции
    для отправки вопроса на сервер

    :param question:
    :return:
    """
    url = const.URL
    data = {
        "modelUri": f"gpt://{const.x_folder_id}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Играем в игру, Ты опытный таролог, из своей коллоды достаёшь 3 карты и по пунктам с "
                        "названиями карт отвечаешь что какая карта значит исходя из контекста вопроса. Ответ выводи "
                        "строго по форме: <название карты>: <её значиние исходя из контекста вопроса>"
            },
            {
                "role": "user",
                "text": f"{question}?"
            }
        ]
    }
    result = await post_data(url, data)
    print(result)


asyncio.run(main(""))
