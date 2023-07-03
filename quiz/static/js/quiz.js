const quizContainer = document.querySelector(".main_test");
const myQuestions = document.querySelectorAll(".test1");
const submitButton = document.querySelector("#quiz-submit");
const answerContainers = quizContainer.querySelectorAll(".quiz-answers");
const answerData = [];
const apiDomen = 'https://quizdeploy-production.up.railway.app'
let sum;

function checkAnswer() {
    for (let i = 0; i < myQuestions.length; i++) {
        answerData[i] = (answerContainers[i].querySelector(`input[name=question${i}]:checked`) || {}).value;
    }

    if (!answerData.includes(undefined)) {
        try {
            sum = sumNumbersFromArray(answerData);
            return true
        } catch (error) {
            return false
        }
    }

    return false
}


function sumNumbersFromArray(arr) {
    let sum = 0;

    for (let i = 0; i < arr.length; i++) {
        const element = arr[i];

        if (typeof element === 'number') {
            sum += element;
        } else if (typeof element === 'string' && !isNaN(Number(element))) {
            sum += Number(element);
        } else {
            throw new Error('Error!');
        }
    }

    return sum;
}

submitButton.onclick = function () {
    if (checkAnswer()) {
        let options = {
            method: 'POST',
            mode: 'same-origin',
            headers: {'X-CSRFToken': csrftoken},
        }

        // add request body
        let formData = new FormData();
        formData.append('quizId', String(quizId));
        formData.append('power', String(sum));
        options['body'] = formData;
        const url = `${apiDomen}/create-result/`;

        // send HTTP request
        fetch(url, options)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                if (data['status'] === 'ok') {
                    window.location.href = `${apiDomen}/result/${data['code']}`;
                }
            })
    }
};
