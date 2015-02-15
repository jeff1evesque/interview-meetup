/**
 * ajax_data.js: this script utilizes ajax to relay the POST data corresponding
 *               to the clicked 'fa-star' element to a defined 'action' script.
 *
 * @uid, corresponds the user who is currently logged-in to the application.
 */

$(document).ready(function() {

  $('.figureset-button fa').on('click', function(event) {
    event.preventDefault();

  // create data array:
    var data_send = {class: $(this).attr('class'), uid: 0};

    $.ajax({
      type: 'POST',
      url: 'python/my_fave.py',
      data: data_send.serialize(),
      beforeSend: function() {

    // add ajax spinner

      }
    }).done(function(data) {

    // remove ajax spinner

    // return result to DOM

    }).fail(function(jqXHR, textStatus, errorThrown) {

    // remove ajax spinner

    // return error message
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);

    });

  });

});
