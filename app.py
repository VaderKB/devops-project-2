from flask import Flask, render_template, jsonify
import time
import threading

app = Flask(__name__)
status = "Waiting for user action..."

def write_to_s3():
    global status
    status = "Running..."
    time.sleep(5)  # Simulating a time-consuming process
    with open("output.txt", "w") as f:
        f.write("File created successfully.")
    status = "Process Completed"

@app.route('/')
def home():
    return render_template('index.html', status=status)

@app.route('/run', methods=['POST'])
def run_process():
    global status
    if status == "Running...":
        return jsonify({"message": "Already running", "status": status})
    
    threading.Thread(target=write_to_s3).start()
    return jsonify({"message": "Started", "status": "Running..."})

@app.route('/status')
def get_status():
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
