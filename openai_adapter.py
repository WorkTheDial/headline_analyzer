import openai
import os
from dotenv import load_dotenv
from retry import retry

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

class OpenAIAdapter:
    def __init__(self, system_prompt: str) -> None:
        # システムプロンプトを初期メッセージとして追加
        self.messages = [self._create_message("system", system_prompt)]  

    def _create_message(self, role: str, message: str) -> dict[str, str]:
        return {
            "role": role,
            "content": message
        }

    @retry(tries=3, delay=2, backoff=2, max_delay=60, exceptions=(TimeoutError,))
    def create_chat(self, question: str, model: str = "gpt-3.5-turbo", requests_timeout: int = 20) -> str:  # タイムアウト時間を20秒に増やす
        user_message = self._create_message("user", question)
        self.messages.append(user_message)

        try:
            res = openai.ChatCompletion.create(
                model=model,
                messages=self.messages,
                temperature=0.6,
                top_p=0.7,
                timeout=requests_timeout
            )
        except TimeoutError as e:
            raise TimeoutError("API request timed out") from e

        self.tokens = res["usage"]["total_tokens"]

        # APIからの応答をmessagesに追加して、会話の履歴を更新
        assistant_message = self._create_message("assistant", res["choices"][0]["message"]["content"])
        self.messages.append(assistant_message)

        return assistant_message["content"]