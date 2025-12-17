Cookie Server - Learning Example

This is a simple Python HTTP server to explore cookies and session handling in web applications. It is intended for local testing and learning about how browsers and servers interact.

Features

Handles GET requests using BaseHTTPRequestHandler.

Generates a session ID for first-time visitors.

Stores the session ID in a cookie on the browser.

Reads the cookie on subsequent visits to identify returning visitors.

Demonstrates basic cookie parsing and handling in Python.

How It Works

Server generates session token:

session_token = generate_session_token()


This is a unique string representing a user session.

Initialized to None to detect first-time visitors.

Check for existing cookie:

cookies = self.headers.get('Cookie')


Reads the Cookie header sent by the browser.

If a sessionID cookie exists, the server uses its value.

Parse multiple cookies:

for cookie in cookies.split(';'):
    name, _, value = cookie.strip().partition('=')


Browser may send multiple cookies in one header.

Splitting and parsing lets the server find the specific sessionID (or other preferences, e.g., theme=dark).

Send cookie to browser:

self.send_header('Set-Cookie', f'sessionID={session_token}; Path=/; HttpOnly')


Instructs the browser to store the session ID.

HttpOnly prevents access via JavaScript for security.

Path=/ ensures the cookie applies to the entire server.

Returning visitors:

If the cookie exists, the else branch is executed.

Server can then use the session ID to maintain user state or preferences.

Key Concepts Highlighted

HTTP is stateless → cookies provide a way to store state.

Cookies live on the browser, not the server (in this simple example).

Session ID is a unique token stored inside a cookie.

Cookie header can contain multiple key=value pairs.

Browser automatically sends cookies to the matching domain/path.

Usage

Run the server locally:

python server.py


Visit: http://localhost:8000

Inspect cookies in browser dev tools: Application → Cookies → localhost

Refresh to see the server recognize returning visitors.

Notes

Restarting the server does not delete cookies stored in the browser.

To start fresh, delete cookies in the browser or expire them via Set-Cookie.

The server does not store session data, only the session ID is generated and sent.

test...
