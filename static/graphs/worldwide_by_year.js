function worldwideByYear(year_data){
    google.charts.load('current', {
      'packages': ['line']
    });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
      for(var i=0; i<year_data.length; i++)
        year_data[i][0] = new Date(year_data[i][0],1,1);
      console.log(year_data);
      var data = new google.visualization.DataTable();
      data.addColumn('date', 'Year');
      data.addColumn('number', 'Suicides');

      data.addRows(year_data);

      var options = {
        width: 1700,
        height: 700,
        colors: ['#E94D20'],
        fontSize: 50,
        hAxis: {
          title: "Year",
          textStyle: {
            fontSize: 25,
          },
          titleTextStyle: {
            color: 'black',
          }
        },
        vAxis: {
          title: "Suicides",
          textStyle: {
            fontSize: 25,
          },
          titleTextStyle: {
            color: 'black',
          }
        },
        legend: {
          textStyle: {
            color: 'black',
            fontSize: 30,
          },
        },
      };

      var chart = new google.charts.Line(document.getElementById('linechart_material'));

      chart.draw(data, google.charts.Line.convertOptions(options));
    }
}
