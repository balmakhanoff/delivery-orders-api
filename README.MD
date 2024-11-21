# API Заказа Доставки

## Реализация на Flask и Flask-SQLAlchemy

### Шаги для настройки проекта

1. **Клонировать репозиторий**:

    ```bash
    git clone git@github.com:balmakhanoff/delivery-orders-api.git
    ```

2. **Перейти в каталог с проектом**:
   
    ```bash
    cd delivery-orders-api
    ```

3. **Создать виртуальную среду**:

    ```bash
    python -m venv venv
    ```

4. **Установить зависимости**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Запустить сервис** с корневого файла `main.py`:

    ```bash
    python main.py
    ```

    Сервис будет доступен по адресу:  
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
