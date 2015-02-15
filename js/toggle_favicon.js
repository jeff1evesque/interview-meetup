/**
 * toggle_favicon.js: this script toggles the classname for the 'fa-star' element
 *                    when it is clicked. Specifically, the element toggles between
 *                    the two classnames, 'fa-star', and 'fa-star-o'.
 */

$(document).ready(function() {
  $('.fa').on('click', function(e) {
    $(this).toggleClass('fa-star fa-star-o');
  });
});
