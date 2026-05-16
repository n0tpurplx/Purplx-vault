let display = document.getElementById('display');
let expression = '';

function appendNumber(num) {
    expression += num;
    updateDisplay();
}

function appendOperator(op) {
    if (expression && !expression.endsWith('+') && !expression.endsWith('-') && 
        !expression.endsWith('*') && !expression.endsWith('/')) {
        expression += op;
        updateDisplay();
    }
}

function deleteLast() {
    expression = expression.slice(0, -1);
    updateDisplay();
}

function clearDisplay() {
    expression = '';
    updateDisplay();
}

function calculate() {
    try {
        if (expression) {
            expression = eval(expression).toString();
            updateDisplay();
        }
    } catch (error) {
        display.value = 'Error';
        expression = '';
    }
}

function updateDisplay() {
    display.value = expression || '0';
}

// Initialize display
updateDisplay();

// Keyboard support
document.addEventListener('keydown', (e) => {
    if (e.key >= '0' && e.key <= '9') appendNumber(e.key);
    if (e.key === '.') appendNumber('.');
    if (e.key === '+') appendOperator('+');
    if (e.key === '-') appendOperator('-');
    if (e.key === '*') appendOperator('*');
    if (e.key === '/') {
        e.preventDefault();
        appendOperator('/');
    }
    if (e.key === 'Enter' || e.key === '=') {
        e.preventDefault();
        calculate();
    }
    if (e.key === 'Backspace') deleteLast();
    if (e.key === 'Escape') clearDisplay();
});