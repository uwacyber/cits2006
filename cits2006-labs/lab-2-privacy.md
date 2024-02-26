# Lab 2: Privacy

## 2.1 Introduction

### Lab Activity: Privacy Breach and Mitigation Techniques

#### Scenario

A water service company has collected data on multiple household water usage within a residential  
areas. Their goal is to be able to curate to different households on their water usage for billing  
purposes. On the other hand, there are concerns about privacy breaches as data contains sensitive information about each household's daily activities.

## 2.2 Re Identification Attack

So what is a Re Identification Attack? In a nutshell, it is a type of privacy attack where an attacker attempts to determine if a specific record, or 'row of data' actually belongs to the dataset that was used for training a specific machine learning model. For a better understanding, in this scenario, a type of Re Identification Attack involves determining whether a specific household's water usage matches with the main dataset. The objective is by exploiting the model's output, an attacker can determine if a specific record was part of the training dataset.

### 2.2.1 Re Identification Attack: Data Preparation

It starts by data collection, as the water service company has collected data on multiple household water usage within a residential area. This dataset is then used as the foundation for the machine learning model. The dataset contains the following columns:

user.key: A unique identifier for each household  
datetime: The date and time of the water usage  
meter.reading: The amount of water used  
diff: The difference in water usage from the previous reading

Run the wget command to download the dataset.

{% hint style="info" %}  
Before you start, download the files you need:

```
wget https://github.com/uwacyber/cits2006/raw/2024/cits2006-labs/files/water_data.csv
```

{% endhint %}

You are also given a pre proccessing script to clean the data. Run the following command to download the script.

```python

import csv
import os

relative_path = os.path.join('water')
#r_folder_format = 'swm_trialA_{}K.csv'
r_folder_format = 'water_data.csv'
w_folder_format = 'households_{}'
w_file_format = os.path.join('households_{}', '{}.csv')
wd = os.getcwd()

FILE_ROWS = 40960  # element number within a section


# Read the CSV file
def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        # Return the header and the rows
        return [row for row in reader]

# Write the CSV file
def gen_csv(id):
    # Read the CSV file
    r_folder_path = os.path.join(wd, relative_path, r_folder_format.format(id))
    with open(r_folder_path, 'r') as file:
        lines = file.readlines()[1:-1]

    # Create a dictionary to store the data
    my_map = {}
    # Iterate through the rows
    for line in lines:
        # Replace the spaces with semicolons and the Null values with 0.001
        line = line.replace(' ', ';').replace('Null\r', '0.001')
        # Split the line by semicolons
        slices = line.split(';')
        # Get the first slice as the key
        file_key = slices[0]
        # If the key is not in the dictionary, add it
        if file_key not in my_map:
            # Add the key to the dictionary
            my_map[file_key] = []
        # Append the slices to the dictionary
        my_map[file_key].append(slices[1:])

    # Create a new folder to store the data
    w_folder_path = os.path.join(wd, relative_path, w_folder_format.format(FILE_ROWS))
    # Create the folder if it does not exist
    os.makedirs(w_folder_path, exist_ok=True)

    # Iterate through the dictionary
    for key, value in my_map.items():
        # If the length of the value is less than the file rows, continue
        if len(value) < FILE_ROWS:
            print(f"[{key}] has {len(value)} rows.")
            continue
        # Create a new file to store the data
        w_file_path = os.path.join(wd, relative_path, w_file_format.format(FILE_ROWS, key))
        # Write the data to the file
        with open(w_file_path, 'w', newline='') as new_file:
            writer = csv.writer(new_file)
            writer.writerows(value)

    print(f"len: {len(my_map)}")


def main():
    print(wd)
    gen_csv(1)


if __name__ == "__main__":
    main()

```

Feel free to explore the dataset and the script to understand the data and the pre processing steps.  
The script outputs in your terminal how many rows of data that a specific household has. This is a potential privacy breach as the data contains sensitive information about each household's daily activities

NOTE: Depending on where you downloaded the dataset, you may need to change the path in the script.

### 2.2.2 Re Identification Attack: Attacker Scenario

Let's assume the position of the attacker. The attacker has access to the publicly available machine learning model, but not the original dataset. Once again, their main objective is to determine if a specific household's water usage matches with the main dataset. The attacker can use the model's output to determine if a specific record was part of the training dataset.

The attacker then begins by selecting a specific target household and obtaining their water usage data. Then it used the trained model to predict the water usage patterns of the target household. The attacker then compares the model's output with the actual water usage data of the target household. If the model's output is similar to the actual water usage data, the attacker can infer that the target household's data was part of the training dataset.

### 2.2.3 Privacy Implications

The successful execution of the Re Identification Attack raises serious privacy concerns for the water service company's customers. By exploiting the model's output, the attacker can deduce whether specific households are included in the training dataset, compromising their privacy.

Furthermore, if the attacker identifies a household as part of the training dataset, they may infer sensitive information about the household's water usage habits, daily routines, and occupancy patterns. This information could be exploited for malicious purposes, such as targeted advertising, profiling, or even burglary.

### 2.2.4 Re Identification Attack: Mitigation Techniques

There a a couple of techniques to mitigate the risk of Re Identification attacks, and some several strategy implementations are:

Differential Privacy: By introduce noise to the training dataset or model predictions to prevent attackers from accurately inferring identification status.

Limited Model Access: Restrict access to the trained model and ensure that only authorized personnel can query the model's predictions.

Homomorphic Encryption: Encrypt the training dataset and model to prevent attackers from accessing sensitive information.

## Task 1

You are to perform a Re Identification Attack using the dataset above:

Complete the TODO section in the code below to perform the Re Identification Attack.  
The code will train a machine learning model using the dataset, and then perform a Re Identification Attack on a specific target record. What you have to write is explained in the comments of the code.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset with semicolon as the separator
data_path = 'water_data.csv'
data = pd.read_csv(data_path, sep=';')

# Display the first few rows of the dataset
X = data.drop(columns=['user.key'])
y = data['user.key']
print("Columns of the CSV file:", data.columns)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['user.key', 'datetime']), data['user.key'], test_size=0.2, random_state=42)

# Display the shapes of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)

# Train a machine learning model using the training set
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
# Predict the testing set and calculate the accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# Perform Re Identification Attack

# ------------TODO--------------
def re_identification_attack(model, target_record):


    # Step 1: Predict Target Record: Use the predict method of the model to predict the target record. Remember to reshape the target record using reshape(1, -1) before passing it to the predict method.
    #TODO
    
    # Step 2: Generate Synthetic Data: Create synthetic data by copying the target record and modifying one spefic feature. Can be a specific data value to make a syntehtic data point.
    #TODO
    
    # Step 3: Predict Synthetic Data: Use the predict method again to predict the synthetic data point.
    #TODO
    
    # Step 4: Return Result: Return True if the predictions are different (indicating re identification), and False otherwise.
    return #TODO

#------------END TODO--------------

# Choose a target record for the attack
target_index = 0
target_record = X_test.iloc[target_index]

# Perform the Re Identification Attack
is_member = re_identification_attack(model, target_record.values)
print(f"Is target record a member of the training set? {'Yes' if is_member else 'No'}")

```

STEPS TO COMPLETE THE TODO SECTION:

Step 1: Predict Target Record: Use the predict method of the model to predict the target record. Remember to reshape the target record using reshape(1, -1) before passing it to the predict method.

Step 2: Generate Synthetic Data: Create synthetic data by copying the target record and modifying one spefic feature. Can be a specific data value to make a syntehtic data point.

Step 3: Predict Synthetic Data: Use the predict method again to predict the synthetic data point.

Step 4: Return Result: Return True if the predictions are different (indicating re identification), and False otherwise.

Hints:

- Use the predict() method to retrieve the prediction of target and syntehtic data.
- ONLY Modify one feature of the target record to isolate prediction.



## 2.3 Task 2: Data Aggregation

### 2.3.1 Overview

Now with privacy concerns raised by the customers, the water company now decide to implement data aggregation techniques to help mitigate the privacy risks caused by a re identification attack or a re-identification attack. The goal of data aggregation is to make it harder for an attacker to identify specific individuals from a large data by extracting sensitive information. This way, data aggregation technique groups the data into larger clusters or intervals, where it gets harder to match if a known dataset matches with the target dataset specified.

### 2.3.2 How it Works

The concept of data aggregation is pretty simple, it aggregates the data into larger intervals making it harder to match. For example, if the water company has a dataset of water usage for each household, they can aggregate the data into larger intervals such as weekly or monthly usage. This way, it becomes harder for an attacker to match the known dataset with the target dataset. The data aggregation technique can be applied to both the training dataset and the model's predictions.

## Task 2

You are to write a python script that reads in the csv file given above and aggregate the data of each 'user.key' into larger intervals and outputs it into a new csv file. Attempt to use your working code of the attack in Task 1 and see if the value ot model prediction changes. Complete the TODO section in the code below to aggregate the data.

```python
import pandas as pd

# Read the CSV file with semicolon delimiter, skipping the first row (header)
df = pd.read_csv('water_data.csv', delimiter=';', skiprows=[0], names=['user.key', 'datetime', 'meter.reading', 'diff'])

# TODO: Iterate through each row and convert 'datetime' column to datetime format

# Set 'datetime' column as the index
df.set_index('datetime', inplace=True)

# Print the first few rows of the DataFrame to verify the changes
print("DataFrame after converting 'datetime' column to datetime format:")
print(df.head())

# Resample data into 5-minute intervals and sum the values
df_aggregated = df.resample('5T').sum()

# Reset index to make 'datetime' column a column again
df_aggregated.reset_index(inplace=True)

# Print the first few rows of the aggregated DataFrame
print("Aggregated DataFrame:")
print(df_aggregated.head())

# Write aggregated data to a new CSV file
df_aggregated.to_csv('water/output_aggregated_5min.csv', index=False)
print("Aggregated data saved to 'output_aggregated_5min.csv'")
```

## 2.4 Task 3: Privacy Techniques

### 2.4.1 Differential Privacy

Now lets head over to privacy techniques that can be used to mitigate such risks of privacy breach. In this lab, two techniques will be discussed and they are Differential Privacy and Homomorphic Encryption.  
Starting off with differential privacy (DP for short), its main technique is to add 'noise' to the data to mainly prevent attackers from accurately inferring re identification status which confirms if a specirfic record was part of a dataset. An easy way to understand it is , imagine you are in a crowded room, and you have a nosy neighbor hoping to know if a specific person is in the room. Due to the absolute noise, the neighbor cannot deduce if that specifric person is in the room or not. Same concept with differential privacy. We will be more focused on using differential privacy in this lab.



### 2.4.2 Homomorphic Encryption

On the other hand, there is homomorphic encryption. What this does is it encrypts the training dataset and the model preventing attackers from accessing any sensitive information. Now what's interesting with this, as it is a homomorphic encryption, it allows the data itself to be encrypted and stay encrypted and to have computations to be done without any need of decrypting the information in the first place. It can be simplified into three main steps:

- Encrypt the data: First the data is encrypted using a momorphic encryption algorithm.
- Computation and training done on the encrypted data: The encrypted data is then used to train the model and perform computations. Interestingly, unlike any other traditional encryption algorithims, homomorphic encryption allows specific operations to be performed directly on the encrypted data.
- Decrypt the results: The results are then decrypted to obtain the final output. After everything has been encrypted and computed, the result that is obtained is in its encrypted form, and using the decryption key from the original algorithm method, the ciphertext is decrypted to obtain the final output.

## Task 3

Your last task for this lab is to complete the differential privacy code below. From the same csv file downloaded above, your task is to use DP on the 'meter.reading' column and add noise to the data. The code below is a template to get you started.

```python

import pandas as pd
import numpy as np

def add_noise(value, epsilon):
    scale = 1 / epsilon
    noise = np.random.laplace(scale=scale)
    return value + noise

def apply_differential_privacy(input_file, output_file, epsilon):
    # TODO

def main():
    input_file = 'water_data.csv'
    output_file = 'output.csv'
    epsilon = 1.0  # Privacy budget
    apply_differential_privacy(input_file, output_file, epsilon)
    print("Differential privacy applied successfully to the CSV file.")

if __name__ == "__main__":
    main()
```

Deducing the code above, we can see there are two functions apart from the main function. Once again, in general, applying DP is basically taking in the original data and add noise to it.

add_noise() function: This function takes in two parameters, the value and the epsilon. The value is the original data and the epsilon is the privacy budget. The function then adds noise to the value and returns the value with noise. What is privacy budget (epsilon)? It is the main parameter that determines how much 'noise' is added to the data. The smaller the value, the more noise is added and more privacy is preserved. Counterwise, the larger the value, the less noise is added. Feel free to play around with the epsilon value to see how it affects the noise data.

apply_differential_privacy() function: This function takes in three parameters, the input file, the output file and the epsilon. This is your TODO function. Use this function to read the csv file, add noise and create a new column in the csv file with the noisy data. From there see how much the value changes.

## Task 4 (Optional)

If you have time and would like to proceed further, you can attempt to implement homomorphic encryption on the dataset. This is an optional task and is not required to complete the lab. Feel free to explore and implement homomorphic encryption on the dataset.

Create a simple python script that reads in the csv file and encrypts the data using homomorphic encryption. Feel free to use any homomorphic encryption library of your choice. Once the data is encrypted, perform some simple computations on the encrypted data and decrypt the results to obtain the final output. Some notable libraries for HE are PySEAL and TenSEAL. Do note that PySEAL does not work properly with Python3, therefore if you would like to use this library, you would have to use Python2.7. (Use a new environment, virtual machine, or docker container)

## Summary

In this lab, you have learned about the concept of Re-Identification Attack and how it can be used to determine if a specific record was part of the training dataset. You have also learned about data aggregation and how it can be used to mitigate the privacy risks caused by a re-identification attack. Finally, you have learned about differential privacy and how it can be used to add noise to the data to prevent attackers from accurately inferring re identification status and knowing if the data is actually part of the training set or not. You have also learned about homomorphic encryption and how it can be used to encrypt the training dataset and model to prevent attackers from accessing sensitive information.
