from flask import Flask, redirect, url_for, request, render_template
import redis
import requests
import jinja2
import conf
import json
import sys, os
import logging
from datetime import date

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.dirname(script_dir))
LOG_FILE = os.path.join(script_dir, 'betting-%s.log' % date.today())
sys.path.append(project_dir)
sys.path.append(os.path.dirname(project_dir))
handler = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger("betui")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


#store = redis.Redis('172.24.2.68', password='8aB4wnwfn7Fj?ZB')
store = redis.Redis()
app = Flask(__name__)


@app.route('/subscribe', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        response = subscribe(**request.form)
        return render_template('index.html', message=response)
    #else:
    #    #user = request.args.get('nm')
    return redirect(url_for('index',))

@app.route('/')
def index():
   logger.info("New Visit %s" % request.remote_addr)
   return render_template('index.html')


def subscribe(**kwargs):
   payload = {"msisdn": kwargs['msisdn'], "service_id": conf.PLAN.get(kwargs['plan'])}
   out_put = jinja2.Template(conf.URL)
   subscription_api = out_put.render(payload)
   result = json.loads(requests.get(subscription_api).text)
   #logger.info("Result %s" % result.text)
   return conf.STATUS.get(result['errorCode']) if kwargs["msisdn"][-10:] != "8129095388x" else json.dumps(result)

if __name__ == '__main__':
   app.run('0.0.0.0', 8001, debug=True)
