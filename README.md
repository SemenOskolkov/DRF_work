Для запуска проекта необходмо:
1. Создать и перейти диреторию "project_drf";
2. Загрузить проект в диреторию "project_drf". Можно используя командой: git clone <ссылка на удаленный репозиторий>

Для запуска проета в Docker-контейненре необходимо:
1. Ввести в терминале команду: docker run --name python --network host -it python bash
3. Установить зависимости проекта: pip install -r requirements.txt
4. Выполнить миграции: python3 manage.py migrate
5. Запустить сервер: python3 manage.py runserver

Для работы с PostgreSQL через Docker необходимо:
1. Остановить работу контейнера "python", командой: docker stop python
2. Ввести в терминале команду: docker run --name db_postgres -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 -v /Users/semenoskolkov/pgdata/data_drf:/var/lib/postgresql/data postgres (команда скачает образ последней верии postgres, запустит контейнер и сохранит данные в директории /Users/semenoskolkov/pgdata/data_drf)
3. Подключиться к БД контейнера postgres: docker exec -it <id контейнера> psql -U postgres
4. Cоздать базу данных: create database test_drf;
5. Остановить контейнер: docker stop db_postgres
6. Перезапустить контейнер используя команду в п.2
7. Переподключиться к БД "test_drf": docker exec -it <id контейнера> psql -U postgres test_drf
