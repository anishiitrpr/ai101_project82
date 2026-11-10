# ai101_project82
# Global Renewable Energy Output & Weather Correlation

**AI101 – Data Science and AI Essentials with Python**  
**School of AI and Data Engineering, IIT Ropar**

---

# 1. Project Overview

This project aims to investigate the relationship between weather conditions and renewable energy generation using Python-based data analysis and statistical techniques.

The study focuses on analysing how environmental factors such as solar radiation, temperature, humidity, wind speed and cloud coverage are associated with solar power generation.

The project uses data preprocessing, exploratory data analysis, correlation analysis and visualization to identify meaningful patterns.

# 2. Problem Statement

To analyse the relationship between weather conditions and renewable energy generation, identify correlations between meteorological variables and solar energy output, and visualize the observed patterns using statistical and data visualization techniques.

# 3. Project Objectives

- Analyse renewable energy generation data.
- Investigate the relationship between solar radiation and energy output.
- Study the association between temperature and solar generation.
- Examine the relationship between wind speed, humidity, cloud coverage and energy output.
- Perform statistical and correlation analysis.
- Visualize findings through graphs and heatmaps.

# 4. Team Members and Roles

| Name | Roll Number | Responsibility |
|---|---|---|
| Anish Kumar | 2026AIB1015 | Video Lead |
| Parmeet | 2026EEB1390 | Execution Lead |
| Dharmesh Meena | 2026AIB1030 | Documentation Lead |
| Sehaj Reen | 2026EEB1409 | PPT Lead |

# 5. Dataset Information

**Dataset Name:** Renewable Power Generation and Weather Conditions

**Dataset Author:** pythonafroz

**Source:** Kaggle

**Dataset Link:** https://www.kaggle.com/datasets/pythonafroz/renewable-power-generation-and-weather-conditions

**Dataset File:** Renewable.csv

## Dataset Statistics

- Total observations: 196,776
- Total columns: 17
- File size: Approximately 14.91 MB
- Date coverage: 1 January 2017 – 31 August 2022
- Missing values: 0
- Duplicate records: 0

## Important Dataset Variables

- Time
- Energy delta[Wh]
- GHI
- temp
- pressure
- humidity
- wind_speed
- rain_1h
- snow_1h
- clouds_all
- isSun
- sunlightTime
- dayLength
- SunlightTime/daylength
- weather_type
- hour
- month

# 6. Project Methodology

The project will follow these stages:

1. Data collection and inspection.
2. Data cleaning and preprocessing.
3. Exploratory Data Analysis (EDA).
4. Statistical analysis.
5. Correlation analysis.
6. Data visualization.
7. Interpretation of results and conclusions.
   

## 7. Project Structure

The repository is organised into the following files and directories:

```text
ai101_project82/
│
├── README.md
├── Renewable.csv
├── main.py
├── requirements.txt
│
├── outputs/
│   ├── figures/
│   │   └── README.md
│   └── results/
│       └── README.md
│
├── presentation/
│   └── README.md
│
└── video/
    └── README.md
```

### Description of Files and Directories

| File/Directory | Description |
|---|---|
| README.md | Main project documentation |
| Renewable.csv | Renewable energy and weather dataset |
| main.py | Python analysis script |
| requirements.txt | Required Python libraries |
| outputs/figures/ | Stores generated graphs and visualizations |
| outputs/results/ | Stores statistical results and analysis outputs |
| presentation/ | Stores the final project presentation |
| video/ | Stores project demonstration video information |


# 8. Installation and Setup

## Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/anishiitrpr/ai101_project82.git
cd ai101_project82
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage project dependencies.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python libraries using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Verify Dataset

Ensure that `Renewable.csv` is present in the project root directory.


# 9. How to Run the Project

## Steps to Execute

1. Open the project folder in your terminal.
2. Activate the virtual environment.
3. Make sure all required dependencies are installed.
4. Run the main Python script:

```bash
python main.py
```

For Linux/macOS, if required:

```bash
python3 main.py
```

5. Wait for the script to finish execution and display the analysis results.

**Note:** Run the command from the project root directory, where the Python script and `Renewable.csv` are located.



# 10. Results and Expected Output

                  Time  Energy delta[Wh]  GHI  temp  ...  SunlightTime/daylength  weather_type  hour  month
0  2017-01-01 00:00:00                 0  0.0   1.6  ...                     0.0             4     0      1
1  2017-01-01 00:15:00                 0  0.0   1.6  ...                     0.0             4     0      1
2  2017-01-01 00:30:00                 0  0.0   1.6  ...                     0.0             4     0      1
3  2017-01-01 00:45:00                 0  0.0   1.6  ...                     0.0             4     0      1
4  2017-01-01 01:00:00                 0  0.0   1.7  ...                     0.0             4     1      1

[5 rows x 17 columns]
<class 'pandas.DataFrame'>
RangeIndex: 196776 entries, 0 to 196775
Data columns (total 17 columns):
 #   Column                  Non-Null Count   Dtype  
---  ------                  --------------   -----  
 0   Time                    196776 non-null  str    
 1   Energy delta[Wh]        196776 non-null  int64  
 2   GHI                     196776 non-null  float64
 3   temp                    196776 non-null  float64
 4   pressure                196776 non-null  int64  
 5   humidity                196776 non-null  int64  
 6   wind_speed              196776 non-null  float64
 7   rain_1h                 196776 non-null  float64
 8   snow_1h                 196776 non-null  float64
 9   clouds_all              196776 non-null  int64  
 10  isSun                   196776 non-null  int64  
 11  sunlightTime            196776 non-null  int64  
 12  dayLength               196776 non-null  int64  
 13  SunlightTime/daylength  196776 non-null  float64
 14  weather_type            196776 non-null  int64  
 15  hour                    196776 non-null  int64  
 16  month                   196776 non-null  int64  
dtypes: float64(6), int64(10), str(1)
memory usage: 25.5 MB
None
Index(['Time', 'Energy delta[Wh]', 'GHI', 'temp', 'pressure', 'humidity',
       'wind_speed', 'rain_1h', 'snow_1h', 'clouds_all', 'isSun',
       'sunlightTime', 'dayLength', 'SunlightTime/daylength', 'weather_type',
       'hour', 'month'],
      dtype='str')
(196776, 17)

Missing Values:
Time                      0
Energy delta[Wh]          0
GHI                       0
temp                      0
pressure                  0
humidity                  0
wind_speed                0
rain_1h                   0
snow_1h                   0
clouds_all                0
isSun                     0
sunlightTime              0
dayLength                 0
SunlightTime/daylength    0
weather_type              0
hour                      0
month                     0
dtype: int64

Duplicate Records:
0

Statistical Summary
       Energy delta[Wh]            GHI           temp  ...   weather_type           hour          month
count     196776.000000  196776.000000  196776.000000  ...  196776.000000  196776.000000  196776.000000
mean         573.008228      32.596538       9.790521  ...       3.198398      11.498902       6.298329
std         1044.824047      52.172018       7.995428  ...       1.289939       6.921887       3.376066
min            0.000000       0.000000     -16.600000  ...       1.000000       0.000000       1.000000
25%            0.000000       0.000000       3.600000  ...       2.000000       5.000000       3.000000
50%            0.000000       1.600000       9.300000  ...       4.000000      11.000000       6.000000
75%          577.000000      46.800000      15.700000  ...       4.000000      17.000000       9.000000
max         5020.000000     229.200000      35.800000  ...       5.000000      23.000000      12.000000

[8 rows x 16 columns]

Column Names
['Time', 'Energy delta[Wh]', 'GHI', 'temp', 'pressure', 'humidity', 'wind_speed', 'rain_1h', 'snow_1h', 'clouds_all', 'isSun', 'sunlightTime', 'dayLength', 'SunlightTime/daylength', 'weather_type', 'hour', 'month']

Data Types
Time                          str
Energy delta[Wh]            int64
GHI                       float64
temp                      float64
pressure                    int64
humidity                    int64
wind_speed                float64
rain_1h                   float64
snow_1h                   float64
clouds_all                  int64
isSun                       int64
sunlightTime                int64
dayLength                   int64
SunlightTime/daylength    float64
weather_type                int64
hour                        int64
month                       int64
dtype: object

Missing Value
Time                      0
Energy delta[Wh]          0
GHI                       0
temp                      0
pressure                  0
humidity                  0
wind_speed                0
rain_1h                   0
snow_1h                   0
clouds_all                0
isSun                     0
sunlightTime              0
dayLength                 0
SunlightTime/daylength    0
weather_type              0
hour                      0
month                     0

First 10 Records
                  Time  Energy delta[Wh]  GHI  temp  ...  SunlightTime/daylength  weather_type  hour  month
0  2017-01-01 00:00:00                 0  0.0   1.6  ...                     0.0             4     0      1
1  2017-01-01 00:15:00                 0  0.0   1.6  ...                     0.0             4     0      1
2  2017-01-01 00:30:00                 0  0.0   1.6  ...                     0.0             4     0      1
3  2017-01-01 00:45:00                 0  0.0   1.6  ...                     0.0             4     0      1
4  2017-01-01 01:00:00                 0  0.0   1.7  ...                     0.0             4     1      1
5  2017-01-01 01:15:00                 0  0.0   1.7  ...                     0.0             4     1      1
6  2017-01-01 01:30:00                 0  0.0   1.7  ...                     0.0             4     1      1
7  2017-01-01 01:45:00                 0  0.0   1.7  ...                     0.0             4     1      1
8  2017-01-01 02:00:00                 0  0.0   1.9  ...                     0.0             4     2      1
9  2017-01-01 02:15:00                 0  0.0   1.9  ...                     0.0             4     2      1

[10 rows x 17 columns]

Duplicate Records
0

Dataset after removing duplicates:
(196776, 17)

Time column converted successfully
datetime64[us]

Final Dataset information:
<class 'pandas.DataFrame'>
RangeIndex: 196776 entries, 0 to 196775
Data columns (total 17 columns):
 #   Column                  Non-Null Count   Dtype         
---  ------                  --------------   -----         
 0   Time                    196776 non-null  datetime64[us]
 1   Energy delta[Wh]        196776 non-null  int64         
 2   GHI                     196776 non-null  float64       
 3   temp                    196776 non-null  float64       
 4   pressure                196776 non-null  int64         
 5   humidity                196776 non-null  int64         
 6   wind_speed              196776 non-null  float64       
 7   rain_1h                 196776 non-null  float64       
 8   snow_1h                 196776 non-null  float64       
 9   clouds_all              196776 non-null  int64         
 10  isSun                   196776 non-null  int64         
 11  sunlightTime            196776 non-null  int64         
 12  dayLength               196776 non-null  int64         
 13  SunlightTime/daylength  196776 non-null  float64       
 14  weather_type            196776 non-null  int64         
 15  hour                    196776 non-null  int64         
 16  month                   196776 non-null  int64         
dtypes: datetime64[us](1), float64(6), int64(10)
memory usage: 25.5 MB
None

Final Dataset:
                 Time  Energy delta[Wh]  GHI  temp  ...  SunlightTime/daylength  weather_type  hour  month
0 2017-01-01 00:00:00                 0  0.0   1.6  ...                     0.0             4     0      1
1 2017-01-01 00:15:00                 0  0.0   1.6  ...                     0.0             4     0      1
2 2017-01-01 00:30:00                 0  0.0   1.6  ...                     0.0             4     0      1
3 2017-01-01 00:45:00                 0  0.0   1.6  ...                     0.0             4     0      1
4 2017-01-01 01:00:00                 0  0.0   1.7  ...                     0.0             4     1      1

[5 rows x 17 columns]

Cleaned dataset saves susccesfully !
Final dataset shape (196776, 17)

Missing values after cleaning
Time                      0
Energy delta[Wh]          0
GHI                       0
temp                      0
pressure                  0
humidity                  0
wind_speed                0
rain_1h                   0
snow_1h                   0
clouds_all                0
isSun                     0
sunlightTime              0
dayLength                 0
SunlightTime/daylength    0
weather_type              0
hour                      0
month                     0
dtype: int64

Duplicate records after cleaning 
0

Final columns :
['Time', 'Energy delta[Wh]', 'GHI', 'temp', 'pressure', 'humidity', 'wind_speed', 'rain_1h', 'snow_1h', 'clouds_all', 'isSun', 'sunlightTime', 'dayLength', 'SunlightTime/daylength', 'weather_type', 'hour', 'month']

Final data shape:
(196776, 17)
(venv) dharmesh@Dharmeshs-MacBook-Air ai101_project82 % 

# 11. Presentation and Video

- Project Presentation: To be added.
- Project Demonstration Video: To be added.

# 12. AI Use Disclosure

AI tools, if used, will be disclosed with details of their purpose and the verification performed by the team.

# 13. Limitations

- The selected dataset represents solar photovoltaic generation associated with weather observations at a particular installation.
- It does not independently provide worldwide country-wise renewable generation data.
- It does not provide separate wind and hydropower generation measurements.
- Correlation does not necessarily imply causation.
- Energy generation may also depend on installed capacity, equipment, infrastructure and other factors.
