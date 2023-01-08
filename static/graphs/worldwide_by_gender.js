function worldwideByGender(gender_data){
  google.charts.load('current', {
    'packages': ['corechart']
  });
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {

    var data = google.visualization.arrayToDataTable(gender_data);

    var options = {
      width: 800,
      height: 400,
      chartArea:{
        top: 0,
        bottom: 0,
        left: 150,
        right: 0,
      },
      legend:{
        alignment: 'center'
      },
      fontSize: 20,
      colors: ['#676FA3', '#FF5959']
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart1'));

    chart.draw(data, options);
  }

}

