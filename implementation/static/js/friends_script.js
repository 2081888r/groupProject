
friend_divs = document.getElementsByClassName("friend_div");

for(var i = 0; i < friend_divs.length; i++){
    row = Math.floor(i/4);
    friend_divs[i].style.top = (((2/7)+row*(3/7))*100)+"%";
}