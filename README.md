# archivist

Store your media data locally

### Util Scripts
There are some scripts to help starting/stopping the container with required env variables -
just chmod +x `start_container.sh` and `stop_container.sh` to use them

### Starting
```
docker-compose up -d --build
```

Then navigate to `localhost:8000`

### Executing a command in the running container
```
docker-compose run web XXXXX
```

e.g. to migrate, `docker-compose run web python manage.py migrate`

### Closing
```
docker-compose down
```

### Database
Database data is stored in ./postgres_data which will be created when starting the container
You can save/move this to backup your database.
