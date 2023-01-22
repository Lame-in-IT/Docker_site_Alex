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
        document.getElementById("101").value = data.number1[0];
        document.getElementById("102").value = data.number1[1];
        document.getElementById("103").value = data.number1[2];
        document.getElementById("104").value = data.number1[3];
        document.getElementById("105").value = data.number1[4];
        document.getElementById("106").value = data.number1[5];
        document.getElementById("107").value = data.number1[6];
        document.getElementById("108").value = data.number1[7];
        document.getElementById("109").value = data.number1[8];
        document.getElementById("110").value = data.number1[9];
        document.getElementById("111").value = data.number1[10];
        document.getElementById("112").value = data.number1[11];
        document.getElementById("113").value = data.number1[12];
        document.getElementById("114").value = data.number1[13];
        document.getElementById("115").value = data.number1[14];
        document.getElementById("116").value = data.number1[15];
        document.getElementById("117").value = data.number1[16];
        document.getElementById("118").value = data.number1[17];
        document.getElementById("119").value = data.number1[18];
        document.getElementById("120").value = data.number1[19];
        document.getElementById("121").value = data.number1[20];
        document.getElementById("122").value = data.number1[21];
        document.getElementById("123").value = data.number1[22];
        document.getElementById("124").value = data.number1[23];
        document.getElementById("125").value = data.number1[24];
        document.getElementById("126").value = data.number1[25];
        document.getElementById("127").value = data.number1[26];
        document.getElementById("128").value = data.number1[27];
        document.getElementById("129").value = data.number1[28];
        document.getElementById("130").value = data.number1[29];
        document.getElementById("131").value = data.number1[30];
        document.getElementById("132").value = data.number1[31];
        document.getElementById("133").value = data.number1[32];
        document.getElementById("134").value = data.number1[33];
        document.getElementById("135").value = data.number1[34];
        document.getElementById("136").value = data.number1[35];
        document.getElementById("137").value = data.number1[36];
        document.getElementById("138").value = data.number1[37];
        document.getElementById("139").value = data.number1[38];
        document.getElementById("140").value = data.number1[39];
        document.getElementById("141").value = data.number1[40];
        document.getElementById("142").value = data.number1[41];
        document.getElementById("143").value = data.number1[42];
        document.getElementById("144").value = data.number1[43];
        document.getElementById("145").value = data.number1[44];
        document.getElementById("146").value = data.number1[45];
        document.getElementById("147").value = data.number1[46];
        document.getElementById("148").value = data.number1[47];
        document.getElementById("149").value = data.number1[48];
        document.getElementById("150").value = data.number1[49];
        document.getElementById("151").value = data.number1[50];
        document.getElementById("152").value = data.number1[51];
        document.getElementById("153").value = data.number1[52];
        document.getElementById("154").value = data.number1[53];
        document.getElementById("155").value = data.number1[54];
        document.getElementById("156").value = data.number1[55];
        document.getElementById("157").value = data.number1[56];
        document.getElementById("158").value = data.number1[57];
        document.getElementById("159").value = data.number1[58];
        document.getElementById("160").value = data.number1[59];
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

async function zakaz_1() {
    const zakaz_sht = document.getElementById("101").value;
    const zakaz_sht1 = document.getElementById("102").value;
    const zakaz_sht2 = document.getElementById("103").value;
    const zakaz_sht3 = document.getElementById("104").value;
    const zakaz_sht4 = document.getElementById("105").value;
    const zakaz_sht5 = document.getElementById("106").value;
    const zakaz_sht6 = document.getElementById("107").value;
    const zakaz_sht7 = document.getElementById("108").value;
    const zakaz_sht8 = document.getElementById("109").value;
    const zakaz_sht9 = document.getElementById("110").value;
    const zakaz_sht10 = document.getElementById("111").value;
    const zakaz_sht11 = document.getElementById("112").value;
    const zakaz_sht12 = document.getElementById("113").value;
    const zakaz_sht13 = document.getElementById("114").value;
    const zakaz_sht14 = document.getElementById("115").value;
    const zakaz_sht15 = document.getElementById("116").value;
    const zakaz_sht16 = document.getElementById("117").value;
    const zakaz_sht17 = document.getElementById("118").value;
    const zakaz_sht18 = document.getElementById("119").value;
    const zakaz_sht19 = document.getElementById("120").value;
    const zakaz_sht20 = document.getElementById("121").value;
    const zakaz_sht21 = document.getElementById("122").value;
    const zakaz_sht22 = document.getElementById("123").value;
    const zakaz_sht23 = document.getElementById("124").value;
    const zakaz_sht24 = document.getElementById("125").value;
    const zakaz_sht25 = document.getElementById("126").value;
    const zakaz_sht26 = document.getElementById("127").value;
    const zakaz_sht27 = document.getElementById("128").value;
    const zakaz_sht28 = document.getElementById("129").value;
    const zakaz_sht29 = document.getElementById("130").value;
    const zakaz_sht30 = document.getElementById("131").value;
    const zakaz_sht31 = document.getElementById("132").value;
    const zakaz_sht32 = document.getElementById("133").value;
    const zakaz_sht33 = document.getElementById("134").value;
    const zakaz_sht34 = document.getElementById("135").value;
    const zakaz_sht35 = document.getElementById("136").value;
    const zakaz_sht36 = document.getElementById("137").value;
    const zakaz_sht37 = document.getElementById("138").value;
    const zakaz_sht38 = document.getElementById("139").value;
    const zakaz_sht39 = document.getElementById("140").value;
    const zakaz_sht40 = document.getElementById("141").value;
    const zakaz_sht41 = document.getElementById("142").value;
    const zakaz_sht42 = document.getElementById("143").value;
    const zakaz_sht43 = document.getElementById("144").value;
    const zakaz_sht44 = document.getElementById("145").value;
    const zakaz_sht45 = document.getElementById("146").value;
    const zakaz_sht46 = document.getElementById("147").value;
    const zakaz_sht47 = document.getElementById("148").value;
    const zakaz_sht48 = document.getElementById("149").value;
    const zakaz_sht49 = document.getElementById("150").value;
    const zakaz_sht50 = document.getElementById("151").value;
    const zakaz_sht51 = document.getElementById("152").value;
    const zakaz_sht52 = document.getElementById("153").value;
    const zakaz_sht53 = document.getElementById("154").value;
    const zakaz_sht54 = document.getElementById("155").value;
    const zakaz_sht55 = document.getElementById("156").value;
    const zakaz_sht56 = document.getElementById("157").value;
    const zakaz_sht57 = document.getElementById("158").value;
    const zakaz_sht58 = document.getElementById("159").value;
    const zakaz_sht59 = document.getElementById("160").value;
    const zakaz_sht60 = document.getElementById("1").textContent;
    const zakaz_sht61 = document.getElementById("2").textContent;
    const zakaz_sht62 = document.getElementById("3").textContent;
    const zakaz_sht63 = document.getElementById("4").textContent;
    const zakaz_sht64 = document.getElementById("5").textContent;
    const zakaz_sht65 = document.getElementById("6").textContent;
    const zakaz_sht66 = document.getElementById("7").textContent;
    const zakaz_sht67 = document.getElementById("8").textContent;
    const zakaz_sht68 = document.getElementById("9").textContent;
    const zakaz_sht69 = document.getElementById("10").textContent;
    const zakaz_sht70 = document.getElementById("11").textContent;
    const zakaz_sht71 = document.getElementById("12").textContent;
    const zakaz_sht72 = document.getElementById("13").textContent;
    const zakaz_sht73 = document.getElementById("14").textContent;
    const zakaz_sht74 = document.getElementById("15").textContent;
    const zakaz_sht75 = document.getElementById("16").textContent;
    const zakaz_sht76 = document.getElementById("17").textContent;
    const zakaz_sht77 = document.getElementById("18").textContent;
    const zakaz_sht78 = document.getElementById("19").textContent;
    const zakaz_sht79 = document.getElementById("20").textContent;
    const zakaz_sht80 = document.getElementById("21").textContent;
    const zakaz_sht81 = document.getElementById("22").textContent;
    const zakaz_sht82 = document.getElementById("23").textContent;
    const zakaz_sht83 = document.getElementById("24").textContent;
    const zakaz_sht84 = document.getElementById("25").textContent;
    const zakaz_sht85 = document.getElementById("26").textContent;
    const zakaz_sht86 = document.getElementById("27").textContent;
    const zakaz_sht87 = document.getElementById("28").textContent;
    const zakaz_sht88 = document.getElementById("29").textContent;
    const zakaz_sht89 = document.getElementById("30").textContent;
    const zakaz_sht90 = document.getElementById("31").textContent;
    const zakaz_sht91 = document.getElementById("32").textContent;
    const zakaz_sht92 = document.getElementById("33").textContent;
    const zakaz_sht93 = document.getElementById("34").textContent;
    const zakaz_sht94 = document.getElementById("35").textContent;
    const zakaz_sht95 = document.getElementById("36").textContent;
    const zakaz_sht96 = document.getElementById("37").textContent;
    const zakaz_sht97 = document.getElementById("38").textContent;
    const zakaz_sht98 = document.getElementById("39").textContent;
    const zakaz_sht99 = document.getElementById("30").textContent;
    const zakaz_sht100 = document.getElementById("41").textContent;
    const zakaz_sht101 = document.getElementById("42").textContent;
    const zakaz_sht102 = document.getElementById("43").textContent;
    const zakaz_sht103 = document.getElementById("44").textContent;
    const zakaz_sht104 = document.getElementById("45").textContent;
    const zakaz_sht105 = document.getElementById("46").textContent;
    const zakaz_sht106 = document.getElementById("47").textContent;
    const zakaz_sht107 = document.getElementById("48").textContent;
    const zakaz_sht108 = document.getElementById("49").textContent;
    const zakaz_sht109 = document.getElementById("50").textContent;
    const zakaz_sht110 = document.getElementById("51").textContent;
    const zakaz_sht111 = document.getElementById("52").textContent;
    const zakaz_sht112 = document.getElementById("53").textContent;
    const zakaz_sht113 = document.getElementById("54").textContent;
    const zakaz_sht114 = document.getElementById("55").textContent;
    const zakaz_sht115 = document.getElementById("56").textContent;
    const zakaz_sht116 = document.getElementById("57").textContent;
    const zakaz_sht117 = document.getElementById("58").textContent;
    const zakaz_sht118 = document.getElementById("59").textContent;
    const zakaz_sht119 = document.getElementById("60").textContent;
    const zakaz_sht120 = document.getElementById('inlineCheckbox16').checked;
    const zakaz_sht121 = document.getElementById('inlineCheckbox17').checked;
    const zakaz_sht122 = document.getElementById('inlineCheckbox18').checked;
    

    const response_1 = await fetch("/zakaz_1", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            zakaz_sht: [zakaz_sht, zakaz_sht1, zakaz_sht2, zakaz_sht3, zakaz_sht4, zakaz_sht5,
                        zakaz_sht6, zakaz_sht7, zakaz_sht8, zakaz_sht9, zakaz_sht10,
                        zakaz_sht11, zakaz_sht12, zakaz_sht13, zakaz_sht14, zakaz_sht15,
                        zakaz_sht16, zakaz_sht17, zakaz_sht18, zakaz_sht19, zakaz_sht20,
                        zakaz_sht21, zakaz_sht22, zakaz_sht23, zakaz_sht24, zakaz_sht25,
                        zakaz_sht26, zakaz_sht27, zakaz_sht28, zakaz_sht29, zakaz_sht30,
                        zakaz_sht31, zakaz_sht32, zakaz_sht33, zakaz_sht34, zakaz_sht35,
                        zakaz_sht36, zakaz_sht37, zakaz_sht38, zakaz_sht39, zakaz_sht40,
                        zakaz_sht41, zakaz_sht42, zakaz_sht43, zakaz_sht44, zakaz_sht45,
                        zakaz_sht46, zakaz_sht47, zakaz_sht48, zakaz_sht49, zakaz_sht50,
                        zakaz_sht51, zakaz_sht52, zakaz_sht53, zakaz_sht54, zakaz_sht55,
                        zakaz_sht56, zakaz_sht57, zakaz_sht58, zakaz_sht59],
            zakaz_sht1: [zakaz_sht60, zakaz_sht61, zakaz_sht62, zakaz_sht63, zakaz_sht64, zakaz_sht65,
                        zakaz_sht66, zakaz_sht67, zakaz_sht68, zakaz_sht69, zakaz_sht70,
                        zakaz_sht71, zakaz_sht72, zakaz_sht73, zakaz_sht74, zakaz_sht75,
                        zakaz_sht76, zakaz_sht77, zakaz_sht78, zakaz_sht79, zakaz_sht80,
                        zakaz_sht81, zakaz_sht82, zakaz_sht83, zakaz_sht84, zakaz_sht85,
                        zakaz_sht86, zakaz_sht87, zakaz_sht88, zakaz_sht89, zakaz_sht90,
                        zakaz_sht91, zakaz_sht92, zakaz_sht93, zakaz_sht94, zakaz_sht95,
                        zakaz_sht96, zakaz_sht97, zakaz_sht98, zakaz_sht99, zakaz_sht100,
                        zakaz_sht101, zakaz_sht102, zakaz_sht103, zakaz_sht104, zakaz_sht105,
                        zakaz_sht106, zakaz_sht107, zakaz_sht108, zakaz_sht109, zakaz_sht110,
                        zakaz_sht111, zakaz_sht112, zakaz_sht113, zakaz_sht114, zakaz_sht115,
                        zakaz_sht116, zakaz_sht117, zakaz_sht118, zakaz_sht119],
            zakaz_sht2: [zakaz_sht120, zakaz_sht121, zakaz_sht122],
        })
    });
    if (response_1.ok) {
        const data = await response_1.json();
        document.getElementById("201").textContent = data.zakaz_sht[0];
        document.getElementById("202").textContent = data.zakaz_sht[1];
        document.getElementById("203").textContent = data.zakaz_sht[2];
        document.getElementById("204").textContent = data.zakaz_sht[3];
        document.getElementById("205").textContent = data.zakaz_sht[4];
        document.getElementById("206").textContent = data.zakaz_sht[5];
        document.getElementById("207").textContent = data.zakaz_sht[6];
        document.getElementById("208").textContent = data.zakaz_sht[7];
        document.getElementById("209").textContent = data.zakaz_sht[8];
        document.getElementById("210").textContent = data.zakaz_sht[9];
        document.getElementById("211").textContent = data.zakaz_sht[10];
        document.getElementById("212").textContent = data.zakaz_sht[11];
        document.getElementById("213").textContent = data.zakaz_sht[12];
        document.getElementById("214").textContent = data.zakaz_sht[13];
        document.getElementById("215").textContent = data.zakaz_sht[14];
        document.getElementById("216").textContent = data.zakaz_sht[15];
        document.getElementById("217").textContent = data.zakaz_sht[16];
        document.getElementById("218").textContent = data.zakaz_sht[17];
        document.getElementById("219").textContent = data.zakaz_sht[18];
        document.getElementById("220").textContent = data.zakaz_sht[19];
        document.getElementById("221").textContent = data.zakaz_sht[20];
        document.getElementById("222").textContent = data.zakaz_sht[21];
        document.getElementById("223").textContent = data.zakaz_sht[22];
        document.getElementById("224").textContent = data.zakaz_sht[23];
        document.getElementById("225").textContent = data.zakaz_sht[24];
        document.getElementById("226").textContent = data.zakaz_sht[25];
        document.getElementById("227").textContent = data.zakaz_sht[26];
        document.getElementById("228").textContent = data.zakaz_sht[27];
        document.getElementById("229").textContent = data.zakaz_sht[28];
        document.getElementById("230").textContent = data.zakaz_sht[29];
        document.getElementById("231").textContent = data.zakaz_sht[30];
        document.getElementById("232").textContent = data.zakaz_sht[31];
        document.getElementById("233").textContent = data.zakaz_sht[32];
        document.getElementById("234").textContent = data.zakaz_sht[33];
        document.getElementById("235").textContent = data.zakaz_sht[34];
        document.getElementById("236").textContent = data.zakaz_sht[35];
        document.getElementById("237").textContent = data.zakaz_sht[36];
        document.getElementById("238").textContent = data.zakaz_sht[37];
        document.getElementById("239").textContent = data.zakaz_sht[38];
        document.getElementById("240").textContent = data.zakaz_sht[39];
        document.getElementById("241").textContent = data.zakaz_sht[40];
        document.getElementById("242").textContent = data.zakaz_sht[41];
        document.getElementById("243").textContent = data.zakaz_sht[42];
        document.getElementById("244").textContent = data.zakaz_sht[43];
        document.getElementById("245").textContent = data.zakaz_sht[44];
        document.getElementById("246").textContent = data.zakaz_sht[45];
        document.getElementById("247").textContent = data.zakaz_sht[46];
        document.getElementById("248").textContent = data.zakaz_sht[47];
        document.getElementById("249").textContent = data.zakaz_sht[48];
        document.getElementById("250").textContent = data.zakaz_sht[49];
        document.getElementById("251").textContent = data.zakaz_sht[50];
        document.getElementById("252").textContent = data.zakaz_sht[51];
        document.getElementById("253").textContent = data.zakaz_sht[52];
        document.getElementById("254").textContent = data.zakaz_sht[53];
        document.getElementById("255").textContent = data.zakaz_sht[54];
        document.getElementById("256").textContent = data.zakaz_sht[55];
        document.getElementById("257").textContent = data.zakaz_sht[56];
        document.getElementById("258").textContent = data.zakaz_sht[57];
        document.getElementById("259").textContent = data.zakaz_sht[58];
        document.getElementById("260").textContent = data.zakaz_sht[59];
        document.getElementById("200").textContent = data.zakaz_sht1;
        document.getElementById("200").style.color = 'red';
        document.getElementById("300").textContent = data.zakaz_sht2;
        document.getElementById("300").style.color = 'red';
    }
}

