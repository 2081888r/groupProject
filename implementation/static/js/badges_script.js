num = 0;
original_visibility = "";
original_left = "";
original_top = "";
original_width = "";
original_height = "";
original_margin = "";
original_border = "";


function expand_badge(i){
    num = i;
    badge_div = document.getElementById("badge_div_"+i);
    expanded_badge_div = document.getElementById("expanded_badge_div_"+i);

    document.getElementById("grey_overlay_1").style.visibility = "visible";
    document.getElementById("grey_overlay_1").style.backgroundColor = "rgba(1, 1, 1, 0.8)";
    document.getElementById("grey_overlay_2").style.visibility = "visible";
    document.getElementById("grey_overlay_2").style.backgroundColor = "rgba(1, 1, 1, 0.8)";
    
    original_visibility = expanded_badge_div.style.visibility;
    original_left       = expanded_badge_div.style.left;
    original_top        = expanded_badge_div.style.top;
    original_width      = expanded_badge_div.style.width;
    original_height     = expanded_badge_div.style.height;
    original_margin     = expanded_badge_div.style.margin;
    original_border     = expanded_badge_div;
    
    badge_div.style.visibility = "hidden";
    
    expanded_badge_div.style.visibility = "visible";
    expanded_badge_div.style.left       = "50%";
    expanded_badge_div.style.top        = "28.6%";
    expanded_badge_div.style.width      = "404px";
    expanded_badge_div.style.height     = "204px";
    expanded_badge_div.style.margin     = "-102px 0px 0px -202px";
    expanded_badge_div.style.border     = "2px solid black";
}

function retract_badge(){
    badge_div = document.getElementById("badge_div_"+num);
    expanded_badge_div = document.getElementById("expanded_badge_div_"+num);

    document.getElementById("grey_overlay_1").style.backgroundColor = "rgba(1, 1, 1, 0)";
    document.getElementById("grey_overlay_2").style.backgroundColor = "rgba(1, 1, 1, 0)";
    
    expanded_badge_div.style.left       = original_left;
    expanded_badge_div.style.top        = original_top;
    expanded_badge_div.style.width      = original_width;
    expanded_badge_div.style.height     = original_height;
    expanded_badge_div.style.margin     = original_margin;
    expanded_badge_div.style.border     = original_border;
    
    window.setTimeout(function(){
                    expanded_badge_div.style.visibility = original_visibility;
                    badge_div.style.visibility = "visible";
                        document.getElementById("grey_overlay_1").style.visibility = "hidden";
                        document.getElementById("grey_overlay_2").style.visibility = "hidden";
                }, 400);
}