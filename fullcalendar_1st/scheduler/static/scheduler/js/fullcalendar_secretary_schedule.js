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
      var new_start = moment(info.start).format('DD/MM/YYYY hh:mm');
      SMM.updateEventStartField('', new_start);

      // // Format set for Datepicker: d/m/Y H:i (DD/MM/YYYY HH:mm)
      // // Format for Django: YYYY-MM-DD hh:mm *[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]
      // // https://fullcalendar.io/docs/date-formatting
      // // console.log(info);

      // var modal = document.getElementById("modal1");

      // // Set Start on both forms based on FullCalendar selection
      // var start_fields = document.querySelectorAll('.schedule_start_field');
      // for (var i = start_fields.length - 1; i >= 0; i--) {
      //   start_fields[i].value = moment(info.start).format('DD/MM/YYYY hh:mm');
      // }
      // console.log(info)

      // // var end_fields = document.querySelectorAll('.schedule_end_field');
      // // for (var i = end_fields.length - 1; i >= 0; i--) {
      // //   end_fields[i].setAttribute('data-start', moment(info.end).toISOString());
      // // }

    }
    // nice examples here
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