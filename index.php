<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Line Display</title>
</head>
<body>
    <h1>Random Line Display</h1>

    <?php
    // Function to get client IP address
    function getClientIp() {
        $ipaddress = '';
        if (getenv('HTTP_CLIENT_IP'))
            $ipaddress = getenv('HTTP_CLIENT_IP');
        else if(getenv('HTTP_X_FORWARDED_FOR'))
            $ipaddress = getenv('HTTP_X_FORWARDED_FOR');
        else if(getenv('HTTP_X_FORWARDED'))
            $ipaddress = getenv('HTTP_X_FORWARDED');
        else if(getenv('HTTP_FORWARDED_FOR'))
            $ipaddress = getenv('HTTP_FORWARDED_FOR');
        else if(getenv('HTTP_FORWARDED'))
           $ipaddress = getenv('HTTP_FORWARDED');
        else if(getenv('REMOTE_ADDR'))
            $ipaddress = getenv('REMOTE_ADDR');
        else
            $ipaddress = 'UNKNOWN';
        return $ipaddress;
    }

    // Check if the IP address has already fetched a key today
    $ip = getClientIp();
    $filename = 'ip_log.txt';
    $lastAccess = file_get_contents($filename);

    // Get the current date
    $currentDate = date('Y-m-d');

    if ($lastAccess != $currentDate) {
        // Read keys from keys.txt
        $keys = file('keys.txt', FILE_IGNORE_NEW_LINES);

        // Select a random key
        $randomKey = $keys[array_rand($keys)];

        // Write the IP address and today's date to the log file
        file_put_contents($filename, $currentDate . PHP_EOL, FILE_APPEND);

        // Display the random key
        echo "<p>Random line from keys.txt:</p>";
        echo "<p>$randomKey</p>";
    } else {
        echo "<p>You have already fetched a key today.</p>";
    }
    ?>

</body>
</html>
