# COVID-19 Global Data Tracker

An interactive web application that tracks and visualizes COVID-19 data across different countries, providing real-time statistics and insights about the pandemic.

## Project Objectives

- Display real-time COVID-19 statistics including cases, deaths, and recoveries
- Provide interactive visualizations of COVID-19 data
- Allow users to compare data across different countries
- Present data in an easily understandable format
- Help users make informed decisions based on current pandemic statistics

## Tools and Libraries Used

- Python 3.x
- Pandas - Data manipulation and analysis
- Plotly - Interactive data visualization
- Dash - Web application framework
- Dash Bootstrap Components - UI components
- Our World in Data COVID-19 Dataset - Primary data source

## Data Source

This project uses the Our World in Data COVID-19 dataset (`owid-covid-data.csv`), which provides comprehensive global COVID-19 statistics including:
- Daily new cases and deaths
- Total cases and deaths
- Vaccination data
- Testing data
- Hospitalization data
- And more

The dataset is regularly updated and includes data from multiple countries and regions.

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/yourusername/covid-tracker.git
cd covid-tracker
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python covid_tracker.py
```

5. Open your browser and navigate to `http://localhost:8050`

## Features

- Interactive country selection dropdown
- Real-time COVID-19 case tracking
- Death statistics visualization
- Vaccination rate monitoring
- Responsive and user-friendly interface

## Project Insights

This project demonstrates the importance of data visualization in understanding complex information. By presenting COVID-19 statistics in an interactive and user-friendly manner, it helps users better comprehend the impact of the pandemic across different regions.

## Future Improvements

- Add more detailed regional breakdowns
- Implement historical data comparison
- Include vaccination statistics
- Add user customization options for data visualization
- Implement data export functionality
- Add data update mechanism to keep statistics current

## Contributing

Feel free to submit issues and enhancement requests! 