import json
from app.database import Database as db
from datetime import datetime
import pika

PRICE_BY_HOUR = 200

def start_appointment(start_date, physician_id, patient_id):
	db.inicialize()

	payload = {
		"start_date": start_date,
		"physician_id": physician_id,
		"patient_id": patient_id
	}

	item_id = db.insert(dict(payload))
	payload["id"] = item_id

	return payload


def end_appointment(item_id):
	
	db.inicialize()
	item = db.get(item_id)

	start_date = datetime.strptime(item["start_date"], '%Y-%m-%d %H:%M:%S')
	end_date = datetime.now()
	timedelta = end_date - start_date

	hours = (timedelta.seconds % 3600) + 1
	price = hours*PRICE_BY_HOUR

	item["end_date"] = end_date.strftime("%Y-%m-%d %H:%M:%S")
	item["price"] = price

	if(db.save(item)):
		payload = {
			"id": item_id,
			"start_date": item["start_date"],
			"physician_id": item["physician_id"],
			"patient_id": item["patient_id"],
			"end_date": item["end_date"],
			"price": item["price"],
		}

		financial_payload = json.dumps({
			"appointment_id": item_id, # id da consulta
			"total_price": item["price"],
		})

		# register a RabbitMQ message
		credentials = pika.PlainCredentials('guest', 'guest')
		parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
		connection = pika.BlockingConnection(parameters)
		channel = connection.channel()
		channel.queue_declare(queue='financial_queue', durable=True)
		channel.basic_publish(
			exchange='',
			routing_key='financial_queue',
			body=financial_payload,
			properties=pika.BasicProperties(
			delivery_mode=2,  # make message persistent
		))
		connection.close()

		return payload
	else:
		return False