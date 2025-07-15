# Python Development Environment

このプロジェクトは、Python開発のためのDevContainerを使用した開発環境です。

## 機能

- コードフォーマッタ（Black、isort）
- リンター（Flake8、Pylint、MyPy）
- テストフレームワーク（pytest、pytest-cov）
- デバッグツール（pdbpp、ipdb）
- Jupyter Notebook対応

## セットアップ

1. VS Codeでこのプロジェクトを開く
2. Dev Containerで再オープンを選択
3. コンテナが自動的にビルドされ、必要な依存関係がインストールされます

## 使用方法

### コードフォーマット
```bash
black .
isort .
```

### リント
```bash
flake8
pylint *.py
mypy *.py
```

### テスト実行
```bash
pytest
```

### Jupyter Notebook
```bash
jupyter notebook
```

## プロジェクト構成

```
/workspaces/pythondev/
├── .devcontainer/          # DevContainer設定ファイル
├── examples/               # Pythonサンプルプログラム集
│   ├── hello.py           # 基本的なHello Worldサンプル
│   ├── web/               # Webアプリケーションサンプル
│   │   ├── hello_flask.py     # Flask Webアプリ
│   │   ├── hello_web.py       # 基本的なWebサーバー  
│   │   ├── simple_web_server.py # シンプルHTTPサーバー
│   │   └── index.html         # 静的HTMLファイル
│   └── gui/               # GUIアプリケーションサンプル（参考用）
│       ├── hello_window.py    # tkinter基本ウィンドウ
│       └── hello_window_advanced.py # tkinter応用ウィンドウ
├── data/                  # データファイル
│   └── sample.csv         # サンプルCSVデータ
├── CLAUDE.md              # Claude開発者向けプロジェクト情報
└── README.md              # このファイル
```

## サンプルプログラムの実行方法

### 基本サンプル
```bash
# Hello World実行
python examples/hello.py
```

### Webアプリケーション
```bash
# 必要なパッケージをインストール
pip install flask

# Flask Webアプリ実行
python examples/web/hello_flask.py

# シンプルWebサーバー実行
python examples/web/simple_web_server.py
```

### GUIアプリケーション（参考用）
```bash
# システムレベルでtkinterライブラリをインストール
sudo apt-get update && sudo apt-get install -y python3-tk

# GUI実行（コンテナ環境では表示されませんが、エラーなく実行可能）
python examples/gui/hello_window.py
```

## 各ディレクトリの説明

### examples/
Python学習用のサンプルプログラム集です。基本的なPython、Webアプリケーション、GUIアプリケーションの例が含まれています。

### examples/web/
Webアプリケーション関連のサンプルです。コンテナ環境での開発に最適で、ブラウザでアクセス可能です。

### examples/gui/
GUIアプリケーションのサンプルです。コンテナ環境では直接表示できませんが、コードの学習に役立ちます。

### data/
プロジェクトで使用するサンプルデータファイルを配置します。