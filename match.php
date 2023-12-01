<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "lorem-ipsum-jobportal";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT Fname,Lname FROM work_request_form as A,applicants as B WHERE A.Location=B.Location AND A.closingTime = B.closingTime;
$result = $conn->query($sql);

if ($result->num_rows == 1) { // I'm assuming you will only have one match if the item exists
  $row = $result->fetch_assoc();
  $sql = "UPDATE eligible_applicants SET Lname='".$row["Lname"]."' WHERE A.Location=B.Location AND A.closingTime = B.closingTime
  $result = $conn->query($sql);
  // check for update errors
} else {
  echo "0 results";
}
$conn->close();
?>