import pandas as pd
from matplotlib import pyplot as plt
import tkinter as tk

ipl_batsman = pd.read_csv('ipl_batsman.csv')
ipl_bowler = pd.read_csv('ipl_bowler.csv')
matches = pd.read_csv('matches.csv')


# ---------------- BOWLER WICKET ----------------

def purple_cap():
    # bowlers total wicket list
    bowler_wickets = ipl_bowler.groupby('bowler')['wickets_taken'].sum()

    # top 10 bowlers
    top10bowler = bowler_wickets.sort_values(ascending=False).head(10)

    # Purple Cap holder
    purple_cap = top10bowler.index[0]
    purple_cap_wickets = top10bowler.iloc[0]

    # Sort for better horizontal chart display
    top10bowler = top10bowler.sort_values()

    # Wicket Plot with Purple Cap
    plt.figure(figsize=(10, 6))
    plt.barh(top10bowler.index, top10bowler.values, color="#7851a9")
    plt.xlabel("Wickets")
    plt.ylabel("Bowler")
    plt.title(
        f"Top 10 Wicket Takers\nPurple Cap: {purple_cap} ({purple_cap_wickets} wickets)"
    )

    plt.tight_layout()
    plt.show()


# ---------------- BATSMAN RUN ----------------

def orange_cap():
    # batsmen total run list
    batsman_score = ipl_batsman.groupby('striker')['runs_scored'].sum()

    # top 10 batsmen
    top10batsman = batsman_score.sort_values(ascending=False).head(10)

    # Orange Cap holder
    orange_cap = top10batsman.index[0]
    orange_cap_run = top10batsman.iloc[0]

    # Sort for better horizontal chart display
    top10batsman = top10batsman.sort_values()

    # Runs Plot with Orange Cap
    plt.figure(figsize=(10, 6))
    plt.barh(top10batsman.index, top10batsman.values, color="#CC5500")
    plt.xlabel("Run Scored")
    plt.ylabel("Batsman")
    plt.title(f"Top 10 Run Scorers\nOrange Cap: {orange_cap} ({orange_cap_run} runs)")

    plt.tight_layout()
    plt.show()


# ---------------- SIXES ----------------

def most_sixes():
    # batsmen total sixes list
    batsman_sixes = ipl_batsman.groupby('striker')['sixes'].sum()

    # top 10 batsmen
    top10sixes = batsman_sixes.sort_values(ascending=False).head(10)

    # Most sixes holder
    name_for_most_sixes = top10sixes.index[0]
    number_of_sixes = top10sixes.iloc[0]

    # Sort for better horizontal chart display
    top10sixes = top10sixes.sort_values()

    # Sixes Plot with Most sixes
    plt.figure(figsize=(10, 6))
    plt.barh(top10sixes.index, top10sixes.values, color="#000080")
    plt.xlabel("Number of Sixes")
    plt.ylabel("Batsman")
    plt.title(
        f"Top 10 Most Sixes\nMost Sixes Hitter: {name_for_most_sixes} ({number_of_sixes} sixes)"
    )

    plt.tight_layout()
    plt.show()


# ---------------- TEAM WIN % ----------------

def team_win_percentage():
    # Teams list
    team1 = matches['team1']
    team2 = matches['team2']

    # Total play match list
    matches_for_team = pd.concat([team1, team2])

    # Total count for each team
    total_matches_for_team = matches_for_team.value_counts()

    # Total winning count for each team
    winning_team = matches['match_winner'].value_counts()

    # Make Team Percentage DataFrame
    team_name = []
    team_per = []

    for team in total_matches_for_team.index:
        team_name.append(team)
        team_per.append(winning_team[team] / total_matches_for_team[team] * 100)

    team_per = pd.DataFrame({"per": team_per}, index=team_name)

    # Sort teams by win percentage
    team_per = team_per.sort_values("per")

    # Make Bar Chart for Winning percentage
    plt.figure(figsize=(10, 6))
    plt.barh(team_per.index, team_per["per"], color="#c64357")

    best_team = team_per["per"].idxmax()
    best_percentage = team_per["per"].max()

    plt.xlabel("Win Percentage (%)")
    plt.ylabel("Team")
    plt.title(f"Team Win Percentage\nBest Team: {best_team} ({best_percentage:.1f}%)")

    plt.tight_layout()
    plt.show()


# ---------------- MOST FOURS ----------------

def most_fours():
    # batsmen total fours list
    batsman_fours = ipl_batsman.groupby('striker')['fours'].sum()

    # top 10 batsmen
    top10fours = batsman_fours.sort_values(ascending=False).head(10)

    # Most fours holder
    name_for_most_fours = top10fours.index[0]
    number_of_fours = top10fours.iloc[0]

    # Sort for better horizontal chart display
    top10fours = top10fours.sort_values()

    # Fours Plot with Most fours
    plt.figure(figsize=(10, 6))
    plt.barh(top10fours.index, top10fours.values, color="#06911D")
    plt.xlabel("Number of Fours")
    plt.ylabel("Batsman")
    plt.title(
        f"Top 10 Most Fours\nMost Fours Hitter: {name_for_most_fours} ({number_of_fours} fours)"
    )

    plt.tight_layout()
    plt.show()


# ---------------- DOT BALLS ----------------

def dot_balls():
    # bowlers total dot bowled list
    bowler_dots = ipl_bowler.groupby('bowler')['dots_bowled'].sum()

    # top 10 bowlers dot
    top10bowler_dot = bowler_dots.sort_values(ascending=False).head(10)

    # Most dot ball bowler
    most_dot_ball = top10bowler_dot.index[0]
    number_of_most_dot_ball = top10bowler_dot.iloc[0]

    # Sort for better horizontal chart display
    top10bowler_dot = top10bowler_dot.sort_values()

    # Dot Ball Plot
    plt.figure(figsize=(10, 6))
    plt.barh(top10bowler_dot.index, top10bowler_dot.values, color="#1ba1c2")
    plt.xlabel("Dot Ball")
    plt.ylabel("Bowler")
    plt.title(
        f"Top 10 Most Dot Ball Bowlers\nMost Dot Ball Bowler: {most_dot_ball} ({number_of_most_dot_ball} dots)"
    )

    plt.tight_layout()
    plt.show()


# ---------------- ECONOMY ----------------

def economy_rate():
    # bowlers total conceded run list
    bowler_run = ipl_bowler.groupby('bowler')['runs_conceded'].sum()
    bowler_total_bowled = ipl_bowler.groupby('bowler')['overs_bowled'].sum() * 6

    # Make DataFrame
    team_run_name = []
    team_run_per = []

    for bowler in bowler_run.index:
        team_run_name.append(bowler)
        team_run_per.append(bowler_run[bowler] / bowler_total_bowled[bowler])

    team_run_per = pd.DataFrame({"per": team_run_per}, index=team_run_name)

    # Sort teams by run given percentage
    team_run_per = team_run_per.sort_values("per", ascending=True).head(10)

    # Bar Chart for economy
    plt.figure(figsize=(10, 6))
    plt.barh(team_run_per.index, team_run_per["per"], color="#ef11b0")

    best_bowler = team_run_per["per"].idxmin()
    best_bowler_percentage = team_run_per["per"].min()

    plt.xlabel("Runs per Ball")
    plt.ylabel("Bowler")
    plt.title(
        f"Top 10 Economical Bowlers\nBest Economy: {best_bowler} ({best_bowler_percentage:.2f})"
    )

    plt.tight_layout()
    plt.show()


# ---------------- TKINTER DASHBOARD (SECTIONED UI) ----------------

root = tk.Tk()
root.title("IPL 2025 Analytics Dashboard")
root.geometry("750x500")
root.resizable(False, False)
root.configure(bg="#e9eef5")


# Header
title = tk.Label(
    root,
    text="🏏 IPL 2025 Analytics Dashboard",
    font=("Helvetica", 16, "bold"),
    bg="#e9eef5",
    fg="#1f3b73"
)
title.pack(pady=8)


subtitle = tk.Label(
    root,
    text="Select any analysis from below sections",
    font=("Helvetica", 10),
    bg="#e9eef5",
    fg="#5b6b8c"
)
subtitle.pack()


# ---------------- MAIN FRAME ----------------
main_frame = tk.Frame(root, bg="#e9eef5")
main_frame.pack(pady=10)


button_style = {
    "font": ("Helvetica", 10, "bold"),
    "width": 18,
    "bd": 0,
    "cursor": "hand2"
}


# ================= BATSMAN SECTION =================
bat_frame = tk.LabelFrame(
    main_frame,
    text="🏏 Batting Analysis",
    font=("Helvetica", 11, "bold"),
    bg="#fff3e0",
    fg="#e65100",
    padx=10,
    pady=10
)
bat_frame.grid(row=0, column=0, padx=10, pady=10)


tk.Button(bat_frame, text="Orange Cap", bg="#ffcc80", command=orange_cap, **button_style)\
    .grid(row=0, column=0, padx=5, pady=5)

tk.Button(bat_frame, text="Most Sixes", bg="#90caf9", command=most_sixes, **button_style)\
    .grid(row=1, column=0, padx=5, pady=5)

tk.Button(bat_frame, text="Most Fours", bg="#a5d6a7", command=most_fours, **button_style)\
    .grid(row=2, column=0, padx=5, pady=5)


# ================= BOWLING SECTION =================
bowl_frame = tk.LabelFrame(
    main_frame,
    text="🎯 Bowling Analysis",
    font=("Helvetica", 11, "bold"),
    bg="#ede7f6",
    fg="#512da8",
    padx=10,
    pady=10
)
bowl_frame.grid(row=0, column=1, padx=10, pady=10)


tk.Button(bowl_frame, text="Purple Cap", bg="#d1c4e9", command=purple_cap, **button_style)\
    .grid(row=0, column=0, padx=5, pady=5)

tk.Button(bowl_frame, text="Dot Balls", bg="#80deea", command=dot_balls, **button_style)\
    .grid(row=1, column=0, padx=5, pady=5)

tk.Button(bowl_frame, text="Economy Rate", bg="#ffab91", command=economy_rate, **button_style)\
    .grid(row=2, column=0, padx=5, pady=5)


# ================= TEAM SECTION =================
team_frame = tk.LabelFrame(
    main_frame,
    text="🏆 Team Analysis",
    font=("Helvetica", 11, "bold"),
    bg="#e3f2fd",
    fg="#1565c0",
    padx=10,
    pady=10
)
team_frame.grid(row=0, column=2, padx=10, pady=10)


tk.Button(team_frame, text="Team Win %", bg="#ef9a9a", command=team_win_percentage, **button_style)\
    .grid(row=0, column=0, padx=5, pady=5)


# ---------------- EXIT BUTTON ----------------
tk.Button(
    root,
    text="Exit Dashboard",
    command=root.quit,
    bg="#e57373",
    fg="white",
    font=("Helvetica", 10, "bold"),
    bd=0,
    padx=15,
    pady=5,
    cursor="hand2"
).pack(pady=10)


root.mainloop()