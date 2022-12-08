async function send(){
    
    // получаем введеное в поле имя и возраст
    const number = document.getElementById("number").value * 214;
    const number1 = document.getElementById("number1").value * 228;
    const number2 = document.getElementById("number2").value * 216;
    const number3 = document.getElementById("number3").value * 168;
    const number4 = document.getElementById("number4").value * 302;
    const number5 = document.getElementById("number5").value * 141;
    const number6 = document.getElementById("number6").value * 195;
    const number7 = document.getElementById("number7").value * 151;
    const number8 = document.getElementById("number8").value * 200;
    const number9 = document.getElementById("number9").value * 450;
    const number10 = document.getElementById("number10").value * 189;
    const number11 = document.getElementById("number11").value * 462;
    const number12 = document.getElementById("number12").value * 858;
    const number13 = document.getElementById("number13").value * 85;
    const number14 = Number(document.getElementById("number").value) + 
                     Number(document.getElementById("number1").value) +
                     Number(document.getElementById("number2").value) +
                     Number(document.getElementById("number3").value) +
                     Number(document.getElementById("number4").value) +
                     Number(document.getElementById("number5").value) +
                     Number(document.getElementById("number6").value) +
                     Number(document.getElementById("number7").value) +
                     Number(document.getElementById("number8").value) +
                     Number(document.getElementById("number9").value) +
                     Number(document.getElementById("number10").value) +
                     Number(document.getElementById("number11").value) +
                     Number(document.getElementById("number12").value) +
                     Number(document.getElementById("number13").value);
    const number15 = number + number1 + number2 + number3 + number3 + number4 + number5 + number6 + number7 + number8 + number9 + number10 + number11 + number12 + number13;

    // отправляем запрос
    const response_1 = await fetch("/hello", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            number: number,
            number1: number1,
            number2: number2,
            number3: number3,
            number4: number4,
            number5: number5,
            number6: number6,
            number7: number7,
            number8: number8,
            number9: number9,
            number10: number10,
            number11: number11,
            number12: number12,
            number13: number13,
            number14: number14,
            number15: number15,
        })
    });
    if (response_1.ok) {
        const data = await response_1.json();
        document.getElementById("message").textContent = data.message;
        document.getElementById("message1").textContent = data.message1;
        document.getElementById("message2").textContent = data.message2;
        document.getElementById("message3").textContent = data.message3;
        document.getElementById("message4").textContent = data.message4;
        document.getElementById("message5").textContent = data.message5;
        document.getElementById("message6").textContent = data.message6;
        document.getElementById("message7").textContent = data.message7;
        document.getElementById("message8").textContent = data.message8;
        document.getElementById("message9").textContent = data.message9;
        document.getElementById("message10").textContent = data.message10;
        document.getElementById("message11").textContent = data.message11;
        document.getElementById("message12").textContent = data.message12;
        document.getElementById("message13").textContent = data.message13;
        document.getElementById("message14").textContent = data.message14;
        document.getElementById("message15").textContent = data.message15;
    }
    else
        console.log(response_1);
}