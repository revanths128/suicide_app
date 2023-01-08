function worldwideByAge(age_data){
    google.charts.load('current', {
      'packages': ['corechart']
    });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
      var data = google.visualization.arrayToDataTable(age_data);

      var options = {
        width: 800,
        height: 400,
        legend:{
          alignment: 'center'
        },
        chartArea:{
          top: 0,
          bottom: 0,
          left: 150,
          right: 0,
        },
        fontSize: 20,
        is3D: true,
        colors: ['#F2F7A1', '#46C2CB', '#6D67E4', '#453C67', '#68B984', '#FAAB78']
      };

      var chart = new google.visualization.PieChart(document.getElementById('piechart2'));

      chart.draw(data, options);
    }

}
