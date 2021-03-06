# KU-Event-Regis

[![Build Status](https://codecov.io/gh/codecov/example-python/branch/master/graph/badge.svg)](https://codecov.io/gh/PunyaweeSrithongkerd/KU-Event-Regis)
[![Build Status](https://travis-ci.com/PunyaweeSrithongkerd/KU-Event-Regis.png?branch=master)](https://travis-ci.com/PunyaweeSrithongkerd/KU-Event-Regis)

## Team Member

| Name                 |  Github                                                         |
| -------------------- | :--------------------------------------------------------------:|
| Punyawee Srithongkerd| [@PunyaweeSrithongkerd](https://github.com/PunyaweeSrithongkerd)|
| Gunn Torcheep        | [@gunnkrub](https://github.com/gunnkrub)                        |
| Warat Narattharaksa  | [@b5710547221](https://github.com/b5710547221)                  |

## Description

An application that has a list of the upcoming events at Kasetsart University to help the user to choose and sign-up for events easier. The event list provides a location, date(s), durations and description for each event. This application can be used by anyone at Kasetsart University and optionally by outsiders if the event allows outside participation.

## Offical website

[Heroku project](https://ku-event-regis.herokuapp.com/events/ "Heroku project")

## Project Documents

### Iteration Plans

[Project's Iteration Plans](https://docs.google.com/document/d/17Ww-Ab97z3rASIH0DlNb7vncsxDX0n_WspsaZHTzSlg/edit?usp=sharing "Project Iteration Plans")

[Project's Iteration Scripts](https://docs.google.com/document/d/1QV8VBchBDVkWlIeu0sfucIXTNJgXq2UmF1JS6uByA8s/edit?usp=sharing "Project's Iteration Scripts")

[Project's task borad in Trello](https://trello.com/b/PlI27dju/ku-event-regis "Task borad")

### Other Project Documents

[Code Review Script](https://docs.google.com/document/d/1JMUrrSyihzThjCtddIpctaNwA_2JpO2OSOeGkjf7pN8/edit?usp=sharing "Code Reviwe Scipt")

[Code Reviwe Checklist](https://docs.google.com/document/d/1pRlqTeCQEq9T0g3NPf8yt26aUKCSKC3rqEyI3L4xy_I/edit?usp=sharing "Code Reviwe Checklist")

[Project Proposal](https://docs.google.com/document/d/19xCopZf3TQyQaAabWN5D3fu3sOZGI43x2DwZauKSLwo/edit?usp=sharing "Project Proposal")

### Setup

1. Clone this Project to your own directory then open your clone directory and install the required packages by using the following command

`pip install -r requirements.txt`

2. Then create .env file and add `DEBUG  = TRUE` in .env file

3. Then run this command

`py manage.py migrate`

### How to run

run this command

`py manage.py runserver`

To enter site

`http://127.0.0.1:8000/events/`

## What we use in this project

- django
- heroku
- google cloud server
