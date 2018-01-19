# Assignment: Login and Registration

Build a flask application that allows login and registration.

## Registration
The user inputs their information, we verify that the information is correct, insert it into the database and return back with a success message. If the information is not valid, redirect to the registration page and show the following requirements:

### Validations and Fields to Include
1. First Name - letters only, at least 2 characters and that it was submitted

2. Last Name - letters only, at least 2 characters and that it was submitted

3. Email - Valid Email format, and that it was submitted

4. Password - at least 8 characters, and that it was submitted

5. Password Confirmation - matches password


## To-do
1. Create a basic login and registration form

2. Redirect user to a success page on successful login and register

3. Display error messages if either login or registration validations fail

4. Use md5 to hash passwords before inserting them into the database
