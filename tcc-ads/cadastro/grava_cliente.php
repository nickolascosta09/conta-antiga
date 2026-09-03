<?php
    $nome = trim($_POST['nome']);
    $cpf = trim($_POST['cpf']);
    $rg = trim($_POST['rg']);
    $sexo = trim($_POST['sexo']);
    $dt_nascimento = trim($_POST['dtNascimento']);
    $cep = trim($_POST['cep']);
    $logradouro = trim($_POST['logradouro']);
    $nr_endereco = trim($_POST['endNum']);
    $complemento = trim($_POST['complemento']);
    $bairro = trim($_POST['bairro']);
    $cidade = trim($_POST['cidade']);
    $uf = trim($_POST['uf']);
    $telefone = trim($_POST['telefone']);
    $celular = trim($_POST['celular']);
    $email = trim($_POST['email']);
    if(($nome == "") || ($cpf == "") || ($dt_nascimento == "") || ($cep == "") || $logradouro == "" || $nr_endereco == "" || $bairro == "" || $cidade == "" || $uf == "" || $celular == "" || $email == ""){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao cadastrar o cliente!</p>";
        return;
    }
    require_once("../db/database.php");
    include("../functions/verificar.php");
    $existe = verificaCliente($nome, $cpf);
    if($existe == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro: Esse cliente j&aacute existe no sistema!</p>";
    }
    $SQL = "INSERT INTO cliente (nome, cpf, rg, sexo, dt_nascimento, cep, logradouro, end_num, complemento, bairro, cidade, uf, telefone, celular, email) VALUES ('$nome', '$cpf', '$rg', '$sexo', '$dt_nascimento', '$cep', '$logradouro', '$nr_endereco', '$complemento', '$bairro', '$cidade', '$uf', '$telefone', '$celular', '$email')";
    $stmt = $conexao->prepare($SQL);
    if($stmt->execute() == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:green;'>Cliente cadastrado com sucesso</p>";
        echo "<button style='margin-top:180px;margin-left:600px;border-radius:5px;border:none;width:100px;height:30px;background-color:#2c2c2c;cursor:pointer;'><a href='../home/tela_home.php' style='color:white;text-decoration:none;'>Voltar</a></button>";
    }else{
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao cadastrar o cliente" . $stmt->errorInfo() . "</p>";
    }
    unset($conexao);
?>