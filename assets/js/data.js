var make_chart = function(json) {
    var symbol = [];
    var data = [];
    for (var key in json) {
        if (json.hasOwnProperty(key)) {
            console.log(json.Symbol, json.Open);
            symbol.push(json.Symbol);
            data.push(json.Open);
        }
    }

    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: symbol,
            datasets: [{
                label: 'My First dataset',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: data,
            }]
        },

        // Configuration options go here
        options: {}
    });
};