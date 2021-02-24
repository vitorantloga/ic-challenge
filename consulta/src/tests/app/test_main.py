# http://flask.pocoo.org/docs/1.0/testing/#testing-json-apis
from app.validation import validate_datetime
from app.database import Database as db

def test_start_appointment(client):
	request_payload = {
		"physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82",
		"patient_id": "86158d46-ce33-4e3d-9822-462bbff5782e",
		"start_date": "2020-12-01 13:00:00",
	}
	response = client.post("/start", json=request_payload)
	result = response.get_json()

	assert response.status_code == 200
	assert result is not None
	assert "payload" in result
	assert "id" in result['payload']

	assert "physician_id" in result['payload']
	assert result['payload']['physician_id'] == request_payload['physician_id']

	assert "patient_id" in result['payload']
	assert result['payload']['patient_id'] == request_payload['patient_id']

	assert "start_date" in result['payload']
	assert result['payload']['start_date'] == request_payload['start_date']

def test_end_appointment(client):
	
	db.inicialize()
	lastId = db.getLast()

	physician_id = "ea959b03-5577-45c9-b9f7-a45d3e77ce82"
	patient_id = "86158d46-ce33-4e3d-9822-462bbff5782e"
	
	request_payload = {"id": str(lastId[0]["_id"])}
	response = client.post("/end", json=request_payload)
	result = response.get_json()

	assert response.status_code == 200
	assert result is not None
	assert "payload" in result

	assert "id" in result['payload']
	assert result['payload']['id'] == request_payload['id']

	assert "physician_id" in result['payload']
	assert result['payload']['physician_id'] == physician_id

	assert "patient_id" in result['payload']
	assert result['payload']['patient_id'] == patient_id

	assert "end_date" in result['payload']
	assert validate_datetime(result['payload']['end_date'])

	assert "price" in result['payload']
