// Function to fetch JSON data from the Flask endpoint
async function fetchData() {
    const response = await fetch('/Graphs'); // Change the URL to match your Flask route
    const data = await response.json();
    return data;
}

// Function to create the Highcharts graph
function createChart(data) {
    Highcharts.chart('chartContainer', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Room Type Counts'
        },
        xAxis: {
            categories: Object.keys(data)
        },
        yAxis: {
            title: {
                text: 'Counts'
            }
        },
        series: [{
            name: 'Counts',
            data: Object.values(data)
        }]
    });
}

// Fetch data and create the Highcharts graph when the DOM is ready
document.addEventListener('DOMContentLoaded', function () {
    fetchData().then(function (data) {
        createChart(data);
    });
});