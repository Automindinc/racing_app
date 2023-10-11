import streamlit as st
import pandas as pd
import numpy as np
import os

# Average of the last 3 runs; we'll use a high value for missing runs
def calculate_average(runs):
    adjusted_runs = []
    for run in runs:
        if run == '0':
            print('zero found')
            adjusted_runs.append(11)  # Adjust this value based on how much you want to penalize
        elif run != '-':
            adjusted_runs.append(int(run))
        else:
            adjusted_runs.append(100)
    return sum(adjusted_runs) / 3


# Define a function to compute the jockey score
def compute_jockey_score(jockey_data):
    win_rate = float(jockey_data["Win %"])  # Convert string percentage to float
    place_percentage = float(jockey_data["Percentage for season"])  # Convert string percentage to float
    
    if jockey_data["All weather"] == 0:
        all_weather_performance = 0
    else:
        all_weather_performance = (jockey_data["No of wins for all weather"] + 
                                   jockey_data["No of 2nds for all weather"] + 
                                   jockey_data["No of 3rds for all weather"]) / jockey_data["All weather"]
    
    stakes_ratio = float(jockey_data["Win stakes"][1:].replace(',', '')) / float(jockey_data["Total stakes"][1:].replace(',', ''))
    
    # Extract number from the "Profit/Loss" string, convert to negative if it's a loss
    profit_loss = int(jockey_data["Profit/Loss"][2:-1])
    if jockey_data["Profit/Loss"].startswith("($"):
        profit_loss = -profit_loss
    
    score = 0.4 * win_rate + 0.4 * place_percentage + 0.1 * all_weather_performance + 0.1 * stakes_ratio - 0.001 * profit_loss
    
    return score

# Open the jockey.txt file
with open("jockey.txt", "r") as file:
    data = file.readlines()
    
    jockey_data_list = []
    jockey_data = {}
    
    # Process each line in the file
    for line in data:
        line = line.strip()
        if not line:
            continue
        if line == "{":
            jockey_data = {}
        elif line == "},":
            jockey_data_list.append(jockey_data)
        else:
            key, value = [item.strip() for item in line.split(":")]
            if value.endswith("%"):
                value = float(value[:-1])
            elif value.startswith("$"):
                value = value
            elif value.startswith("(") and value.endswith(")"):
                value = value
            else:
                try:
                    value = int(value)
                except ValueError:
                    value = value.strip()
            jockey_data[key] = value


# First, compute the scores for all jockeys and store in a dictionary
jockey_scores = {}
for jockey in jockey_data_list:
    score = compute_jockey_score(jockey)
    jockey_scores[jockey['Name']] = score

# Function to get jockey performance score
def jockey_performance(jockey_name):
    score = jockey_scores.get(jockey_name)
    if score is None:  # If no data found for the jockey
        print(f"No data found for jockey: {jockey_name}")
        return 0  # Default value when no data exists for the jockey
    return score

###################################################
########## STREAMLIT ##############################
###################################################

st.title("Horse Racing Predictor")

# Initialize a variable for the current race

MAX_RACES = 8

if 'current_race' not in st.session_state:
    st.session_state.current_race = 1

# Button logic for navigating between races
if st.button('Previous Race'):
    st.session_state.current_race -= 1
    st.session_state.current_race = max(1, st.session_state.current_race)

if st.button('Next Race'):
    st.session_state.current_race += 1
    st.session_state.current_race = min(MAX_RACES, st.session_state.current_race)


# Load the HTML content based on the current race
with open(f"race{st.session_state.current_race}.html", "r") as file:
    html_content = file.read()

# Read HTML table into DataFrame
dfs = pd.read_html(html_content, attrs={'id': 'racecard-table'})

# The result is a list of DataFrames; in your case, you'd probably have just one table
df = dfs[0]

# Set the columns to the second level of the MultiIndex
df.columns = df.columns.get_level_values(1)

df['ON'] = df['ON'].replace('-', np.nan)
df['TD'] = df['TD'].replace('-', np.nan)
df['ON'] = pd.to_numeric(df['ON'], errors='coerce')
df['TD'] = pd.to_numeric(df['TD'], errors='coerce')

# Now you can use the .str accessor on the 'Last runs' column
df['Last 3 runs'] = df['Last runs'].str.split('/').str[-3:]

df['Average last 3 runs'] = df['Last 3 runs'].apply(calculate_average)

# Now, apply the above functions to the dataframe
df['Last 3 runs'] = df['Last runs'].str.split('/').str[-3:]
df['Average last 3 runs'] = df['Last 3 runs'].apply(calculate_average)

# Factor in the age of the horse. Younger horses might be faster but less experienced.
# This is just an example and can be adjusted.
df['Age Score'] = df['Age'].apply(lambda age: 1 if age <= 4 else 0.8 if age <= 6 else 0.6)

df['Jockey Score'] = df['Jockey'].apply(jockey_performance)

st.markdown("""
This app is intended for entertainment purposes only and should not be used for any real-world applications or betting decisions. 
The displayed scores and data are based solely on specific data sets and are not indicative of future outcomes.
""")

st.markdown("""
**Data Source & Details:** 
All data presented in this app pertains only to the first race of 11.10.23. Data was manually extracted from [SCMP](https://www.scmp.com/sport/racing/racecard/1).
""")

# Allow user to adjust weights
weight_average_last_3 = st.sidebar.slider("Weight for Average Last 3 Runs", 0.0, 2.0, 1.0)
weight_on = st.sidebar.slider("Weight for ON", 0.0, 2.0, 1.0)
weight_td = st.sidebar.slider("Weight for TD", 0.0, 2.0, 1.0)
weight_jockey = st.sidebar.slider("Weight for Jockey Score", -2.0, 0.0, -1.0)
weight_age = st.sidebar.slider("Weight for Age Score", 0.0, 2.0, 1.0)

# Score Calculation
df['Score'] = (
    df['Average last 3 runs'] * weight_average_last_3
    + df['ON'] * weight_on
    + df['TD'] * weight_td
    - df['Jockey Score'] * weight_jockey
    + df['Age Score'] * weight_age
)

best_bets = df.sort_values(by='Score')
st.write(best_bets[['Horse', 'Score']])

# Explanation Section
if st.button('Show Explanation'):
    st.subheader("Horse Betting Score Formula")
    
    st.markdown("### Notation:")
    st.markdown("""
    Let:
    
    - \( L_i \) denote the \( i^{th} \) latest run of a horse.
    - \( ON \) represent the odds for a horse not winning.
    - \( TD \) represent the "Today's" odds for a horse to win.
    - \( J \) represent the jockey score.
    - \( A \) represent the age score of the horse.
    - \( S \) represent the final score of the horse.
    - \( W \) denote the win rate percentage of the jockey.
    - \( P \) represent the placement percentage for the season.
    - \( AW \) represent the wins in all-weather conditions.
    - \( A2 \) represent the second places in all-weather conditions.
    - \( A3 \) represent the third places in all-weather conditions.
    - \( AT \) denote the total races in all-weather conditions.
    - \( WS \) represent the total win stakes.
    - \( TS \) represent the total stakes.
    - \( PL \) represent the profit/loss value.
    
    ### 1. Average of Last 3 Runs:
    
    The average of the last 3 runs for a horse is given by:
    
    $$
    \\text{Average\_last\_3\_runs} = \\frac{L_1 + L_2 + L_3}{3}
    $$
    
    ### 2. Jockey Performance Score:
    
    The jockey score \( J \) is derived from the jockey's performance metrics. A higher \( J \) indicates a more skilled jockey.
    
    ### Jockey Performance Score Calculation:
    
    The all-weather performance ratio \( R \) is given by:
    
    $$
    R = \\frac{AW + A2 + A3}{AT}
    $$
    
    The stakes ratio \( SR \) is calculated as:
    
    $$
    SR = \\frac{WS}{TS}
    $$
    
    The jockey score \( J \) is then:
    
    $$
    J = 0.4W + 0.4P + 0.1R + 0.1SR - 0.001PL
    $$
    
    ### 3. Horse Age Score:
    
    The age score \( A \) is determined as:
    
    $$
    A = 
    \\begin{cases} 
    1 & \\text{if } \\text{age} \leq 4 \\
    0.8 & \\text{if } 4 < \\text{age} \leq 6 \\
    0.6 & \\text{otherwise}
    \end{cases}
    $$
    
    ### 4. Final Score Calculation:
    
    The final score \( S \) for a horse is:
    
    $$
    S = \\text{Average\_last\_3\_runs} + ON + TD - J + A
    $$
    """)