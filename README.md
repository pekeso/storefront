# storefront

This is a store app 

## Set Up

This step involved creating the virtual environment with `pipenv`

## Create the storefront project

This step involves creating the Django project with the following command

`django-admin startproject storefront .`

The project is named storefront and the `.` signifies that the project is stored under the current directory.

## Create the store, tags and likes apps

A Django project is composed of one or many apps.

To create an app, we use the following command

`python manage.py startapp appname`

After an app is created, it must be added to the `INSTALLED_APPS` in the project's settings.

There are configurations like mapping URLs to views 

## Building the data model

This is an e-commerce app.

The data model is based on a simple e-commerce app with not a lot of features.

In Django it's so easy to create a model. 

Example

`class Product(models.Model)`

We also define the data relationships when creating the data model.

## Setting Up the database

After the data modeling is done, the next step is make migrations with the following command 
`python manage.py makemigrations`.


