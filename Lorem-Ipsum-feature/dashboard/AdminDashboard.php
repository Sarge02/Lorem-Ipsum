<?php 

require_once('db.php');
$query = "SELECT * FROM jobs";
$result = mysqli_query($con,$query);

?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title> Dashboard | Titan Finder </title>
        <meta name="description" content="Admin Dashboard">
        <link rel="stylesheet" href="conDash.css">
    </head>
        
    <body>
        <div class="containerBig">
            <div class="containerCard">
                <div class="card">
                    <h2>Labor (Last 30 Days)</h2>
                </div>
                <div class="card">
                    <h2>Top Jobs(Top 10)</h2>
                    <div class="card-body">
                        <table class="job table">
                            <tr class="bg-dark">
                                <td>Job</td>
                                <td>Employer</td>
                                <td>Sort By</td>
                            </tr>
                            <tr>
                                <?php 
                                  while($row = mysqli_fetch_assoc($result))
                                  {
                                ?>
                                <td><?php echo $row['Job'];?></td>
                                <td><?php echo $row['Employer'];?></td>
                                <td><?php echo $row['Sort By'];?></td>
                                </tr>    
                                <?php 
                                  }
                                ?>
                        </table>
                    </div>
                </div>
                <div class="card">
                    <h2>Messages</h2>
                </div>
            </div>
            <div class="bigBox">
                <h2>Filtered Jobs</h2>
            </div>
        </div>

    </body>
</html>