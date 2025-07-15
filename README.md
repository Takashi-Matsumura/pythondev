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

## ファイル構成

- `.devcontainer/` - DevContainer設定ファイル
- `hello.py` - サンプルPythonファイル
- `sample.csv` - サンプルデータファイル