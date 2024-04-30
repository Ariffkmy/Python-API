# import necessary modules
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Read users from an Excel file
df = pd.read_excel('users.xlsx')  # Replace with your Excel file path
users = df.to_dict('records')

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def add_user():
    user = request.get_json()
    users.append(user)
    # Optionally, you can save the updated users list to the Excel file:
    pd.DataFrame(users).to_excel('users.xlsx', index=False)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True)