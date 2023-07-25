# Just-your-AI-assistant
基于SpeechRecognition、ChatGLM、VITS以及Sadtalker搭建的可自定义人设、形象以及声音的AI助手
# 基本介绍
主要参考[https://github.com/ruoqiu6/chat-with-Elysia2.0.git ](https://github.com/hhhwmws0117/GLM-VITS-SadTalker)
chatGLM-6B模型为清华大学开源，使用时请注意查看对应的使用需知，严格遵守使用规定
模型下载链接 点击这里 请仔细阅读说明根据自己的硬件配置下载对应模型
模型下载后请将模型及响应的文件放置在./chatglm-model路径下
参数下载方式可参考这里的视频
情绪设定和前序prompt设定暂时维持原作者default.json，可自行修改
vits模型来自up主“saya睡大觉中”，严禁商用

下载后请将模型以及配置文件放在./model-vits路径下
内部含有多种模型，可根据自己的需求进行选择 选择参数在soundmaker.py中的self.speaker_choice中进行修改
Sadtalker模型下载参考https://github.com/OpenTalker/SadTalker

模型下载：bash scripts/download_models.sh
自行部署项目时，使用下面命令以安装模块，注意：pip安装的torch可能为cpu版本，请按照torch官网的安装方式安装对应的cuda版本，如果出现模块兼容性问题，请使用python3.9.6

pip install -r requirements.txt

运行项目时，使用 python gradio.py 即可运行

在运行gradio文件后,通过点选选择对应的模式进行对话即可。需要注意的是，助理模式下，需要按顺序，填写问题，提供人物图片，生成对话，生成对话视频
## 对话模式
默认方式，采用传统一问一答的方式进行进行聊天
## 助理模式
按顺序执行，填写问题、提供人物图片、选择目标音色（目前共计805个声音）、生成对话、生成对话视频即可。需要注意的是，目前使用的sadtalker模型对二次元划分很不敏感，容易出现"can not detect the landmark from source image"的问题，这里建议重新训练，或者使用真人以及sd绘制的2.5d图片。
