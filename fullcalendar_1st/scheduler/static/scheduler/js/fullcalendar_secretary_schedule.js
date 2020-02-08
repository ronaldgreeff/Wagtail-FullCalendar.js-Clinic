
document.addEventListener('DOMContentLoaded', function() {

  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    // OPTIONS
    plugins: [ 'interaction', 'dayGrid', 'timeGrid' ],
    defaultView: 'dayGridMonth',
    defaultDate: '2020-01-01',
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    events: '../api/load/',
    // dateClick: function() {
    //   alert('a day has been clicked!');
    // }
  });
  // HANDLERS
  calendar.render();
  calendar.on('dateClick', function(info) {
    console.log('clicked on ' + info.dateStr);
  });
});