# Lab 5: IDS (NOT READY)

## 5.1. Introduction
In this lab, we will setup and run IDS for vehicle network. Smart cars are becoming more widely used today, allowing hackers to gain access to the vehicle network and control the vehicle. Consequently, the attacker can cause undesireable effects on the car, which can physically impact the driver and passengers. Therefore, it is important to detect and prevent such attacks.

## 5.2. Lab Environment
We will use Jupyter notebook to conduct this lab. To do this, we need to have the Jupyter notebook installed. You could technically use the web version, but that would require uploading files (i.e., datasets), which will take time to setup. Therefore, you are encouraged to use the local version of Jupyter notebook (e.g., plugin to VSCode or other similar IDEs).

If you are stuck getting Jupyter notebook running, it is a good time to seek help from the facilitator.



{% hint style="info" %}
Before you start, download the files you need:
```
wget https://github.com/uwacyber/cits2006/raw/2024/cits2006-labs/files/ids.zip
```
{% endhint %}

## 5.3. Data Manipulation
In order to perform IDS, we need to first understand how to access and manipulate dataset we will be using. This is done by using [Pandas](https://pandas.pydata.org/), a Python library for data analysis. We will use Pandas to access the dataset and perform data analysis. If you already know how to use Pandas, you may skip this section (you can always come back as necessary).

{% hint style="info" %}
In this section, we will be using the pandas.ipynb from the zip file.
{% endhint %}

### 5.3.1. Loading the data
Pandas provides a DataFrame class, which is a 2D array (i.e., a table). We will use the DataFrame class to load the dataset and perform data analysis. This is simply done by importing pandas, then loading dataset using pandas (such as CSV files).

```python
import pandas as pd

df = pd.read_csv('dataset.csv')
```

#### TASK 1
Rewrite the code in your Jupyter notebook's first cell so that it loads the file: 0_Preliminary/0_Training/Pre_train_D_1.csv

You should get an output similar to this:
<figure><img src="/img/pandas_load.png" alt=""><figcaption></figcaption></figure>


### 5.3.2. Accessing the data
- [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html): a Pandas class representing a table (2D array)
- [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html): a Pandas class representing an 1D array

#### DataFrame
There are three main cases on how you can access the dataframe using pandas:
- Case 1. Access a column: **`df[COL_IDX]`**, `df.loc[, COL_IDX]` -> It returns a *Series*.
- Case 2. Access a row: **`df.loc[ROW_IDX]`**, `df.loc[ROW_IDX, ]`  -> It returns a *Series*.
- Case 3: Access an element: `df.loc[ROW_IDX, COL_IDX]` -> It returns a *value*.

The first two cases will return a *Series* object, which is a 1D array. You can access the value of the *Series* object using the index (e.g., `series[IDX]`). The last case is used to access a value in the dataframe by specifying both the row and column index.

#### Series
Just consider it a Python list: `series[IDX]`

For more information, you should read the pandas documentation:
[Pandas user guide: Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html)

#### TASK 2
Write the code required in subsequent cells as specified in the comments.
You should also experiment by trying to load different series as well as values.




