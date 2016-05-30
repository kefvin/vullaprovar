
var baseMargin = 20;

$('#mates').hover(function(){
    $('#u').stop().animate({marginTop: (baseMargin+20)+'%'}, 1000);
    $('#ix').stop().animate({marginLeft: (baseMargin+20)+'%'}, 1000);
    $('#quatre').stop().animate({marginTop: (-baseMargin-40)+'%'}, 1000);
},
    function() {
    $('#u').stop().animate({marginTop: (baseMargin-20)+'%'}, 1000);
    $('#ix').stop().animate({marginLeft: (baseMargin-20)+'%'}, 1000);
    $('#quatre').stop().animate({marginTop: (baseMargin-20)+'%'}, 1000);
  })



$('#ciencies').hover(function(){
    $('#mon').stop().animate({marginTop: (baseMargin+20)+'%'}, 1000);
    $('#atomm').stop().animate({marginTop: (-baseMargin-40)+'%'}, 1000);
},
    function() {
    $('#mon').stop().animate({marginTop: (baseMargin-20)+'%'}, 1000);
    $('#atomm').stop().animate({marginTop: (0)+'%'}, 1000);
  })



$('#llengues').hover(function(){
    $('#e').stop().animate({marginTop: (baseMargin+30)+'%'}, 1000);
    $('#g').stop().animate({marginLeft: (baseMargin+20)+'%'}, 1000);
    $('#a').stop().animate({marginTop: (-baseMargin-30)+'%'}, 1000);
},
    function() {
    $('#e').stop().animate({marginTop: (baseMargin-20)+'%'}, 1000);
    $('#g').stop().animate({marginLeft: (baseMargin-20)+'%'}, 1000);
    $('#a').stop().animate({marginTop: (baseMargin-20)+'%'}, 1000);
  })
