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
      // Format set for Datepicker: DD/MM/YYYY hh:mm
      // Format for Django: YYYY-MM-DD hh:mm *[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]
      // https://fullcalendar.io/docs/date-formatting
      // console.log(info);

      var modal = document.getElementById("modal1");

      // Set Start and End on both forms based on FullCalendar selection
      var start_fields = document.querySelectorAll('.schedule_start_field');
      for (var i = start_fields.length - 1; i >= 0; i--) {
        start_fields[i].value = moment(info.start).format('YYYY-MM-DD hh:mm');
      }

      var end_fields = document.querySelectorAll('.schedule_end_field');
      for (var i = end_fields.length - 1; i >= 0; i--) {
        end_fields[i].value = moment(info.end).format('YYYY-MM-DD hh:mm');
      }

      // get data from active_form
      // active form is referenced the button '.switch_form' data attr
      var active_form_type = document.getElementById('switch_form').dataset.formtype;
      var active_form = document.getElementById(active_form_type + '_form');
      var active_form_start = active_form.querySelector('#id_start');
      // convert value from DatePicker format to Django's required one
      var afs_value = active_form_start.value;
      console.log(afs_value);
      var conv = moment(afs_value, 'YYYY-MM-DD hh:mm').format('DD/MM/YYYY hh:mm');
      console.log(conv);

      // use ajax to validate that the event/appointment doesn't clash
      // then use form.save to save the data and refetch events -
      //    calendar.fullCalendar('refetchEvents');
      $.ajax({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/events/',
        data: {
          'csrftoken': getCookie('csrftoken'),
          'start': moment(info.start).format('YYYY-MM-DD hh:mm'),
          success: function (data) {
            console.log(data)
            // calendar.fullCalendar('refetchEvents');
          },
          error: function (xhr, status, error) {
            console.log(xhr, status, error)
            // alert('there was an error')
          }
        }
      });
    }
    // nice examples here
    // https://www.webslesson.info/2017/12/jquery-fullcalandar-integration-with-php-and-mysql.html
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