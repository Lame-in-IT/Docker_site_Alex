async function prodaji() {
    const prodaji = document.getElementById("inp").value
    const prodaji_1 = document.getElementById("Маркетплейс").value
    const response = await fetch("/prodaji", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            prodaji: prodaji,
            prodaji_1: prodaji_1,
        })
    });
    if (response.ok) {
        const data = await response.json();
        document.getElementById("prib").textContent = data.prodaji;
        document.getElementById("prib_1").textContent = data.prodaji1;
        document.getElementById("prib_2").textContent = data.prodaji2;
        document.getElementById("prib_3").textContent = data.prodaji3;
        document.getElementById("prib_4").textContent = data.prodaji4;
        document.getElementById("prib_5").textContent = data.prodaji5;
        document.getElementById("prib_10").textContent = data.prodaji6;
        document.getElementById("prib_16").textContent = data.prodaji7;
        document.getElementById("inp_1").value = data.prodaji8;
        document.getElementById("prib_11").textContent = data.prodaji9;
        document.getElementById("prib_17").textContent = data.prodaji10;
        document.getElementById("prib_6").textContent = data.prodaji11;
        document.getElementById("prib_12").textContent = data.prodaji12;
        document.getElementById("prib_18").textContent = data.prodaji13;
        document.getElementById("prib_7").textContent = data.prodaji14;
        document.getElementById("prib_13").textContent = data.prodaji15;
        document.getElementById("prib_19").textContent = data.prodaji16;
        document.getElementById("prib_8").textContent = data.prodaji17;
        document.getElementById("prib_14").textContent = data.prodaji18;
        document.getElementById("prib_20").textContent = data.prodaji19;
        document.getElementById("prib_9").textContent = data.prodaji20;
        document.getElementById("prib_15").textContent = data.prodaji21;
        document.getElementById("prib_21").textContent = data.prodaji22;
        document.getElementById("valu_5").textContent = data.prodaji23;
        document.getElementById("valu_6").textContent = data.prodaji24;
        document.getElementById("prib_22").textContent = data.prodaji1;
        document.getElementById("prib_23").textContent = data.prodaji25;
        document.getElementById("prib_24").textContent = data.prodaji26;
        document.getElementById("prib_25").textContent = data.prodaji27;
        document.getElementById("prib_26").textContent = data.prodaji28;
        document.getElementById("prib_27").textContent = data.prodaji29;
        document.getElementById("prib_28").textContent = data.prodaji30;
        document.getElementById("prib_29").textContent = data.prodaji31;
        document.getElementById("prib_30").textContent = data.prodaji32;
        document.getElementById("prib_31").textContent = data.prodaji33;
        document.getElementById("prib_32").textContent = data.prodaji34;
        document.getElementById("prib_33").textContent = data.prodaji35;
        document.getElementById("prib_34").textContent = data.prodaji36;
        document.getElementById("prib_35").textContent = data.prodaji37;
        document.getElementById("prib_36").textContent = data.prodaji38;
    }
}