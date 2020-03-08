# Setting Up Your Python Stack

Below you can find the tools we'll use throughout the semester to work with Python. Please complete these technical tasks as soon as possible.

## Task 1: Python Setup

1. In the course we'll use Python 3.7/3.8, the latest Python versions. The easiest way to install Python is via Anaconda, a popular Python distribution for the scientific community. We'll get to know Anaconda throughout the course.
2. Download __Miniconda__ from [here](https://conda.io/miniconda.html) for Python 3.7/3.8. Miniconda contains the Python interpreter, i.e. the software that can run Python code, and grants you the ability to install third party libraries for Python, which will become very useful later in the course. We'll explore Miniconda's other important features throughout the course.
3. During Miniconda's installation you have to make sure to install in for "All Users". You'll also be asked whether to use conda's Python as the system's default Python and add it to the PATH. __Please check these options.__
4. Now that you have Python installed, you probably want to write some code to go along with it. Python code can be written in any editor, as long as the file is saved with a `.py` suffix. However, some editors are better than others, containing more features and making the developers' lives easier. In this course I _highly recommend_ using Visual Studio Code (VSCode) as your main editor, especially if you have no previous Python experience. To install it, download it from its [download page](https://code.visualstudio.com/Download). After installing it, you'll also have to install the Python Extension, which can be found either inside VSCode (in the extensions menu on the left side of your screen) or from [here](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
5. Lastly, you'll have to help VSCode find your Python installation. After opening a `.py` file (you can create one just for this purpose), click on the yellow "Select Python Environment" button on the bottom left side of your screen and select from the list the conda "base" environment.
6. That's it! Python is installed and you're ready to code.
Note: After that Python installation will finish you'll probably receive quite a few prompts from VSCode regarding the installation of different packages and libraries. Feel free to press Yes on all of them, they're not malware and they'll generally improve the behavior of this editor.

## Task 2: Version Control

Scripts are saved and catalogued using version control. The application we'll use this semester is called `git`, and as a web interface we'll use GitHub.com.

To install `git`, go [here](https://git-scm.com/downloads), download the client for your operating system and install it. Before using it you'll have to tell `git` who you are. Open a new command-line session, i.e. one that was opened after you finished installing `git`, and write the following two commands (with the proper values replaced):

```bash
git config --global user.name "MY_NAME"
git config --global user.email "MY_EMAIL_ADDRESS"
```

The actual username and email don't matter that much, they just identify you when looking at your commits.
<!--
## Task 3: Repl.it

The first exercise will be written, run and submitted using `repl.it`, a website in which you can write and execute Python code, alongside many other languages. Please [go there](https://repl.it/repls) and sign up. Then go to [our classroom](https://repl.it/community/classrooms/136766) and click "Take and Learn" to enroll yourself. You should see the details of your first assignment there. Submission is also done through the `repl.it` interface. -->

## Extra: Jupyter Notebook

The classes are posted in an editable Jupyter Notebook format, which allows for live coding and easy code presentation. It's also a great tool for "quick-and-dirty" data analysis. Thus I recommend you to install it and use it throughout the semester and beyond.

1. Open a command line and write `conda install jupyter notebook`.
2. The notebook is installed! Run it with a simple `jupyter notebook` command in the command line. It will open a file browser which you can use to navigate to the folder containing existing notebooks, or to the folder in which you wish to create a new one.
