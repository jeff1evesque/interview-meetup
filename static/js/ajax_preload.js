/**
 * ajax_preload.js: this script utilizes ajax to determine if current search
 *                  Meetup events are stored in the database as favorites.
 *
 *                  If contained within the database, the 'fave_button'
 *                  element is given the css classname 'fa-star', otherwise
 *                  the element will be given the css classname 'fa-star-o'.
 *
 * @window.ajax_search, a global 'deferred promise' defined from 'app.js'.
 *
 * @uid, corresponds the user who is currently logged-in to the application.
 */

$(document).ready(function() {

// local variables
  var event_meetup = new Array();

// implement global 'deferred promise'
  window.ajax_search.done(function(data) {

  // get all current Meetup 'group ids'
    $.each($('.fave-button'), function() {
      event_meetup.push( $(this).attr('id') );
    });

  // create data array
    var data_send = {events: JSON.stringify( event_meetup ), uid: 0};

  // intersection between 'group ids', with previously selected (database)
    if ( event_meetup.length > 0 ) {
      window.ajax_groupid = $.ajax({
        type: 'POST',
        url: '/get_fave/',
        data: data_send,
        beforeSend: function() {

        }
      }).done(function(data) {
        var class_intersection = data.class_intersection;
      }).fail(function(data) {
        console.log('Error Thrown: '+errorThrown);
        console.log('Error Status: '+textStatus);
      });
    }

  // toggle 'fave-button' css classes based on intersection
    if ( typeof class_intersection !== 'undefined' ) {
      $.each(class_intersection, function( index, value ) {
        $('#gid-' + value).addClass('fa-star');
        $('#gid-' + value).removeClass('fa-star-o');
      });
    }
  });

});
