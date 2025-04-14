# API 自動化測試專案（使用 pytest + requests）

本專案使用 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) 提供的 RESTful API 作為測試目標，採用 Python + `pytest` 測試框架，結合 `requests` 進行 API 自動化測試。

## ✅ 專案目標

- 熟悉 API 測試流程與實作方式
- 建立可維護的自動化測試架構
- 用於面試作品展示

## 🏗 專案結構

```plaintext
api_test_project/
├── apis/                         # 封裝各資源 API 請求的模組
│   ├── __init__.py               # 讓 apis 資料夾可作為 Python 模組匯入
│   ├── users_api.py              # /users 的 API 操作封裝
│   ├── posts_api.py              # /posts 的 API 操作封裝
│   └── comments_api.py           # /comments 的 API 操作封裝
├── tests/                        # pytest 測試腳本
│   ├── __init__.py               # 讓 tests 資料夾可作為 Python 模組匯入（非必要但建議）
│   ├── test_users.py             # 測試 /users API
│   ├── test_posts.py             # 測試 /posts API
│   └── test_comments.py          # 測試 /comments API
├── utils/
│   ├── __init__.py               # 公用模組初始化
│   └── config.py                 # 設定 base URL 等參數
├── Pipfile                       # pipenv 套件管理
├── Pipfile.lock                  # 套件版本鎖定
├── README.md                     # 專案說明文件
├── .gitignore                    # 用來設定 Git 忽略的檔案或資料夾
└── run.py                        # 執行測試的程式
```

## 📦 使用套件
- Python 3.10
- pytest
- requests
- pipenv（管理虛擬環境與套件）
