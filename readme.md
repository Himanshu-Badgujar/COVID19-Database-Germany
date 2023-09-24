# Germany COVID-19 Database

## Description

This project was created as part of my 'Communication & Visualization' subject.

- **index.html:** The objective of this code is to create a simple web page that provides access to a Germany COVID-19 database. When a user clicks the "Show Database" button, it triggers the runScript JavaScript function. This function sends an XMLHttpRequest to the "runMain.php" server-side script. If the request is successful (status code 200), it redirects the user to the "table.html" page, presumably where the COVID-19 data is displayed in tabular form. In essence, this code serves as a user interface for accessing and viewing COVID-19 data related to Germany.

- **runMain.php:** The objective of this PHP code is to execute a Python script named "main.py" on the server using the exec function. After successfully running the Python script, it sends an HTTP response with a status code of 200, indicating that the execution was successful. Essentially, this PHP code is a server-side script responsible for running a specific Python script when it is called, and it responds with a success status code to indicate that the operation was completed without errors.

- **main.py:** This code retrieves up-to-date COVID-19 data for German counties from a specific URL and updates an existing dataset stored in a JSON file. It then generates an HTML table with CSS styling to display the latest COVID-19 statistics, including cases, deaths, and related metrics, for each county. Each county in the table is clickable, and when clicked, it triggers a JavaScript function to request historical data for that county from a PHP script. The HTML table is subsequently saved as "table.html." In essence, the code keeps the COVID-19 data up to date, presents it in an easily readable format, and allows users to explore historical data for individual counties.

- **runHistorianData.php:** The objective of this PHP code is to execute a Python script named "historianData.py" on the server, passing an "ID" parameter obtained from the URL as an argument to the script. The code sets the encoding to UTF-8 and then uses the exec function to run the Python script with the specified ID as an argument. After successfully running the script, it sends an HTTP response with a status code of 200, indicating that the execution was successful. Essentially, this code is responsible for triggering the execution of a Python script with a specific parameter and responding with a success status code.

- **historianData.py:** - This code generates a detailed HTML report for a specific country's COVID-19 historian data. It reads JSON data from "database.json," extracts information for a given country, and creates an HTML table displaying historical data, including cases, deaths, cases per population, and cases in the last 7 days per 100k. The code also plots four graphs (cases, deaths, cases per population, cases in 7 days per 100k) based on the historical data using Matplotlib and saves them as an image file. The generated HTML report includes both the table and the plotted graphs, providing a comprehensive view of COVID-19 statistics for the selected country.


## Prerequisites

Before using this program, ensure that you have the following prerequisites installed on your system:

- Python
- Apache
- Perl
- HTML
- CSS
- JS

## Usage

- git clone git@github.com:Himanshu-Badgujar/COVID19-Database-Germany.git
- Install Apache server
- Paste scripts in var/www/html/
- type localhost in browser

## Contribution

Contributions are welcome! If you find any issues or want to enhance this project, please feel free to open a pull request.
