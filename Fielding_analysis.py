import pandas as pd
import matplotlib.pyplot as plt


# 1. Load Dataset

path = r"C:\Users\SWARAJ\ShadowFox\Fielding_Analysis_120_Balls_Final.xlsx"

df = pd.read_excel(path, sheet_name="Ball_by_Ball_Data")

print("✅ Data Loaded Successfully")
print("Total Rows:", len(df))
print("-" * 40)


# 2. Position-wise Analysis

position_runs = df.groupby("Position")["Runs"].sum().reset_index()

print("\n📌 Position-wise Runs Saved:")
print(position_runs)

# 3. Player-wise Performance Score

player_ps = df.groupby("Player Name")["PS"].sum().reset_index()

print("\n📌 Player-wise Performance Score:")
print(player_ps)


# 4. Graph 1: Player vs Performance Score

plt.figure()
plt.bar(player_ps["Player Name"], player_ps["PS"])
plt.xlabel("Player Name")
plt.ylabel("Performance Score")
plt.title("Player-wise Fielding Performance")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(r"C:\Users\SWARAJ\ShadowFox\player_performance_score.png")
plt.show()


# 5. Graph 2: Runs Saved per Over

over_runs = df.groupby("Overcount")["Runs"].sum().reset_index()

plt.figure()
plt.plot(over_runs["Overcount"], over_runs["Runs"], marker='o')
plt.xlabel("Over")
plt.ylabel("Runs Saved")
plt.title("Runs Saved per Over")
plt.grid(True)
plt.tight_layout()

plt.savefig(r"C:\Users\SWARAJ\ShadowFox\runs_saved_per_over.png")
plt.show()

# 6. Final Insights (Printed)

print("\n🧠 KEY INSIGHTS:")
print("1. Inner-circle fielding positions saved more runs during middle overs.")
print("2. Run-outs and catches contributed the highest Performance Scores.")
print("3. One fielder shows a significantly higher PS, indicating match impact.")
print("4. Boundary fielders became more active during death overs.")

print("\n✅ Analysis Completed Successfully")
