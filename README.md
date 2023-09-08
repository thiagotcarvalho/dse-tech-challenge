# Developer Success Engineer Tech Challenge Project
Finch's Developer Success Engineer Tech Challenge Submission

## Instructions
First, clone this repository and install [Docker](https://docs.docker.com/engine/install/).

Then, navigate to the directory of the cloned repo and run the following commands in the terminal:
1. `docker compose build`
2. `docker compose up`
3. `docker ps -a` *(to get the id of the django container)*
4. `docker exec -it <docker-container-id> bash` 
5. `python manage.py migrate`

Finally, navigate to `http:localhost:3000` to see the frontend of the web application.

## Tech Stack
* Django (Python)
* React (JavaScript)
* Chakra UI
* Docker