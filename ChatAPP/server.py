from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"

socketio = SocketIO(app)


@app.route("/")
def server():
    return render_template("server.html",response="Server is running")


@socketio.on("connect")
def connect():
    print("Client connected")

@socketio.on("disconnect")
def disconnect():
    print("User Disconnected")


@socketio.on("send_message")
def message(data):
    print(data)
    # Send to everyone except sender
    socketio.emit("receive_message", data)
if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0",port=5000,debug=True)