# Just-your-AI-assistant
基于SpeechRecognition、ChatGLM、VITS以及Sadtalker搭建的可自定义人设、形象以及声音的AI助手
# 基本介绍
主要参考https://github.com/hhhwmws0117/GLM-VITS-SadTalker
chatGLM-6B模型为清华大学开源，使用时请注意查看对应的使用需知，严格遵守使用规定
模型下载链接 点击这里 请仔细阅读说明根据自己的硬件配置下载对应模型
模型下载后请将模型及响应的文件放置在./chatglm-model路径下

情绪设定和前序prompt设定暂时维持原作者default.json，可自行修改

vits模型来自up主“saya睡大觉中”，严禁商用

下载后请将模型以及配置文件放在./model-vits路径下
内部含有多种模型，可根据自己的需求进行选择 选择参数在soundmaker.py中的self.speaker_choice中进行修改
Sadtalker模型下载参考https://github.com/OpenTalker/SadTalker

模型下载：bash scripts/download_models.sh
自行部署项目时，使用下面命令以安装模块，注意：pip安装的torch可能为cpu版本，请按照torch官网的安装方式安装对应的cuda版本，如果出现模块兼容性问题，请使用python3.9.6

模型网盘下载链接：https://pan.baidu.com/s/1S0SsAsUJz89XHB_0SzPtTw提取码：amrw

pip install -r requirements.txt

运行项目前，请确保完成ffmpeg的安装，并完成环境变量的添加

运行项目时，使用 python main_gradio.py 即可运行

在运行gradio文件后,通过点选选择对应的模式进行对话即可。需要注意的是，助理模式下，需要按顺序，填写问题，提供人物图片，生成对话，生成对话视频
# 对话模式
默认方式，采用传统一问一答的方式进行进行聊天
### 界面
![img/1.png](https://github.com/zsdfaker/Just-your-AI-assistant/blob/main/img/1.png)
### 测试效果
![img/11.png](https://github.com/zsdfaker/Just-your-AI-assistant/blob/main/img/11.png)

# 助理模式

按顺序执行，填写问题、提供人物图片、选择目标音色（目前共计805个声音，也可以自行训练独有的声音，参考https://github.com/Plachtaa/VITS-fast-fine-tuning）

、生成对话、生成对话视频即可。需要注意的是，目前使用的sadtalker模型对2D图片划分很不敏感，容易出现"can not detect the landmark from source image"的问题，这里建议重新训练，或者使用真人图片、3D图片以及sd绘制的2.5d图片。
### 界面
![img/2.png](https://github.com/zsdfaker/Just-your-AI-assistant/blob/main/img/2.png)
### 测试效果
![img/12.png](https://github.com/zsdfaker/Just-your-AI-assistant/blob/main/img/12.png)
### 输出demo

![video](https://github.com/zsdfaker/Just-your-AI-assistant/blob/main/img/video-to-gif.gif)

# 注意事项
1.未修改sdatalker模型的话，最好使用真人、2.5D以及3D图片

2.SpeechRecognition需要梯子才可以正常使用

3.sadtalker的face render比较慢，可以通过设置batch_size稍微加快，但对显存消耗很大(batchsize取 4时大概需要总计12g显存)

# 更新
根据sadtalker原项目的issue添加了facerender模块，在不选face enhance的前提下处理10s左右音频，整个流程控制大改在1分半左右，速度上有了一定的提升。
从https://drive.google.com/file/d/1-0xOf6g58OmtKtEWJlU3VlnfRqPN9Uq7/view 下载 epoch_00190_iteration_000400000_checkpoint.pt 并放在checkpoints目录下

![img/newpage.png](https://github.com/zsdfaker/Just-your-AI-assistant/blob/main/img/newpage.png)
# todo
- [ ]  尝试流式的方式进行加速
- [ ]  进行界面优化
