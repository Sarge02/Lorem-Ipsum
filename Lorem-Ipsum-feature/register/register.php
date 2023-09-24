<?php
    //connect to the db
    $servername = "localhost";
    $username = "root";
    $dbpassword = "";
    $dbname = "user_accounts";
	
	$fname = $_POST["fname"];
    $lname = $_POST["lname"];
    $email = $_POST["email"];
	$password = $_POST["password"];
    $phone = $_POST["phone"];
    $company = $_POST["company"];
    $website = $_POST["website"];

    $conn = new mysqli($servername, $username, $dbpassword, $dbname);
	
	//post input into the 'registration' table
	$sql = $conn->prepare("INSERT INTO registration (fname, lname, email, password, phone, company, website) VALUES (?, ?, ?, ?, ?, ?, ?)");
	$sql->bind_param("sssssss", $fname, $lname, $email, $password, $phone, $company, $website);
	$sql->execute();
	$sql->close();
	$conn->close();
	header("Location:..\login\login.html");  
	exit(); 
?>