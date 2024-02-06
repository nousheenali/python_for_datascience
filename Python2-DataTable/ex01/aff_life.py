from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def plot_graph(df: DataFrame) -> None:
    """
    Plot the life expectancy graph
    """
    # extract data for UAE and also remove index column
    # by setting index to country
    df1 = df.query(
        "country == 'United Arab Emirates'"
        ).set_index("country")
    x = df1.columns  # extract column names
    y = df1.values.flatten()  # extract values and flatten to 1D array

    # plot the data
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("United Arab Emirates Life Expectancy Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Life Expectancy")
    tick_spacing = 40
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.show()


def main():
    """"
    load the data and draw the plot
    """
    try:
        df = load("../life_expectancy_years.csv")
        plot_graph(df)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
