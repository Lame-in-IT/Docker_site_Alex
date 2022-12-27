async function zakaz(){
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
    const chbox18 = document.getElementById('inlineCheckbox18').checked;

    const response = await fetch("/zakaz", {
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
            chbox18: chbox18,
        })
    });
    if (response.ok) {
        const data = await response.json();
        document.getElementById("1").textContent = data.number[0];
        document.getElementById("2").textContent = data.number[1];
        document.getElementById("3").textContent = data.number[2];
        document.getElementById("4").textContent = data.number[3];
        document.getElementById("5").textContent = data.number[4];
        document.getElementById("6").textContent = data.number[5];
        document.getElementById("7").textContent = data.number[6];
        document.getElementById("8").textContent = data.number[7];
        document.getElementById("9").textContent = data.number[8];
        document.getElementById("10").textContent = data.number[9];
        document.getElementById("11").textContent = data.number[10];
        document.getElementById("12").textContent = data.number[11];
        document.getElementById("13").textContent = data.number[12];
        document.getElementById("14").textContent = data.number[13];
        document.getElementById("15").textContent = data.number[14];
        document.getElementById("16").textContent = data.number[15];
        document.getElementById("17").textContent = data.number[16];
        document.getElementById("18").textContent = data.number[17];
        document.getElementById("19").textContent = data.number[18];
        document.getElementById("20").textContent = data.number[19];
        document.getElementById("21").textContent = data.number[20];
        document.getElementById("22").textContent = data.number[21];
        document.getElementById("23").textContent = data.number[22];
        document.getElementById("24").textContent = data.number[23];
        document.getElementById("25").textContent = data.number[24];
        document.getElementById("26").textContent = data.number[25];
        document.getElementById("27").textContent = data.number[26];
        document.getElementById("28").textContent = data.number[27];
        document.getElementById("29").textContent = data.number[28];
        document.getElementById("30").textContent = data.number[29];
        document.getElementById("31").textContent = data.number[30];
        document.getElementById("32").textContent = data.number[31];
        document.getElementById("33").textContent = data.number[32];
        document.getElementById("34").textContent = data.number[33];
        document.getElementById("35").textContent = data.number[34];
        document.getElementById("36").textContent = data.number[35];
        document.getElementById("37").textContent = data.number[36];
        document.getElementById("38").textContent = data.number[37];
        document.getElementById("39").textContent = data.number[38];
        document.getElementById("40").textContent = data.number[39];
        document.getElementById("41").textContent = data.number[40];
        document.getElementById("42").textContent = data.number[41];
        document.getElementById("43").textContent = data.number[42];
        document.getElementById("44").textContent = data.number[43];
        document.getElementById("45").textContent = data.number[44];
        document.getElementById("46").textContent = data.number[45];
        document.getElementById("47").textContent = data.number[46];
        document.getElementById("48").textContent = data.number[47];
        document.getElementById("49").textContent = data.number[48];
        document.getElementById("50").textContent = data.number[49];
        document.getElementById("51").textContent = data.number[50];
        document.getElementById("52").textContent = data.number[51];
        document.getElementById("53").textContent = data.number[52];
        document.getElementById("54").textContent = data.number[53];
        document.getElementById("55").textContent = data.number[54];
        document.getElementById("56").textContent = data.number[55];
        document.getElementById("57").textContent = data.number[56];
        document.getElementById("58").textContent = data.number[57];
        document.getElementById("59").textContent = data.number[58];
        document.getElementById("60").textContent = data.number[59];
        // document.getElementById("61").textContent = data.number[60];
        // document.getElementById("62").textContent = data.number[61];
        // document.getElementById("63").textContent = data.number[62];
        // document.getElementById("64").textContent = data.number[63];
        // document.getElementById("65").textContent = data.number[64];
        // document.getElementById("66").textContent = data.number[65];
        // document.getElementById("67").textContent = data.number[66];
        // document.getElementById("68").textContent = data.number[67];
        // document.getElementById("69").textContent = data.number[68];
        // document.getElementById("70").textContent = data.number[69];
        // document.getElementById("71").textContent = data.number[70];
        // document.getElementById("72").textContent = data.number[71];
        // document.getElementById("73").textContent = data.number[72];
        // document.getElementById("74").textContent = data.number[73];
        // document.getElementById("75").textContent = data.number[74];
        // document.getElementById("76").textContent = data.number[75];
        // document.getElementById("77").textContent = data.number[76];
        // document.getElementById("78").textContent = data.number[77];
        // document.getElementById("79").textContent = data.number[78];
        // document.getElementById("80").textContent = data.number[79];
        // document.getElementById("81").textContent = data.number[80];
        // document.getElementById("82").textContent = data.number[81];
        // document.getElementById("83").textContent = data.number[82];
        // document.getElementById("84").textContent = data.number[83];
        // document.getElementById("85").textContent = data.number[84];
        document.getElementById("101").textContent = data.number1[0];
        document.getElementById("102").textContent = data.number1[1];
        document.getElementById("103").textContent = data.number1[2];
        document.getElementById("104").textContent = data.number1[3];
        document.getElementById("105").textContent = data.number1[4];
        document.getElementById("106").textContent = data.number1[5];
        document.getElementById("107").textContent = data.number1[6];
        document.getElementById("108").textContent = data.number1[7];
        document.getElementById("109").textContent = data.number1[8];
        document.getElementById("110").textContent = data.number1[9];
        document.getElementById("111").textContent = data.number1[10];
        document.getElementById("112").textContent = data.number1[11];
        document.getElementById("113").textContent = data.number1[12];
        document.getElementById("114").textContent = data.number1[13];
        document.getElementById("115").textContent = data.number1[14];
        document.getElementById("116").textContent = data.number1[15];
        document.getElementById("117").textContent = data.number1[16];
        document.getElementById("118").textContent = data.number1[17];
        document.getElementById("119").textContent = data.number1[18];
        document.getElementById("120").textContent = data.number1[19];
        document.getElementById("121").textContent = data.number1[20];
        document.getElementById("122").textContent = data.number1[21];
        document.getElementById("123").textContent = data.number1[22];
        document.getElementById("124").textContent = data.number1[23];
        document.getElementById("125").textContent = data.number1[24];
        document.getElementById("126").textContent = data.number1[25];
        document.getElementById("127").textContent = data.number1[26];
        document.getElementById("128").textContent = data.number1[27];
        document.getElementById("129").textContent = data.number1[28];
        document.getElementById("130").textContent = data.number1[29];
        document.getElementById("131").textContent = data.number1[30];
        document.getElementById("132").textContent = data.number1[31];
        document.getElementById("133").textContent = data.number1[32];
        document.getElementById("134").textContent = data.number1[33];
        document.getElementById("135").textContent = data.number1[34];
        document.getElementById("136").textContent = data.number1[35];
        document.getElementById("137").textContent = data.number1[36];
        document.getElementById("138").textContent = data.number1[37];
        document.getElementById("139").textContent = data.number1[38];
        document.getElementById("140").textContent = data.number1[39];
        document.getElementById("141").textContent = data.number1[40];
        document.getElementById("142").textContent = data.number1[41];
        document.getElementById("143").textContent = data.number1[42];
        document.getElementById("144").textContent = data.number1[43];
        document.getElementById("145").textContent = data.number1[44];
        document.getElementById("146").textContent = data.number1[45];
        document.getElementById("147").textContent = data.number1[46];
        document.getElementById("148").textContent = data.number1[47];
        document.getElementById("149").textContent = data.number1[48];
        document.getElementById("150").textContent = data.number1[49];
        document.getElementById("151").textContent = data.number1[50];
        document.getElementById("152").textContent = data.number1[51];
        document.getElementById("153").textContent = data.number1[52];
        document.getElementById("154").textContent = data.number1[53];
        document.getElementById("155").textContent = data.number1[54];
        document.getElementById("156").textContent = data.number1[55];
        document.getElementById("157").textContent = data.number1[56];
        document.getElementById("158").textContent = data.number1[57];
        document.getElementById("159").textContent = data.number1[58];
        document.getElementById("160").textContent = data.number1[59];
        document.getElementById("201").textContent = data.number2[0];
        document.getElementById("202").textContent = data.number2[1];
        document.getElementById("203").textContent = data.number2[2];
        document.getElementById("204").textContent = data.number2[3];
        document.getElementById("205").textContent = data.number2[4];
        document.getElementById("206").textContent = data.number2[5];
        document.getElementById("207").textContent = data.number2[6];
        document.getElementById("208").textContent = data.number2[7];
        document.getElementById("209").textContent = data.number2[8];
        document.getElementById("210").textContent = data.number2[9];
        document.getElementById("211").textContent = data.number2[10];
        document.getElementById("212").textContent = data.number2[11];
        document.getElementById("213").textContent = data.number2[12];
        document.getElementById("214").textContent = data.number2[13];
        document.getElementById("215").textContent = data.number2[14];
        document.getElementById("216").textContent = data.number2[15];
        document.getElementById("217").textContent = data.number2[16];
        document.getElementById("218").textContent = data.number2[17];
        document.getElementById("219").textContent = data.number2[18];
        document.getElementById("220").textContent = data.number2[19];
        document.getElementById("221").textContent = data.number2[20];
        document.getElementById("222").textContent = data.number2[21];
        document.getElementById("223").textContent = data.number2[22];
        document.getElementById("224").textContent = data.number2[23];
        document.getElementById("225").textContent = data.number2[24];
        document.getElementById("226").textContent = data.number2[25];
        document.getElementById("227").textContent = data.number2[26];
        document.getElementById("228").textContent = data.number2[27];
        document.getElementById("229").textContent = data.number2[28];
        document.getElementById("230").textContent = data.number2[29];
        document.getElementById("231").textContent = data.number2[30];
        document.getElementById("232").textContent = data.number2[31];
        document.getElementById("233").textContent = data.number2[32];
        document.getElementById("234").textContent = data.number2[33];
        document.getElementById("235").textContent = data.number2[34];
        document.getElementById("236").textContent = data.number2[35];
        document.getElementById("237").textContent = data.number2[36];
        document.getElementById("238").textContent = data.number2[37];
        document.getElementById("239").textContent = data.number2[38];
        document.getElementById("240").textContent = data.number2[39];
        document.getElementById("241").textContent = data.number2[40];
        document.getElementById("242").textContent = data.number2[41];
        document.getElementById("243").textContent = data.number2[42];
        document.getElementById("244").textContent = data.number2[43];
        document.getElementById("245").textContent = data.number2[44];
        document.getElementById("246").textContent = data.number2[45];
        document.getElementById("247").textContent = data.number2[46];
        document.getElementById("248").textContent = data.number2[47];
        document.getElementById("249").textContent = data.number2[48];
        document.getElementById("250").textContent = data.number2[49];
        document.getElementById("251").textContent = data.number2[50];
        document.getElementById("252").textContent = data.number2[51];
        document.getElementById("253").textContent = data.number2[52];
        document.getElementById("254").textContent = data.number2[53];
        document.getElementById("255").textContent = data.number2[54];
        document.getElementById("256").textContent = data.number2[55];
        document.getElementById("257").textContent = data.number2[56];
        document.getElementById("258").textContent = data.number2[57];
        document.getElementById("259").textContent = data.number2[58];
        document.getElementById("260").textContent = data.number2[59];
    }
}