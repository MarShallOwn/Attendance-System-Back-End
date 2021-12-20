# Attendance-System-Back-End

Attendance Tracking System is a system where admins/managers can track the attendance of their employers and handle leave request easily.
while the employers can check-in / check-out and request leave from just a click of a button.
The Admin is responsible for creating / deleting/ editing employer account and departments, creating holidays and weekends date, handle leave requests and check reports.

## About
The system uses the core features a company would want to use from software like Attendance Tracking System. Included features are:
* Signup / login.
* Forgot password workflow.
* View / edit profile details.
* Give roles to specific user (example: admin, employer)
* Change password while logged in.
* admins/managers can handle leave requests of all the employers.
* admins/managers can create / delete / edit employers accounts and departments.
* employers can check-in / check-out when starting their work hours or ending it.
* employers can request leave requests and it can keep track of them.
* Authentication of a route before allowing access to the page.

## Prerequisites
You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Python3](https://www.python.org/downloads/) (with PIP)
* [mysql](https://dev.mysql.com/downloads/installer/)

## Installation
* `git clone https://github.com/MarShallOwn/Attendance-System-Back-End.git`
* `enter the folder`
* `open cmd`
* `create virtual enviroment that will be holding our packages using: "py -3 -m venv env" or "python -m venv env"`
* `activate virtual enviroment using: "env\Scripts\activate"`
* `install the packages needed using : "pip install -r requirements.txt"`

## Running / Development
* `to run the backend server go to api terminal and run (py manage.py runserver) for development running on ` [http://localhost:8000](http://localhost:8000)

## Guidelines and Rules
* all inputs and outputs variables comming in and out the api should be in a camelCase form for example
```
{
    phoneNumber: "329434895865"
}
```
* the response of the api should be return two attributes which are **(error and data)** for example
```
{
    error: null,
    data: {
        id: 1,
        name: "marwan",
        age: 21
    }
}
```
* error attribute should contain a list of serialized errors in the excepected format for example
```
{
    error: ["Input fields shouldn't be empty empty", "username shouldn't be less than 3 characters"],
    data: null
}
```
