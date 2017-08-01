import time
from yaml import load as load_yaml
from flask import Flask
from json import dumps
from kubernetes import client
from kubernetes.client import Configuration, ApiClient
from kubernetes.client.rest import ApiException

app = Flask(__name__)

k8s_local_config = Configuration()
k8s_local_config.host = "localhost:8001"

k8s_local_client = ApiClient(config=k8s_local_config)
batch_api = client.BatchV1Api(api_client=k8s_local_client)

@app.route('/trigger-job', methods=['POST'])
def trigger_job():
    print('trigger-job')

    with open('job-template.yaml', 'r') as yaml_file:
        job_spec = load_yaml(yaml_file)

    job_spec['metadata']['name'] = 'job-%s' % int(time.time() * 1000)

    try:
        job = batch_api.create_namespaced_job('default', job_spec, pretty='true')
        return dumps({'result':'SUCCESS'}), 200, {"Content-Type" : "application/json"}
    except ApiException as e:
        print("Exception when calling create_namespaced_job: %s\n" % e)
        return dumps({'result':'FAILURE'}), 500, {"Content-Type" : "application/json"}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
