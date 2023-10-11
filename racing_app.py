import streamlit as st
import pandas as pd

html_content = """
<table id="racecard-table" class="tablesorter"><thead align="center"><tr class="tablesorter-header"><th rowspan="2" data-column="0" class="tablesorter-header"><div class="tablesorter-header-inner">No<div class="arrows"><span class="icon icon-ui_arrow_up"></span><span class="icon icon-ui_arrow_down"></span></div></div></th><th data-sorter="false" class="" rowspan="2" data-column="1"><div class="tablesorter-header-inner">Last runs</div></th><th data-sorter="false" class="" rowspan="2" data-column="2"><div class="tablesorter-header-inner">Colour</div></th><th rowspan="2" data-column="3" class="tablesorter-header"><div class="tablesorter-header-inner">Horse<div class="arrows"><span class="icon icon-ui_arrow_up"></span><span class="icon icon-ui_arrow_down"></span></div></div></th><th data-sorter="false" class="" rowspan="2" data-column="4"><div class="tablesorter-header-inner">Priority</div></th><th data-sorter="false" class="horse_weight" rowspan="2" data-column="5"><div class="tablesorter-header-inner">Horse Wt.</div></th><th data-sorter="false" class="" rowspan="2" data-column="6"><div class="tablesorter-header-inner">Gear</div></th><th data-sorter="false" class="" rowspan="2" data-column="7"><div class="tablesorter-header-inner">Trainer</div></th><th data-sorter="false" class="" rowspan="2" data-column="8"><div class="tablesorter-header-inner">Age</div></th><th data-sorter="false" class="" rowspan="2" data-column="9"><div class="tablesorter-header-inner">Wt.</div></th><th data-sorter="false" class="" rowspan="2" data-column="10"><div class="tablesorter-header-inner">Rating</div></th><th data-sorter="false" class="" rowspan="2" data-column="11"><div class="tablesorter-header-inner">Jockey</div></th><th data-sorter="false" class="" rowspan="2" data-column="12"><div class="tablesorter-header-inner">Draw</div></th><th data-sorter="false" class="win" rowspan="1" colspan="2" data-column="13"><div class="tablesorter-header-inner">Win</div></th><th data-sorter="false" class="" rowspan="2" data-column="15"><div class="tablesorter-header-inner">Place</div></th><th data-sorter="false" rowspan="2" class="star-form" data-column="16"><div class="tablesorter-header-inner">Star Form</div></th></tr><tr class="tablesorter-header"><th data-sorter="false" class="on" data-column="13"><div class="tablesorter-header-inner">ON</div></th><th data-sorter="false" class="td" data-column="14"><div class="tablesorter-header-inner">TD</div></th></tr></thead><tbody class=""><tr><td align="center" class="horse_number">1</td><td align="center" class="last_six_run">5/7/9/8/-/8/8</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/H209.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/H209.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/H209/good-boy">GOOD BOY<br>幸運天賦<span> (H209)</span></a></td><td align="center">1</td><td align="center">1141 +3</td><td align="center">B/TT</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/535/p-c-ng">P. C. Ng</a></td><td align="center">4</td><td align="center">135 +17</td><td align="center">40-1</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/826/k-c-leung">K. C. Leung</a></td><td align="center">2</td><td align="center" class="overnight_win_odds">12</td><td align="center" class="win_odds">9.0</td><td align="center">2.7</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>One rallying fifth over 1,200m from five Sha Tin runs up to 1,400m last term. Resumed non-factor from low draw over Sha Tin 1,000m, then never in act trying Valley 1,200m. Gets downgrade. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">2</td><td align="center" class="last_six_run">6/5/0/6/-/0/8</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/G201.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/G201.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/G201/diamond-soars">DIAMOND SOARS<br>鑽飾翱翔<span> (G201)</span></a></td><td align="center">1</td><td align="center">1198 +1</td><td align="center">TT</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/83/p-f-yiu">P. F. Yiu</a></td><td align="center">5</td><td align="center">133 -2</td><td align="center">38-2</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/976/y-l-chung">Y. L. Chung -7</a></td><td align="center">10</td><td align="center" class="overnight_win_odds">12</td><td align="center" class="win_odds">11</td><td align="center">3.4</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>Winner once each over dirt 1,200m in Class Five and C&amp;D in Class Four from 12 runs last term. Resumed non-factor over C&amp;D, then front-running C&amp;D eighth down in class. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">3</td><td align="center" class="last_six_run">9/0/4/0/-/3/4</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/D443.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/D443.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/D443/multimore">MULTIMORE<br>萬事有<span> (D443)</span></a></td><td align="center">1</td><td align="center">1236 +19</td><td align="center">TT</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/453/t-p-yung">T. P. Yung</a></td><td align="center">7</td><td align="center">133 +1</td><td align="center">38-1</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/931/h-t-mo">H. T. Mo -2</a></td><td align="center">5</td><td align="center" class="overnight_win_odds">6.4</td><td align="center" class="win_odds">7.0</td><td align="center">2.1</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>Veteran placed fourth once from four runs in injury-prone campaign. Resumed pace-pressing  Valley 1,200m third down in grade, then speed-tracking C&amp;D fourth. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">4</td><td align="center" class="last_six_run">6/4/0/2/3/3</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/E307.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/E307.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/E307/theta-hedge">THETA HEDGE<br>精算其然<span> (E307)</span></a></td><td align="center">1</td><td align="center">1025 -1</td><td align="center">B/TT</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/86/k-w-lui">K. W. Lui</a></td><td align="center">6</td><td align="center">133 +2</td><td align="center">38</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/964/l-hewitson">L. Hewitson</a></td><td align="center">4</td><td align="center" class="overnight_win_odds">4.6</td><td align="center" class="win_odds">4.6</td><td align="center">1.4</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>Valley mile win in November and ended 13-start campaign with three consecutive Valley 1,200m placings. Unplaced in one C&amp;D run. Scratched last month after rearing and dislodging rider. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">5</td><td align="center" class="last_six_run">2/4/3/2/5/-/1</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/E210.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/E210.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/E210/tronic-mighty">TRONIC MIGHTY<br>創福威<span> (E210)</span></a></td><td align="center">1</td><td align="center">1047 +11</td><td align="center">V/XB/TT</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/534/j-richards">J. Richards</a></td><td align="center">6</td><td align="center">133 +6</td><td align="center">38+6</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/552/z-purton">Z. Purton</a></td><td align="center">9</td><td align="center" class="overnight_win_odds">3.7</td><td align="center" class="win_odds">3.3</td><td align="center">1.6</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>First-up C&amp;D win last term for new trainer, then earned minor cheques in next five starts. Resumed C&amp;D winner from better than midfield. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">6</td><td align="center" class="last_six_run">9/4/0/9/0/-/5</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/H061.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/H061.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/H061/happy-horse">HAPPY HORSE<br>開心馬<span> (H061)</span></a></td><td align="center">+1</td><td align="center">1097 +10</td><td align="center">H/TT</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/266/k-l-man">K. L. Man</a></td><td align="center">5</td><td align="center">130 +1</td><td align="center">35-1</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/941/m-f-poon">M. F. Poon -2</a></td><td align="center">8</td><td align="center" class="overnight_win_odds">8.3</td><td align="center" class="win_odds">9.6</td><td align="center">2.8</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>One shock speed-chasing Sha Tin 1,000m fourth wearing blinkers from eight sprints last term. Downgraded for return and resumed C&amp;D fifth after following pace wide without cover. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">7</td><td align="center" class="last_six_run">0/7/0/0/-/0/9</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/G341.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/G341.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/G341/dashing-triumph">DASHING TRIUMPH<br>吉吉利高<span> (G341)</span></a></td><td align="center">+1</td><td align="center">1144 +16</td><td align="center">B1/TT</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/347/y-s-tsui">Y. S. Tsui</a></td><td align="center">4</td><td align="center">127 -2</td><td align="center">32-2</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/895/k-teetan">K. Teetan</a></td><td align="center">6</td><td align="center" class="overnight_win_odds">10</td><td align="center" class="win_odds">12</td><td align="center">3.9</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>Negative impressions in 10 starts up to 1,400m last term. Never involved from near rear over Sha Tin 1,200m for new trainer on resumption, then similar C&amp;D effort. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">8</td><td align="center" class="last_six_run">0/7/0/6/5/-/0</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/H035.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/H035.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/H035/har-har-at-heart">HAR HAR AT HEART<br>存喜心<span> (H035)</span></a></td><td align="center">1</td><td align="center">1064 +5</td><td align="center">E</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/267/john-size">John Size</a></td><td align="center">5</td><td align="center">126 -2</td><td align="center">31-2</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/938/a-badel">A. Badel</a></td><td align="center">7</td><td align="center" class="overnight_win_odds">12</td><td align="center" class="win_odds">11</td><td align="center">4.1</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>Ran on better for C&amp;D sixth in May following downgrade, then late bid to go one better in July. Resumed flat C&amp;D 10th from worse than midfield. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">9</td><td align="center" class="last_six_run">0/0/0/8/0/0</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/G205.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/G205.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/G205/six-best-friends">SIX BEST FRIENDS<br>星叻無敵<span> (G205)</span></a></td><td align="center">2</td><td align="center">1147 +11</td><td align="center">CP/TT</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/266/k-l-man">K. L. Man</a></td><td align="center">5</td><td align="center">122 -7</td><td align="center">27-7</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/825/m-l-yeung">M. L. Yeung</a></td><td align="center">1</td><td align="center" class="overnight_win_odds">13</td><td align="center" class="win_odds">16</td><td align="center">4.5</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>Finished among backmarkers in each of first five Valley sprints in Class Four last term, then two weak C&amp;D efforts despite downgrade before mile defeat with blood in trachea. <span class="icon icon-ui_star"></span><span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr><tr><td align="center" class="horse_number">10</td><td align="center" class="last_six_run">0/0/-/0/0/0/0</td><td align="center" class="jockey_jersey"><img class="jerkey_img" src="https://api.racing.scmp.com/StatImg/Photo/JocColor/svg/G116.svg" onerror="https://api.racing.scmp.com/StatImg/Photo/JocColor/G116.gif"></td><td align="left" class="horse_name"><a href="/sport/racing/stats/horses/G116/bell-of-victory">BELL OF VICTORY<br>勝利鐘聲<span> (G116)</span></a></td><td align="center">1</td><td align="center">1108 +3</td><td align="center">SR-/B2</td><td align="left" class="trainer_name"><a href="/sport/racing/stats/trainer/521/d-whyte">D. Whyte</a></td><td align="center">5</td><td align="center">117 -8</td><td align="center">22-8</td><td align="center" class="jockey_name"><a href="/sport/racing/stats/jockey/982/k-de-melo">K. De. Melo</a></td><td align="center">3</td><td align="center" class="overnight_win_odds">22</td><td align="center" class="win_odds">36</td><td align="center">7.9</td><td align="left" class="star-form-data"><div class="starInfo"><h1>Star Form: </h1><p>Still to come right in 10 starts, including four lifeless runs down in class across both tracks last term. No improvement last time despite stepping out for new trainer. <span class="icon icon-ui_star"></span></p></div><span class="icon-ui_comment"></span></td></tr></tbody></table>
"""

# Average of the last 3 runs; we'll use a high value for missing runs
def calculate_average(runs):
    return sum([int(run) if run != '-' else 100 for run in runs]) / 3

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
# Read HTML table into DataFrame
dfs = pd.read_html(html_content, attrs={'id': 'racecard-table'})

# The result is a list of DataFrames; in your case, you'd probably have just one table
df = dfs[0]

# Set the columns to the second level of the MultiIndex
df.columns = df.columns.get_level_values(1)

# Now you can use the .str accessor on the 'Last runs' column
df['Last 3 runs'] = df['Last runs'].str.split('/').str[-3:]

df['Average last 3 runs'] = df['Last 3 runs'].apply(calculate_average)

# First, compute the scores for all jockeys and store in a dictionary
jockey_scores = {}
for jockey in jockey_data_list:
    score = compute_jockey_score(jockey)
    jockey_scores[jockey['Name']] = score

# Function to get jockey performance score
def jockey_performance(jockey_name):
    return jockey_scores.get(jockey_name, 0)  # Returns 0 if the jockey name is not in our data

# Now, apply the above functions to the dataframe
df['Last 3 runs'] = df['Last runs'].str.split('/').str[-3:]
df['Average last 3 runs'] = df['Last 3 runs'].apply(calculate_average)

df['Jockey Score'] = df['Jockey'].apply(jockey_performance)

# Factor in the age of the horse. Younger horses might be faster but less experienced.
# This is just an example and can be adjusted.
df['Age Score'] = df['Age'].apply(lambda age: 1 if age <= 4 else 0.8 if age <= 6 else 0.6)

###################################################
########## STREAMLIT ##############################
###################################################

st.title("Horse Racing Predictor")

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