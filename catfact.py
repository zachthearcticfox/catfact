#!/usr/bin/env python
"""
Catfact module.
Generates a random catfact.
Module Version 1.0.0

:Example:
>>> print(get_catfact())
Example catfact.
"""

try:
	import requests
except ModuleNotFoundError:
	exit('Error: \'requests\' module not found. | Solution: Install the \'requests\' module with \'pip install requests\'')

def get_catfact():
	## Get the fact and set it to the fact variable
	fact_req = requests.get(url='https://meowfacts.herokuapp.com/') # Sends a get request to the meowfacts API
	if fact_req.status_code == '404': # Checks for error 404
		raise FileNotFoundError('404 | File not found') # Raises an error if 404 occurs
	fact_json = fact_req.json() # Turn the catfact into json
	fact = fact_json['data'][0] # Turn the catfact into a string
	return fact # Returns the fact

if __name__ == "__main__":
	print(get_catfact())