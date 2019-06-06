# Introduction

This project objective is to explore on writing RESTful APIs. The README will include detail that will guide me in setting up the project.

## Python virtualenv

To work on virtual env

```
$ mkvirtualenv restful-venv
$ workon restful-venv
$ cd restful-tutorial
$ pip freeze > requirements.txt
$ pip freeze > requirements.txt
```

To leave virtual env

```
$ deactivate
```

## Starting the server

Ensure that `FLASK_APP=restful_tutorial.py` is saved in `.flaskenv` in the application root directory. Next, in your terminal run `flask run` to start the server. By default it will run on `127.0.0.1:5000`.


## Database Migration

### Database Upgrade and Downgrade Workflow

After modifications to `models.py` we will run `flask db migrate` command. This command will generate a migration script which can be checked in the at `/migrations`. After confirmation that the script is generated properly, run `flask db upgrade` command for modifications to take effect on the development database. In the event of undo is needed in the development phase, `flask db downgrade` command undo the last migration.


## API

### Routes Implemented
| HTTP Method        | Resource URL                             | Remarks                                          |
| :----------------: | :--------------------------------------: | :----------------------------------------------: |
| GET                | /users                                   | Returns a user.                                  |
| GET                | /users/<int:user_id>                     | Returns the collection of all users.             |
| GET                | /users/<int:user_id>/posts               | Returns a collection of posts by specified user. |
| POST               | /users/<int:user_id>/posts               | Creates a post for the specified user.           |
| DELETE             | /users/<int:user_id>/posts/<int:post_id> | Deletes an exisiting user's post.                |
| PUT                | /users/<int:user_id>/posts/<int:post_id> | Updates a post for the specified user.           |

### Todo Routes
| HTTP Method        | Resource URL                             | Remarks                                          |
| :----------------: | :--------------------------------------: | :----------------------------------------------: |
| POST               | /users                                   | Registers a new user account.                    |
| PUT                | /users/<int:user_id>                     | Modifies an existing user.                       |
| DELETE             | /users/<int:user_id>/                    | Deletes an exisiting user.                       |
