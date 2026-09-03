<?php
    include("../db/database.php");
    include("../login/verifica_login.php");
    $login = $_SESSION["login"];
    $senha_old = trim($_POST['senhaAntiga']);
    $senha_new = trim($_POST['senhaNova']);
    $confirma_senha = trim($_POST['confirmaSenha']);
    if($senha_old == "" || $senha_new == "" || $confirma_senha == ""){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro: senha não informada</p>";
        return;
    }
    if($senha_new != $confirma_senha){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro: as senhas não correspondem</p>";
        return;
    }
    $select = "SELECT senha FROM usuario WHERE id = '{$login}' AND senha = '{$senha_old}'";
    $registro = mysqli_query($conexao, $select);
    $qtdRegistro = mysqli_num_rows($registro);
    if($qtdRegistro > 1){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro</p>";
        return;
    }
    $SQL = "UPDATE usuario SET senha = '{$senha_new}' WHERE senha = '{$senha_old}'";
    $stmt = $conexao->prepare($SQL);
    $retorno = $stmt->execute();
    if($retorno == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:green;'>Senha alterada com sucesso</p>";
        echo "<button style='margin-top:180px;margin-left:600px;border-radius:5px;border:none;width:100px;height:30px;background-color:#2c2c2c;cursor:pointer;'><a href='../home/tela_home.php' style='color:white;text-decoration:none;'>Voltar</a></button>";
    }else{
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao alterar a senha " . $stmt->errorInfo() . "</p>";
        return;
    }
    unset($conexao);
?>