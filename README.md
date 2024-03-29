# LAMP-Stack-App
This is an educational project on creating a LAMP stack application within your Linux virtual environment.  It serves as a tutorial to follow along with and learn how to create a LAMP stack application. This repository is primarily to display penetration testing concepts within another repository but can serve as a rudimentary introduction to LAMP.


# Introduction
Hello, My name is Robert H. and I'm an aspiring Cyber Security enthusiast. This repository is meant to serve as a tutorial on building a LAMP stack application within Ubuntu.
* * *
# External Prerequisites
You should already have some type of virtual machine software installed. In this repository I will be utilizing virtual box, and ubuntu. Feel free to use any compatible linux distribution and virtual machine software you prefer. We will also be utilizing a python script so you will need pip installed onto your ubuntu system. The primary purpose for this tutorial will be to help display different penetration testing techniques within my other repository which can be found here - [link will be updated soon]

Virtual Box Link - https://www.virtualbox.org/wiki/Downloads

Ubuntu Link - https://ubuntu.com/


***

# Installation

## Installing Python
You'll first want to ensure that your system is updated, and pip is installed onto your system. You can do this by heading over to your command line console `Ctrl + Alt + T` and running the command `sudo apt install python3-pip`

## Installing MySQL
Next we're gonna install mysql for the database server by running the command `sudo apt install mysql-server`

## Configuring MySQL
Next you're gonna want to pop into the configuration mode for your database server by running the command `sudo mysql`  where you should then be greeted by a welcome message.

Next we're going to want to set up a root user password so that people are not able to login to your database without a password. **DO NOT FORGET THIS PASSWORD!** 

To do this we're going to run the command: `alter user 'root'@'localhost' identified with mysql_native_password by 'Password Here';`

Be sure to include the single quotes with your password in the "password here" section.

## Signing into MySQL
You'll notice now that when you sudo into mysql you are given an error *Access denied for user 'root@localhost' (using password:**NO**)* this is entirely normal and you shouldnt be alarmed.


The new command to sudo into your mysql will be `mysql -u root -p` where you will now be prompted to enter a password. This means you have done everything correctly and your database server is now password protected.

## Installing a pymySQL 
Next, we're going to install a connector between the python script and the database. We can do this by running the command: `sudo pip3 install pymysql` 

## Installing Apache Web-Server
Next, we're going to install a web-server by running the command: `sudo apt install apache2`  You may check this is successfully installed by entering localhost on your browser. You should be greeted by the Apache2 Default Web Page.

## Understanding Apache Web Server

You can modify the default page for the web server by navigating to the apache directory or utilizing the command: `cd /var/www/html` here if you `ls` the directory you should see the default index.html file. You can also create new html files within this directory and navigate to them utilizing the webserver by typing into your browser `localhost/filenamehere.html`

* * *
# Setting up the Yoga Application

## enable multi-processing module for CGI scripting

We want to tell apache that we want to use the multiprocessing module and to allow a CGI script which is the common gateway interface (allow a CGI script to run) by running the command:  `sudo a2dismod mpm_event`  Now we're going to enable the CGI script to run by typing the command: `sudo a2enmod mpm_prefork cgi` and finally we'll restart our apache for these changes to take place. Command: `Sudo systemctl restart apache2`

## Creating a new directory to work with in Apache for our application

We're going to navigate back to the Apache Web Server directory by using the command `cd /var/www/html` We now want to create a new test directory for good practice. We can do this by running the command: `sudo mkdir var/www/test` 

## Modifying the Apache Default Sites Config

Next we're going to open the apache default site configuration within linux's nano editor. We can do this by running the command: `sudo nano /etc/apache2/sites-enabled/000-default.conf` This should open the nano editor for the default conf file. 

You'll want to add the following code to your default configuration file to utilize the provided python script:
```
<Directory /var/www/test>
	Options +ExecCGI
	DirectoryIndex index.py
	</Directory>
	AddHandler cgi-script .py
```

This is essentially telling apache to include the directory we created earlier and the options for that directory is allowing it to execute a CGI file and that cgi file by default will be index.py. Then it's adding a handler as a general rule by telling it to treat .py files as CGI scripts.

Next we're going to modify the line DocumentRoot from `/var/www/html` to `/var/www/test`

Now use `Ctrl + O` to write the file and save it, and `Ctrl + X` to exit out of the nano editor. Restart Apache and continue.

## Creating the SQL database 

Navigate into your mySQL database and enter your previously created password.

next, create a database by entering the command: `create database yoga;` and then go into the database with the command: `use yoga;`  you'll notice that your database is empty. This is becuase we need to create tables which are known as entities in mysql. 

## Creating Tables

Entities can be referred to as object of which data is to be captured. We can create these "objects" by using the command: `create table instructors (id INT, name VARCHAR(20))`  we've now created a table for instructors and we can confirm this by using the command `show tables;` 

## Inserting into tables

You may now insert instructors into your database. with the command insert into instructors values `(number, 'name');` where the number is the ID for the instructor, and the name is the instructors name.

## Finishing up

Now all that is left to do is to place the index.py file provided within this repository into your /var/www/test folder. 

Once you've placed it inside of the folder, you'll want to modify the database values within it to your credentials that you entered.

Example:
``` 
import pymysql
con = pymysql.connect(
			db ='yoga', user='root', passwd='Your Password Goes Here', host=localhost)

```

# You've successfully created a LAMP stack application	

You've now successfully created a LAMP stack application on your Ubuntu Virtual Machine using Apache Web Server. (Linux, Apache, MySQL, PhP)
