# CM4: Complex Decisions Challenges

This code conducts an analysis of weather data for Papua New Guinea in the year 2022 to assess the risk of lower water production efficiency at different times throughout the year. The focus is on the total solar radiation per day (in W/m²) and the water production of a 100m² system (in kg), both based on solar radiation data. The analysis includes graphical representations to visualize trends and distributions.

## Prerequisites

- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy

## Usage

1. Ensure that the required Python packages are installed:

    ```bash
    pip install pandas matplotlib seaborn numpy
    ```

2. Clone the repository and navigate to the project directory.

3. Run the script:

    ```bash
    python weather_analysis.py
    ```

## Code Explanation

1. **Data Loading:**
   - Reads weather data from the provided CSV file (`Papua New Guinea Weather Data 2022.csv`) using the `read_weather_data` function from `helper_functions` to read it and drop columns that are not necessary. 

2. **Data Transformation:**
   - Calculates the hours of sunlight for each day based on sunrise and sunset times.
   - Computes the total solar radiation per day (`totalsolarradiation`) in W/m².
   - Estimates water production for a 100m² system (`waterproduction`) based on total solar radiation.

3. **Visualization:**
   - Plots a histogram and line graph for the total solar radiation per day.
   - Displays a line graph for water production each day.

4. **Descriptive Analysis:**
   - Calculates mean, median, and mode for both total solar radiation and water production.
   - Presents the results in a DataFrame (`descriptive_df`).

## Author

Konrad Johannes Baumann

TODO:
1. Graph that shows lower limit of acceptable production
2. Multi class classifification model for the last 10 years
3. Population at coastal lines
4. ARIMA
