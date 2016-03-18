currently_open_pop_up = "";

function openLogInPopUp(){
    document.getElementById("log_in_pop_up").style.visibility = "visible";
    document.getElementById("grey_overlay").style.visibility = "visible";
    document.getElementById("log_in_pop_up").style.transform = "scale(1, 1)";
    document.getElementById("grey_overlay").style.backgroundColor = "rgba(1, 1, 1, 0.8)";
    
    currently_open_pop_up = "log_in"
}

function closeLogInPopUp(){
    document.getElementById("log_in_pop_up").style.transform = "scale(0, 0)";
    document.getElementById("grey_overlay").style.backgroundColor = "rgba(1, 1, 1, 0)";
    
    window.setTimeout(function(){
        document.getElementById("grey_overlay").style.visibility = "hidden";
        document.getElementById("log_in_pop_up").style.visibility = "hidden";
    }, 400);
    
    currently_open_pop_up = "";
}

function switchToRegisterPopUp(){
    closeLogInPopUp();
    window.setTimeout(openRegisterPopUp, 400);
}

function openRegisterPopUp(){
    document.getElementById("register_pop_up").style.visibility = "visible";
    document.getElementById("grey_overlay").style.visibility = "visible";
    document.getElementById("register_pop_up").style.transform = "scale(1, 1)";
    document.getElementById("grey_overlay").style.backgroundColor = "rgba(1, 1, 1, 0.8)";
    
    currently_open_pop_up = "register";
}

function closeRegisterPopUp(){
    document.getElementById("register_pop_up").style.transform = "scale(0, 0)";
    document.getElementById("grey_overlay").style.backgroundColor = "rgba(1, 1, 1, 0)";
    
    window.setTimeout(function(){
        document.getElementById("grey_overlay").style.visibility = "hidden";
        document.getElementById("register_pop_up").style.visibility = "hidden";
    }, 400);
    
    currently_open_pop_up = "";
}

function closePopUp(){
    if(currently_open_pop_up == "log_in"){
        closeLogInPopUp();
    }
    if(currently_open_pop_up == "register"){
        closeRegisterPopUp();
    }
}