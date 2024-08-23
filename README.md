# Cities API Test Case

## Описание
HTTP API для получения информации о координатах городов.
Функции:
  - Добавление/удаление городов;
  - Запрашивание информации о городе или всех городах, имеющиеся в базе данных;
  - Вычисление расстояния до двух ближайших городов по широте и долготе.

## Стек
* FastAPI
* Uvicorn (server)
* Redis
* Docker
* aiohttp
* graphhopper

## Как запустить?
:ballot_box_with_check: Клонировать репозиторий
```
git clone https://github.com/Vireynn/cities_cdnvideo.git
cd cities_cdnvideo
```
:ballot_box_with_check: Установить зависимости
```
poetry install
poetry shell
```
:ballot_box_with_check: Настроить переменные окружения
```
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_USER=redis
REDIS_PASSWORD=secret_password
REDIS_DB=0

API_KEY=secret_api_key
```
:ballot_box_with_check: Получить API-key для интеграции Graphhopper
  - Зарегистрироваться на сайте [Graphhopper](https://www.graphhopper.com)
  - Получить API-key и вставить в переменную окружения API_KEY

:ballot_box_with_check: Docker
```
docker-compose up --build
```
## FastAPI docs
Для взаимодействия с API перейти по ссылке http://localhost:8000/docs
