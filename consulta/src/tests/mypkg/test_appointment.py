from mypkg.appointment import start_appointment, end_appointment
import json
from app.database import Database as db
from app.validation import validate_datetime

class EverythingEquals:
    def __eq__(self, other):
        return True

everything_equals = EverythingEquals()

def test_start_appointment():
	physician_id = "ea959b03-5577-45c9-b9f7-a45d3e77ce82"
	patient_id = "86158d46-ce33-4e3d-9822-462bbff5782e"
	start_date = "2020-12-01 13:00:00"
	

	request_response = {
		"id": everything_equals,
		"physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82",
		"patient_id": "86158d46-ce33-4e3d-9822-462bbff5782e",
		"start_date": "2020-12-01 13:00:00",
	}
	assert start_appointment(start_date, physician_id, patient_id) == request_response


def test_end_appointment():
	db.inicialize()
	lastItem = db.getLast()
	lastId = str(lastItem[0]["_id"])

	item_id = lastId
	physician_id = "ea959b03-5577-45c9-b9f7-a45d3e77ce82"
	patient_id = "86158d46-ce33-4e3d-9822-462bbff5782e"

	item = end_appointment(item_id) 
	
	assert "id" in item
	assert item['id'] == lastId

	assert "physician_id" in item
	assert item['physician_id'] == physician_id

	assert "patient_id" in item
	assert item['patient_id'] == patient_id

	assert "end_date" in item
	assert validate_datetime(item['end_date'])

	assert "price" in item