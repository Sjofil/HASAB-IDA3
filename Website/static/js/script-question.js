
const submitButton = document.getElementById("next");
const input = document.getElementById("answer");
const radioButton = document.getElementById("radio1");
const radioButton2 = document.getElementById("radio2");
const totalPages = document.getElementById("totalPages").childElementCount;


change = false;

window.addEventListener('load', function() {
    var page = getRequestVariable("page");
    var pageNumber = parseInt(page);
    if(pageNumber > 1){
          document.getElementById("back").disabled=false; 
    }else {
        document.getElementById("back").disabled=true;
    }
  
  })

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
    if(page != undefined && page != NaN) 
    {
        if(totalPages > pageNumber){
            
            let answers = JSON.parse(getCookie("answers"));
            answers[pageNumber] = $('form').serialize();
            setCookie("answers", JSON.stringify(answers), 1);
            document.location.href="/question?page=" + (pageNumber + 1);
        }
        else if(totalPages == pageNumber) {
            console.log(getCookie("answers"));
            document.location.href="/send-form";
        }
    }
    else
    {
        document.location.href="/question?page=2";
        let answers = [];
        answers[0] = $('form').serialize();
        setCookie("answers", JSON.stringify(answers), 1);
    }

}

function sendCookie(){
    let answers = getCookie("answers");
    console.log(answers)
    $.ajax({
        url: "/send-form",
        type: 'POST',
        contentType: "application/json",
        data : answers,
    });
}

function prevQuest(){
    var page = getRequestVariable("page");
    var pageNumber = parseInt(page);
    if(page != undefined && page != NaN) 
    {
        if(pageNumber > 1){
            document.location.href="/question?page=" + (pageNumber - 1);
        }
        
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

