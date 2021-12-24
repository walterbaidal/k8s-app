from flask import Flask
from flask_restx import Resource, Api
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


@api.route('/time')
@api.header("Access-Control-Allow-Origin", "*")
class HelloWorld(Resource):
    def get(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return {'time': current_time}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
