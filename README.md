## Teste SRE Arquiteto

O teste consiste em 2 microserviços que possibilitam realizar uma consulta entre um médico e um paciente e gerar uma entrada financeira de cobrança da consulta.

## Restrições
Os serviços foram desenvolvidos em Python.
*TODO: Utilizar docker para provisionar os serviços.*
Os serviços utilizam um banco de dados compartilhado.

## Serviço 1: API de consultas
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

## Serviço 2: API financeira
Este serviço deve realizar uma entrada financeira de cobrança para a consulta. Uma entrada de cobrança pode ser representada dessa forma:

{
	"appointment_id": "84ab6121-c4a8-4684-8cc2-b03024ec0f1d", # id da consulta
	"total_price": 400.00,
}

## Considerações
Caso a API financeira não esteja funcionando corretamente no momento da notificação de consulta finalizada, assim que ela subir, deve ser possível processar a entrada de cobrança. (Não pode perder o registro de cobrança).

# STACK UTILIZADA
Os serviços foram desenvolvidos utilizando:
- Python
- Flask
- MongoDB
- RabbitMQ

# Arquitetura:
- O **serviço 1** é uma API desenvolvida em Flask com 2 endpoints: /start e /end. 
- Quando uma consulta é criada um novo registro é feito no mongoDB.
- Quando uma consulta é finalizada este registro é atualizado com o valor calculado e uma mensagem é gerada no RabbitMQ.
- A queue do RabbitMQ é consumida pelo **serviço 2**, que é desenvolvido em python e consulta a fila de 10 em 10 segundos.  

# Documentação dos endpoints
TODO 

# TESTES
Como executar os testes unitários do serviço 1:
Iniciar containers rabbitMQ e mongoDB
```docker run -d  --name mongo-on-docker  -p 27888:27017 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo```
```docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management```
acessar diretório consulta/src  edigitar o comando:
```python -m pytest -s```

# COMO EXECUTAR O PROJETO (TODO)
Acesse o diretório raiz do projeto e execute o comando:
```docker-compose up -d```

A API será servida na porta 80.
O RabbitMQ pode ser acessado na porta 15672 (usuário: guest, pass: guest)

O banco de dados (mongoDB) é servido na porta 27888. 
Para visualizar os dados utilizei o noSQLBooster. 

### OBSERVAÇÃO
Os dockers dos serviços não estão funcionando corretamente. Para executar o projeto executar os serviços 'na mão':
Serviço 1: consulta
acessar diretório src rodar o comando:
python -m app.main

# Referencias
Algumas das referencias que utilizei para desenvolver o desafio:

**Getting Started with Python Microservices in Flask**
https://mikebridge.github.io/post/python-flask-kubernetes-1/ (partes 1, 2 e 3)

**Background Processing With RabbitMQ, Python, and Flask**
https://betterprogramming.pub/background-processing-with-rabbitmq-python-and-flask-5ca62acf409c

**First steps with Docker: download and run MongoDB locally**
https://www.code4it.dev/blog/run-mongodb-on-docker