
const submitButton = document.getElementById("next");
const input = document.getElementById("answer");
const radioButton = document.getElementById("radio1");

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

//Disables text-input before radiobutton
document.body.addEventListener('change', (e) => {
    
    const value = e.target;
    if(value.id === 'radio2'){ // om [NEJ] - disable input
        input.disabled = true;
        submitButton.disabled = false;
    } else {
        input.disabled =false;
    }
    
});

function submitForm(){
document.location.href="last.html";
}

function nextQuest(){
    document.location.href="/question2";
}
