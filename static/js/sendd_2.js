async function sendd_2(){
    const chbox1 = document.getElementById('inlineCheckbox1').checked;
    const chbox2 = document.getElementById('inlineCheckbox2').checked;
    const chbox3 = document.getElementById('inlineCheckbox3').checked;
    const chbox4 = document.getElementById('inlineCheckbox4').checked;
    const chbox5 = document.getElementById('inlineCheckbox5').checked;
    const chbox6 = document.getElementById('inlineCheckbox6').checked;
    const chbox7 = document.getElementById('inlineCheckbox7').checked;
    const chbox8 = document.getElementById('inlineCheckbox8').checked;
    const chbox9 = document.getElementById('inlineCheckbox9').checked;
    const chbox10 = document.getElementById('inlineCheckbox10').checked;
    const chbox11 = document.getElementById('inlineCheckbox11').checked;
    const chbox12 = document.getElementById('inlineCheckbox12').checked;
    const chbox13 = document.getElementById('inlineCheckbox13').checked;
    const chbox14 = document.getElementById('inlineCheckbox14').checked;
    const chbox15 = document.getElementById('inlineCheckbox15').checked;
    const chbox16 = document.getElementById('inlineCheckbox16').checked;
    const chbox17 = document.getElementById('inlineCheckbox17').checked;

    const response = await fetch("/hello_2", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            chbox1: chbox1,
            chbox2: chbox2,
            chbox3: chbox3,
            chbox4: chbox4,
            chbox5: chbox5,
            chbox6: chbox6,
            chbox7: chbox7,
            chbox8: chbox8,
            chbox9: chbox9,
            chbox10: chbox10,
            chbox11: chbox11,
            chbox12: chbox12,
            chbox13: chbox13,
            chbox14: chbox14,
            chbox15: chbox15,
            chbox16: chbox16,
            chbox17: chbox17,
        })
    });
    if (response.ok) {
        const data_1 = await response.json();
        document.getElementById("number").value = data_1.number;
        document.getElementById("number1").value = data_1.number1;
        document.getElementById("number2").value = data_1.number2;
        document.getElementById("number3").value = data_1.number3;
        document.getElementById("number4").value = data_1.number4;
        document.getElementById("number5").value = data_1.number5;
        document.getElementById("number6").value = data_1.number6;
        document.getElementById("number7").value = data_1.number7;
        document.getElementById("number8").value = data_1.number8;
        document.getElementById("number9").value = data_1.number9;
        document.getElementById("number10").value = data_1.number10;
        document.getElementById("number11").value = data_1.number11;
        document.getElementById("number12").value = data_1.number12;
        document.getElementById("number13").value = data_1.number13;
    }
    else
        console.log(response);
}