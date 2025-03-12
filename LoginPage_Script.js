function togglePassword() {
    let eyeicon = document.getElementById("eyeicon");
    let Password = document.getElementById("Password");

    eyeicon.onclick = function(){
        if(Password.type == "password"){
            Password.type = "text";
            eyeicon.src = "Images/eye-open.png"
        }
        else{
            Password.type = "password";
            eyeicon.src = "Images/eye-close.png"
        }
    }
}

function ConfirmPasswordToggle() {
    let eyeicon = document.getElementById("eyeicon_password");
    let Confirm_Password = document.getElementById("Confirm_Password");

    eyeicon.onclick = function(){
        if(Confirm_Password.type == "password"){
            Confirm_Password.type = "text";
            eyeicon.src = "Images/eye-open.png"
        }
        else{
            Confirm_Password.type = "password";
            eyeicon.src = "Images/eye-close.png"
        }
    }
}
