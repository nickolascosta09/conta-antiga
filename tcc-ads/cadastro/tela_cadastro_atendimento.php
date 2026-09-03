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
            <h2>CADASTRO DE ATENDIMENTO</h2>
        </div>
        <div class="form">
            <form action="/cadastro/grava_atendimento.php" method="post">
                <div class="row">
                    <label for="dtAtendimento">
                        <p>Data de Atendimento</p>
                        <input type="date" id="dtAtendimento" name="dtAtendimento" class="input-form">
                    </label>
                    <label for="cliente">
                        <p>Cliente</p>
                        <input type="text" id="cliente" name="cliente" class="input-form">
                    </label>
                    <label for="vendedor">
                        <p>Vendedor</p>
                        <input type="text" id="vendedor" name="vendedor" class="input-form">
                    </label>
                    <label for="usuario">
                        <p>Usu&aacute;rio que cadastrou</p>
                        <input type="text" id="usuario" name="usuario" class="input-form">
                    </label>
                </div>
                <div class="row">
                    <label for="produto">
                        <p>Produto/Servi&ccedil;o</p>
                        <input type="text" id="produto" name="produto" class="input-form">
                    </label>
                    <label for="assunto">
                        <p>Assunto</p>
                        <input type="text" id="assunto" name="assunto" class="input-form">
                    </label>
                </div>
                <div class="row">
                    <label for="descricao">
                        <p>Descri&ccedil;&atilde;o</p>
                        <input type="text" id="descricao" name="descricao" class="input-form">
                    </label>
                </div>
                <div class="row">
                    <label for="solucao">
                        <p>Solu&ccedil;&atilde;o</p>
                        <input type="text" id="solucao" name="solucao" class="input-form">
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