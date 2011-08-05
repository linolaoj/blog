

function change_color(comp_id){
$(comp_id).css("background","#eeeeee");
}

function change_back(comp_id){
$(comp_id).css("background","#ffffff");
}

function delete_post(post_key,post_id){
var res = confirm("delete "+post_key);
if(res == true){

var xmlhttp;
xmlhttp=new XMLHttpRequest();
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    var resposta =xmlhttp.responseText;
	if(resposta == 'done'){
	$("div#"+post_id).slideToggle("slow");
	$("hr#sep_"+post_id).hide();
    }
	}
  }
xmlhttp.open("POST","/post/delete",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("post_key="+post_key);
  }
}