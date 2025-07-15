from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # HTTPレスポンスを送信
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # HTMLコンテンツ
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f0f0;
                }
                .container {
                    text-align: center;
                    background-color: white;
                    padding: 50px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #333;
                    font-size: 48px;
                    margin-bottom: 20px;
                }
                p {
                    color: #666;
                    font-size: 18px;
                }
                .button {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 15px 30px;
                    font-size: 16px;
                    border-radius: 5px;
                    cursor: pointer;
                    margin-top: 20px;
                }
                .button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello World!</h1>
                <p>これはPythonで作った初めてのWebページです</p>
                <button class="button" onclick="alert('こんにちは！ボタンがクリックされました！')">
                    クリックしてみて
                </button>
            </div>
        </body>
        </html>
        """
        
        # HTMLを送信
        self.wfile.write(html_content.encode('utf-8'))

# サーバーの設定
port = 8000
server_address = ('', port)
httpd = HTTPServer(server_address, HelloHandler)

print(f"サーバーが起動しました！")
print(f"ブラウザで http://localhost:{port} にアクセスしてください")
print("終了するには Ctrl+C を押してください")

# サーバーを起動
httpd.serve_forever()