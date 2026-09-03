<?php
    $dt_atendimento = trim($_POST['dtAtendimento']);
    $cliente = trim($_POST['cliente']);
    $vendedor = trim($_POST['vendedor']);
    $usuario = trim($_POST['usuario']);
    $produto = trim($_POST['produto']);
    $assunto = trim($_POST['assunto']);
    $descricao = trim($_POST['descricao']);
    $solucao = trim($_POST['solucao']);
    if(($dt_atendimento == "") || ($cliente == "") || ($vendedor == "") || ($usuario == "") || $produto == "" || $assunto == "" || $descricao == ""){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao cadastrar o atendimento!</p>";
        return;
    }
    require_once("../db/database.php");
    $cliente_select = "SELECT id FROM cliente WHERE nome = '{$cliente}'";
    $cliente_resultado = mysqli_query($conexao, $cliente_select);
    $cliente_id = ($cliente_resultado && mysqli_num_rows($cliente_resultado) > 0) ? mysqli_fetch_assoc($cliente_resultado)['id'] : null;
    $vendedor_select = "SELECT id FROM vendedor WHERE nome = '{$vendedor}'";
    $vendedor_resultado = mysqli_query($conexao, $vendedor_select);
    $vendedor_id = ($vendedor_resultado && mysqli_num_rows($vendedor_resultado) > 0) ? mysqli_fetch_assoc($vendedor_resultado)['id'] : null;
    $usuario_select = "SELECT id FROM usuario WHERE `login` = '{$usuario}'";
    $usuario_resultado = mysqli_query($conexao, $usuario_select);
    $usuario_id = ($usuario_resultado && mysqli_num_rows($usuario_resultado) > 0) ? mysqli_fetch_assoc($usuario_resultado)['id'] : null;
    $SQL = "INSERT INTO atendimento (dt_atendimento, cliente_id, vendedor_id, usuario_id, produto_servico, assunto, descricao, solucao) VALUES ('$dt_atendimento', '$cliente_id', '$vendedor_id', '$usuario_id', '$produto', '$assunto', '$descricao', '$solucao')";
    $stmt = $conexao->prepare($SQL);
    if($stmt->execute() == true){
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:green;'>Atendimento cadastrado com sucesso</p>";
        echo "<button style='margin-top:180px;margin-left:600px;border-radius:5px;border:none;width:100px;height:30px;background-color:#2c2c2c;cursor:pointer;'><a href='../home/tela_home.php' style='color:white;text-decoration:none;'>Voltar</a></button>";
    }else{
        echo "<p style='text-align:center; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; color:red;'>Erro ao cadastrar o atendimento" . $stmt->errorInfo() . "</p>";
    }
    unset($conexao);
?>