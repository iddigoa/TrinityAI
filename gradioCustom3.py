import gradio as gr
from openai import OpenAI
import os
import time
import random
import matplotlib.pyplot as plt
# https://www.gradio.app/guides/creating-a-custom-chatbot-with-blocks


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

def answer(state, state_chatbot, text):
    messages = state + [{
        'role': 'user',
        'content': text
    }]

    res = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    msg = res['choices'][0]['message']['content']

    new_state = [{
        'role': 'user',
        'content': text
    }, {
        'role': 'assistant',
        'content': msg
    }]

    state = state + new_state
    state_chatbot = state_chatbot + [(text, msg)]

    print(state)

    return state, state_chatbot, state_chatbot


def response(message, chat_history):
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # 선 그래프 그리기
    plt.plot(x, y)

    # 그래프에 제목과 레이블 추가
    plt.title('Graph')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig("test.png")
    # bot_message = gr.HTML("<img src='/file=test.png' style='width: 600px; height: 600px; max-width:none; max-height:none'></img>")
    bot_message = [("DATA/test.png")]
    # pngPath = os.path.join(os.path.dirname(__file__), 'Data/test.png')
    # bot_message = gr.Image(type="pil", value=pngPath)
    # bot_message.
    # bot_message = random.choice(["I love you", "I'm very hungry", ("DATA/avatar.png",)])
    chat_history.append((message, bot_message))
    # time.sleep(2)

    print(f"Chat History: {chat_history}")
    return "", chat_history

with gr.Blocks(css='#chatbot .overflow-y-auto{height:500px}') as demo:
    state = gr.State([{
        'role': 'system',
        'content': 'You are a helpful assistant.'
    }])
    state_chatbot = gr.State([])


    with gr.Row():
        gr.HTML("""<div style="text-align: center; max-width: 500px; margin: 0 auto;">
            <div>
                <h1>Trinity AI's ChatGPT-3.5</h1>
            </div>
            <p style="margin-bottom: 10px; font-size: 94%">
                Blog <a href="https://naver.com/">Be Original</a>
            </p>
        </div>""")

    with gr.Row():
        chatbot = gr.Chatbot(
            [],
            elem_id='chatbot',
            bubble_full_width=False,
            height=800,
            min_width=1000,
            avatar_images=(None, (os.path.join(os.path.dirname(__file__), "DATA/avatar.png"))),
        )

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder='Send a message...', scale=4)
        btn = gr.Button(value="Submit")
        btn.click(response, [txt, chatbot], [txt, chatbot])

    with gr.Row():
        clear = gr.ClearButton([txt, chatbot])

    with gr.Accordion("Open for More!"):
        # gr.Markdown("Look at me...")
        gr.Examples(
            ["Hi", "Hello"],
            txt
        )



    txt.submit(response, [txt, chatbot], [txt, chatbot])
    # txt.submit(answer, [state, state_chatbot, txt], [state, state_chatbot, chatbot])
    # txt.submit(lambda: '', None, txt)

demo.launch(debug=True)