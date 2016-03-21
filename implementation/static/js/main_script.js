function new_game(){
    var form = document.getElementById("submission_form");
    
    var action_field = document.createElement("input");
    action_field.setAttribute("type", "hidden");
    action_field.setAttribute("name", "is_new_game");
    action_field.setAttribute("value", "yes");
    
    form.appendChild(action_field);
    
    document.body.appendChild(form);
    document.body.appendChild(form);
    form.submit();
}