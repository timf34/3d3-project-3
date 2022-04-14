# Project 3 - 3D3 - Blockchain messaging network 

# General TODO - Project 3

- [ ] Need to improve the robustness of the network nodes
  - The best way to do this is to post status responses, to the 
  terminal is probably not the best way to do this but enough for now.
  We would probably want to have a **constant status response displayed 
  on the webpage**!
- [ ] Need to show robustness to content types in the network
  - Show that our network can handle different input types.
- [ ] Refamiliarize myself with the code base to spot where the improvements
  are needed.

## Programming TODO 
- [ ] Add test cases directly in the code rather than having to use the 
    web interface. 
- [ ] Post the https response status to the web interface.





## Project 3 - Global Problem 

With this project we are looking to contribute to the global problem 
that is Cancel Culture and Free Speech. In order to help combat this 
problem we are looking to build a network of nodes that can be used 
to communicate and publish to a public message board where all messages 
are stored _forever_. 

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

### Setting up multiple nodes 

We can set up multiple nodes by using multiple terminals. Also note that for these
instructions, its best to use a bash terminal for the `curl` commands as command 
prompt and powershell seem to act strangely to the quotes ' and ". 

Follow from the instructions above where we have a node set up at local port `8000`.
We can now repeat the process setting up nodes with ports `8001`, `8002`, `8003` etc.

Ensure to set the environment variable `FLASK_APP` to `network.py` in each terminal.

Run `flask run --port 8001` 

Then to register the nodes, and **ensure you do this in a bash terminal** (such as Git Bash) (to avoid issues with parsing the " and ')
run 

```
curl -X POST http://127.0.0.1:8001/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://127.0.0.1:8000"}'
```

It should say _registration successful_. 
Also make sure to do this before you have posted to the message board. 

You can repeat this process on as many ports as you want. 

To check whether this is working, we can query the nodes for a copy of their blockchain.
So after we have posted a few messages to the message board, we can run:

```
curl -X GET http://localhost:8001/chain
```

This will show us whether the multiple nodes are working or not - we can query it to 
see if the other nodes (8001, 8002, etc.) are updating their blockchain!



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





