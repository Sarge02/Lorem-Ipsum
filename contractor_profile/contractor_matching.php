<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Records</title>
    <style>
        table{
            width: 70%;
            margin: auto;
            font-family: Arial, Helvetica, sans-serif;
        }
        table, tr, th, td{
            border: 1px solid #d4d4d4;
            border-collapse: collapse;
            padding: 12px;
        }
        th, td{
            text-align: left;
            vertical-align: top;
        }
        tr:nth-child(even){
            background-color: #e7e9eb;
        }
    </style>
<body>
      
<?php
    //storing database details in variables.
    $hostname = "localhost";
    $username = "root";
    $password = "";
    $dbname = "profile_db";

    //creating connection to database
    $con = mysqli_connect($hostname, $username, $password, $dbname);
    //checking if connection is working or not
    if(!$con)
    {
        die("Connection failed!" . mysqli_connect_error());
    }
    else 
    {
        echo "Successfully Connected! <br>";
    }
    //Output Form Entries from the Database
    $sql = "SELECT id, lastname, email, image FROM users";
    //fire query
    $result = mysqli_query($con, $sql);
    if(mysqli_num_rows($result) > 0)
    {
       echo '<table> <tr> <th> Id </th> <th> Name </th> <th> Email </th> <th> Image </th> </tr>';
       while($row = mysqli_fetch_assoc($result)){
         // to output mysql data in HTML table format
           echo '<tr > <td>' . $row["id"] . '</td>
           <td>' . $row["lastname"] . '</td>
           <td> ' . $row["email"] . '</td>
           <td>' . $row["image"] . '</td> </tr>';
       }
       echo '</table>';
    }
    else
    {
        echo "0 results";
    }
    // closing connection
    mysqli_close($con);

?>
</body>
</html>