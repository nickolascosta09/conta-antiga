<?php
    include("../db/database.php");
    $user = trim($_POST['user']);
    $status = trim($_POST['status']);
    if($user == "" || $status == ""){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro: dados n&atilde;o informados</p>";
        return;
    }
    $select = "SELECT `status` FROM usuario WHERE nome = '{$user}'";
    $registro = mysqli_query($conexao, $select);
    $qtdRegistro = mysqli_num_rows($registro);
    if($qtdRegistro > 1){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro</p>";
        return;
    }
    $SQL = "UPDATE usuario SET `status` = '{$status}' WHERE nome = '{$user}'";
    $stmt = $conexao->prepare($SQL);
    $retorno = $stmt->execute();
    if($retorno == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:green;'>Status alterado com sucesso</p>";
        echo "<button style='margin-top:180px;margin-left:600px;border-radius:5px;border:none;width:100px;height:30px;background-color:#2c2c2c;cursor:pointer;'><a href='../home/tela_home.php' style='color:white;text-decoration:none;'>Voltar</a></button>";
    }else{
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao alterar a senha " . $stmt->errorInfo() . "</p>";
        return;
    }
    unset($conexao);
?>