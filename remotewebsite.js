

//website side

const pitch = document.getElementById("pitch");
const throttle = document.getElementById("throttle");

pitch.addEventListener("input", send);
throttle.addEventListener("input",send);

function send() {

	const pitchVal = parseInt(pitch.value);
	const throttleVal = parseInt(throttle.value);
	console.log(pitchVal,throttleVal);
	
}

//controllerside


gameControl.on("connect",gamepad => {
	console.log("gamepad connection!")
})
