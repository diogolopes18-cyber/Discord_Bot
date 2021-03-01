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

**3. Docker Image**

This repository provides an already built docker image, supposed to be built in your computer (however it won't work due to the token inavailability). Keep in mind that the docker image is just supposed help you through the creation of your own Docker image.

**Build the Docker image**

- ```cd docker_image```
- ```sudo docker build -t <name> .```

**Run the Docker image**

```sudo docker run -it <name> bash```
