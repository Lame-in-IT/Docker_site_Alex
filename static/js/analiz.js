const ctx = document.getElementById('myChart').getContext('2d');
var ctx_1 = document.getElementById('Chart_1')
const data = {
    labels: ['Бутылка', 'Бутылка 1 литр', 'Кошелек',
        'Лампа с датчиком', 'Магнит', 'Овощечистка нерж',
        'Овощечистка пластик', 'Планшет 8,5',
        'Планшет 10', 'Планшет 12',
        'Полотенце', 'Шейкер 4 цвета', 'Шейкер черный'],
    datasets: [{
        label: 'Рентабельность по категориям',
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

const data_sum = {
    labels: ['Бутылка', 'Бутылка 1 литр', 'Кошелек',
        'Лампа с датчиком', 'Магнит'],
    datasets: [{
        label: 'Доля валовой прибыли по товарам',
        data: [0, 0, 0, 0, 0],
        backgroundColor: [
            'rgba(255, 99, 132, 0.5)',
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(153, 102, 255, 0.5)',
        ],
        borderColor: [
            'rgba(255, 99, 132, 0.5)',
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(153, 102, 255, 0.5)',
        ],
        borderWidth: 1
    }]
};

const data_kryg = {
    labels: ['2022-11-19', '2022-11-18', '2022-11-17',
        '2022-11-16', '2022-11-15', '2022-11-14',
        '2022-11-13', '2022-11-12',
        '2022-11-11', '2022-11-10',
        '2022-11-09', '2022-11-08', '2022-11-07'],
    datasets: [{
        label: 'Выручка по датам',
        data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        borderWidth: 1
    }, {
        label: 'Сравнение по датам',
        data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        borderWidth: 1
    }]
};

const data_pie = {
    labels: ['ожидает упаковки', 'ожидает отгрузки',
        'доставляется', 'доставлено', 'отменено',
        'не принят'],
    datasets: [{
        label: 'Доля выкупа',
        data: [5, 5, 5, 5, 5, 5],
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

// config
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

const config_sum = {
    type: 'polarArea',
    data: data_sum,
    options: {}
};

const config_2 = {
    type: 'line',
    data: data_kryg,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

const config_pie = {
    type: 'pie',
    data: data_pie,
    options: {}
};

async function analiz() {
    const analiz = document.getElementById("Категория").value
    const analiz1 = document.getElementById("Маркетплейс").value
    const analiz2 = document.getElementById("airdatepicer").value
    const response_3 = await fetch("/analiz", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            analiz: analiz,
            analiz1: analiz1,
            analiz2: analiz2,
        })
    });
    if (response_3.ok) {
        const data = await response_3.json();
        document.getElementById("Продажи").textContent = data.message;
        document.getElementById("Валовая").textContent = data.message1;
        document.getElementById("Количество").textContent = data.message2;
        document.getElementById("Процент").textContent = data.message3;
        MyCart.data.labels = data.message4;
        MyCart.data.datasets[0].data = data.message5;
        MyCart.update()
        MyCart_1.data.labels = data.message6;
        MyCart_1.data.datasets[0].data = data.message7;
        MyCart_1.update()
        MyCart_pie.data.labels = data.message8;
        MyCart_pie.data.datasets[0].data = data.message9;
        MyCart_pie.update()
        MyCart_sun.data.labels = data.message10;
        MyCart_sun.data.datasets[0].data = data.message11;
        MyCart_sun.update()
        document.getElementById("Выручка").textContent = data.message12;
    }
}

async function analiz_1() {
    const analiz = document.getElementById("Категория").value
    const analiz1 = document.getElementById("Маркетплейс").value
    const analiz2 = document.getElementById("airdatepicer_1").value
    const analiz3 = document.getElementById("Продажи").textContent
    const analiz4 = document.getElementById("Валовая").textContent
    const analiz5 = document.getElementById("Количество").textContent
    const analiz6 = document.getElementById("Процент").textContent
    const analiz7 = document.getElementById("Выручка").textContent
    const response_4 = await fetch("/analiz_1", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            analiz: analiz,
            analiz1: analiz1,
            analiz2: analiz2,
            analiz3: analiz3,
            analiz4: analiz4,
            analiz5: analiz5,
            analiz6: analiz6,
            analiz7: analiz7,
        })
    });
    if (response_4.ok) {
        const data = await response_4.json();
        document.getElementById("Продажи_1").textContent = data.message;
        document.getElementById("Валовая_1").textContent = data.message1;
        document.getElementById("Количество_1").textContent = data.message2;
        document.getElementById("Процент_1").textContent = data.message3;
        document.getElementById("Выручка_1").textContent = data.message4;
        document.getElementById("Выручка_2").textContent = data.message5;
        document.getElementById("Продажи_2").textContent = data.message6;
        document.getElementById("Валовая_2").textContent = data.message7;
        document.getElementById("Количество_2").textContent = data.message8;
        document.getElementById("Процент_2").textContent = data.message9;
        MyCart_1.data.datasets[1].data = data.message10;
        MyCart_1.update()
    }
}

const MyCart = new Chart(
    document.getElementById('myChart'),
    config,
    );


const MyCart_1 = new Chart(
    document.getElementById('Chart_1'),
    config_2,
    );

const MyCart_pie = new Chart(
    document.getElementById('pieChart'),
    config_pie
    );

const MyCart_sun = new Chart(
    document.getElementById('Chartsum'),
    config_sum
    );