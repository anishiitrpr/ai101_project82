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

## Output After Execution

After running the project, the program displays the following dataset inspection, cleaning, and preprocessing results.

### 1. Initial Dataset Preview

```text
         Time             Energy delta[Wh]  GHI  temp  ...  weather_type  hour  month
0  2017-01-01 00:00:00          0           0.0  1.6   ...       4         0     1
1  2017-01-01 00:15:00          0           0.0  1.6   ...       4         0     1
2  2017-01-01 00:30:00          0           0.0  1.6   ...       4         0     1
3  2017-01-01 00:45:00          0           0.0  1.6   ...       4         0     1
4  2017-01-01 01:00:00          0           0.0  1.7   ...       4         1     1

[5 rows x 17 columns]
```

### 2. Dataset Information

```text
RangeIndex: 196776 entries, 0 to 196775
Data columns (total 17 columns)

Non-Null Count: 196776 for all 17 columns

dtypes:
float64(6)
int64(10)
str(1)

memory usage: 25.5 MB
```

### 3. Dataset Dimensions

```text
(196776, 17)
```

The dataset contains **196,776 records and 17 columns**.

### 4. Missing Values Analysis

```text
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
```

### 5. Duplicate Records

```text
Duplicate Records:
0
```

### 6. Statistical Summary

```text
       Energy delta[Wh]       GHI          temp
count  196776.000000     196776.000000  196776.000000
mean      573.008228         32.596538       9.790521
std      1044.824047         52.172018       7.995428
min         0.000000          0.000000     -16.600000
25%         0.000000          0.000000       3.600000
50%         0.000000          1.600000       9.300000
75%       577.000000         46.800000      15.700000
max      5020.000000        229.200000      35.800000

[8 rows x 16 columns]
```

### 7. Data Preprocessing

The program performs the following operations:

- Checks missing values.
- Identifies duplicate records.
- Removes duplicate records.
- Converts the `Time` column into datetime format.
- Displays the cleaned dataset information.

```text
Dataset after removing duplicates:
(196776, 17)

Time column converted successfully

datetime64[us]
```

### 8. Final Dataset Information

```text
Final Dataset information:

RangeIndex: 196776 entries, 0 to 196775
Data columns (total 17 columns)

Time                     datetime64[us]
Energy delta[Wh]         int64
GHI                      float64
temp                     float64
pressure                 int64
humidity                 int64
wind_speed               float64
rain_1h                  float64
snow_1h                  float64
clouds_all               int64
isSun                    int64
sunlightTime             int64
dayLength                int64
SunlightTime/daylength   float64
weather_type             int64
hour                     int64
month                    int64

memory usage: 25.5 MB
```

### 9. Final Cleaning Results

```text
Cleaned dataset saved successfully!

Final dataset shape: (196776, 17)

Missing values after cleaning: 0
Duplicate records after cleaning: 0
```

### 10. Final Output

```text
Final columns:

['Time', 'Energy delta[Wh]', 'GHI', 'temp', 'pressure',
 'humidity', 'wind_speed', 'rain_1h', 'snow_1h',
 'clouds_all', 'isSun', 'sunlightTime', 'dayLength',
 'SunlightTime/daylength', 'weather_type', 'hour', 'month']

Final data shape:
(196776, 17)
```

The dataset is successfully loaded, inspected, cleaned, and prepared for further analysis.

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
