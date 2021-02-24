from flask import Flask, jsonify, request
from mypkg.appointment import start_appointment, end_appointment
from app.invalid_usage import InvalidUsage
from app.validation import validate_start, validate_end

app = Flask(__name__)


@app.route("/")
def index() -> str:
    # transform a dict into an application/json response 
    return jsonify({"message": "It Works"})

@app.route("/start", methods=['POST'])
def start() -> str:
   errors = validate_start(request)
   if errors is not None:
       print(errors)
       raise InvalidUsage(errors)
   start_date = request.json.get("start_date", None)
   physician_id = request.json.get("physician_id", None)
   patient_id = request.json.get("patient_id", None)
   response = {"payload": start_appointment(start_date, physician_id, patient_id)}
   return jsonify(response)


@app.route("/end", methods=['POST'])
def end() -> str:
   errors = validate_end(request)
   if errors is not None:
       print(errors)
       raise InvalidUsage(errors)
   item_id = request.json.get("id", None)
   response = {"payload": end_appointment(item_id)}
   return jsonify(response)
   

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
   response = jsonify(error.to_dict())
   response.status_code = error.status_code
   return response
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 