## Teste SRE Arquiteto

O teste consiste em 2 microserviços que possibilitam realizar uma consulta entre um médico e um paciente e gerar uma entrada financeira de cobrança da consulta.

![alt text] https://user-images.githubusercontent.com/6026357/102815834-ce078500-43ab-11eb-9b10-3c27f3149365.png

Restrições
Os serviços foram desenvolvidos em Python.
TODO: Utilizar docker para provisionar os serviços.
Os serviços utilizam um banco de dados compartilhado.

Serviço 1: API de consultas
Este serviço deve ter endpoints para iniciar e finalizar uma consulta. Uma consulta pode ser representada dessa forma:

{
	"id": "84ab6121-c4a8-4684-8cc2-b03024ec0f1d",
	"start_date": "2020-12-01 13:00:00",
	"end_date": "2020-12-01 14:00:00",
	"physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82",
	"patient_id": "86158d46-ce33-4e3d-9822-462bbff5782e",
	"price": 200.00
}
O valor da consulta é fixo R$ 200,00 por hora.

TODO: Quando uma consulta é finalizada, deve ser realizada uma notificação para a criação de uma cobrança no serviço financeiro.

TODO: Serviço 2: API financeira
Este serviço deve realizar uma entrada financeira de cobrança para a consulta. Uma entrada de cobrança pode ser representada dessa forma:

{
	"appointment_id": "84ab6121-c4a8-4684-8cc2-b03024ec0f1d", # id da consulta
	"total_price": 400.00,
}
Considerações
Caso a API financeira não esteja funcionando corretamente no momento da notificação de consulta finalizada, assim que ela subir, deve ser possível processar a entrada de cobrança. (Não pode perder o registro de cobrança).