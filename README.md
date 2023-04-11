# Hexagonal Calculator

Calculator application using Hexagonal Architecture in Python.

Other patterns involved:

* Domain modelling
* Repository
* Unit of Work
* Services
* Use Cases

## How to install?

Use virtualenv as:

* `python3 -m venv .venv`
* `source .venv/bin/activate`

We use flit for the installation and package management:

Install flit:

* `pip install flit==3.7.1`

The rest of the commands can be found using `make help`:

```
---------------HELP-----------------
To install the project type -> make install
To install the project for development type -> make install-dev
To test the project type -> make test
To test with coverage -> make test-cov
To format code type -> make format
To check linter type -> make lint
To run type checker -> make type-check
To run all security related commands -> make secure
To create database migrations -> make migrations
To run database migrations -> make migrate
------------------------------------
```

For development purposes the main command is `make install-dev` as it will enable editable installation.



## Dependency Graphs

### Graph from FastAPI router

* The graph below is from FastAPI router. 
As you see use case is used by router and the framework itself is only responsible for routing.

![dependency from fastapi router](docs/calculator_adapters_entrypoints_api_v1_route_calculate.svg)

### Graph from Flask router

* The graph below is from Flask router. 
Practically it is the same as FastAPI graph, again Flask is only responsible for routing.

![dependency from flask router](docs/calculator_adapters_entrypoints_api_v2_route_calculate.svg)

### Graph from Use Case

* The graph below is from Use Case.

![dependency from use case](docs/calculator_adapters_use_cases_calculate.svg)

Why to analyze the dependency graphs? 
The rule I strongly advice to follow is: 

`"If it is hard to understand the dependency flow from the dependency graph, simply you are closer to have small to big ball of mud"`

If you have spotted something wrong here, just go back and try to simplify or fix the abstractions, dependencies, layers, etc.