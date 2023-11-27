import gradio as gr
import time, random

global global_code

def getRadioButton(choice):
    global index
    if choice == "형상정보시스템":
        print("형상정보시스템")
        index = 1
    elif choice == "운영정보시스템":
        print("운영정보시스템")
        index = 2
    elif choice == "모니터링정보시스템":
        print("모니터링정보시스템")
        index = 3

def vote(data: gr.LikeData):
    if data.liked:
        print("You upvoted this response: " + data.value)
    else:
        print("You downvoted this response: " + data.value)


def inference(message, history):
    sentence = ["Nice ","to ","meet ","you!"]
    history = ""
    return "Nice to meet you!"
    # for word in sentence:
    #     time.sleep(0.3)
    #     history += word
    #     yield history


def fake_gan():
    print(mcode)
    exec(mcode)
    # 결과값을 저장한다.
    global result
    import matplotlib.pyplot as plt
    result = plt.gcf().savefig("graph_image.png")
    time.sleep(1)
    images = [
        ("./graph_image.png", "label 0")
    ]
    return images

if __name__ == '__main__':
    mcode = ""
    with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple", neutral_hue="purple")) as demo:

        with gr.Row():
            with gr.Column():
                chatbot = gr.Chatbot()
                msg = gr.Textbox()
                clear = gr.ClearButton([msg, chatbot])
                radio = gr.Radio(["형상정보시스템","운영정보시스템","모니터링정보시스템"],show_label=False)
                radio.change(fn=getRadioButton, inputs=radio)
                # # 출력하고싶으면 outputs에다가 gr 객체 넣으면 됨. 함수에서 return도 해줘야함.


            from PIL import Image
            with gr.Column():
                gallery = gr.Gallery(height="auto", columns=[1], rows=[1], object_fit="contain")
                btn = gr.Button("Generate images", scale=0)
                btn.click(fake_gan, None, gallery)


        def respond(message, chat_history):
            bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])

            if index == 3:
                global mcode
                mcode = message
                print(mcode)


            chat_history.append((message, bot_message))
            time.sleep(2)


            return "", chat_history

        msg.submit(respond, [msg, chatbot], [msg, chatbot])




    demo.launch()