import tkinter as tk

# ウィンドウを作成
window = tk.Tk()

# ウィンドウのタイトルを設定
window.title("はじめてのウィンドウ")

# ウィンドウのサイズを設定
window.geometry("400x300")

# ラベル（テキスト）を作成
label = tk.Label(window, text="Hello World", font=("Arial", 24))

# ラベルをウィンドウの中央に配置
label.pack(expand=True)

# ウィンドウを表示して待機
window.mainloop()