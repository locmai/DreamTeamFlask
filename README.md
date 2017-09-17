#Dream Team - Flask Training

export FLASK_CONFIG=development
$ export FLASK_APP=run.py

# Dream Team Flask

Simple Flask Application. Includes Unit Test Module and Selenium for UI Automation.

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

tests.py is a sample for unit test the models,
```
python tests.py
```

## Coding Conventions

Following the PEP8 Coding Style.

## Deployment

Deployment note about how to deploy this app on live system: **TBD**

