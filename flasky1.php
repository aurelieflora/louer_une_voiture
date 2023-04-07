<?php
$servername = "localhost";
$username = "spcom_userkouadio";
$password = "FIKS4X6ZAHIF";
$dbase = "spcom_kouadio";


// -- Structure de la table `authentic`



$conn =  mysqli_connect($servername, $username, $password, $dbase);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "CREATE TABLE `flask1` (
  `id_flask1` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `nom` varchar(20) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mdp` varchar(300) NOT NULL
)";


$sql2 = "INSERT INTO `flask1` (`id_flask1`, `nom`, `prenom`, `email`, `mdp`) 
VALUES (1, 'kouadio', 'flora', 'flora@gmail.com', '$2b$12$NC5RihByG4jYE/JpxtPol.llMm7NML9ZHcmVakkcky.5ZOEB7P3Xm')";

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