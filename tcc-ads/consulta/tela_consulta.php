<html>
    <head>
        <title>Sistema de Gerenciamento de Clientes</title>
        <link rel="icon" type="image/png" sizes="16x16" href="../favicon.png">
        <link rel="stylesheet" type="text/css" href="../css/style-consulta.css">
    </head>
    <body>
        <header class="cabecalho">
            <img src="../favicon.png" alt="Logo do Sistema" class="imgsys">
            <div id="linha"></div>
        </header>
        <div class="title">
            <h2>CONSULTA</h2>
        </div>
        <div class="tela-body">
            <div>
                <label class="subtitle">O que deseja consultar?</label>
            </div>
            <div class="container">
                <span class="container-block" id="container-atendimento">
                    <img src="../assets/atendee_icon.png">
                    <br><br><br>
                    <a href="/consulta/tela_atendimento.php">Atendimento</a>
                </span>
                <span class="container-block" id="container-vendedor">
                    <img src="../assets/seller_icon.png">
                    <br><br><br>
                    <a href="/consulta/tela_vendedor.php">Vendedor</a>
                </span>
                <span class="container-block" id="container-cliente">
                    <img src="../assets/customer_icon.png">    
                    <br><br><br>
                    <a href="/consulta/tela_cliente.php">Cliente</a>
                </span>
            </div>
        </div>
        <div>
            <button type="button" id="btn-voltar"><a href="../home/tela_home.php">Voltar</a></button>
        </div>
    </body>
</html>
<?php
    include("../login/verifica_login.php");
?>