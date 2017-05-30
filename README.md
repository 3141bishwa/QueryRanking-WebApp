# Query Classification using Word Vectors

The following web application creates a web application locally that classifies  queries into different catgeories based on the North American Product Classification System (NAPCS).

Here are the steps to install and run the web application


Assuming you have virtualenv installed on your computer (if not)

Create a directory 'QueryApp' somewhere on your machine.

Change your directory to that folder using `cd`.

Create a virtual environment using

`virtualenv query`

To begin using the virtual environment, it needs to be activated. For that , go inside the directory and do

`cd query`

`source bin/activate`

Now copy the Git repository inside the directory using:

`git clone https://github.com/bishwa3141/QueryRanking-WebApp.git`

Since we are in a virtual environment, we need to add dependencies required to run the app separately. These dependencies are mentioned in requirements.txt. Install them on your virtual environment by going into the project folder 

`cd QueryRanking-WebApp`

and doing

`pip install -r requirements.txt`

Next, download the pre-trained word2vec model (from here)[https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download] and put it inside your directory.


Run the application locally using 
`python manage.py runserver`
