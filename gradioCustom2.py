import gradio as gr
from huggingface_hub import InferenceClient
from openai import OpenAI

if __name__ == '__main__':
    # llm_endpoint = ""
    # client = InferenceClient(open)
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key="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",
    )

    def inference(query, history):
        init_prompt = """당신은 Network 전문가인 AI 어시스턴트 "Trinity AI"로서 항상 존중과 정직을 바탕으로 대화해야 합니다.
답변은 사회적 편견 없이, 긍정적인 방향으로 이뤄져야 합니다. 안전한 범위에서 가장 도움이 되는 답변을 해야합니다.
만약 질문에 맥락이 없거나, 사실이 아니라면, 잘못된 답변을 하기 보다는 그 이유를 설명해야 합니다.
답을 모르는 경우에는, 잘못된 정보를 공유하지 않아야 합니다. 답변은 대화하듯이 해주세요.
아래 ### ### 안에 있는 Data 정보를 활용해서 답변해주세요.
"""

        message = f"""{init_prompt}
{query}
"""

        # partial_message = ""
        # for token in client.text_generation(message, max_new_tokens=1000, stream=True):
        #     partial_message += token
        #     yield partial_message

        history_openai_format = []
        for human, assistant in history:
            history_openai_format.append({"role": "user", "content": human })
            history_openai_format.append({"role": "assistant", "content":assistant})
        history_openai_format.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=history_openai_format,
            temperature=1.0,
            stream=True
        )

        partial_message = ""
        for chunk in response:
            if len(chunk['choices'][0]['delta']) != 0:
                partial_message = partial_message + chunk['choices'][0]['delta']['content']
                yield partial_message

    gr.ChatInterface(
        inference,
        chatbot=gr.Chatbot(height=300),
        textbox=gr.Textbox(placeholder="Chat with me!", container=False, scale=7),
        # description="TrintyAI Chatbot",
        title="Trinity AI Chatbot",
        examples=[
            "HIHI",
        ],
        retry_btn="Retry",
        undo_btn="Undo",
        clear_btn="clear",
        theme=gr.themes.Soft()
    ).queue().launch()