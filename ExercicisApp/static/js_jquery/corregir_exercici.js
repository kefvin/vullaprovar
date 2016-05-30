$(document).ready(function(){

    var resposta = $("#id_resposta").val();
    $("p").after('<h3>Resposta:</h3><p> '+resposta);

    $("#div_id_resposta").hide();
    $("#div_id_exercici").hide();
    $("#div_id_usuari").hide();

})
