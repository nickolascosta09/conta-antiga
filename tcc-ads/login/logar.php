<?php
    session_start();
    include('../db/database.php');
    include("../functions/verificar.php");
    if(empty($_POST['login']) || empty($_POST['senha'])){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro: login ou senha n&atilde;o informado</p>";
        header('Location: ../index.php');
        exit();
    }
    $usuario = mysqli_real_escape_string($conexao, $_POST['login']);
    $senha = mysqli_real_escape_string($conexao, $_POST['senha']);
    $existe = verificaStatus($usuario);
    if($existe == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Acesso Negado</p>";
        header('Location: ../index.php');
        exit();
    }
    $SQL = "SELECT * FROM usuario WHERE login = '{$usuario}' AND senha = '{$senha}'";
    $stmt = mysqli_query($conexao, $SQL);
    $retorno = mysqli_num_rows($stmt);
    if($retorno == 1){
        $_SESSION['login'] = $usuario;
        header('Location: ../home/tela_home.php');
        exit();
    }else{
        $_SESSION['nao_autenticado'] = true;
        header('Location: ../index.php');
        exit();
    }
?>