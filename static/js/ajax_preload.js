/**
 * ajax_preload.js: this script utilizes ajax to determine if current search
 *                  Meetup events are stored in the database as favorites.
 *
 *                  If contained within the database, the 'fave_button'
 *                  element is given the css classname 'fa-star', otherwise
 *                  the element will be given the css classname 'fa-star-o'.
 */

$(document).ready(function() {

// local variables
  var event_meetup = new Array();

  window.ajax_search.done(function(data) {
    $.each($('.fave-button'), function() {
      event_meetup.push( $(this).attr('id');
    });
  });

});
