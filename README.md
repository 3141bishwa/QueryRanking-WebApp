# Query Classification using Word Vectors

The following web application creates a web application locally that classifies  queries into different catgeories based on the North American Product Classification System (NAPCS). For a full description of how the application works, have a look at the [paper](https://drive.google.com/file/d/0B1ttwhq718PdV1Rrbk0tT01iOGxhRHlsOHJJYkV4Qmx6OHhv/view?usp=sharing)

Here are the steps to install and run the web application on a **Unix-based machine(Linux, macOS)**. If you use a Windows machine, the steps are similar but not exactly the same. Have a look at [this article](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/) to figure out how to use pip and virtual environments in Windows. 

Assuming you have virtualenv installed on your computer (if not you can install virtualenv using `pip install virtualenv`)

Create a directory 'QueryApp' somewhere on your machine.

`cd QueryApp`

Create a virtual environment using

`virtualenv query`

Virtualenv creates a Python environment that is segregated from your system wide Python installation. In this way, you can test your module without any external packages mucking up the result. To begin using the virtual environment, it needs to be activated. For that, do

`cd query`

`source bin/activate`

Now copy the Git repository inside the directory using:

`git clone https://github.com/3141bishwa/QueryRanking-WebApp.git`

Since we are in a virtual environment, we need to add dependencies required to run the app separately. These dependencies are mentioned in requirements.txt. Install them on your virtual environment by going into the project folder 

`cd QueryRanking-WebApp`

and doing

`pip install -r requirements.txt`

Next, download the pre-trained word2vec model [from here](https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download) and put it inside your directory.

The directory will look somewhat like this now.

```
QueryRanking-WebApp/
├── db.sqlite3
├── GoogleNews-vectors-negative300.bin.gz
├── manage.py
├── query_rank
├── rank
├── README.md
├── requirements.txt
└── runtime.txt
```

Run the application locally using 
`python manage.py runserver`

Wait up for a couple of minutes for the model to load.
Once the model is loaded, you should see a message on the command line like this.

```
Time taken to load the model: 114.003504
System check identified no issues (0 silenced).
May 30, 2017 - 19:54:40
Django version 1.11, using settings 'query_rank.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now, open a browser and type http://127.0.0.1:8000/ in the address bar. The web application will load.

