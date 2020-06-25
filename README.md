# Building & Running simple-flask-webapp container

**To build:**

```$ docker build . -t simple-flask-webapp```

within the directory of the Dockerfile

**To run container:** 

```$ docker run -p 8081:8080 simple-flask-webapp```

Replacing 8081 with whatever port you like.

Visit localhost:8081 to see the app in action!
