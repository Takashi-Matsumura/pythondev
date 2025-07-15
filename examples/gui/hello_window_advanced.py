import tkinter as tk
from tkinter import messagebox

class HelloWorldApp:
    def __init__(self):
        # メインウィンドウを作成
        self.window = tk.Tk()
        self.window.title("Hello World アプリ")
        self.window.geometry("500x400")
        
        # 背景色を設定
        self.window.configure(bg="#f0f0f0")
        
        # メインフレームを作成
        main_frame = tk.Frame(self.window, bg="#f0f0f0")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # タイトルラベル
        title_label = tk.Label(
            main_frame,
            text="Hello World!",
            font=("Arial", 28, "bold"),
            fg="#333333",
            bg="#f0f0f0"
        )
        title_label.pack(pady=20)
        
        # 説明ラベル
        desc_label = tk.Label(
            main_frame,
            text="これは初めてのGUIアプリケーションです",
            font=("Arial", 12),
            fg="#666666",
            bg="#f0f0f0"
        )
        desc_label.pack(pady=10)
        
        # ボタンフレーム
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=30)
        
        # 挨拶ボタン
        hello_button = tk.Button(
            button_frame,
            text="挨拶する",
            command=self.show_greeting,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        hello_button.pack(side="left", padx=10)
        
        # 終了ボタン
        exit_button = tk.Button(
            button_frame,
            text="終了",
            command=self.exit_app,
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        exit_button.pack(side="left", padx=10)
        
        # メッセージ表示エリア
        self.message_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 14),
            fg="#2196F3",
            bg="#f0f0f0"
        )
        self.message_label.pack(pady=20)
    
    def show_greeting(self):
        """挨拶メッセージを表示"""
        self.message_label.config(text="こんにちは！Pythonの世界へようこそ！")
        messagebox.showinfo("挨拶", "Hello World!\nボタンをクリックしてくれてありがとう！")
    
    def exit_app(self):
        """アプリケーションを終了"""
        if messagebox.askokcancel("確認", "本当に終了しますか？"):
            self.window.quit()
    
    def run(self):
        """アプリケーションを実行"""
        self.window.mainloop()

# アプリケーションを起動
if __name__ == "__main__":
    app = HelloWorldApp()
    app.run()