![GitHub Repo stars](https://img.shields.io/github/stars/GRusl/Dossier)
![GitHub](https://img.shields.io/github/license/GRusl/Dossier)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/GRusl/Dossier)

![GitHub repo size](https://img.shields.io/github/repo-size/GRusl/Dossier)
![GitHub all releases](https://img.shields.io/github/downloads/GRusl/Dossier/total)

# Dossier

[ru](../readme.md) • [tat](/readme/readme_tat.md)

_Create a dossier in a couple of clicks with access to view and edit
from anywhere in the world_

You can upload this project to Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

You can also check out a more advanced version
of the project on **Django**:
https://github.com/YandexLyceumPP/Resume

## Content
* [Content](#Content)
* [Installation and launch](#Installation-and-launch)
  * [Copying repository](#Copying-repository)
  * [Installing dependencies](#Installing-dependencies)
  * [Launch](#Launch)
* [Launching on Heroku](#Launching-on-Heroku)
* [ngrok](#ngrok)

## Installation and launch

### Copying repository

```shell
git clone https://github.com/GRusl/Dossier.git
```

### Installing dependencies

```shell
pip install -r requirements.txt
```

### Launch

```shell
python app.py
```

## Launching on Heroku

1. Register on Heroku. Then [create](https://dashboard.heroku.com/apps) 
new application
2. Come up with a name for the app and choose a location
3. Perform the previously mentioned installation

| :exclamation:  Don't forget to specify the environment variables |
|------------------------------------------------------------------|

### ngrok

1. Register or log in on [website](https://ngrok.com)
2. You need to download the executable file of the application
for the desired operating system from the [download page](https://ngrok.com/download )
3. Unpack the archive and in the terminal window go to the folder
with the unpacked utility
4. Copy the command from the Settings and Installations page to configure ngrok
to work with your account, and run it in the terminal
<br>It looks like this: `ngrok authtoken 37srTxReQIIwsPMX67ZiY1E5TMH_7KbpfVGLcg9rRDd2hwgh1`
5. Now let's launch the application and execute it in the terminal: `ngrok http 5000`
