const display = document.getElementById('display');

window.onload = () => display.focus();

function insertChar(char) {
    const pos = display.selectionStart;
    const text = display.value;
    
    display.value = text.slice(0, pos) + char + text.slice(display.selectionEnd);
    
    const newPos = pos + char.length;
    display.setSelectionRange(newPos, newPos);
    display.focus();
}

function insertParentheses() {
    const pos = display.selectionStart;
    const text = display.value;
    
    display.value = text.slice(0, pos) + "()" + text.slice(display.selectionEnd);
    
    const newPos = pos + 1;
    display.setSelectionRange(newPos, newPos);
    display.focus();
}

function clearDisplay() {
    display.value = "";
    display.focus();
}

function deleteLast() {
    const pos = display.selectionStart;
    const text = display.value;
    
    if (pos > 0) {
        display.value = text.slice(0, pos - 1) + text.slice(pos);
        display.setSelectionRange(pos - 1, pos - 1);
    }
    display.focus();
}

function calculate() {
    try {
        let expression = display.value.replace(/,/g, '.');
        
        let result = eval(expression);
        
        if (result === Infinity || isNaN(result)) {
            display.value = "Erro";
        } else {
            let finalResult = Number.isInteger(result) ? 
                result.toString() : 
                parseFloat(result.toFixed(8)).toString();
            
            display.value = finalResult.replace(/\./g, ',');
        }
    } catch (e) {
        display.value = "Erro";
    }
    display.focus();
}