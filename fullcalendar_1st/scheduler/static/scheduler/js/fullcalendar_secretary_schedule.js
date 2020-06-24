document.addEventListener('DOMContentLoaded', function() {

  $.ajaxSetup({
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    }
  });

  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    // OPTIONS
    plugins: [ 'interaction', 'dayGrid', 'timeGrid' ],
    defaultView: 'dayGridMonth',
    defaultDate: '2020-05-20',
    eventTimeFormat: { hour12: false, hour: '2-digit', minute: '2-digit' },
    titleFormat: { year: 'numeric', month: 'long' },
    header: {
      left: 'prev, next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    businessHours: {
      daysOfWeek: [1,2,3,4,5,6], // Mon - Sat
      startTime: '10:00',
      endTime: '18:00',
    },
    // TODO: use attr to pass in events URL -
    // https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
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
      // set data attributes and values in form fields
      var m = moment(info.start);
      $.each( $('.schedule_start_field'), function(i, v) {
          $(v).attr('info', m.toISOString());
          v.value = m.format('DD-MM-YYYY HH:mm');
        });
    }
    // nice examples here for expanding fullcalendar
    // https://www.webslesson.info/2017/12/jquery-fullcalandar-integration-with-php-and-mysql.html
    // eventResize: function(event){},
    // eventDrop: function(event){},
    // eventClick: function(event){},

    // TODO: once event/appointment form submitted, should refetch events
    // calendar.fullCalendar('refetchEvents');
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