
# Тестовое задание

Тестовое задание на позицию Fullstack-разработчик


##  Built in
- Django Rest Framework
- dj-rest-auth - for authentication 
- Docker

## Related

Front end part of project

[Task managment system]()


## Run Locally

Clone the project

```bash
  git clone https://github.com/Persepha/task-managment-system-backend.git
  
```

Go to the project directory

```bash
  cd task-managment-system
```

To correctly execute docker scripts, run the following command on linux or use wsl on windows

Run the docker containers:

```bash
  docker-compose up --build
```

or

```bash
  make build-server
```


Test it out at http://localhost:8000. 


## Documentation

Swagger docs at 

http://localhost:8000/api/schema/swagger-ui/

Default superuser for admin panel

email
```bash
    admin@test.com
```

login
```bash
    admin
```

pass
```bash
    admin123
```


## notes

- Email token for reset password sends into console






