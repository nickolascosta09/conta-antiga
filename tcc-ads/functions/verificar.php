<?php
    function verificaCliente($nome_cliente, $cpf_cliente){
        include("../db/database.php");
        $select_verifica = "SELECT * FROM cliente WHERE nome = '{$nome_cliente}' AND cpf = '{$cpf_cliente}'";
        $resultado = mysqli_query($conexao, $select_verifica);
        $linha = mysqli_num_rows($resultado);
        if(1 == $linha){
            return true;
        }else{
            return false;
        }   
    }

    function verificaVendedor($nome_vendedor, $cpf_vendedor){
        include("../db/database.php");
        $select_verifica = "SELECT * FROM vendedor WHERE nome = '{$nome_vendedor}' AND cpf = '{$cpf_vendedor}'";
        $resultado = mysqli_query($conexao, $select_verifica);
        $linha = mysqli_num_rows($resultado);
        if(1 == $linha){
            return true;
        }else{
            return false;
        }
    }

    function verificaStatus($usuario_login){
        include("../db/database.php");
        $verifica_status = "SELECT * FROM usuario WHERE `login` = '{$usuario_login}' AND `status`= 'Inativo'";
        $resultado = mysqli_query($conexao, $verifica_status);
        $linha = mysqli_num_rows($resultado);
        if(1 == $linha){
            return true;
        }else{
            return false;
        }
    }
?>