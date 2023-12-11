function servicios(){
    let container1 = document.getElementById("inicio");
    let container2 = document.getElementById("servicios")
    let container3 = document.getElementById("ganancias")
    let container4 = document.getElementById('produccion')
    let bpr = document.getElementById('pro')
    let bga = document.getElementById("gan")
    let bsv = document.getElementById("sv")

    container1.style.display = "none";
    container2.style.display = "block";
    container3.style.display = "none";
    container4.style.display = "none";
    bsv.style.backgroundColor = "rgb(46, 46, 46)";
    bsv.style.borderRadius = "5px";
    bga.style.backgroundColor = ""
    bga.style.borderRadius = "5px";
    bpr.style.backgroundColor = "";
    bpr.style.borderRadius = "5px";
}
function ganancias(){
    let container1 = document.getElementById("inicio");
    let container2 = document.getElementById("servicios")
    let container3 = document.getElementById("ganancias")
    let container4 = document.getElementById('produccion')
    let bpr = document.getElementById('pro')
    let bga = document.getElementById("gan")
    let bsv = document.getElementById("sv")

    container1.style.display = "none";
    container2.style.display = "none";
    container3.style.display = "block"
    container4.style.display = "none";
    bsv.style.backgroundColor = "";
    bsv.style.borderRadius = "5px";
    bga.style.backgroundColor = "rgb(46, 46, 46)"
    bga.style.borderRadius = "5px";
    bpr.style.backgroundColor = "";
    bpr.style.borderRadius = "5px";
}
function produccion(){
    let container1 = document.getElementById("inicio");
    let container2 = document.getElementById("servicios")
    let container3 = document.getElementById("ganancias")
    let container4 = document.getElementById('produccion')
    let bpr = document.getElementById('pro')
    let bga = document.getElementById("gan")
    let bsv = document.getElementById("sv")

    container1.style.display = "none";
    container2.style.display = "none";
    container3.style.display = "none";
    container4.style.display = "block";
    bsv.style.backgroundColor = "";
    bsv.style.borderRadius = "5px";
    bga.style.backgroundColor = "";
    bga.style.borderRadius = "5px";
    bpr.style.backgroundColor = "rgb(46, 46, 46)"
    bpr.style.borderRadius = "5px";
}