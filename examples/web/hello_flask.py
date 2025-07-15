from flask import Flask, render_template_string

app = Flask(__name__)

# HTMLテンプレート
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello Flask</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 60px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        h1 {
            font-size: 60px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        p {
            font-size: 24px;
            margin-bottom: 30px;
        }
        .info {
            background: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
        }
        .time {
            font-size: 20px;
            margin-top: 20px;
        }
        a {
            color: white;
            text-decoration: none;
            background: rgba(255, 255, 255, 0.3);
            padding: 15px 30px;
            border-radius: 30px;
            display: inline-block;
            margin-top: 20px;
            transition: all 0.3s ease;
        }
        a:hover {
            background: rgba(255, 255, 255, 0.5);
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello World!</h1>
        <p>Flaskで作ったWebアプリケーションです</p>
        
        <div class="info">
            <p>🎉 おめでとうございます！</p>
            <p>初めてのWebアプリケーションが動いています</p>
        </div>
        
        <div class="time">
            現在時刻: <span id="clock"></span>
        </div>
        
        <a href="/about">このアプリについて</a>
    </div>
    
    <script>
        function updateClock() {
            const now = new Date();
            const timeString = now.toLocaleTimeString('ja-JP');
            document.getElementById('clock').textContent = timeString;
        }
        
        updateClock();
        setInterval(updateClock, 1000);
    </script>
</body>
</html>
"""

ABOUT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>About - Hello Flask</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #667eea;
        }
        .feature {
            background: #f8f9fa;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        a {
            color: #667eea;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>このアプリケーションについて</h1>
        
        <div class="feature">
            <h2>🐍 Python + Flask</h2>
            <p>このWebアプリケーションは、Pythonの人気フレームワーク「Flask」を使って作られています。</p>
        </div>
        
        <div class="feature">
            <h2>✨ 特徴</h2>
            <ul>
                <li>シンプルで軽量なWebフレームワーク</li>
                <li>HTMLとCSSでデザインをカスタマイズ</li>
                <li>JavaScriptで動的な機能を追加</li>
                <li>複数のページを持つアプリケーション</li>
            </ul>
        </div>
        
        <div class="feature">
            <h2>📚 次のステップ</h2>
            <p>このアプリケーションを拡張して、以下のような機能を追加してみましょう：</p>
            <ul>
                <li>データベースとの連携</li>
                <li>ユーザー認証機能</li>
                <li>フォームの作成と処理</li>
                <li>APIの作成</li>
            </ul>
        </div>
        
        <p><a href="/">← ホームに戻る</a></p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/about')
def about():
    return render_template_string(ABOUT_TEMPLATE)

if __name__ == '__main__':
    print("Flaskアプリケーションを起動します...")
    print("ブラウザで http://localhost:5000 にアクセスしてください")
    print("終了するには Ctrl+C を押してください")
    app.run(host='0.0.0.0', port=5000, debug=True)