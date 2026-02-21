from flask import Flask, request, jsonify

app = Flask(__name__)

MAX_QUERY_PARAMS = 10

@app.route('/add', methods=['GET'])
def add():
    if len(request.args) > MAX_QUERY_PARAMS:
        return jsonify({
            'error': 'Too many query parameters',
            'max_allowed': MAX_QUERY_PARAMS,
            'received': len(request.args)
        }), 400
    left_str = request.args.get('left')
    right_str = request.args.get('right')
    if left_str is None or right_str is None:
        return jsonify({
            'error': 'Missing required parameters',
            'required': ['left', 'right'],
            'received': list(request.args.keys())
        }), 400
    try:
        left = int(left_str)
        right = int(right_str)
        return jsonify({'sum': left + right}), 200
    except ValueError:
        return jsonify({
            'error': 'left and right must be valid integers'
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
