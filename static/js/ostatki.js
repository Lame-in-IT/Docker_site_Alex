async function ostatkiTable_1() {
    const table_1 = document.getElementById('table_alex');
    table_1.remove();
}

async function ostatki() {
    const kategori = document.getElementById("Категория").value
    const market = document.getElementById("Маркетплейс").value
    const response = await fetch("/ostatki", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            kategori: kategori,
            market: market,
        })
    });
    if (response.ok) {
        const data = await response.json();
        document.getElementById("2").textContent = data.ostatki[0];
        document.getElementById("3").textContent = data.ostatki[1];
        document.getElementById("4").textContent = data.ostatki[2];
        document.getElementById("5").textContent = data.ostatki[3];
        document.getElementById("6").textContent = data.ostatki[4];
        document.getElementById("7").textContent = data.ostatki[5];
        document.getElementById("8").textContent = data.ostatki[6];
        document.getElementById("9").textContent = data.ostatki[7];
        document.getElementById("10").textContent = data.ostatki[8];
        document.getElementById("11").textContent = data.ostatki[9];
        document.getElementById("12").textContent = data.ostatki[10];
        document.getElementById("13").textContent = data.ostatki[11];
        document.getElementById("14").textContent = data.ostatki[12];
        document.getElementById("15").textContent = data.ostatki[13];
        document.getElementById("16").textContent = data.ostatki[14];
        document.getElementById("17").textContent = data.ostatki[15];
        document.getElementById("18").textContent = data.ostatki[16];
        document.getElementById("19").textContent = data.ostatki[17];
        document.getElementById("20").textContent = data.ostatki[18];
        document.getElementById("21").textContent = data.ostatki[19];
        document.getElementById("22").textContent = data.ostatki[20];
        document.getElementById("24").textContent = data.ostatki1[0];
        document.getElementById("25").textContent = data.ostatki1[1];
        document.getElementById("26").textContent = data.ostatki1[2];
        document.getElementById("27").textContent = data.ostatki1[3];
        document.getElementById("28").textContent = data.ostatki1[4];
        document.getElementById("29").textContent = data.ostatki1[5];
        document.getElementById("30").textContent = data.ostatki1[6];
        document.getElementById("31").textContent = data.ostatki1[7];
        document.getElementById("32").textContent = data.ostatki1[8];
        document.getElementById("33").textContent = data.ostatki1[9];
        document.getElementById("34").textContent = data.ostatki1[10];
        document.getElementById("35").textContent = data.ostatki1[11];
        document.getElementById("36").textContent = data.ostatki1[12];
        document.getElementById("37").textContent = data.ostatki1[13];
        document.getElementById("38").textContent = data.ostatki1[14];
        document.getElementById("39").textContent = data.ostatki1[15];
        document.getElementById("40").textContent = data.ostatki1[16];
        document.getElementById("41").textContent = data.ostatki1[17];
        document.getElementById("42").textContent = data.ostatki1[18];
        document.getElementById("43").textContent = data.ostatki1[19];
        document.getElementById("44").textContent = data.ostatki1[20];
        document.getElementById("45").textContent = data.ostatki2[0];
        document.getElementById("46").textContent = data.ostatki2[1];
        document.getElementById("47").textContent = data.ostatki2[2];
        document.getElementById("48").textContent = data.ostatki2[3];
        document.getElementById("49").textContent = data.ostatki2[4];
        document.getElementById("50").textContent = data.ostatki2[5];
        document.getElementById("51").textContent = data.ostatki2[6];
        document.getElementById("52").textContent = data.ostatki2[7];
        document.getElementById("53").textContent = data.ostatki2[8];
        document.getElementById("54").textContent = data.ostatki2[9];
        document.getElementById("55").textContent = data.ostatki2[10];
        document.getElementById("56").textContent = data.ostatki2[11];
        document.getElementById("57").textContent = data.ostatki2[12];
        document.getElementById("58").textContent = data.ostatki2[13];
        document.getElementById("59").textContent = data.ostatki2[14];
        document.getElementById("60").textContent = data.ostatki2[15];
        document.getElementById("61").textContent = data.ostatki2[16];
        document.getElementById("62").textContent = data.ostatki2[17];
        document.getElementById("63").textContent = data.ostatki2[18];
        document.getElementById("64").textContent = data.ostatki2[19];
        document.getElementById("65").textContent = data.ostatki2[20];
        document.getElementById("1").textContent = data.ostatki3;
        document.getElementById("23").textContent = data.ostatki4;
    }
}

async function ostatkiTable() {
    const kategori = document.getElementById("Категория").value
    const market = document.getElementById("Маркетплейс").value
    var table = document.createElement('table');
    const response_4 = await fetch("/ostatkiTable", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            kategori: kategori,
            market: market,
        })
    });
    if (response_4.ok) {
        const data = await response_4.json();
        for (var i = 0; i < data.ostatki11; i++) {
            var tr = document.createElement('tr');
            for (var j = 0; j < 6; j++) {
                var td = document.createElement('td');
                if (j == 0) {
                    var text1 = document.createTextNode(data.ostatki5[i]);
                    td.appendChild(text1);
                }
                if (j == 1) {
                    var text1 = document.createTextNode(data.ostatki6[i]);
                    td.appendChild(text1);
                }
                if (j == 2) {
                    var text1 = document.createTextNode(data.ostatki7[i]);
                    td.appendChild(text1);
                }
                if (j == 3) {
                    var text1 = document.createTextNode(data.ostatki8[i]);
                    td.appendChild(text1);
                }
                if (j == 4) {
                    var text1 = document.createTextNode(data.ostatki9[i]);
                    td.appendChild(text1);
                }
                if (j == 5) {
                    var text1 = document.createTextNode(data.ostatki10[i]);
                    td.appendChild(text1);
                }
                tr.appendChild(td);
            }
            table.appendChild(tr);
        }
        document.querySelector('#table_alex').appendChild(table);
    }
}