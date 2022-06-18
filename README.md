# SIAI4sustainability

## 

How to use:

1) Create a new project in the SIAI4sustainability repository in the Github cloning the repository.

2) Open the project in the IDE of your choice (e.g. Visual Studio Code).

3) Create a new terminal and navigate to the project folder.

4) Run the following command to create a virtual environment:

```virtualenv -p python3 env_name```

5) Activate the virtual environment:

```source env_name/bin/activate```

6) Install the dependencies:

```pip3 install -r requirements.txt```

7) Run the following command to run the application and build maps with the data in the csv files from Scopus:

```python3 gendata-scopus.py```

8) To build the maps with the data in the text files extracted from Web of Science, you need to run the following command:

```python3 gendata-wos.py```

9) For more details and instructions on how to use the application, please refer to instructions in the comments inside of the *.py files available in the repository.

10) To cite the application, please refer to bibtex entry below:

TBD.