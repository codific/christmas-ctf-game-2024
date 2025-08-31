# CTF Game

## Story

This game was made by Codific team member. The game was played on the company Christmas party. 


## Description

The game has only one flag that looks like CDF{...}. In order to find it the player will have to go some challenges. Each solved challenge will give insights about what the next step is. There is no "hacking" actions needed towards the application. It is more like "exploration" approach needed. Some steps will require a little thinking out of the box.
The starting place is /api/docs

## Technical information

The game is writtein in Python PHP. It is API and the docs is on /api/docs. 
```
 docker build -t my-app .
```

```
 docker run -d -p 8000:8000 --name my-running-app my-app
```

The application will run on 8080 port


