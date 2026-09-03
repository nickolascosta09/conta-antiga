function mostraMenu(){
    document.getElementById("menuLateral").style.width = "250px";
    document.getElementById("tela-body").classList.add("empurrar");
}

function fechaMenu(){
    document.getElementById("menuLateral").style.width = "0";
    document.getElementById("tela-body").classList.remove("empurrar");
}
