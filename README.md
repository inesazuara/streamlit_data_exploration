# Streamlit Data Exploration App

This is a **data exploration web application** built with [Streamlit](https://streamlit.io/) that allows users to upload CSV or Excel files, view the data, and apply filters (both numeric and categorical). The app is designed to make it easy for users to explore their data interactively.

## Features

- Upload CSV or Excel files.
- Display the uploaded data in a table format.
- Apply **numeric filters** with range sliders for columns that have varying numeric data.
- Apply **categorical filters** to select specific values for columns with categorical data.
- Dynamic filtering: hides unnecessary filters if no numeric or categorical columns are available.
- Automatically detects file delimiters (comma, semicolon, etc.) with the ability for the user to specify a custom delimiter.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up and run the application on your local machine.

### Prerequisites

Make sure you have Python 3.8 or higher installed on your system. You can check the Python version by running:

```bash
python --version
```
### Clone the repository

```bash
git clone https://github.com/inesazuara/streamlit_data_exploration.git
cd streamlit_data_exploration
```

### Set up virtual environment (optional but recommendeed)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate

# Activate virtual environment (MacOS/Linux)
source venv/bin/activate
```

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Usage

If you want to see the deployed version of the app go to: https://app-data-exploration.streamlit.app/

For using the code in your own computer:

```bash
streamlit run app.py
```
This will open the application in your web browser. You can now interactively upload datasets, apply filters, and explore your data.

How to use
Upload a CSV or Excel file: Click on the "Browse files" button and upload your dataset. There are different sections:
- Data preview: The uploaded data will be displayed in a table format.
- Apply filters:
  - If numeric columns are detected, use the range slider to filter the data by numeric values.
  - If categorical columns are detected, select the specific values you want to filter by.
- Real-time filtering: The table updates dynamically based on the applied filters.


