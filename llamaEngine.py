from llama_cpp import Llama
from prompts import SYSTEM_PROMPT


def get_model(
        model_path="model-q4_K.gguf",
        n_ctx=8192,
):
    return Llama(
        model_path=model_path,
        n_ctx=n_ctx,
        verbose=True,
    )


class AiEngine:
    def __init__(self):
        self.model = get_model()
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
