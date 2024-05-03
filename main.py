from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Home , Hello from Docker</h1>"

@app.route("/get-user/<user_id>")
def get_user(user_id):
  user_data = {
    "user_id": user_id,
    "name" : "Felix",
    "email" : "felix@email.com"
  }
  return jsonify(user_data), 200

@app.route("/home")
def homepage():
    return "<h2>Home page</h2>"

@app.route("/contact")
def contact():
    return "<h2>Contact page</h2>"

if __name__ == "__main__":
  app.run(debug=True)
