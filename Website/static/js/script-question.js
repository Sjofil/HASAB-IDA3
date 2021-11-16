
const submitButton = document.getElementById("next");
const input = document.getElementById("answer");
const radioButton = document.getElementById("radio1");
const radioButton2 = document.getElementById("radio2");


change = false;


//disablar knappen tills man skrivit in något
console.log(input);

input.addEventListener('keyup', (e) => {
    console.log(e.currentTarget.value);

    const value = e.currentTarget.value;
    if(value === ""){
        submitButton.disabled = true;
    } else {
        submitButton.disabled=false;
    }
});

//Enables input "answer" and clears input "answer" after radiobutton change
document.body.addEventListener('change', (e) => {
    
   value = e.target;
    
    // if radio1 is pressed
    if(value.id === 'radio1'){
        input.disabled = false;
        if(change){
           submitButton.disabled = false;
        }else{
            submitButton.disabled = true;
        }
        change = true;
    }
    // if radio2 is pressed, disables 
    if(value.id === 'radio2'){ 
        input.disabled = true;
        submitButton.disabled = false;
        change = false;
        document.getElementById("answer").value = 5;
    } 
   
});

function submitForm(){
document.location.href="last.html";
}

function nextQuest(){
    var page = getRequestVariable("page");
    var pageNumber = parseInt(page);
    var totalPages = document.getElementById("totalPages").childElementCount;
    if(page != undefined && page != NaN) 
    {
        document.location.href="/question?page=" + (pageNumber + 1);
    }
    else
    {
        document.location.href="/question?page=2"
    }

}


    function getSelectedValue(){
        var selectedValue = document.getElementById("answer").value;
        console.log(selectedValue);
    }

