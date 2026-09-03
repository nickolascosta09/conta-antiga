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
            <h2>CADASTRO DE CLIENTE</h2>
        </div>
        <div class="form">
            <form action="/cadastro/grava_cliente.php" method="post">
                <div class="row">
                    <label for="nome">
                        <p>Nome</p>
                        <input type="text" id="nome" name="nome" class="input-form">
                    </label>
                    <label for="cpf">
                        <p>CPF</p>
                        <input type="text" id="cpf" name="cpf" class="input-form">
                    </label>
                    <label for="rg">
                        <p>RG</p>
                        <input type="text" id="rg" name="rg" class="input-form">
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
                    <label for="email">
                        <p>Email</p>
                        <input type="text" id="email" name="email" class="input-form">
                    </label>
                </div>
                <div class="row">
                    <label for="cep">
                        <p>CEP</p>
                        <input type="text" id="cep" name="cep" class="input-form">
                    </label>
                    <label for="logradouro">
                        <p>Logradouro</p>
                        <input type="text" id="logradouro" name="logradouro" class="input-form">
                    </label>
                    <label for="endNum">
                        <p>N&uacute;mero</p>
                        <input type="text" id="endNum" name="endNum" class="input-form">
                    </label>
                    <label for="complemento">
                        <p>Complemento</p>
                        <input type="text" id="complemento" name="complemento" class="input-form">
                    </label>
                    <label for="bairro">
                        <p>Bairro</p>
                        <input type="text" id="bairro" name="bairro" class="input-form">
                    </label>
                    <label for="cidade">
                        <p>Cidade</p>
                        <input type="text" id="cidade" name="cidade" class="input-form">
                    </label>
                    <label for="uf">
                        <p>UF</p>
                        <input type="text" id="uf" name="uf" class="input-form">
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