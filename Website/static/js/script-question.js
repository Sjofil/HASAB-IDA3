
const submitButton = document.getElementById("next");
const input = document.getElementById("answer");
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

document.body.addEventListener('change', (e) => {
    const radioButton = document.getElementById("radio1");
    const value = e.target;
    if(value.id === 'radio2'){
        input.disabled = true;
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

console.log(555555);