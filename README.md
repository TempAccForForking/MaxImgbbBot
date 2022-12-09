
<p align="center"><a href="#"><img src="https://pangnote.com/icon/QLkXt3iaKFLiOwdN8.png" width="150"></a></p> 
<h1 align="center"><b>ImgBB-Bot</b></h1>
<h4 align="center">Telegram Bot That Hosts Your Image On imgbb.com And Returns Link</h4>

# 🤖 Demo:
<a href="https://t.me/imgbbXbot"><img src="https://img.shields.io/badge/@imgbbXbot-1a66ff?style=for-the-badge&logo=telegram&logoColor=white"></a>
# 👨‍💻 Deploy:

<details>	
  <summary><b>❤ Deploy Your Own Bot :</b></summary>

# Star 🌟 Fork 🍴 & Deploy

<a name="deploy-to-koyeb"></a>

<h2> <b><img src="https://user-images.githubusercontent.com/87380104/205833766-633843a2-d802-4c72-8732-70d826d5c144.png" height="20" width="20">  Deploy on Koyeb</b> </h2>

<b>Run program totally for free on Koyeb with single click deployment button!</b>
#### **1. Click the following one-click deployment button:**
[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/apps/deploy?type=docker&image=docker.io/maxparker9/imgbot&tag=latest&name=imgbbot&ports=8000;http;/&env%5BPORT%5D=8000&env%5BAPI_ID%5D=Enter-Telegram-API-ID&env%5BAPI_HASH%5D=Enter-API-Hash&env%5BBOT_TOKEN%5D=Enter-BOT-TOKEN&env%5BAPI%5D=Enter-ImgBB-API-Key&env%5B%5D=Enter-ImgBB-API-Key)
#### **2. Fill the given variables as [discussed above](#variables) and click `Deploy`.**
![image](https://i.ibb.co/xjTy4Cn/Document-695.jpg)
#### **3. While deployment, you can choose `Nano` instance type since it requires <256 RAM.**
![image](https://user-images.githubusercontent.com/87380104/205841570-6a43c020-eecf-4574-8c53-41f9454b5d79.png)
#### **⛔NOTE: This method uses ready-to-use Docker Image made specially for Koyeb, hence any change requires building of new image with NPM's `http-server` or `Flask` to listen on port `8000` & `8080`.**
### -Self-hosting (For Devs)

```python3
## Clone The Repo
git clone https://github.com/TempAccForForking/MaxImgbbBot
## Enter The Directory
cd ImgBB-Bot
## Install Requirements
pip3 install -r requirements.txt
## Run The Bot
python3 main.py
```
### -Mandatory Configs 
```
[+] Make Sure You Add All These Mandatory Vars. 
    [-] API_ID:     You can get this value from https://my.telegram.org
    [-] API_HASH :  You can get this value from https://my.telegram.org
    [-] BOT_TOKEN : You can get this value from https://t.me/botfather
    [-] API: You Can Get An API Key From https://api.imgbb.com.
[+] Bot will not work without setting the mandatory vars.
```
</details>

### **❤️Credits & Thanks**
**[AmineSoukara](https://github.com/AmineSoukara/): The Original Developer of the [repo](https://github.com/AmineSoukara/ImgBB-Bot)**
