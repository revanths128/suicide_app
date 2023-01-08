function country(country_data){
    google.charts.load('current', {
            'packages':['geochart'],
          });
          google.charts.setOnLoadCallback(drawRegionsMap);

          function drawRegionsMap() {
            var data = google.visualization.arrayToDataTable(country_data);

            var options = {
              width: 1700,
              height: 700,
              colorAxis:{
                colors: ['#BBE1FA', '#3282B8', '#0F4C75', '#1B262C']
              }
            };

            var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

            chart.draw(data, options);
    }
}

