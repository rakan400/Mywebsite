var k = 0;
var j = 0;
var i = 0;
function one(){
    var a = "one()";
    var b = 0/1;
    var c = 5.7 - 1;
    var d = 11 % 3;
    var e = 'hello my name is "rakan"';
    var f = e.length;
    var g = e[0] + e[2] +e[6];
    var h = ['rakan',23,2,[1,3,4],2];
    
    document.getElementById("demo").innerHTML = a;
    document.getElementById("demo1").innerHTML = b;
    document.getElementById("demo2").innerHTML = c;
    document.getElementById("demo3").innerHTML = d;
    document.getElementById("demo4").innerHTML = e;
    document.getElementById("demo5").innerHTML = f;
    document.getElementById("demo6").innerHTML = g;
    document.getElementById("demo7").innerHTML = h;
    document.getElementById("demo8").innerHTML = i;
    document.getElementById("demo9").innerHTML = j;
    document.getElementById("demo10").innerHTML = k;
}

function addk(){
    k = k+1;
    document.getElementById("demo10").innerHTML = k;
}
function subtractk(){
    k = k-1;
    document.getElementById("demo10").innerHTML = k;
}
function addj(){
    j = j+1;
    document.getElementById("demo9").innerHTML = j;
}
function subtractj(){
    j = j-1;
    document.getElementById("demo9").innerHTML = j;
}
function equals(){
    i = j + k;
    document.getElementById("demo8").innerHTML = i;
}