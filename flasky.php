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

$sql = "CREATE TABLE `authentic` (
  `id_authentic` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `nom_complet` varchar(200) NOT NULL,
  `num_piece` varchar(100) NOT NULL,
  `num_permis` varchar(100) NOT NULL,
  `antecedent` varchar(500) NOT NULL,
  `paiement` varchar(100) NOT NULL,
  `img` varchar(255) NOT NULL
)";


$sql2 = "INSERT INTO `authentic` (id_authentic, nom_complet, num_piece, num_permis, antecedent, paiement, img) 
VALUES (1, 'kouadio flora', '1234567890', '0987654321', 'sans antecedent', 'wave', '')";


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