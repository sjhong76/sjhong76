import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LUAAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def get_system_prompt(self, step, user_name="주인님"):
        prompts = {
            "opening": "당신은 LUA입니다. 친절하게 이름과 생년월일을 요청하세요.",
            "trading": f"{user_name}님의 주문을 통역하세요. 종목, 수량, 구분을 명확히 추출해야 합니다.",
            "confirm": "주문 내용을 요약하고 최종 확인을 받으세요. 2-step 확인 원칙을 지키세요."
        }
        return prompts.get(step, "친절한 투자 조력자 LUA입니다.")

    def ask_llm(self, step, message, user_name="주인님"):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.get_system_prompt(step, user_name)},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content