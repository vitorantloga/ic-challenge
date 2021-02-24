import pytest
from flask import Flask, request

from app.validation import validate_start, validate_end, validate_datetime

app = Flask(__name__)

#START_APPOINTMENT
@pytest.mark.parametrize("params", [
   {"start_date": 1},
   {"physician_id": 1},
   {"patient_id": 1}
])
def test_invalid_types_are_rejected_start(params, create_valid_start_request):
   json_input = create_valid_start_request(**params)
   with app.test_request_context('/', json=json_input):
       errors = validate_start(request)
       assert errors is not None

@pytest.mark.parametrize("required_parm_name", ["start_date", "physician_id", "patient_id"])
def test_missing_required_params_is_rejected_start(required_parm_name, create_valid_start_request):
   json_input = create_valid_start_request()
   del json_input[required_parm_name]
   with app.test_request_context('/', json=json_input):
       errors = validate_start(request)
       assert errors is not None

def test_valid_start_is_accepted_start(create_valid_start_request):
	json_input = create_valid_start_request(
		start_date="2020-12-01 13:00:00", 
		patient_id="86158d46-ce33-4e3d-9822-462bbff5782e",
		physician_id="ea959b03-5577-45c9-b9f7-a45d3e77ce82"
	)
	with app.test_request_context('/', json=json_input):
		errors = validate_start(request)
		assert errors is None

#END_APPOINTMENT
@pytest.mark.parametrize("params", [{"id": 1}])
def test_invalid_types_are_rejected_end(params, create_valid_end_request):
   json_input = create_valid_end_request(**params)
   with app.test_request_context('/', json=json_input):
       errors = validate_end(request)
       assert errors is not None

@pytest.mark.parametrize("required_parm_name", ["id"])
def test_missing_required_params_is_rejected_end(required_parm_name, create_valid_end_request):
   json_input = create_valid_end_request()
   del json_input[required_parm_name]
   with app.test_request_context('/', json=json_input):
       errors = validate_end(request)
       assert errors is not None

def test_valid_end_is_accepted_end(create_valid_end_request):
	json_input = create_valid_end_request(id="602ef418fb19a2231f798eb5")
	with app.test_request_context('/', json=json_input):
		errors = validate_end(request)
		assert errors is None

def test_validate_datetime(client):
  assert validate_datetime("2020-12-30 23:59:59") == True
  assert validate_datetime("2020-02-31 23:59:59") == False
  assert validate_datetime("2020/02/31 23:59:59") == False
  assert validate_datetime("20-12-31 23:59:59") == False