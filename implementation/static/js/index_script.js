function openLogInPopUp(){
    document.getElementById("log_in_pop_up").style.visibility = "visible";
    document.getElementById("grey_overlay").style.visibility = "visible";
    document.getElementById("log_in_pop_up").style.transform = "scale(1, 1)";
    document.getElementById("grey_overlay").style.backgroundColor = "rgba(1, 1, 1, 0.8)";
}

function closeLogInPopUp(){
    document.getElementById("log_in_pop_up").style.transform = "scale(0, 0)";
    document.getElementById("grey_overlay").style.backgroundColor = "rgba(1, 1, 1, 0)";
    
    window.setTimeout(function(){
        document.getElementById("grey_overlay").style.visibility = "hidden";
        document.getElementById("log_in_pop_up").style.visibility = "hidden";
    }, 400);
    
}