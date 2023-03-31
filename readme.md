![GitHub Repo stars](https://img.shields.io/github/stars/GRusl/Dossier)
![GitHub](https://img.shields.io/github/license/GRusl/Dossier)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/GRusl/Dossier)

![GitHub repo size](https://img.shields.io/github/repo-size/GRusl/Dossier)
![GitHub all releases](https://img.shields.io/github/downloads/GRusl/Dossier/total)

# Dossier
_Создавайте досье за пару кликов с доступом для просмотра и редактирования
из любой точки планеты_

Вы можете загрузить этот проект на Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Вы также можете ознакомиться с более продвинутой версией 
проекта на **Django**:
https://github.com/YandexLyceumPP/Resume

## Содержание
* [Содержание](#Содержание)
* [Установка и запуск](#Установка-и-запуск)
  * [Копирование репозитория](#Копирование-репозитория)
  * [Установка зависимостей](#Установка-зависимостей)
  * [Запуск](#Запуск)
* [Запуску на Heroku](#Запуску-на-Heroku)
* [ngrok](#ngrok)

## Установка и запуск 

### Копирование репозитория

```shell
git clone https://github.com/GRusl/Dossier.git
```

### Установка зависимостей

```shell
pip install -r requirements.txt
```

### Запуск

```shell
python app.py
```

## Запуску на Heroku

1. Зарегистрируйтесь на Heroku. Затем [создайте](https://dashboard.heroku.com/apps) 
новое приложение
2. Придумайте название для приложения и выберите местоположение
3. Проведите ранее сказанную установку

| :exclamation:  Не забудьте указать переменные окружения |
|---------------------------------------------------------|

### ngrok

1. Зарегестрируйтесб или войтиде в систему на [сайте](https://ngrok.com)
2. Вам необходимо загрузить исполняемый файл приложения
для желаемой операционной системы со [страницы загрузки](https://ngrok.com/download )
3. Распакуйте архив и в окне терминала перейдите в папку
с распакованной утилитой
4. Скопируйте команду со страницы Настройки и установки, чтобы настроить ngrok
для работы с вашей учетной записью, и запустите ее в терминале
<br>Она выглядит так: `ngrok authtoken 37srTxReQIIwsPMX67ZiY1E5TMH_7KbpfVGLcg9rRDd2hwgh1`
5. Теперь давайте запустим приложение и выполним его в терминале: `ngrok http 5000`
