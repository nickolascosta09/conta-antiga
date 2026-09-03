<html>
    <head>
        <title>Sistema de Gerenciamento de Clientes</title>
        <link rel="icon" type="image/png" sizes="16x16" href="../logo/SGC_logo_nova.png">
    </head>
</html>
<?php
    include("../db/database.php");
    //$nome_filtro = filter_input(INPUT_POST, 'nome');
    $SQL = "SELECT * FROM vendedor";
    $registro = mysqli_query($conexao, $SQL);
    $qtdRegistro = mysqli_num_rows($registro);
    if($qtdRegistro == 0){
        echo "<p>Nenhum registro encontrado</p>";
        return;
    }
    echo "<table border = 1>";
    echo "  <tr>";
    echo "      <td>Código</td>";
    echo "      <td>Nome</td>";
    echo "      <td>CPF</td>";
    echo "      <td>Sexo</td>";
    echo "      <td>Data de Nascimento</td>";
    echo "      <td>Telefone</td>";
    echo "      <td>Celular</td>";
    echo "      <td>Email</td>";
    echo "      <td>Conselho</td>";
    echo "      <td>N&uacute;mero do Conselho</td>";
    echo "  </tr>";
    while($linha = mysqli_fetch_array($registro)){
        echo "<tr>";
        echo "<td>" . $linha['id'] . "</td>";
        echo "<td>" . $linha['nome'] . "</td>";
        echo "<td>" . $linha['cpf'] . "</td>";
        echo "<td>" . $linha['sexo'] . "</td>";
        $data_banco = $linha['dt_nascimento'];
        $data_tratamento = DateTime::createFromFormat('Y-m-d', $data_banco);
        $data_tela = $data_tratamento ? $data_tratamento->format('d/m/Y') : 'Data Inválida';
        echo "<td>" . $data_tela . "</td>";
        echo "<td>" . $linha['telefone'] . "</td>";
        echo "<td>" . $linha['celular'] . "</td>";
        echo "<td>" . $linha['email'] . "</td>";
        echo "<td>" . $linha['conselho'] . "</td>";
        echo "<td>" . $linha['nr_conselho'] . "</td>";
        echo "</tr>";
    }
    echo "</table>";
    print_r($linha);
    echo "<button style='margin-top:180px;margin-left:600px;border-radius:5px;border:none;width:100px;height:30px;background-color:#2c2c2c;cursor:pointer;'><a href='../home/tela_home.php' style='color:white;text-decoration:none;'>Voltar</a></button>";
?>