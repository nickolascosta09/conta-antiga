<html>
    <head>
        <title>Sistema de Gerenciamento de Clientes</title>
        <link rel="icon" type="image/png" sizes="16x16" href="../favicon.png">
        <link rel="stylesheet" type="text/css" href="../css/style-form.css">
    </head>
    <body>
        <header class="cabecalho">
            <img src="../logo/SGC_logo_nova.png" alt="Logo do Sistema" class="imgsys">
            <div id="linha"></div>
        </header>
        <div class="title">
            <h2>ALTERAR STATUS</h2>
        </div>
        <div class="form">
            <form action="/user/mudar_status.php" method="post">
                <div class="row">
                    <label for="user">
                        <p>Digite o usu&aacute;rio</p>
                        <input type="text" id="user" name="user" class="input-form">
                    </label>
                    <label for="status">
                        <p>Digite o status</p>
                        <input type="text" id="status" name="status" class="input-form">
                    </label>
                </div>
                <div>
                    <button type="button"><a href="../home/tela_home.php">Voltar</a></button>
                    <input type="submit" value="Gravar" class="btn-form-yes">
                </div>
            </form>
        </div>
    </body>
</html>
<?php
    include("../login/verifica_login.php");
?>