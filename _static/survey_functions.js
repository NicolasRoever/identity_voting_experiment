function updateElementColorByValue(elementId, targetValueForGreen) {
    console.log("updateElementColorByValue is run");
    const element = document.getElementById(elementId);
    const currentValue = parseInt(element.textContent);  // Get the current value and convert to a number

    // Change the color based on the target value
    if (currentValue === targetValueForGreen) {
        element.style.color = 'green';
    } else {
        element.style.color = 'red';
    }
}



// Function to count words in the textarea
function countWords(text) {
    const words = text.trim().split(/\s+/).filter(function(word) {
        return word.length > 0;
    });
    return words.length;
}

// Function to update the HTML with the word count
function updateWordCount(element_id, count) {
    document.getElementById(element_id).innerText = count + " Wörter.";
}


// Function to handle the input and call the other two functions
function triggerWordCountUpdate(textInputField, wordCountOutput) {
    const text = document.getElementById(textInputField).value;
    const wordCount = countWords(text);
    updateWordCount(wordCountOutput, wordCount);
}

function setupPointsSummation(formfieldNames, totalElementId) {
    console.log("setupPointsSummation is run");
    function updateTotalPoints() {
        console.log("updateTotalPoints is run");
        let total = 0;
        formfieldNames.forEach(name => {
            const fields = document.getElementsByName(name);
            if (fields.length > 0) {
                const field = fields[0];
                const value = parseFloat(field.value) || 0;
                total += value;
            }
        });
        document.getElementById(totalElementId).textContent = total;
    }

    formfieldNames.forEach(name => {
        const fields = document.getElementsByName(name);
        if (fields.length > 0) {
            const field = fields[0];
            field.addEventListener('input', updateTotalPoints);
            field.addEventListener('input', () => {console.log("Calling updateElementColorByValue");updateElementColorByValue(totalElementId, 100)});
        }
    });

    // Initialize total points on page load
    updateTotalPoints();
}


function sendTextInputToServer(formfieldName){
    var input = document.getElementById(formfieldName).value;
   liveSend({formfieldName, input});
}



module.exports = {  countWords, setupPointsSummation } ; // Export the function for testing