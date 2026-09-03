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
            <h2>CADASTRO DE USU&Aacute;RIO</h2>
        </div>
        <div class="form">
            <form action="/cadastro/grava_user.php" method="post">
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
                    <label for="status">
                        <p>Status</p>
                        <input type="text" id="status" name="status" class="input-form">
                    </label>
                </div>
                <div class="row">
                    <label for="cargo">
                        <p>Cargo</p>
                        <input type="text" id="cargo" name="cargo" class="input-form">
                    </label>
                    <label for="setor">
                        <p>Setor</p>
                        <input type="text" id="setor" name="setor" class="input-form">
                    </label>
                    <label for="dtAdmissao">
                        <p>Data de Admiss&atilde;o</p>
                        <input type="date" id="dtAdmissao" name="dtAdmissao" class="input-form">
                    </label>
                </div>
                <div class="row">
                    <label for="login">
                        <p>Login</p>
                        <input type="text" id="login" name="login" class="input-form">
                    </label>
                    <label for="senha">
                        <p>Senha</p>
                        <input type="password" id="senha" name="senha" class="input-form">
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