from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


# Define the path to the file where the data will be saved
data_file = "data.txt"


@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_data(as_text=True)

    try:
        with open(data_file, 'a') as file:
            file.write(data)
        return jsonify({"message": "Data saved successfully"}), 200
    except Exception as e:
        print(f"filed at appending with data: {e}")
        return jsonify({"message": "Failed to write data"}), 500


if __name__ == '__main__':
   # Ensure the file exists or create it if necessary
   if not os.path.exists(data_file):
       with open(data_file, 'w') as f:
           pass  # Just create the file if it doesn't exist
   app.run(debug=True, port=8000)

