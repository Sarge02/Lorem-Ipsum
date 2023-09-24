<?php
    //connect to the db
    $servername = "localhost";
    $username = "root";
    $dbpassword = "";
    $dbname = "user_accounts";
	
    $email = $_POST["email"];
	$password = $_POST["password"];

    $conn = new mysqli($servername, $username, $dbpassword, $dbname);
	
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}

	//4 2 handle sql injection
	$sql = sprintf("SELECT * FROM registration WHERE email = '%s'", $conn->real_escape_string($_POST["email"]));
	$result = $conn->query($sql);

	if (!$result) {
		die("Query failed: " . $conn->error);
	}

	if ($result->num_rows > 0) {
		$user = $result->fetch_assoc();
		header("Location: ../dashboard/clientDashboard.html");
		//var_dump($user);
	} else {
		echo "No user found with that email.";
	}

	$conn->close();
?>