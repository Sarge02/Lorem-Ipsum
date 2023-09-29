<?php
    //connect to the db
    $servername = "localhost";
    $username = "root";
    $dbpassword = "";
    $dbname = "user_accounts";
	
	$fname = $_POST["FirstName"];
    $lname = $_POST["LastName"];
    $email = $_POST["Email"];
	$password = $_POST["Password"];
    $phone = $_POST["Phone"];
    $company = $_POST["Company"];
    $website = $_POST["Website"];

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