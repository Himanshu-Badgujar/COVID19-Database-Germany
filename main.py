import requests
import json

url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=cases,deaths,cases_per_population,cases7_per_100k,county,last_update&returnGeometry=false&outSR=&f=json"

response = requests.get(url)
data = response.json()

# Read the existing JSON file
with open("database.json", "r", encoding='utf-8') as file:
    existing_data = json.load(file)

if existing_data["database_update"] != data["features"][0]["attributes"]["last_update"]:
    existing_data["database_update"] = data["features"][0]["attributes"]["last_update"]
    for i in range(411):
        if data["features"][i]["attributes"]["county"] == existing_data["database"][i][0]:
            new_data = {
                "last_update": data["features"][0]["attributes"]["last_update"],
                "cases": data["features"][i]["attributes"]["cases"],
                "deaths": data["features"][i]["attributes"]["deaths"],
                "cases_per_population": data["features"][i]["attributes"]["cases_per_population"],
                "cases7_per_100k": data["features"][i]["attributes"]["cases7_per_100k"],
            }
            existing_data["database"][i][2].append(new_data)

# Write the updated JSON data back to the file
with open("database.json", "w", encoding='utf-8') as file:
    json.dump(existing_data, file, ensure_ascii=False, indent=4)

# Generate HTML table with CSS
html_table = """
<meta charset="UTF-8">
<style>
     table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        padding: 8px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }

    th {
        background-color: #f2f2f2;
    }

    .red {
        background-color: #FF6961;
    }

    .green {
        background-color: #87AB69;
    }

    .center-content {
        text-align: center;
    }

    .fixed-header {
        position: sticky;
        top: 0;
        z-index: 1;
        background-color: #f2f2f2;
    }

    .link {
  	color: blue;
  	text-decoration: underline;
  	cursor: pointer;
    }
</style>

<script>
    function runScript(ID) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "runHistorianData.php?ID=" + encodeURIComponent(ID), true);
    xhr.send();

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location.href = "historianData.html";
        }
    };
}
</script>

<table>
    <tr class="fixed-header">
        <th>ID</th>
        <th class="center-content">Country</th>
        <th class="center-content">Last Update</th>
        <th class="center-content">Cases</th>
        <th class="center-content">Deaths</th>
        <th class="center-content">Cases per Population</th>
        <th class="center-content">Cases in last 7 days per 100k</th>
    </tr>
"""

with open("database.json", "r", encoding='utf-8') as file:
    existing_data = json.load(file)

for item in existing_data["database"]:
    ID = item[0]
    country = item[1]
    data_item = item[2][-1]  # Get the last item in the list
    last_update = data_item["last_update"]
    cases = data_item["cases"]
    deaths = data_item["deaths"]
    cases_per_population = round(data_item["cases_per_population"], 1)
    cases7_per_100k = round(data_item["cases7_per_100k"], 1)

    death_class = "red" if cases7_per_100k > 3.0 else "green"

    html_table += "<tr>"
    html_table += f'<td onclick="runScript(\'{ID}\')" class="link">{ID}</td>'
    html_table += f'<td style="text-align: center;">{country}</td>'
    html_table += f'<td style="text-align: center;">{last_update}</td>'
    html_table += f'<td style="text-align: center;">{cases}</td>'
    html_table += f'<td style="text-align: center;">{deaths}</td>'
    html_table += f'<td style="text-align: center;">{cases_per_population}</td>'
    html_table += f'<td style="text-align: center;" class="{death_class}">{cases7_per_100k}</td>'
    html_table += "</tr>"

html_table += "</table>"

# Write the HTML table to a file
with open("table.html", "w", encoding="utf-8") as file:
    file.write(html_table)
