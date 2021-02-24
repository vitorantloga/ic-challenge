import pytest
from app import main

# see: http://flask.pocoo.org/docs/1.0/testing/
@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    client = main.app.test_client()
    yield client

@pytest.fixture()
def create_valid_start_request():
    """
    Helper function for creating a correctly-structured
    json request
    """
    def _create_valid_start_request(
    	start_date="fixture",
    	physician_id="fixture",
    	patient_id="fixture"
    ):
        return {
			"start_date": start_date,
			"physician_id": physician_id,
			"patient_id": patient_id,
		}
    return _create_valid_start_request

@pytest.fixture()
def create_valid_end_request():
    """
    Helper function for creating a correctly-structured
    json request
    """
    def _create_valid_end_request(id="fixture"):
        return {"id": id}
		
    return _create_valid_end_request