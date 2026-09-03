<html>
    <head>
        <title>Sistema de Gerenciamento de Clientes</title>
        <link rel="icon" type="image/png" sizes="16x16" href="../favicon.png">
        <link rel="stylesheet" type="text/css" href="../css/style-home.css">
    </head>
    <body>
        <header class="cabecalho">
            <img src="../logo/SGC_logo_nova.png" alt="Logo do Sistema" class="imgsys">
            <div id="linha"></div>
        </header>
        <div id="menuLateral" class="menuLateral">
            <nav class="menu">
                <div id="icon">
                    <div>
                        <button id="btnClose" onclick="fechaMenu();">X</button>
                    </div>
                    <div>
                        <img src="../logo/SGC_logo_nova.png" alt="Logo do Sistema" class="img-menu">
                    </div>
                    <div>
                        <p class="texto-menu">Ol&aacute;, Seja bem-vindo!</p>
                    </div>
                </div>
                <div class="lista-nav">
                    <ul>
                        <li class="item-lista"><a href="../login/user_list.php" style="color:black; text-decoration:none; margin-left: 10px;">Lista de usu&aacute;rios</a></li>
                        <li class="item-lista"><a href="../user/alterar_senha.php" style="color:black; text-decoration:none; margin-left: 10px;">Alterar senha</a></li>
                        <li class="item-lista"><a href="../user/alterar_status.php" style="color:black; text-decoration:none; margin-left: 10px;">Alterar status</a></li>
                    </ul>
                </div>
                <div class="logout">
                    <button type="button" id="btn-logout"><a href="../login/logout.php" style="color:white; text-decoration:none; padding-right:8px;">Sair</a><img src="../assets/sign-out-option.png" style="height:10px; width:10px; background-color:white;"></button>
                </div>
            </nav>
        </div>
        <div id="tela-body" class="tela-body">
            <div id="mostrar-menu">
                <span style="font-size:30px; cursor:pointer;">
                    <button type="button" id="btn-menu" onclick="mostraMenu();"><img class="btn-logo-menu" src="../assets/bars-solid.png"></button>
                </span>
            </div>
            <div class="tela-container">
                <span id="cadastro-container">
                    <img src="../assets/register_icon.png">
                    <br><br><br>
                    <a href="../cadastro/tela_cadastro_principal.php">Cadastro</a>
                </span>
                <span id="consulta-container">
                    <img src="../assets/search_icon.png">
                    <br><br><br>
                    <a href="../consulta/tela_consulta.php">Consulta</a>
                </span>
            </div>
        </div>
    </body>
    <script src="../js/menu_lateral.js"></script>
</html>
<?php
    include('../login/verifica_login.php');
?>