import gradio as gr
import webbrowser
import argparse
import sys
import time
from parse import Parse
from src.gradio_demo import SadTalker  
import speech_recognition as sr
try:
    import webui  # in webui
    in_webui = True
except:
    in_webui = False
ps = Parse()
# 创建一个Recognizer对象
r = sr.Recognizer()
sad_talker = SadTalker('checkpoints', 'src/config', lazy_load=True)
text = "语音输入或键盘输入"

with gr.Blocks() as app:
    gr.Markdown(
        "# <center> Just your AI assistant\n"
    )
    with gr.Tabs():
        with gr.TabItem("对话模式"):
            chatbot = gr.Chatbot()
            with gr.Row():
                with gr.Column(scale=4):
                    with gr.Column(scale=12):     
                        msg = gr.Textbox(label="输入信息")
                    with gr.Column(min_width=32, scale=1):
                        generate_chat = gr.Button("generate", variant="primary")
                with gr.Column(scale=1):
                    clear = gr.ClearButton([msg, chatbot])
                    max_length = gr.Slider(label="max length", minimum=0, maximum=4096, value=2048, step=1.0, interactive=True)
                    top_p = gr.Slider(label="top p", minimum=0, maximum=1, value=0.7, step=0.01, interactive=True)
                    temperature = gr.Slider(label="temperature", minimum=0, maximum=1, value=0.95, step=0.01, interactive=True)
            def respond(message, max_length, top_p, temperature, chat_history):
                bot_message = ps.getText(message, max_length, top_p, temperature)
                chat_history.append((message, bot_message))
                time.sleep(2)
                return "", chat_history
            generate_chat.click(respond,
                    inputs=[msg, max_length, top_p, temperature, chatbot],
                    outputs=[msg, chatbot])
                    
                       
        with gr.TabItem("助理模式"):
            with gr.Row().style(equal_height=False):
                with gr.Column():
                    def stt():
                        # 使用麦克风录音
                        with sr.Microphone() as source:
                            print("请说话：")
                            audio = r.listen(source)
                        # 将语音转换为文本
                        try:
                            text = r.recognize_google(audio, language='zh-CN')
                            # print("你说的是：" + text)
                        except sr.UnknownValueError:
                            print("无法识别你的语音")
                        except sr.RequestError as e:
                            print("无法连接到Google API，错误原因：" + str(e))
                        return text
                    
                    textbox = gr.TextArea(label="对话内容",
                        placeholder="Type your sentence here",
                        value=text, elem_id=f"tts-input")
                    sttbutton = gr.Button("audio2txt")
                    sttbutton.click(stt, None, textbox)


                    with gr.Row():
                        with gr.Column():
                            max_length = gr.Slider(label="max length", minimum=0, maximum=4096, value=2048, step=1.0, interactive=True)
                            top_p = gr.Slider(label="top p", minimum=0, maximum=1, value=0.7, step=0.01, interactive=True)
                            temperature = gr.Slider(label="temperature", minimum=0, maximum=1, value=0.95, step=0.01, interactive=True)
                        # with gr.Column():
                        #     sc = gr.Slider(label="speaker_choice", minimum=0, maximum=804, step=1, value=422, interactive=True)
                        #     ns = gr.Slider(label="emotion change", minimum=0.1, maximum=1.0, step=0.1, value=0.6, interactive=True)
                        #     nsw = gr.Slider(label="noise_scale", minimum=0.1, maximum=1.0, step=0.1, value=0.668, interactive=True)
                        #     ls = gr.Slider(label="language speed", minimum=0.1, maximum=2.0, step=0.1, value=1.2, interactive=True)
                    with gr.Tabs(elem_id="sadtalker_source_image"):
                        with gr.TabItem('Upload image'):
                            with gr.Row():
                                source_image = gr.Image(label="Source image", source="upload", type="filepath", elem_id="img2img_image").style(width=512)

                with gr.Column():
                    text_output = gr.Textbox(label="回复信息")
                    sc = gr.Slider(label="speaker_choice", minimum=0, maximum=804, step=1, value=422, interactive=True)
                    ns = gr.Slider(label="emotion change", minimum=0.1, maximum=1.0, step=0.1, value=0.6, interactive=True)
                    nsw = gr.Slider(label="noise_scale", minimum=0.1, maximum=1.0, step=0.1, value=0.668, interactive=True)
                    ls = gr.Slider(label="language speed", minimum=0.1, maximum=2.0, step=0.1, value=1.2, interactive=True)
                    audio_output = gr.Audio(label="音频信息", elem_id="tts-audio")
                    generate = gr.Button("生成对话")
                    # upload = gr.UploadButton('读取聊天记录', file_types=['file'])
                    # logdown = gr.Button("记录当前聊天记录")
                    # upload.upload(ps.loadHistory, inputs=[upload])
                    # logdown.click(ps.logContent)
                    # # sttbutton.click(stt,)
                    generate.click(ps.PipeChat,
                            inputs=[textbox, max_length, top_p, temperature, sc, ns, nsw, ls],
                            outputs=[text_output, audio_output])


                with gr.Column(variant='panel'): 
                    with gr.Tabs(elem_id="sadtalker_checkbox"):
                        with gr.TabItem('Settings'):
                            gr.Markdown("need help? please visit website for more detials")
                            with gr.Column(variant='panel'):
                                # width = gr.Slider(minimum=64, elem_id="img2img_width", maximum=2048, step=8, label="Manually Crop Width", value=512) # img2img_width
                                # height = gr.Slider(minimum=64, elem_id="img2img_height", maximum=2048, step=8, label="Manually Crop Height", value=512) # img2img_width
                                with gr.Row():
                                    pose_style = gr.Slider(minimum=0, maximum=46, step=1, label="Pose style", value=0) #
                                    exp_weight = gr.Slider(minimum=0, maximum=3, step=0.1, label="expression scale", value=1) # 
                                    blink_every = gr.Checkbox(label="use eye blink", value=True)
                                with gr.Row():
                                    size_of_image = gr.Radio([256, 512], value=256, label='face model resolution', info="use 256/512 model?") # 
                                    preprocess_type = gr.Radio(['crop', 'resize','full', 'extcrop', 'extfull'], value='crop', label='preprocess', info="How to handle input image?")
                                with gr.Row():
                                    is_still_mode = gr.Checkbox(label="Still Mode (fewer head motion, works with preprocess `full`)")
                                    facerender = gr.Radio(['facevid2vid','pirender'], value='facevid2vid', label='facerender', info="which face render?")
                                with gr.Row():
                                    batch_size = gr.Slider(label="batch size in generation", step=1, maximum=10, value=2)
                                    enhancer = gr.Checkbox(label="GFPGAN as Face enhancer")                                  
                                submit = gr.Button('Generate', elem_id="sadtalker_generate", variant='primary')                      
                    with gr.Tabs(elem_id="sadtalker_genearted"):
                            gen_video = gr.Video(label="Generated video", format="mp4").style(width=256)     
        submit.click(
                fn=sad_talker.test, 
                inputs=[source_image,
                        audio_output,
                        preprocess_type,
                        is_still_mode,
                        enhancer,
                        batch_size,                            
                        size_of_image,
                        pose_style,
                        facerender,
                        exp_weight
                        ], 
                outputs=[gen_video]
                )         
webbrowser.open("http://127.0.0.1:7860")
app.launch()