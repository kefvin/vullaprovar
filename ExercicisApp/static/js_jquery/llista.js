$(document).ready(function(){
    $("#user").find(".table").hide();
    $("#mater").find(".table").hide();
    $("#exer").find(".table").hide();

    $("#user").on("click", function(){
          $("#user").find(".table").fadeToggle(1000);
      })

    $("#mater").on("click", function(){
          $("#mater").find(".table").fadeToggle(1000);
      })

    $("#exer").on("click", function(){
          $("#exer").find(".table").fadeToggle(1000);
      })

})
