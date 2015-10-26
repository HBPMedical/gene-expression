// Variables to store current data
var currentGene;
var dataGenExp;
var dataCorrelAll;
var dataCorrelTime;

// Variables for browser resize management
var rtime;
var timeout = false;
var delta = 200;
var browserWidth;

$(document).ready(function() {
	
	// Initialize selectors
	initBrainSelect();
	addTimeFrameSlider();
	
	// Add listeners
	$("#searchButton").click(updateUI);
	$(window).resize(function(){ resizeUI(); });
	
	// Get initial browser width
	browserWidth = $(document).width();
	
});

