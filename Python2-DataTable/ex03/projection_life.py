from load_csv import load
import matplotlib.pyplot as plt


def plot_graph(df_gdp, df_life, year):
    """
    Plot the scatter graph to show correlation between GDP and life expectancy
    """
    # plot the scatter graph with filtered data for year 1900
    plt.scatter(df_gdp[year], df_life[year])
    plt.xlabel("Gross Domestic Product")
    plt.xscale("log")  # logaritmic scale
    plt.xticks([300, 1000, 10000], labels=["300", "1K", "10K"])
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.show()


def main():
    try:
        df_gdp = load(
            "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df_life = load("../life_expectancy_years.csv")
        plot_graph(df_gdp, df_life, "1900")
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()

"""
Notes:
A logarithmic scale is a scale of measurement that uses logarithms to
represent the values of a variable. In a logarithmic scale, equal
intervals on the scale represent equal ratios of values. This is in
contrast to a linear scale, where equal intervals represent equal
differences in the values.
"""
