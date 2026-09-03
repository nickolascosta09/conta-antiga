<html>
    <head>
        <title>Sistema de Gerenciamento de Clientes</title>
        <link rel="icon" type="image/png" sizes="16x16" href="../logo/SGC_logo_nova.png">
    </head>
    <body>
        <?php
            include("../db/database.php");
            $SQL = "SELECT * FROM usuario";
            $registro = mysqli_query($conexao, $SQL);
            $qtdRegistro = mysqli_num_rows($registro);
            echo "<table border = 1 style='text-align:center;margin-top:50px;margin-left:530px';>";
            echo "  <tr>";
            echo "      <td>Nome</td>";
            echo "      <td>Login</td>";
            echo "      <td>Status</td>";
            echo "  </tr>";
            if($qtdRegistro == 0){
                echo "  <tr>";
                echo "      <td>Nenhum registro encontrado</td>";
                echo "  </tr>";
            }
            while($linha = mysqli_fetch_array($registro)){
                echo "  <tr>";
                echo "      <td>" . $linha['nome'] . "</td>";
                echo "      <td>" . $linha['login'] . "</td>";
                echo "      <td>" . $linha['status'] . "</td>";
                echo "  </tr>";
            }
            echo "</table>";
            print_r($linha);
            echo "<button style='margin-top:180px;margin-left:600px;border-radius:5px;border:none;width:100px;height:30px;background-color:#2c2c2c;cursor:pointer;'><a href='../home/tela_home.php' style='color:white;text-decoration:none;'>Voltar</a></button>";
        ?>
    </body>
</html>
<?php
    include("../login/verifica_login.php");
?>