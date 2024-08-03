# Global Terrorism 

[![GitHub license](https://img.shields.io/github/license/jassatish/global-terrorism-eda)
## Introduction

This repository contains code and analysis for performing Exploratory Data Analysis (EDA) on the Global Terrorism dataset. The goal is to identify terrorism hot zones, analyze attack trends, and derive actionable security insights. This analysis is valuable for security and defense analysts aiming to understand global terrorism patterns and impacts.

## Contents

- [Introduction](#introduction)
- [Contents](#contents)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The dataset used for this analysis is `globalterrorismdb_0718dist.csv`, which includes detailed records of terrorist attacks worldwide. It provides information such as attack dates, locations, weapon types, and target types.

## Installation

To run the analysis, you'll need Python and several libraries. Follow these steps to set up your environment:

### Clone the Repository

```bash
git clone https://github.com/jassatish/global-terrorism-eda.git
cd global-terrorism-eda
```
## Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Install Dependencies
Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage
Once the environment is set up, you can run the analysis script. Make sure you have the dataset file globalterrorismdb_0718dist.csv in the same directory as the script.


### Run the Analysis


```bash
python analysis.py
```


This command will execute the EDA script and generate visualizations to help in understanding the dataset.


## Results
The analysis produces:

1. Identification of terrorism hot zones.
2. Trends in terrorist attacks over the years.
3. Distribution of attack types and regions.
4. Security insights and recommendations.
5. Results are visualized through plots and charts generated by the analysis script

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.




