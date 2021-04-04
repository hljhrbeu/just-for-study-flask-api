from flask import jsonify

def make_response(code,data,message):
    return jsonify({
        "code": 200,
        "data": data,
        "message": message
    })