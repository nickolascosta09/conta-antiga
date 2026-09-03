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
            <h2>CONSULTA DE VENDEDOR</h2>
        </div>
        <div class="form">
            <form action="/consulta/busca_vendedor.php">
                <p>Mostrar Vendedores</p>
                <!--<h4>Pesquisar por:</h4>
                <label for="nome">
                    <h4>Nome</h4>
                    <input type="text" id="nome" name="nome">
                </label>-->
                <input type="submit" value="Pesquisar" class="btn-form">
            </form>
        </div>
        <div>
            <button type="button" id="btn-voltar"><a href="../home/tela_home.php">Voltar</a></button>
        </div>
    </body>
</html>
<?php
    include("../login/verifica_login.php");
?>