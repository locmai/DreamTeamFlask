# Dream Team Flask

Simple Flask CRUD Application. Includes Unit Test Module and Selenium for UI Automation.

## Getting Started

For setting the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 2.7
* Python packages

```
pip install -r requirements.txt
```

## Database Configurations
Create a user and a database for it.

```
$ mysql -u root

mysql> CREATE USER 'locmai'@'localhost' IDENTIFIED BY 'locmai';

mysql> CREATE DATABASE dreamteam_db;

mysql> GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'locmai'@'localhost';
```

## Running the Program

```
export FLASK_APP=run.py
export FLASK_CONFIG=development
flask run
```

## Running the Unit Tests

Change directory to 'tests', use nose2 command for running all the python files' name started with 'test'
```
cd tests
nose2
```

## Coding Conventions

Following the PEP8 Coding Style.

## Deployment

Deployment note about how to deploy this app on live system: **TBD**

## To-Do

* Update Selenium Demo for UI Automation. - Finished Setup for Test.
* Reformat the code follow Python coding style and conventions. - **Done**
* Update Procfile and setup for Heroku deployment.
* Update this file after finished all the above tasks.
