from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Extend with APIs to receive moves, state, and update game logic for multiplayer

if __name__ == "__main__":
    app.run(debug=True)
