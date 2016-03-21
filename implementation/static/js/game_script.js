function left_panel_buttons_onclick(){
    if(is_left_panel_open()){
       open_left_panel();
    }
    else{
        close_left_panel();
    }
}

function left_panel_switch_to_party(){
    document.getElementById("");
}

function is_left_panel_open(){
    return window.getComputedStyle(document.getElementById("left_panel")).width == "0px";
}

function open_left_panel(){
    document.getElementById("left_panel").style.width = "200px";
    document.getElementById("left_panel_tag").style.left = "202px";
    document.getElementById("left_panel").style.left = "2px";
    
    window.setTimeout(function(){
        document.getElementById("left_panel_arrow_image").style.transform = "scale(-1, -1)";
    }, 750);
}
function close_left_panel(){
    document.getElementById("left_panel").style.width = "0px";
    document.getElementById("left_panel_tag").style.left = "0px";
    
    window.setTimeout(function(){
        document.getElementById("left_panel").style.left = "0px";
        document.getElementById("left_panel_arrow_image").style.transform = "scale(1, 1)";
    }, 750);
}

function submitAction(action, pos){
    var form = document.getElementById("submission_form");
    
    var action_field = document.createElement("input");
    action_field.setAttribute("type", "hidden");
    action_field.setAttribute("name", "action");
    action_field.setAttribute("value", action);
    
    form.appendChild(action_field);
    
    if(pos != ""){
        var pos_field = document.createElement("input");
        pos_field.setAttribute("type", "hidden");
        pos_field.setAttribute("name", "pos");
        pos_field.setAttribute("value", pos);
        form.appendChild(pos_field);
    }
    
    document.body.appendChild(form);
    document.body.appendChild(form);
    form.submit();
}