#!/usr/bin/python3
"""returns info about to-do list of employee using REST API"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/todo/<user_id>'
def user_todo(user_id):
           """route to get user data"""
           user_data = {
               "user_id": user_id,
               "EMPLOYEE_NAME": "John Doe",
           }

           extra = request.args.get("extra")
           if extra:
           user_data["extra"] = extra

           return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)
