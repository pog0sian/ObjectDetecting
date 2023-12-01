[app]

# (обязательно) Имя вашего приложения
title = ObjectDetecting

# (обязательно) Пакет вашего приложения
package.name = objectdetectingapp

# (обязательно) Версия вашего приложения
package.version = 1.0

# (обязательно) Код приложения
package.domain = org.example

# Источники файлов, включаемые в пакет приложения
source.include_exts = py,kv,atlas,jpg,png

# Используемый язык (опционально)
source.lang = ru

# Путь к вашему основному файлу .py
source.main.filename = main.py

# Добавьте источник (указан в `source`), который не следует включать в пакет
source.exclude_exts = spec,kv

# Дополнительные данные, для включения в пакет
source.include_patterns = images/*.png

# Зависимости для сборки (через `requirements =`)
requirements = kivy

# Зависимости с помощью системы пакетов
# (через `apt-get = ...`, `apt = ...`, `urpmi = ...`, `yum = ...`, `pip = ...` или `pip3 = ...`)
#requirements.apt = build-essential

# Найденные порты сервиса Android, которые должны быть доступны на хосте (опционально, можно вручную настроить)
# android.permissions = INTERNET

# Список сервисов для запуска приложения (опционально)
services = CAMERA

# Дополнительные параметры для buildozer (например, задать версию android)
# (опционально)
#android.ndk_path = /opt/android-ndk-r9c
#android.sdk_path = /opt/android-sdk
#android.sdk_path = /home/kivy/Android/sdk
#android.minapi = 9
#android.targetapi = 19
#android.permissions = CAMERA