<?php
    $nome = trim($_POST['nome']);
    $cpf = trim($_POST['cpf']);
    $sexo = trim($_POST['sexo']);
    $dt_nascimento = date('dd/mm/yyyy', strtotime($_POST['dtNascimento']));
    $telefone = trim($_POST['telefone']);
    $celular = trim($_POST['celular']);
    $email = trim($_POST['email']);
    $conselho = trim($_POST['conselho']);
    $nr_conselho = trim($_POST['numConselho']);
    if(($nome == "") || ($cpf == "") || ($dt_nascimento == "") || ($celular == "") || $email == ""){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao cadastrar o vendedor!</p>";
        return;
    }
    require_once("../db/database.php");
    include("../functions/verificar.php");
    $existe = verificaVendedor($nome, $cpf);
    if($existe == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro: Esse vendedor j&aacute existe no sistema!</p>";
    }
    $SQL = "INSERT INTO vendedor (nome, cpf, sexo, dt_nascimento, telefone, celular, email, conselho, nr_conselho) VALUES ('$nome', '$cpf', '$sexo', '$dt_nascimento', '$telefone', '$celular', '$email', '$conselho', '$nr_conselho')";
    $stmt = $conexao->prepare($SQL);
    if($stmt->execute() == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:green;'>Vendedor cadastrado com sucesso</p>";
        echo "<button style='margin-top:180px;margin-left:600px;border-radius:5px;border:none;width:100px;height:30px;background-color:#2c2c2c;cursor:pointer;'><a href='../home/tela_home.php' style='color:white;text-decoration:none;'>Voltar</a></button>";
    }else{
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao cadastrar o vendedor" . $stmt->errorInfo() . "</p>";
    }
    unset($conexao);
?>