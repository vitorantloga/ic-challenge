from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
import datetime 
# https://pythonhosted.org/Flask-Inputs/#module-flask_inputs
# https://json-schema.org/understanding-json-schema/
# we want an object containing a required start appointment values
start_schema = {
   'type': 'object',
   'properties': {
       'start_date': {
           'type': 'string',
       },
       'physician_id': {
           'type': 'string',
       },
       'patient_id': {
           'type': 'string',
       },
   },
   'required': ['start_date','physician_id', 'patient_id']
}

# we want an object containing a required end appointment values
end_schema = {
   'type': 'object',
   'properties': {
       'id': {
           'type': 'string',
       }
   },
   'required': ['id']
}

class StartInputs(Inputs):
   json = [JsonSchema(schema=start_schema)]


def validate_start(request):
   inputs = StartInputs(request)
   if inputs.validate():
       return None
   else:
       return inputs.errors

class EndInputs(Inputs):
   json = [JsonSchema(schema=end_schema)]

def validate_end(request):
   inputs = EndInputs(request)
   if inputs.validate():
       return None
   else:
       return inputs.errors

def validate_datetime(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
        return True
    except:
        return False