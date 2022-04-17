var first=document.querySelector(".heading-1");
first.addEventListener('click',login);
var second=document.querySelector(".heading-2");
second.addEventListener('click',signup);

function signup(){
    console.log("clicked second");
    document.querySelector(".signup-1").classList.remove("hidden");
    document.querySelector(".login-1").classList.add("hidden");
    document.querySelector(".heading-1").classList.remove("color");
    document.querySelector(".heading-2").classList.add("color");
}

function login(){
    console.log("clicked first")
    document.querySelector(".signup-1").classList.add("hidden");
    document.querySelector(".login-1").classList.remove("hidden");
    document.querySelector(".heading-1").classList.add("color");
    document.querySelector(".heading-2").classList.remove("color");
}
