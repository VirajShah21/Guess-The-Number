var gtn = {
    number,
    currGameStatus: "notStarted",
    check: function() {
	var guess = document.getElementById("guess");
	guess = guess.parseInt(guess);
	var number = gtn.number;
	if(guess == number) {
	    gtn.output(guess + ": YOU GOT IT!!!\tClick the 'Start' Button.");
	}
	else if(guess < number) {
	    gtn.output(guess + ": Too low<br>\tTry guessing higher");
	}
	else if(guess > number) {
	    gtn.output(guess + ": Too high<br>\tTry guessing lower");
	}
	else {
	    gtn.output(guess + ": There is something wrong with your input");
	}
    },
    
    start: function() {
	gtn.currGameStatus = "started";
	gtn.number = Math.random()
    }

}
