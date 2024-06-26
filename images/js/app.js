const signUpButton = document.getElementById('signUp');
const logInButton = document.getElementById('logIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

logInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

function Validate(){
    var a = document.getElementById('pw1');
    var b = document.getElementById('pw2');

    if(a!=b){
        document.getElementById('validate').innerHTML("Password not Matched");
    }else{
        document.getElementById('validate').innerHTML("Successfuly Registered");
    }
}