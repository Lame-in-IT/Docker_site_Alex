async function createTable_1() {
    const table_1 = document.querySelector('table');
    table_1.remove();
}

async function ABC_analiz() {
    const analiz = document.getElementById("Mouth_1").value
    const response_5 = await fetch("/ABC_analiz", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            analiz: analiz,
        })
    });
    if (response_5.ok) {
        const data = await response_5.json();
        myChart_22.data.labels = data.message1;
        myChart_22.data.datasets[0].data = data.message;
        myChart_22.update()
        document.getElementById("1").textContent = data.message1[0];
        document.getElementById("2").textContent = data.message1[1];
        document.getElementById("3").textContent = data.message1[2];
        document.getElementById("4").textContent = data.message1[3];
        document.getElementById("5").textContent = data.message1[4];
        document.getElementById("6").textContent = data.message1[5];
        document.getElementById("7").textContent = data.message1[6];
        document.getElementById("8").textContent = data.message1[7];
        document.getElementById("9").textContent = data.message1[8];
        document.getElementById("10").textContent = data.message1[9];
        document.getElementById("11").textContent = data.message1[10];
        document.getElementById("12").textContent = data.message1[11];
        document.getElementById("13").textContent = data.message1[12];
        document.getElementById("14").textContent = data.message1[13];
        document.getElementById("15").textContent = data.message1[14];
        document.getElementById("16").textContent = data.message1[15];
        document.getElementById("17").textContent = data.message1[16];
        document.getElementById("18").textContent = data.message1[17];
        document.getElementById("19").textContent = data.message1[18];
        document.getElementById("20").textContent = data.message1[19];
        document.getElementById("21").textContent = data.message1[20];
        document.getElementById("22").textContent = data.message1[21];
        document.getElementById("23").textContent = data.message3[0];
        document.getElementById("24").textContent = data.message3[1];
        document.getElementById("25").textContent = data.message3[2];
        document.getElementById("26").textContent = data.message3[3];
        document.getElementById("27").textContent = data.message3[4];
        document.getElementById("28").textContent = data.message3[5];
        document.getElementById("29").textContent = data.message3[6];
        document.getElementById("30").textContent = data.message3[7];
        document.getElementById("31").textContent = data.message3[8];
        document.getElementById("32").textContent = data.message3[9];
        document.getElementById("33").textContent = data.message3[10];
        document.getElementById("34").textContent = data.message3[11];
        document.getElementById("35").textContent = data.message3[12];
        document.getElementById("36").textContent = data.message3[13];
        document.getElementById("37").textContent = data.message3[14];
        document.getElementById("38").textContent = data.message3[15];
        document.getElementById("39").textContent = data.message3[16];
        document.getElementById("40").textContent = data.message3[17];
        document.getElementById("41").textContent = data.message3[18];
        document.getElementById("42").textContent = data.message3[19];
        document.getElementById("43").textContent = data.message3[20];
        document.getElementById("44").textContent = data.message3[21];
        document.getElementById("45").textContent = data.message4[0];
        document.getElementById("46").textContent = data.message4[1];
        document.getElementById("47").textContent = data.message4[2];
        document.getElementById("48").textContent = data.message4[3];
        document.getElementById("49").textContent = data.message4[4];
        document.getElementById("50").textContent = data.message4[5];
        document.getElementById("51").textContent = data.message4[6];
        document.getElementById("52").textContent = data.message4[7];
        document.getElementById("53").textContent = data.message4[8];
        document.getElementById("54").textContent = data.message4[9];
        document.getElementById("55").textContent = data.message4[10];
        document.getElementById("56").textContent = data.message4[11];
        document.getElementById("57").textContent = data.message4[12];
        document.getElementById("58").textContent = data.message4[13];
        document.getElementById("59").textContent = data.message4[14];
        document.getElementById("60").textContent = data.message4[15];
        document.getElementById("61").textContent = data.message4[16];
        document.getElementById("62").textContent = data.message4[17];
        document.getElementById("63").textContent = data.message4[18];
        document.getElementById("64").textContent = data.message4[19];
        document.getElementById("65").textContent = data.message4[20];
        document.getElementById("66").textContent = data.message4[21];
        document.getElementById("67").textContent = data.message5[0];
        document.getElementById("68").textContent = data.message5[1];
        document.getElementById("69").textContent = data.message5[2];
        document.getElementById("70").textContent = data.message5[3];
        document.getElementById("71").textContent = data.message5[4];
        document.getElementById("72").textContent = data.message5[5];
        document.getElementById("73").textContent = data.message5[6];
        document.getElementById("74").textContent = data.message5[7];
        document.getElementById("75").textContent = data.message5[8];
        document.getElementById("76").textContent = data.message5[9];
        document.getElementById("77").textContent = data.message5[10];
        document.getElementById("78").textContent = data.message5[11];
        document.getElementById("79").textContent = data.message5[12];
        document.getElementById("80").textContent = data.message5[13];
        document.getElementById("81").textContent = data.message5[14];
        document.getElementById("82").textContent = data.message5[15];
        document.getElementById("83").textContent = data.message5[16];
        document.getElementById("84").textContent = data.message5[17];
        document.getElementById("85").textContent = data.message5[18];
        document.getElementById("86").textContent = data.message5[19];
        document.getElementById("87").textContent = data.message5[20];
        document.getElementById("88").textContent = data.message5[21];
    }
}

async function createTable() {
    const analiz1 = document.getElementById("Маркетплейс").value
    const analiz2 = document.getElementById("airdatepicer").value
    var table = document.createElement('table');
    const response_4 = await fetch("/createTable", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            analiz1: analiz1,
            analiz2: analiz2,
        })
    });
    if (response_4.ok) {
        const data = await response_4.json();
        for (var i = 0; i < data.message6; i++) {
            var tr = document.createElement('tr');
            for (var j = 0; j < data.message1; j++) {
                var td = document.createElement('td');
                if (i == 0) {
                    var text1 = document.createTextNode(data.message[j]);
                    td.appendChild(text1);
                }
                else if (i == 1) {
                    var text2 = document.createTextNode(data.message2[j]);
                    td.appendChild(text2);
                }
                else if (i == 2) {
                    var text3 = document.createTextNode(data.message3[j]);
                    td.appendChild(text3);
                }
                else if (i == 3) {
                    var text4 = document.createTextNode(data.message4[j]);
                    td.appendChild(text4);
                }
                else if (i == 4) {
                    var text5 = document.createTextNode(data.message5[j]);
                    td.appendChild(text5);
                }
                tr.appendChild(td);
            }
            table.appendChild(tr);
        }
        document.querySelector('#table_alex').appendChild(table);
    }
}

const data = {
    labels: ['Бутылка', 'Бутылка 1 литр', 'Кошелек',
        'Лампа с датчиком', 'Магнит', 'Овощечистка нерж',
        'Овощечистка пластик', 'Планшет 8,5',
        'Планшет 10', 'Планшет 12',
        'Полотенце', 'Шейкер 4 цвета', 'Шейкер черный'],
    datasets: [{
        label: 'Прибыль категорий по выручке (руб.)',
        data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        backgroundColor: [
            'rgba(255, 99, 132, 0.5)',
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(153, 102, 255, 0.5)',
            'rgba(255, 159, 64, 0.5)',
        ],
        borderColor: [
            'rgba(255, 99, 132, 0.5)',
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(153, 102, 255, 0.5)',
            'rgba(255, 159, 64, 0.5)',
        ],
        borderWidth: 1
    }]
};

const config = {
    type: 'bar',
    data,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

const myChart_22 = new Chart(
    document.getElementById('myChart_22'),
    config,
    );

// var table = document.createElement('table');
// for (var i = 1; i < 4; i++){
//     var tr = document.createElement('tr');

//     var td1 = document.createElement('td');
//     var td2 = document.createElement('td');

//     var text1 = document.createTextNode('Text1');
//     var text2 = document.createTextNode('Text2');

//     td1.appendChild(text1);
//     td2.appendChild(text2);
//     tr.appendChild(td1);
//     tr.appendChild(td2);

//     table.appendChild(tr);
// }
// document.body.appendChild(table);