# TestsYandexMarketAndroid

Окружение:

MacOS 12.5

PyCharm 2022.1.3

Appium Server GUI 1.22.3-4

Appium Inspector 2022.7.1

Android Studio 2021.2

Emulator Pixel 5 API 31 Android 12 1080x2340

Python 3.8

Pytest 7.1.3


Инструкция по запуску:

1. Загрузить репозиторий к себе на пк
2. В Android Studio создать эмулиркемое устройство Pixel 5 API 31 Android 12 1080x2340
3. Загрузить apk файл https://disk.yandex.ru/d/RaztIOz6TZtSyw
4. Разместить apk файл в папке App внутри проекта
5. В файле conftest.py прописать путь к apk файлу 
6. Тесты запускаются из терминала командой pytest -s -v tests/test.py 


Тест-кейсы находятся по ссылке: 
https://docs.google.com/spreadsheets/d/1uZTN2N6zPV-RjBdxNTP3qD5xtZvDkV7lDXaNky3j-a0/edit?usp=sharing


