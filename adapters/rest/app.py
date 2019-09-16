import os
import sys
sys.path.append('./src/main/')

from flask import Flask, json, request
from index import get_diet

app = Flask(__name__)

@app.route('/diet', methods=['POST'])
def diet():
    params = request.get_json()

    data = get_diet(params)

    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)