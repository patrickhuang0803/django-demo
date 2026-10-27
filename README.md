# django-demo

## 功能

- `/login/`：登入
- `/register/`：註冊（成功後自動登入）
- `/logout/`：登出
- `/password-change/`：修改密碼（需先登入，登入後導覽列會出現【修改密碼】）

## 執行方式

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

開啟 http://127.0.0.1:8000/

## 說明

1. 【修改密碼】部分：需輸入舊密碼、新密碼與確認新密碼，修改成功後不會被登出。
2. 本專案代碼皆為 Claude 所產出。
3. 正式上線前，請更換 `mysite/settings.py` 中的 `SECRET_KEY`，並將 `DEBUG` 改為 `False`。

## 專案價值

本專案證明作者懂得透過 AI 進行自動化開發
能清楚理解需求、驗證與修正 AI 產出的程式碼
（例如排除 `migrate` 未執行的錯誤、逐步追加修改密碼功能）
並將成果整合成可運行的完整專案。