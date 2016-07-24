# Sentiment
##Introduction
Sentiment Analysis Marketplace for Software Engineering course

This repository has currently been only tested on a unix system (Ubuntu 16.04 LTS)

##Setup
###1. Python
The project was mainly tested using Python 3.5.1 but should run in Python 2.7.
- https://www.python.org/

###2. pip
Pip is normally installed with Python but if it wasn't you can download it if necessary.
- https://pip.pypa.io/en/stable/

###3. Virtual Environment (Optional)
As with any Python project, it is recommended to set up a virtual environment prior to installing Python packages. You can find resources for this at the Python Packaging Authority (PyPA).
- https://virtualenv.pypa.io/en/stable/

*You can also use this in combination with virtaulenvwrapper which can simplify the commands to managing different virtual environments.*
- https://virtualenvwrapper.readthedocs.io/en/latest/

###4. Python Packages
All the Python packages used in this project can be found in the requirements.txt file at the root. To install all the packages using the file, use the command `pip install -r requirements.txt`. If using Python 3+, use the command `pip3 install -r requirements.txt`.

- **Django**: Framework used for the web backend in combination with bootstrap to create the user interface.
  - https://www.djangoproject.com/
  - http://getbootstrap.com/

- **Pillow**: Library used for the display of images.
  - https://python-pillow.org/

- **vaderSentiment**: A lexicon and rule-based sentiment analysis tool that to assist in our rating system.
  - https://github.com/cjhutto/vaderSentiment/

###4.5 Python 3+ Modifications
If using Python 3+ you will need to modify a file from the vaderSentiment Python package. Locate and open vaderSentiment.py in your system and make the following changes:

- Insert `from imp import reload` after line 19
- Change the following line:
  - Old line: `return dict(map(lambda w, m: (w, float(m)), (wmsr.strip().split('\t')[:2] for wmsr in open(f, encoding="utf-8"))))`
  - New line: `return dict(map(lambda wm: (wm[0], float(wm[1])), [wmsr.strip().split('\t')[0:2] for wmsr in open(f, encoding="latin-1") ]))`
- Change the following line:
  - Old line: `print sentence`
  - New line: `print(sentence)`
- Change the following line:
  - Old line: `print "\t" + str(ss)`
  - New line: `print("\t",str(ss))`
- Change the following line:
  - Old line: `print "\n\n Done!"`
  - New line: `print("\n\n Done!")`
  
###5. Clone Repository
You can do this in two ways. You can clone the repository using Git or by simply downloading the copying the source files to the working directory.
- https://git-scm.com/

##Running the Project
To run the project, enter into the directory where the `manage.py` file is located. Once there, you will need to set the appropriate migrations to make the initial database. To do this enter the command `python manage.py makemigrations`. If no errors were encountered you can enter the command `python manage.py migrate` to create the database. Once complete, you can start the local server by entering the command `python manage.py runserver`. After the server has successfully started, you can go to the site by opening a browser and entering http://127.0.0.1:8000.
