<html>
    <head>
        <title>Sistema de Gerenciamento de Clientes</title>
        <link rel="icon" type="image/png" sizes="16x16" href="../favicon.png">
        <link rel="stylesheet" type="text/css" href="../css/style-form-consulta.css">
    </head>
    <body>
        <header class="cabecalho">
            <img src="../favicon.png" alt="Logo do Sistema" class="imgsys">
            <div id="linha"></div>
        </header>
        <div class="title">
            <h2>CONSULTA DE ATENDIMENTO</h2>
        </div>
        <div class="form">
            <form action="/consulta/busca_atendimento.php">
                <p>Mostrar Atendimentos</p>
                <!--<h4>Pesquisar por:</h4>
                <label for="dtAtendimento">
                    <h4>Nome</h4>
                    <input type="date" id="dtAtendimento" name="dtAtendimento">
                </label>-->
                <input type="submit" value="Pesquisar" class="btn-form">
            </form>
        </div>
        <div>
            <button type="button" id="btn-voltar"><a href="../home/tela_home.php">Voltar</a></button>
    </body>
</html>
<?php
    include("../login/verifica_login.php");
?>