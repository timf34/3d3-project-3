# Project 3 - 3D3 - Blockchain messaging network 

# TODO - Project 3

- [ ] Need to improve the robusteness of the network nodes
  - ie show that... 
  - Also include response statuses for each request 
  - Also include a way to show the status of the network
- [ ] Need to show robustness to content types in the network
  - ie strings, integers, etc.

## Instructions
### Setup:

Clone the project (or not, we will keep this repository private till the deadline)
```
git clone https://github.com/satwikkansal/python_blockchain_app.git
```

Set up a virtual environment if you would like to
```
virtualenv venv
```

Install the requirments - we will use pip
```
pip install -r requirements.txt
```

This was tested with Python 3.7.3

### Running the code:
Ensure you're in the project directory
```
cd 3D3-project-2
```

Now open a terminal and set the flask_app variable to network.py - this will depend on your OS/ terminal, we will consider powershell
```
# On Windows PowerShell
$env:FLASK_APP = "network.py"

# On Bash 
export FLASK_APP=network.py

On Windows CMD 
set FLASK_APP=network.py
```

Then run (note that the port isn't important, we will use port 8000). It is important to do this in the same terminal that you set the environment variable aove/
```
flask run --port 8000
```

Now in another terminal run the app. This will start the server and it is this link that you follow for the web app!
```
python run_app.py
```

Now you should be able to access the app at [http://localhost:5000](http://localhost:5000). 

### Functionality

1. Type your message in the text box, and your name in the name box, and then click post. 
   1. The message will be posted to the blockchain. 
2. Now click 'Request to mine'
   1. The node will request all other nodes to mine the block. 
3. Then click 'Resync'
   1. Our message board will refresh and the message will be posted to the page. 
   

## Resources

This project was inspired by:
- [Blockchain](https://en.wikipedia.org/wiki/Blockchain)
- [Blockchain basics](https://www.youtube.com/watch?v=Q_XZQZQZQZQ)
- [Python Blockchain App](https://github.com/satwikkansal/python_blockchain_app)
  - It was inspired by this repo in particular, from which we modified the web app interface. Much larger changes were 
  made to the blockchain code, which we refactored quite a bit to produce cleaner and more modular code - this really
  helped with our understanding of blockchain. We also refactored the networking code to suit our needs, and once 
  again, make it more 'clean' and readable.





