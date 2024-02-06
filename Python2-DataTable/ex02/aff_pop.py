from pandas import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def draw_plot(df: DataFrame) -> None:
    """
    Draw the population graph
    """

    # filter data for UAE and Belgium and set index to country
    df1 = df.query(
        "country in ['United Arab Emirates', 'Belgium']"
        ).set_index("country")
    # transpose the data so that the countries are on the x-axis
    df2 = df1.transpose()

    # all values are stored as strings, so convert to numbers
    repl_dict = {'[kK]': '*1e3', '[mM]': '*1e6', '[bB]': '*1e9', }
    df2['United Arab Emirates'] = df2['United Arab Emirates'].replace(
        repl_dict, regex=True).map(pd.eval)
    df2['Belgium'] = df2['Belgium'].replace(
        repl_dict, regex=True).map(pd.eval)

    # Plotting the data
    plt.plot(
        df2.index, df2['United Arab Emirates'],
        label='United Arab Emirates')
    plt.plot(df2.index, df2['Belgium'], label='Belgium')

    # Adding labels and legend
    plt.xlabel('Year')
    plt.xticks(df2.index[::40])  # Show every 40th year
    plt.ylabel('Population')
    # Show every 4 million
    labels = ['0M', '4M', '8M', '12M']
    plt.yticks(range(0, int(df2.max().max()), 4000000), labels)
    plt.title('Population Projections')
    plt.legend(loc='lower right')
    plt.show()

    # #Alternative Code
    # df2.plot()
    # plt.show()


def main():
    """
    load the data and draw the plot
    """
    try:
        df = load("../population_total.csv")
        draw_plot(df)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()

    """
    Notes:
    Regex=True is included so replace can use regular expressions to match the
    patterns in the strings. If it is not included, the patterns with square
    brackets [kK], [mM], and [bB] will be treated as literal strings and the
    program will search for the exact strings '[kK]', '[mM]', and '[bB]' in the
    data column.

    map(pd.eval) is used to apply the pd.eval function to each element in a
    Pandas Series. The pd.eval function is a pandas function that evaluates
    a string as a Python expression. For example, if the 'Belgium' column
    contains the string '3.5k', after this the above operation, it would
    be replaced with the value '3.5*1e3', and then pd.eval is used to
    evaluate the expression,resulting in the numeric value 3500.

    df2.max().max() finds the maximum value across all columns in the df2.
    The first max() calculates the maximum value for each column, and the
    second max() finds the maximum value across all columns. This value is
    then used to set the range.
    """
