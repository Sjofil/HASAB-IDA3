const email = document.getElementById("email");
const username = document.getElementById("name");
const branch = document.getElementById("branch");

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