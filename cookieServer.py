from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import string

def generate_session_token(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class CookieHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check if cookie exists
        cookies = self.headers.get('Cookie')
        session_token = None
        if cookies:
            for cookie in cookies.split(';'):
                name, _, value = cookie.strip().partition('=')
                if name == 'sessionID':
                    session_token = value
        
        # If no session cookie, create one
        if not session_token:
            session_token = generate_session_token()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Set-Cookie', f'sessionID={session_token}; Path=/; HttpOnly')
            self.end_headers()
            message = f"<p>No session cookie found. Creating one: {session_token}</p>"
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = f"<p>Session cookie found: {session_token}</p>"
        
        # Include instructions
        message += "<p>Check your browser dev tools → Application → Cookies.</p>"
        self.wfile.write(message.encode())

# Run the server
port = 8000
print(f"Serving on http://localhost:{port}")
HTTPServer(('localhost', port), CookieHandler).serve_forever()
