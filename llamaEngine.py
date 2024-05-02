from llama_cpp import Llama

SYSTEM_PROMPT = """Ты — Виталий, русскоязычный автоматический ассистент по Информационной безопасности.
Твоя основная задача анализировать новости по теме "Информационная безопасность" и формировать на основе них отчет в формате Json.
Структура Json:
{
    "date": "Дата",
    "threatType": "Тип угрозы",
    "countries": "Страны распространения",
    "typeOfDistribution": "Тип распространения"
    "description": "Краткое описание"
}
Правила заполнения полей Json:
- Дата берется из текста. Если в тексте нет информации, то заполни поле значением 'null';
- Тип угрозы может принимать одно из следующих значений: нежелательный контент, несанкционированный доступ, yтечки информации, потеря данных, мошенничество, кибервойны, кибертерроризм;
- Страны распространения должны выводиться из текста новости, но если в тексте нет информации о стране, то заполни поле значением 'Любые страны';
- Тип распространения должен выводиться из текста, если в тексте нет информации то выведи свои предположения, но кратко аргументируй их.
- Краткое описание формируется на основе текста, но оно должно быть не больше 20-30 слов.
"""

def get_model(
        model_path="model-q4_K.gguf",
        n_ctx=8192,
):
    return Llama(
        model_path=model_path,
        n_ctx=n_ctx,
        n_parts=1,
        verbose=True,
        device = "cuda"
    )


class AiEngine:
    def __init__(self):
        self.model = get_model()
        self.model.to("cuda")
        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        self.top_k: int = 30
        self.top_p: float = 0.9
        self.temperature: float = 0.6
        self.repeat_penalty: float = 1.1

    def ask_and_response(self, question: str):
        final_result = ""
        self.messages.append({"role": "user", "content": question})
        for part in self.model.create_chat_completion(
                self.messages,
                temperature=self.temperature,
                top_k=self.top_k,
                top_p=self.top_p,
                repeat_penalty=self.repeat_penalty,
                stream=True,
        ):
            delta = part["choices"][0]["delta"]
            if "content" in delta:
                final_result += delta["content"]
                print("-", end="", flush=True)
        print()

        return final_result
