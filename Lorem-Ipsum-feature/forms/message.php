<?php
ini_set("SMTP","smtp.gmail.com");
ini_set('smtp_port', 587);
ini_set('sendmail_path', "\"C:\xampp\sendmail\sendmail.exe\" -t");
ini_set('smtp_ssl', "tls");
ini_set('extension', "openssl");

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["submit"])) {
    $to = "titanmailtesting@gmail.com";
    $subject = "New Titan Finder Message" . " from " . $_POST["fname"] . " " . $_POST["lname"];
    $message = $_POST["message"];
    
    $headers = "From: titanmailtesting@gmail.com" . "\r\n" .
               "Reply-To: titanmailtesting@gmail.com" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();
    
    if (mail($to, $subject, $message, $headers)) {
        echo "Email sent successfully!";
		header("Location: contacted.html");
    } else {
        echo "Email could not be sent.";
		header("Location: uncontacted.html");
    }
}
?>
