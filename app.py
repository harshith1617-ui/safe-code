from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.json
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    print("\n" + "="*50)
    print(f"🚨 CHEATING ALERT RECEIVED AT {timestamp} 🚨")
    print(f"Student ID: {data.get('student_id')}")
    print(f"Trigger Reason: {data.get('reason')}")
    print("="*50 + "\n")
    
    return jsonify({"status": "Alert Logged"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
