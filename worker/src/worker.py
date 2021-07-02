from flask import Flask, request
import subprocess
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api')
def api():
    try:
        task = request.args.get('task')
        action = request.args.get('action')

        if task == "cpudiscount" and action == "execute":
            result = subprocess.run(["nproc | xargs seq | xargs -n1 -P4 md5sum /dev/zero"], shell=True, capture_output=True, text=True)
            return ('Running CPU Stress on Discount  ' + result.stdout)

        if task == 'cpudiscount' and action == 'cancel':
            result = subprocess.run(["killall md5sum && ps -def |grep md5sum"], shell=True, capture_output=True, text=True)
            return (result.stdout)

        if task == 'ls':
            result = subprocess.run(["ls -al"], shell=True, capture_output=True, text=True)
            return (result.stdout)

        if task == 'getpods3':
            result = subprocess.run(["kubectl get pods"], shell=True, capture_output=True, text=True)
            return (result.stdout)

    except:
            return("Invalid Call.")
if __name__ == "__main__":
 app.run(debug=True,host='0.0.0.0', port=7607)