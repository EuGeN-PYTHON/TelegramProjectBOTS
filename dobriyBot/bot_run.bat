@echo off

call %~dp0telegram_bot\venv\bin\activate

cd %~dp0telegram_bot

set TOKEN = 1234

python3 bot_telegram.py

pause 