$(".main").onepage_scroll({
	sectionContainer: ".section",     
	easing: "ease",                  
	animationTime: 1000,             
	pagination: true,               
	updateURL: true,                
	beforeMove: function(index) {},  
	afterMove: function(index) {},   
	loop: false,                    
	keyboard: true,                  
	responsiveFallback: false,        
	direction: "vertical"            
	});
	
$(document).ready(function(){
	  $("#section1,#section2,#section3,#section4,#section5").carousel();
	    
	  $(".carousel-control-prev").click(function(){
	    $("#section1,#section2,#section3,#section4,#section5").carousel("prev");
	  });
	  $(".carousel-control-next").click(function(){
	    $("#section1,#section2,#section3,#section4,#section5").carousel("next");
	  });
	});


