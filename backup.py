from flask import Flask, redirect, url_for, request, render_template
import redis

#store = redis.Redis('172.24.2.68', password='8aB4wnwfn7Fj?ZB')
store = redis.Redis()
app = Flask(__name__)


# @app.route('/redis/')
# def redis_req():
#     keys = store.keys("HBB*")
#     return render_template("BS3/dashboard.html", keys=keys)

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name=user))
#     else:
#         user = request.args.get('nm')
#     return redirect(url_for('success', name=user))


# @app.route('/redis/')
# def whitelist():
#     return render_template("BS3/user.html")


# @app.route('/redis/whitelisted')
# def hbb_whitelisted():
#     return render_template("BS3/table.html")


@app.route('/')
def hello_world():
   return render_template('index.html', foo=42)


if __name__ == '__main__':
   app.run('0.0.0.0', 80, debug=True)
