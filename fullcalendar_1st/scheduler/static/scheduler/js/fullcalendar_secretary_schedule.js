document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'interaction', 'dayGrid', 'timeGrid' ],
    defaultView: 'dayGridMonth',
    defaultDate: '2020-01-01',
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    events: '../api/events/',
    dateClick: function() {
      alert('a day has been clicked!');
    }
  });
  calendar.render();

  calendar.on('dateClick', function(info) {
    console.log('clicked on ' + info.dateStr);
  });
});