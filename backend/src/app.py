from flask import Flask
from flask_restx import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)


@api.route('/time')
@api.header("Access-Control-Allow-Origin", "*")
@api.header("Content-Type", "application/json")
class HelloWorld(Resource):
    def get(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return {'time': current_time}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
