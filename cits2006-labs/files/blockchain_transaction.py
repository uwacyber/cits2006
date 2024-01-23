import requests

# Create a new transaction
new_transaction = None #remove after completing this task
#
#
# YOUR CODE GOES HERE
#
#

# Send the transaction to the server
response = requests.post('http://localhost:8000/transactions/new', json=new_transaction)
print(response.json())
