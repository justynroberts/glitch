import json
from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing Namespaces")
ret = v1.list_namespace(watch=False)
for i in ret.items:
    print(i.metadata.name)

print("IP Address")



from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/getworkers")
def namespaces():
    ret = v1.list_pod_for_all_namespaces(watch=False)
    listNamespaces=['glitch-worker']

    res_data = []
    tmp = {}

    for i in ret.items:
        if str(i.metadata.namespace)in listNamespaces:
            print (repr(i.status.pod_ip))
            tmp =i.status.pod_ip
            res_data.append(tmp)
    return(json.dumps(res_data))




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5595)
