const email = document.getElementById("email");
const username = document.getElementById("name");
const branch = document.getElementById("branch");


$(document).ready(function(){
   $("#livebox").on("input",function(e){
       $("#datalist").empty();
       $.ajax({
           method:"post",
           url:"/adminIndex",
           data:{text:$("#livebox").val()},
           success:function(res){
               var data = "<ul>";
               $.each(res,function(index,value){
                   data += "<li>" + value + "</li>";
               });
               data += "</ul>";
               $("#datalist").html(data);
           }
       });
   });
});


window.addEventListener('input', function(){  
     if(email.value != "" && username.value != "" && branch.value != 0){
        this.document.getElementById("addUser").disabled = false;
     }else{
        this.document.getElementById("addUser").disabled = true;
     }

})

window.addEventListener('input', function(){  
   if(email.value != ""){
      this.document.getElementById("removeUser").disabled = false;
   }else{
      this.document.getElementById("removeUser").disabled = true;
   }

})

