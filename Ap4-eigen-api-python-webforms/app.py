from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

devices = []
next_id = 1

@app.route('/')
def index():
    return render_template('index.html', devices=devices)

@app.route('/add', methods=['POST'])
def add_device():
    global next_id
    hostname = request.form.get('hostname')
    ip       = request.form.get('ip')
    dtype    = request.form.get('device_type')
    if hostname and ip and dtype:
        devices.append({'id': next_id, 'hostname': hostname, 'ip': ip, 'type': dtype})
        next_id += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:device_id>', methods=['POST'])
def delete_device(device_id):
    global devices
    devices = [d for d in devices if d['id'] != device_id]
    return redirect(url_for('index'))

@app.route('/api/devices', methods=['GET'])
def api_devices():
    return jsonify(devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

