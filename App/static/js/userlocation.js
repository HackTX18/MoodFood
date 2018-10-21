function userLocation() {
	var output = document.getElementById("out");

	if(!navigator.geolocation){
	output.innerHTML = "<p>Your browser does not support geolocation.</p>";
	return;
	}

	function success(position){
	var latitude = position.coords.latitude;
	var longitude = position.coords.longitude;

	output.innerHTML = '<p>Latitude: ' + latitude + ' Longitude: ' + longitude + '</p>';
	console.log( '<p>Latitude: ' + latitude + ' Longitude: ' + longitude + '</p>');
	}
	
	function error(){
	output.innerHTML = "<p>Failed to retrieve location.</p>";
	}
	output.innerHTML = "<p>Locating</p>";

	navigator.geolocation.getCurrentPosition(success, error);
}