import asyncio

from services.deep_seek.api import make_request


async def simple_answer(message):

    def async_wrapper(message):
        return make_request(
            [
                {
                    "role": "system",
                    "content": "Ты — креативный и внимательный менеджер-помощник "
                               "с воображением писателя и чувством юмора опытного тимлида. "
                               "Отвечай на каждое сообщение так, будто это не первый контакт "
                               "с пользователем: тепло, дружелюбно и по делу. "
                               "Ты умеешь ставить задачи, давать чёткие рекомендации, "
                               "помогать организовывать хаос, и при этом не стесняешься "
                               "использовать метафоры, неожиданные сравнения и лёгкий юмор, "
                               "чтобы даже скучные вопросы превращались в приятный диалог. "
                               "Будь умным, структурным, но живым."
                },
                {"role": "user", "content": message},
            ],
            "deepseek-chat",
            temperature=0.65,
            max_tokens=128
        )

    response = await asyncio.to_thread(async_wrapper, message)

    return response.choices[0].message.content
