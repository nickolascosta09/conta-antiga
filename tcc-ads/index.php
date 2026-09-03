<html>
    <head>
        <title>Sistema de Gerenciamento de Clientes</title>
        <link rel="icon" type="image/png" sizes="16x16" href="/favicon.png">
        <link rel="stylesheet" type="text/css" href="/css/style-index.css">
    </head>
    <body>
        <div id="formLogin">
            <div id="form-index">
                <img src="/logo/SGC_logo_nova.png" id="logo-index">
                <div class="input-field">
                    <form action="login/logar.php" method="POST" id="form-label">
                        <label for="login" class="label">Login</label>
                        <div class="input">
                            <input type="text" id="login" name="login">
                        </div>
                        <label for="password" class="label">Senha</label>
                        <div class="input">
                            <input type="password" id="senha" name="senha">
                        </div>
                        <div id="btnLogin">
                            <input type="submit" value="Entrar" style="border-radius: 5px; background-color: #2c2c2c; color: #ffffff; border: none; width: 70px; height:30px; cursor:pointer;">
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <footer>
            <div id="rodape">
                <div class="copyright">
                    <p>Desenvolvido por Nickolas Markus da Silva Costa &#169;</p>
                    <button type="button" id="btn-github"><img id="github" src="/assets/github_11376339.png" alt="Logo Github"><a href="https://github.com/nikolau96" target="_blank"></a></button> <button type="button" id="btn-linkedin"><img id="linkedin" src="/assets/linkedin_3536505.png" alt="Logo Linkedin"><a href="https://www.linkedin.com/in/nickolas09" target="_blank"></a></button>
                </div>
            </div>
        </footer>
    </body>
</html>
<?php
    if(isset($_SESSION['nao_autenticado'])){
        echo "<p>Login ou senha inv&aacute;lido</p>";
    }
    unset($_SESSION['nao_autenticado']);
?>