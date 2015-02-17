/**
 * ajax_preload.js: this script utilizes ajax to determine if current search
 *                  Meetup events are stored in the database as favorites.
 *
 *                  If contained within the database, the 'fave_button'
 *                  element is given the css classname 'fa-star', otherwise
 *                  the element will be given the css classname 'fa-star-o'.
 *
 * @window.ajax_search, a global 'deferred promise' defined from 'app.js'.
 */

$(document).ready(function() {

// local variables
  var event_meetup = new Array();

// implement global 'deferred promise'
  window.ajax_search.done(function(data) {

  // get all current Meetup 'group ids'
    $.each($('.fave-button'), function() {
      event_meetup.push( $(this).attr('id');
    });

  // intersection between 'group ids', with previously selected

  // toggle 'fave-button' css classes based on intersection
  });

});
