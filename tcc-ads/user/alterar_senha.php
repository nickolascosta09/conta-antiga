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
            <h2>ALTERAR SENHA</h2>
        </div>
        <div class="form">
            <form action="/user/mudar_senha.php" method="post">
                <div class="row">    
                    <label for="senhaAntiga">
                        <p>Senha antiga</p>
                        <input type="password" id="senhaAntiga" name="senhaAntiga" class="input-form">
                    </label>
                    <label for="senhaNova">
                        <p>Nova Senha</p>
                        <input type="password" id="senhaNova" name="senhaNova" class="input-form">
                    </label>
                    <label for="confirmaSenha">
                        <p>Confirmar senha</p>
                        <input type="password" id="confirmaSenha" name="confirmaSenha" class="input-form">
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