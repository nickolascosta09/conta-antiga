<?php
    $nome = trim($_POST['nome']);
    $cpf = trim($_POST['cpf']);
    $sexo = trim($_POST['sexo']);
    $cargo = trim($_POST['cargo']);
    $setor = trim($_POST['setor']);
    $dt_admissao = trim($_POST['dtAdmissao']);
    $status = trim($_POST['status']);
    $login = trim($_POST['login']);
    $senha = trim($_POST['senha']);
    if(($nome == "") || ($cpf == "") || ($cargo == "") || ($setor == "") || $status == "" || $login == "" || $senha == ""){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao cadastrar o usuário!</p>";
        return;
    }
    require_once("../db/database.php");
    $SQL = "INSERT INTO `usuario` (`nome`, `cpf`, `sexo`, `cargo`, `setor`, `dt_admissao`, `status`, `login`, `senha`) VALUES ('$nome', '$cpf', '$sexo', '$cargo', '$setor', '$dt_admissao', '$status', '$login', '$senha')";
    $stmt = $conexao->prepare($SQL);
    if($stmt->execute() == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:green;'>Usuário cadastrado com sucesso</p>";
        echo "<button style='margin-top:180px;margin-left:600px;border-radius:5px;border:none;width:100px;height:30px;background-color:#2c2c2c;cursor:pointer;'><a href='../home/tela_home.php' style='color:white;text-decoration:none;'>Voltar</a></button>";
    }else{
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao cadastrar o usuário" . $stmt->errorInfo() . "</p>";
    }
    unset($conexao);
?>