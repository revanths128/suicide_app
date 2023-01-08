function countryByAge(age_data){
    google.charts.load("current", {packages:["corechart"]});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {
          var data = google.visualization.arrayToDataTable(age_data);

          var view = new google.visualization.DataView(data);

          var options = {
                  width: 800,
                  isStacked: 'percent',
                  height: 2500,
                  fontSize: 15,
                  legend: {position: 'top', maxLines: 3},
                  hAxis: {
                      minValue: 0,
                      ticks: [0, .3, .6, .9, 1]
                  },
                  chartArea: {
                                        right: 0,
                                        left: 250,
                                        top: 50,
                                        bottom: 50
                                    },
                                    bar:{
                                      groupWidth: 20,
                                    },
                                    colors: ['#F2F7A1', '#46C2CB', '#6D67E4', '#453C67', '#68B984', '#FAAB78']
           };
          var chart = new google.visualization.BarChart(document.getElementById("barchart_values1"));
          chart.draw(view, options);
      }
}
