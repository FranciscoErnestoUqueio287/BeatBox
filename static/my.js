$(document).ready(function() {;
	$("p#progressbar").replaceWith("<p id='progressbar'>0%</p>");
	$('form').on('submit',function(event) {
		event.preventDefault();
		var formData = new FormData($('form')[0]);
		$.ajax({
			xhr: function() {
			var xhr = new window.XMLHttpRequest();
			xhr.upload.addEventListener('progress', function(event) {
				if (event.lengthComputable) {
				var how = Math.round((event.loaded / event.total) * 100 );
				$("#progressbar").replaceWith("<p id='progressbar'>"+ how.toString() + "%"+"</p>");
				}
			});
			return xhr;
		},
		type: 'POST',
		url:$('#urt').value,
		data : formData,
		processData : false,
		contentType : false,
		sucess : function() {
		console.log("Done uploading");
		console.log($('#urp').value);
		 window.location = $('#urp').value }
		})
		});
	});




