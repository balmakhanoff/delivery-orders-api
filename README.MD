# API Заказа доставки

## Реализация на flask, flask_sqlalchemy

### Склонировать к себе репозиторий

```
    git clone git@github.com:balmakhanoff/delivery-orders-api.git
```

### Создать виртуальную среду

```
    python -m venv venv
```

### Установить зависимости

```
    pip install -r requirements.txt
```

### Запустить с корневого файла main.py

```
    cd .../python/main.py
```

### Сервис доступен по ссылке

[Кликни меня](http://127.0.0.1:5000/)

---

## Самый просто способ взаимодействия с программой вводить в терминал cmd команды curl

### Добавить заказ, нужно передать адресс доставки

```
    curl -X POST http://127.0.0.1:5000/api/orders -H "Content-Type: application/json" -d "{\"delivery_address\": \"123 Main St\"}"

```

#### Показать заказ по ID

```
    curl -X GET http://127.0.0.1:5000/api/orders/1
```

#### Изменить статус доставки по ID

```
    curl -X PUT http://127.0.0.1:5000/api/orders/1/status -H "Content-Type: application/json" -d "{\"status\": \"IN_DELIVERY\"}"
```

#### Деактивировать заказ по ID

```
    curl -X PUT http://127.0.0.1:5000/api/orders/1/deactivate
```

#### Добавление комментария к заказу по ID

```
    curl -X POST http://127.0.0.1:5000/api/orders/1/comments -H "Content-Type: application/json" -d "{\"text\": \"The order is being processed.\"}"

```

### Показать комментарии по ID

```
    curl -X GET http://127.0.0.1:5000/api/orders/1/comments
```
