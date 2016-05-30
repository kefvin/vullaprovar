$(document).ready(function(){

    var comentari = $("#id_comentari_professor").val();
    $("p").after('<h3>Comentari del professor:</h3><p> '+comentari);

    $("#div_id_comentari_professor").hide();
    $("#div_id_exercici").hide();
    $("#div_id_usuari").hide();

})
