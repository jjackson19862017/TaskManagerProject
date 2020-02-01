# Task Manager Project

# From the begining

## Flask

### Install Flask
For GitPod I typed 
    "pip3 install flask"
        (However you might need "sudo")

### Creating Python file
Created app.py
    "touch app.py"

## Heroku

### Connection
Created new app in Heroku and added it in the webpage not CLI

### Requirements file

"pip3 freeze --local > requirements.txt"

### Procfile

"echo web: python app.py > Procfile"

### Notes
Check for order of imports and alignment of text.

## MongoDB

### Giving Flask Ability to connect to it
"pip3 install flask-pymongo"
"pip3 install dnspython"

### Notes
Make sure the "templates" folder is in lower case otherwise it wont find the files. IE tasks.html

## Generating HTML template
Goto templates folder and type "touch base.html"

### Materlize
old version
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
icons
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

JS to be inserted before "/body"
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>

## Tasks HTML
Had to copy in the GITHUB Code, as mine for some reason didnt work. :(

# Add Task Section
Created addtask.html, and gave it basic content.

## Added Form
Use materlize to copy across form elements.

Added Form functionality

# Static content
Created folder using "mkdir static"

## CSS
Added some code to make the buttons smaller.

# Category Options
Created categories.html, and copied the content from tasks.html.
Modified the code to work with categories.html

# Code Institute

Welcome Stephen Jackson,

We have preinstalled all of the tools you need to get started.

To run a frontend application in GitPod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Expose*,

Another blue button should appear to click: *Open Browser*.

To run a backend python file, type `python3 app.py`, if your python file is named `app.py` of course.

A blue button should appear to click: *Expose*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons. 

Happy coding!
