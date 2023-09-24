<?php
// Execute the Python script
exec("python3 main.py");

// Return a response indicating successful execution
http_response_code(200);
?>

