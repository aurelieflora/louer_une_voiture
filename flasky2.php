<?php
$servername = "localhost";
$username = "spcom_userkouadio";
$password = "FIKS4X6ZAHIF";
$dbase = "spcom_kouadio";


$conn =  mysqli_connect($servername, $username, $password, $dbase);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}


$sql = "CREATE TABLE `utilisateurs` (
  `id_utilisateurs` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `np` varchar(200) NOT NULL,
  `telephone` varchar(15) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mdp` varchar(300) NOT NULL
)";

$sql2 = "INSERT INTO `utilisateurs` (`id_utilisateurs`, `np`, `telephone`, `email`, `mdp`) 
VALUES (1, 'kouadio flora', '+2250934567890', 'simplon@gmail.com', '12345')";


if (mysqli_query($conn, $sql)) {
  echo "Table MyGuests created successfully";
} else {
  echo "Error creating table: " . mysqli_error($conn);
}

if (mysqli_query($conn, $sql2)) {
  echo "New record created successfully";
  } else {
  echo "Error: " . $sql2 . "<br>" . mysqli_error($conn);
  }


?>