# landbank
This coding project is to satisfy the [CCLRC code test](https://github.com/CCLRC/code-test).


## Installation
To install on Ubuntu, first you will need to confirm that Python3 and virtualenv is installed.

```
sudo apt install python3
pip3 install virtualenv
```

You will then create your virtual environment and install the required packaged (flask, jsonpickle, requests, and its dependencies). Set landbank as your current directory if you haven't already. Then run

```
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

For the program to work correctly, you should add a Google Maps API key. I removed mine from the project since it is a security risk to have a completely open API key like that in a public GitHib repo (and Google reminded me of this within a minute of me pushing it). You can add a key by creating a text file in the root directory called 'mapskey.txt' and place your API key there. Without this file, the program will still work, but there will be an error over the map.

To run the program, just type `python run.py` and the flask program will start.

## Using
To use the API endpoint and convert NEOCANDO data to json, just go to localhost:3000/api. You can attach the parcel id as either a query string (using the letter "p") or as an additonal page. For example:

* [localhost:3000/api?p=109-02-088](http://localhost:3000/api?p=109-02-088)

or

* [localhost:3000/api/109-02-088](http://localhost:3000/api/109-02-088)

If you do not give a parcel, it will assume 109-02-088.

To go to the front-end site, just go to the home page at [localhost:3000](http://localhost:3000). Click on one of the five parcels availabe, and it will load the data for that parcel. Data is displayed in two columns if the screen is wide enough. Update date is available as a tooltip by hovering over the data value field.
