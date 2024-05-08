# RabbitMQ-Example

## Configuracion

### Exchange

* Name: nameTopic

* Type: Direct

* Durability: Durable

### Queue

* Type: Default

* Name: nameQueue

* Durability: Durable

### Bindings

* Exchange: nameTopic

* Routing Key: name.*

### Admin / Topic Permision

* Accept all