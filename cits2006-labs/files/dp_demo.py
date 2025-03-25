from diffprivlib.mechanisms import Laplace
import pandas as pd


def example1():
    # higher value of epsilon means weaker protection (i.e., less noise)
    # higher sensitivity means how much noise is required (0 means none)
    pri_mechanism = Laplace(epsilon=1.2, sensitivity=1.0)

    runs = 10
    sums = 0

    for i in range(runs):
        data = [6, 7, 8, 9, 10]
        result =[]
        for val in data:
            result.append(pri_mechanism.randomise(val))
        print(f"({i+1:2}) Difference: {sum(data) - sum(result)}")
        print()
        sums += sum(data) - sum(result)

    print(f"Average difference: {sums/runs}")




def example2():
    #import partitioned database files
    dataset = pd.read_csv("data.csv" ,sep=",", engine = "python")

    #create a copy of the db
    redact_dataset = dataset.copy()

    #remove the first row data
    redact_dataset = redact_dataset[1:]

    ##uncomment to see the removed first row
    #print(original_dataset.head())
    #print(redact_dataset.head())

    #now, only use the sales_amount column for calculations
    sum_original_dataset = round(sum(dataset['sales_amount'].to_list()), 2)
    sum_redact_dataset = round(sum(redact_dataset['sales_amount'].to_list()), 2)
    sales_amount_Osbourne = round((sum_original_dataset - sum_redact_dataset), 2)

    ##uncomment below to check the difference, which we can use to identify the person
    #print(sales_amount_Osbourne)
    #assert sales_amount_Osbourne == original_dataset.iloc[0, 4]


    #######################
    ###    Now use DP   ###
    #######################
    pri_mechanism = Laplace(epsilon=10.0, sensitivity=1.0)

    #This is the sum for the original db
    dp_sum_original_dataset =[]
    for val in dataset['sales_amount'].to_list():
        dp_sum_original_dataset.append(pri_mechanism.randomise(val))
    dp_sum_og = sum(dp_sum_original_dataset)

    #this is the sum for the modified db
    dp_redact_dataset =[]
    for val in redact_dataset['sales_amount'].to_list():
        dp_redact_dataset.append(pri_mechanism.randomise(val))
    dp_sum_redact = sum(dp_redact_dataset)



    #Final output
    #note, DP output changes every run since it adds random value
    print(f"Sum of sales_value in the orignal dataset: {sum_original_dataset}")
    print(f"Sum of sales_value in the orignal dataset with DP: {dp_sum_og:.2f}")
    print()
    print(f"Sum of sales_value in the second dataset: {sum_redact_dataset}")
    print(f"Sum of sales_value in the second dataset with DP: {dp_sum_redact:.2f}")
    print()
    print(f"Actual Difference in Sum: {sales_amount_Osbourne}")
    print(f"Difference in Sum with DP: {round(dp_sum_og - dp_sum_redact, 2)}")



# example1()

example2()
