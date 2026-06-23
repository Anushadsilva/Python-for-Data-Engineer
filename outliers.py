import pandas as pd
import matplotlib.pyplot as plt

my_df = pd.DataFrame({"input1": [15,41,44,47,50,53,56,59,99],
                  "input2": [29,41,44,47,50,53,56,59,66]})

print(my_df.boxplot(vert=False))

outliers_col = ["input1", "input2"]


for col in outliers_col:
    lower_quartile = my_df[col].quantile(0.25)
    upper_quartile = my_df[col].quantile(0.75)
    iqr = upper_quartile - lower_quartile
    min_border = lower_quartile - iqr * 1.5
    max_border = upper_quartile + iqr * 1.5

    outliers_df = my_df[
        (my_df[col] < min_border) |
        (my_df[col] > max_border)
        ].index

    print(outliers_df)
    print(f"{len(outliers_df)} outliers detected in column {col}")

    my_df.drop(outliers_df, inplace=True)

my_df = pd.DataFrame({"input1": [15,41,44,47,50,53,56,59,99],
                  "input2": [29,41,44,47,50,53,56,59,66]})


for col in outliers_col:
    mean = my_df[col].mean()
    std = my_df[col].std()

    min_border = mean - std * 3
    max_border = mean + std * 3
    outliers_df = my_df[
        (my_df[col] < min_border) |
        (my_df[col] > max_border)
        ].index

    print(outliers_df)
    print(f"{len(outliers_df)} outliers detected in column {col}")

    my_df.drop(outliers_df, inplace=True)






