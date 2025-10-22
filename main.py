import matplotlib.pyplot as plt
import pandas as pd

csv_file_path = r'C:\Users\hunte\Desktop\pitching_hitting_graph\2025_TeamHitting.csv'
df_hitting_full = pd.read_csv(csv_file_path)

csv_file_path = r'C:\Users\hunte\Desktop\pitching_hitting_graph\2025_TeamPitching.csv'
df_pitching_full = pd.read_csv(csv_file_path)

df_hitting = df_hitting_full[['Team', 'wRC+']]
df_pitching = df_pitching_full[['Team', 'FIP']]

merged_df = pd.merge(df_hitting, df_pitching, on='Team', how='inner')

avg_wRC = merged_df['wRC+'].mean()
avg_FIP = merged_df['FIP'].mean()

fig, ax = plt.subplots(figsize=(12, 8))

# Team color map
team_colors = {
    'NYY': '#132440', 
    'BOS': '#BD3039',  
    'HOU': "#F4911E",  
    'LAD': '#005A9C',  
    'PHI': '#E81828',  
    'TBR': "#75AEE4",  
    'TOR': '#134A8E',  
    'ARI': '#A71930',
    'ATL': '#CE1141',
    'BAL': '#DF4601',
    'CHC': '#0E3386',
    'CHW': '#27251F',
    'CIN': '#C6011F',
    'CLE': '#E50022',
    'COL': '#333366',
    'DET': '#0C2340',
    'KCR': '#004687',
    'LAA': '#BA0021',
    'MIA': '#00A3E0',
    'MIL': '#ffc52f',
    'MIN': '#002B5C',
    'NYM': '#FF5910',
    'ATH': '#003831',
    'PIT': '#FDB827',
    'SDP': '#2F241D',
    'SFG': '#FD5A1E',
    'SEA': '#005C5C',
    'STL': '#C41E3A',
    'TEX': '#003278',
    'WSN': '#AB0003'
}

# Loops through the data and plots each team individually
for index, row in merged_df.iterrows():
    team = row['Team']
    wrc_plus = row['wRC+']
    fip = row['FIP']
    
    color = team_colors.get(team, '#000000')

    # Plot the dots
    ax.scatter(wrc_plus, fip, color=color, s=100) # s=100 controls the size of the dot
    
    # Adds the text labels
    ax.text(wrc_plus + 1, fip + 0.01, team, fontsize=10, ha='left', color=color)

ax.axhline(y=avg_FIP, color='gray', linestyle='--', linewidth=2, label=f'Avg FIP ({avg_FIP:.2f})')
ax.axvline(x=avg_wRC, color='gray', linestyle='--', linewidth=2, label=f'Avg wRC+ ({avg_wRC:.2f})')

ax.set_title('Team Performance Based on wRC+ and FIP', weight='bold')
ax.set_xlabel('wRC+', weight='bold')
ax.set_ylabel('FIP', weight='bold')

# Inverts the y-axis (FIP) so lower values are at the top
ax.invert_yaxis()

ax.legend()

ax.text(0.95, 0.95, 'Good Hitting\nGood Pitching', ha='right', va='top', transform=ax.transAxes, fontsize=12, weight='bold')
ax.text(0.05, 0.95, 'Bad Hitting\nGood Pitching', ha='left', va='top', transform=ax.transAxes, fontsize=12, weight='bold')
ax.text(0.05, 0.05, 'Bad Hitting\nBad Pitching', ha='left', va='bottom', transform=ax.transAxes, fontsize=12, weight='bold')
ax.text(0.95, 0.05, 'Good Hitting\nBad Pitching', ha='right', va='bottom', transform=ax.transAxes, fontsize=12, weight='bold')

plt.tight_layout()
plt.savefig('pitching_hitting_graph.png', dpi=300, bbox_inches='tight')
plt.show() 





