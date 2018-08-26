# archivist

Store your media data locally

### Requirements
Docker, Docker-Compose, Python3.6, Pipenv

```
pipenv install
chmod +x *.sh
./start_container.sh
```

Then visit localhost:8000 for the catalog, and localhost:8000/admin for adding data

### MediaItem and MediaInformation
A media item is an invidual piece of media, with certain shared properties.

MediaInformation is any arbitrary json (comments, media details, etc.) that can be linked to a media item

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
