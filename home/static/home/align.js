
function setEqualHeight(){
	var x = document.getElementsByClassName("toalign");
	var i;
	for (i = 0; i < x.length; i++) {
	    var a = (x[i].clientWidth);
	    x[i].style.height = (a)+"px";
	}
	
}
    


setEqualHeight();
window.onresize = setEqualHeight;