$(document).ready(function() {;
	var pro = $("div.progress-bar")[0];
	pro.style.width = '0%';
	$('form').on('submit',function(event) {
		event.preventDefault();
		var formData = new FormData($('form')[0]);
		$.ajax({
			xhr: function() {
			var xhr = new window.XMLHttpRequest();
			xhr.upload.addEventListener('progress', function(event) {
				if (event.lengthComputable) {
				var how = Math.round((event.loaded / event.total) * 100 );
				pro.style.width = how.toString()+"%";
				pro.ariaValueNow = how.toString();
				pro.innerHTML = how.toString()+"%";
				}
			});
			return xhr;
		},
		type: 'POST',
		url:$('#urt').value,
		data : formData,
		processData : false,
		contentType : false,
		success : function() {
		 alert("Publicada com sucesso!");
		}
		});
	});
});











