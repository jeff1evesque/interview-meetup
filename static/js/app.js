(function($, Mustache) {


	var template, //Storing mustache template we're grabbing from the DOM.
		$events, //DOM element for appending events, spinners, etc.
		$topic, //Topic search input field.
		months       = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], //Short-hand months for display.
		spinner_opts = { lines: 13, length: 20, width: 10, radius: 60, color: '#333', className: 'spinner' }; //Options for spin.js.

	var getEvents = function(e) {

		if (e !== undefined) {
			e.preventDefault();
		}

		//spin.js -- http://fgnass.github.io/spin.js/
		new Spinner(spinner_opts).spin($events[0]);

              // global 'deferred promise'
		window.ajax_search = $.ajax({
			url:"http://api.meetup.com/2/open_events/?callback=?",
			data: {
				zip:"10012",
				text:$topic.val(),
				page:"10",
				key:"6752511f3291b2b182ee4d2ef312",
				time:"1w,"
			},
			dataType:"json",
			success: renderEvents,
			error: ajaxError
		});

	};

	var renderEvents = function(data) {

		//console.dir(data);

		//Make sure there are events and that there isn't an error.
		if (typeof(data.results) !== "undefined" && data.meta.count > 0) {

			for(var i=0, len=data.results.length; i<len; i++) {

				var e    = data.results[i],
					date = new Date(e.time);

				e.month = months[date.getMonth()]
				e.date =  date.getDate();

			}
			
			$events.html(Mustache.render(template, data));

		} else {

			$events.html('<p class="big bold">We couldn\'t find any matching events :(</p>');

		}

	};

	var ajaxError = function() {

		$events.html('<p class="big bold">Uh oh. Something went wrong here.</p>');

	};

	var init = function() {

		template = $("#meetup-template").html();
		$events = $("#events");
		$topic = $("#topic");

		$("#search-button").on("click", getEvents);

		getEvents();

	};

	$(init);

})($, Mustache);
