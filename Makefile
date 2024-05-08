run-container:
	@echo 'Running RabbitMQ container, wait ...'
	@Docker run -d --restart always -p 15672:15672 -p 5672:5672 --name rabbitmq rabbitmq:3.11.13-management

run-producer:
	@echo 'Running producer server, wait ...'
	@uvicorn producer:app --host 127.0.0.1 --port 8000 --reload

run-consumer:
	@echo 'Running consumer server, wait ...'
	@python consumer.py

freeze:
	@conda list --export > requirements.txt