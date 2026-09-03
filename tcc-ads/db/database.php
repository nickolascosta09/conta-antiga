<?php
    $servidor = "localhost";
    $user = "root";
    $password = "tiarute";
    $banco = "sgc";
    $conexao = mysqli_connect($servidor, $user, $password) or die("Servidor indisponível");
    mysqli_select_db($conexao, $banco) or die("Banco de Dados indisponível");
?>