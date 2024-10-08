//--------------------------------------------------------------------------------------
const    { countWords, setupPointsSummation }    = require('../_static/survey_functions.js');




//--------------------------------------------------------------------------------------
// Test countWords

test('countWords returns the correct number of words in a string', () => {
    expect(countWords('Hello, world!')).toBe(2);
});

//--------------------------------------------------------------------------------------
// Test setupPointsSummation

// Mock DOM elements
document.body.innerHTML = `
    <input type="number" name="field1" value="0">
    <input type="number" name="field2" value="0">
    <span id="total-points">0</span>
`;

test('setupPointsSummation sums values from two fields correctly', () => {
    // Setup
    const formfieldNames = ['field1', 'field2'];
    const totalElementId = 'total-points';
    
    // Call the function
    setupPointsSummation(formfieldNames, totalElementId);
    
    // Get references to the elements
    const field1 = document.getElementsByName('field1')[0];
    const field2 = document.getElementsByName('field2')[0];
    const totalElement = document.getElementById(totalElementId);
    
    // Initial state
    expect(totalElement.textContent).toBe('0');
    
    // Change values
    field1.value = '30';
    field1.dispatchEvent(new Event('input'));
    expect(totalElement.textContent).toBe('30');
    
    field2.value = '70';
    field2.dispatchEvent(new Event('input'));
    expect(totalElement.textContent).toBe('100');
    
    // Change again
    field1.value = '45';
    field1.dispatchEvent(new Event('input'));
    expect(totalElement.textContent).toBe('115');
});






