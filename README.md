# IEEE_ISEP_Discord_Bot
Bot for automating membership actions in server

IEEE ISEP Student Branch Discord server bot for automating some processes like creating channels, roles or just getting information

**1. Running bot**

- ```cd bot```
- ```python3 bot.py```

**2. Basic Commands**

- ```!info``` returns information about the server like its owner and numbr of members
- ```!new <channel_type> <channel_name>``` creates a text or voice channel depending on the second argument value
- ```!search <question>``` searches for a specific topic and returns the answer from Wikipedia
- `!new role <role_name>` creates a new role in te server

**3. Docker Image**

This repository provides an already built docker image, supposed to be built in your computer (however it won't work due to the token inavailability). Keep in mind that the docker image is just supposed help you through the creation of your own Docker image.

**Build the Docker image**

- ```cd docker_image```
- ```sudo docker build -t <name> .```

**Run the Docker image**

```sudo docker run -it <name> bash```

**4. Bot Server**

In order to get a continuosly running bot, we must host the bot in a web server. At the moment, the bot is not being continuosly hosted in the web server, but it does give an example on how to achieve it.
Inside the `bot` folder, we have two separate scripts `bot.py` and `server.py`. The first one concerns with the actual bot commands, while the second one establishes the connection to the server, while runnning the server on a separate thread so that both the bot and the server can run simultaneously.
In the future, it will be improved.
