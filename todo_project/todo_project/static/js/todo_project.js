/* Project specific Javascript goes here. */
$('.datepicker').datepicker('hide');
$('#login_form').appendTo("body").modal('show');

function replaceAll(find, replace, str) {
  return str.replace(new RegExp(find, 'g'), replace);
}

// DIsplay create event form
$("span[data-cal-view*='day']").click(function() {
    var date = $(this).attr("data-cal-date");
    date = replaceAll("-", "/", date)

    $("input[name*='created_date']").val(date);
    $('#events-modal').modal({
        show: true
    });
});


// Display event detail
$('a.event').click(function() {
    var event_id = $(this).attr("data-event-id");
    // Make an ajax call to retrieve detail
    ajx_url = "/event_detail/" + event_id
    console.log(ajx_url);
    $.ajax({
        url: ajx_url,
        dataType: 'json',
		type:     'GET',
		async:    false
    }).done(function(json) {
            if(!json.success) {
                $.error(json.error);
            }
            if(json.result) {
                events = json.result;
                event = events[0]

                $("#detail-modal").find("form").attr("action", "/event_detail/" + event_id + "/")
                $("#detail-modal").find("input[name*='created_date']").val(event.created_date);
                $("#detail-modal").find("input[name*='title']").val(event.title);
                $("#detail-modal").find("input[name*='location']").val(event.location);
                $("#detail-modal").find("input[name*='description']").val(event.description);

                $("input[name*='created_date_disable']").val(event.created_date);
                $("input[name*='title_disable']").val(event.title);
                $("input[name*='location_disable']").val(event.location);
                $("input[name*='description_disable']").val(event.description);
            }
    });

    $('#detail-modal').modal({
        show: true
    });
})