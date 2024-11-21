# API Заказа доставки

## 

## Самый просто способ взаимодействия с программой вводить в терминал cmd команды curl

### ADDING ORDER WITH ADDRESS

```
    curl -X POST http://127.0.0.1:5000/api/orders -H "Content-Type: application/json" -d '{"delivery_address": "123 Main St"}'

```

### SHOW ORDER BY ID

```
    curl -X GET http://127.0.0.1:5000/api/orders/1
```

### TURN OFF ORDER

```
    curl -X PUT http://127.0.0.1:5000/api/orders/1/deactivate
```

### ADDING COMMENT BY ORDER ID

```
    curl -X POST http://127.0.0.1:5000/api/orders/1/comments -H "Content-Type: application/json" -d "{\"text\": \"The order is being processed.\"}"

```

### SHOW COMMENTS BY ORDER ID

```
    curl -X GET http://127.0.0.1:5000/api/orders/1/comments
```
