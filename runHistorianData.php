<?php
$ID = $_GET['ID'];

// Set the default encoding to UTF-8
mb_internal_encoding("UTF-8");

// Execute the Python script with the country value as an argument
exec("python3 historianData.py " . escapeshellarg($ID));

// Return a response indicating successful execution
http_response_code(200);
?>

