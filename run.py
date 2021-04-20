from flaskmusic import app
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(local_ip)
if __name__ == '__main__':
    app.run(debug=True, host=local_ip)
