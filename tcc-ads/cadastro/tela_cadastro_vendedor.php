<html>
    <head>
        <title>Sistema de Gerenciamento de Clientes</title>
        <link rel="icon" type="image/png" sizes="16x16" href="../favicon.png">
        <link rel="stylesheet" type="text/css" href="../css/style-form.css">
    </head>
    <body>
        <header class="cabecalho">
            <img src="../logo/SGC_logo_nova.png" alt="Logo do Sistema">
            <div id="linha"></div>
        </header>
        <div class="title">
            <h2>Cadastro de Vendedor</h2>
        </div>
        <div class="form">
            <form action="/cadastro/grava_vendedor.php" method="post">
                <div class="row">
                    <label for="nome">
                        <p>Nome</p>
                        <input type="text" id="nome" name="nome" class="input-form">
                    </label>
                    <label for="cpf">
                        <p>CPF</p>
                        <input type="text" id="cpf" name="cpf" class="input-form">
                    </label>
                    <label for="sexo">
                        <p>Sexo</p>
                        <input type="text" id="sexo" name="sexo" class="input-form">
                    </label>
                </div>
                <div class="row">
                    <label for="dtNascimento">
                        <p>Data de Nascimento</p>
                        <input type="date" id="dtNascimento" name="dtNascimento" class="input-form">
                    </label>
                    <label for="telefone">
                        <p>Telefone</p>
                        <input type="text" id="telefone" name="telefone" class="input-form">
                    </label>
                    <label for="celular">
                        <p>Celular</p>
                        <input type="text" id="celular" name="celular" class="input-form">
                    </label>
                </div>
                <div class="row">
                    <label for="email">
                        <p>Email</p>
                        <input type="text" id="email" name="email" class="input-form">
                    </label>
                    <label for="conselho">
                        <p>Conselho</p>
                        <input type="text" id="conselho" name="conselho" class="input-form">
                    </label>
                    <label for="numConselho">
                        <p>N&uacute;mero</p>
                        <input type="text" id="numConselho" name="numConselho" class="input-form">
                    </label>
                </div>
                <div>
                    <button type="button"><a href="../home/tela_home.php">Cancelar</a></button>
                    <input type="reset" value="Limpar" class="btn-form-no">
                    <input type="submit" value="Gravar" class="btn-form-yes">
                </div>
            </form>
        </div>
    </body>
</html>
<?php
    include("../login/verifica_login.php");
?>