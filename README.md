# COWORKING

## Contents:open_file_folder:

- Description:newspaper:
- Built with:hammer:
- Instalation:wrench:
- API tests:clipboard:
- Author:black_nib:

## Description:newspaper:

Creation of an api for reservations in a coworking space with the following use cases:

1. La reserva debe hacerse con mínimo 2 días de anticipación
2. La duración de la reserva no puede superar las dos semanas
3. La reserva se realiza con mínimo el 10% del valor del espacio
4. El formato de la “fechaPago” debe ser dd/mm/yyyy

## Built with:hammer:

You need:

- MYSQL
- Python3
- Flask

**Note:** There is a file named "requirements.txt" with all the necessary packages for the proper operation of the api

## Instalation:wrench:

**Set up the enviroment**

It is recommended to run the application in a virtual environment so as not to download packages to your operating system

To do that you need to install **virtualenv**

`USER$: sudo pip3 install virtualenv`

Now you can create a virtual enviroment called **venv**

`USER$: virtualenv venv`

To activate your environment, once you are inside the folder venv type:

`venv$: . ./bin/activate`

Now you can work with the folder containing the application inside your environment

**Run the API**

- **First step**

  First of all you need to install the dependencies neccesary to run the api:

```
(venv) USER$: pip3 install -r requirements.txt
```

- **Second step**

  Then, you need to create the database and the table with with the help of the **schema.sql** file

  **Note:** This is going to create two schemas **pruebaceiba** and **testprueba** (for the test enviroment)

```
(venv) USER$: cat schema.sql | sudo mysql -hlocalhost -uroot -p
Enter password sudo:
Enter password root:
```

* **Third step**

  Before running the application it is recommended for security reasons to define some environment variables

  **Note:** The environment variable MYSQL_DB should be defined as "testprueba" when you want to run the tests

```bash
(venv) USER$: export MYSQL_DB=coworking_dev
(venv) USER$: export MYSQL_USER=ceiba
(venv) USER$: export MYSQL_PWD=ceiba
(venv) USER$: export MYSQL_HOST=localhost
```

* **Fourth Step**

  You can run the app with

```
(venv) USER$: python3 app/app.py
```

## API tests:clipboard:

To test the app you must set the MYSQL_DB variable to "testprueba" and run the **test_app.py** file

```bash
(venv) USER$: export MYSQL_DB=coworking_test
(venv) USER$: export PYTHONPATH=app
(venv) USER$: python3 tests/test_models.py
(venv) USER$: python3 tests/test_controllers.py
```

## Author

* **Juan Pablo Yepes Tamayo**

- [GitHub](https://github.com/PabloYepes27)
- [Linkedin](https://www.linkedin.com/in/pabloyepes27)
- [Twitter](https://twitter.com/pabloyepes27)
