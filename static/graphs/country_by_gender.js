function countryByGender(gender_data){
    google.charts.load("current", {packages:["corechart"]});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {
          var data = google.visualization.arrayToDataTable(gender_data);

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
                  colors: ['#676FA3', '#FF5959']
           };
          var chart = new google.visualization.BarChart(document.getElementById("barchart_values2"));
          chart.draw(view, options);
      }
}
