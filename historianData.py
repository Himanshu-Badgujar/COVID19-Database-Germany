import sys
import json
import numpy as np
import matplotlib.pyplot as plt

last_update_plot = np.array([])
cases_plot = np.array([])
deaths_plot = np.array([])
cases_per_population_plot = np.array([])
cases7_per_100k_plot = np.array([])

# Read the existing JSON file
with open("database.json", "r", encoding='utf-8') as file:
    existing_data = json.load(file)

# Retrieve the country value from command-line arguments
ID = int(sys.argv[1])

country = None
for database in existing_data["database"]:
    if database[0] == ID:
        country = database[1]
        break

html_table = f"""
<meta charset="UTF-8">
<style>
    table {{
        width: 100%;
        border-collapse: collapse;
    }}

    th, td {{
        padding: 8px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }}

    th {{
        background-color: #f2f2f2;
    }}

    .red {{
        background-color: #FF6961;
    }}

    .green {{
        background-color: #87AB69;
    }}

    .center-content {{
        text-align: center;
    }}

    .fixed-header {{
        position: sticky;
        top: 0;
        z-index: 1;
        background-color: #f2f2f2;
    }}

    .link {{
        color: blue;
        text-decoration: underline;
        cursor: pointer;
    }}
</style>

<h1 style="text-align: center;">{country} Historian Data</h1>

<table>
    <tr class="fixed-header">
        <th>Last Update</th>
        <th class="center-content">Cases</th>
        <th class="center-content">Deaths</th>
        <th class="center-content">Cases per Population</th>
        <th class="center-content">Cases in last 7 days per 100k</th>
    </tr>
"""

for database in existing_data["database"]:
    if database[0] == ID:
        historian_data = database[2]
        for data in historian_data:
            last_update = data["last_update"]
            last_update_plot = np.append(last_update_plot, [data["last_update"].split(",")[0]])

            cases = data["cases"]
            cases_plot = np.append(cases_plot, [cases])

            deaths = data["deaths"]
            deaths_plot = np.append(deaths_plot, [deaths])

            cases_per_population = round(data["cases_per_population"], 1)
            cases_per_population_plot = np.append(cases_per_population_plot, [cases_per_population])

            cases7_per_100k = round(data["cases7_per_100k"], 1)
            cases7_per_100k_plot = np.append(cases7_per_100k_plot, [cases7_per_100k])

            death_class = "red" if cases7_per_100k > 3.0 else "green"

            html_table += "<tr>"
            html_table += f'<td>{last_update}</td>'
            html_table += f'<td style="text-align: center;">{cases}</td>'
            html_table += f'<td style="text-align: center;">{deaths}</td>'
            html_table += f'<td style="text-align: center;">{cases_per_population}</td>'
            html_table += f'<td style="text-align: center;" class="{death_class}">{cases7_per_100k}</td>'
            html_table += "</tr>"

html_table += "</table>"

# Plot the graphs
plt.figure(figsize=(10, 7))
plt.subplot(2, 2, 1)
plt.bar(last_update_plot, cases_plot)
plt.title('Cases')

plt.subplot(2, 2, 2)
plt.bar(last_update_plot, deaths_plot)
plt.title('Deaths')

plt.subplot(2, 2, 3)
plt.bar(last_update_plot, cases_per_population_plot)
plt.title('Cases per Population')

plt.subplot(2, 2, 4)
plt.bar(last_update_plot, cases7_per_100k_plot)
plt.title('Cases in 7 days per 100k')

# Display the figure with all subplots
plt.tight_layout()
plt.savefig('graph.png')
html_table += """<div style="text-align: center;"><img src="graph.png" alt="Graph" /></div>"""

# Write the HTML table to a file
with open("historianData.html", "w", encoding="utf-8") as file:
    file.write(html_table)

