import asyncio
import aiohttp
import const

headers = {'Authorization': f'Bearer {const.IAM_TOKEN}',
           "x-folder-id": f'{const.x_folder_id}'}


async def post_data(url, data):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=data, headers=headers) as response:
            return await response.text()


async def main(question):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completionAsync'
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
                "text": "Играем в игру, Ты опытный таролог, из своей коллоды достаёшь 3 карты и по пунктам с названиями карт отвечаешь что какая карта значит исходя из контекста вопроса. Ответ выводи строго по форме: <название карты>: <её значиние исходя из контекста вопроса>"
            },
            {
                "role": "user",
                "text": f"{question}?"
            }
        ]
    }
    result = await post_data(url, data)
    print(result)


if __name__ == "__main__":
    asyncio.run(main("я буду киберспортсменом по доте 2?"))
