document.addEventListener('DOMContentLoaded', function() {



  $.ajaxSetup({
    headers: {
      'X-CSRF-TOKEN': getCookie('csrftoken')
    }
  });

  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    // OPTIONS
    plugins: [ 'interaction', 'dayGrid', 'timeGrid' ],
    defaultView: 'dayGridMonth',
    defaultDate: '2020-05-20',
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    businessHours: {
      daysOfWeek: [1,2,3,4,5,6], // Mon - Sat
      startTime: '10:00',
      endTime: '18:00',
    },
    events: 'http://127.0.0.1:8000/api/events/',
    editable: true,
    selectable: true,
    // eventRender: function (event, element, view) {
    //   if (event.allDay === 'true') {
    //     event.allDay = true;
    //   } else {
    //     event.allDay = false;
    //   }
    // },
    select: function(info) {
      console.log(info);
      var title = prompt('Enter event title');
      if (title) {
        var start = FullCalendar.formatDate(info.start);
        var end = FullCalendar.formatDate(info.end);
        
        $.ajax({
          method: 'POST',
          url: '../InsertEventView/',
          data: {
            'title': title,
            'start': start,
            'end': end,
            'all_day': info.allDay,
            'csrftoken': getCookie('csrftoken'),
            success: function (data) {
                alert(title + " added successfully");
            }
          }
        });
      }
    },
    // eventResize: function(event){},
    // eventDrop: function(event){},
    // eventClick: function(event){},
  });

  // HANDLERS
  calendar.render();
  // calendar.on('select', function(info) {
  // });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

});