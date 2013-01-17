$(function(){

    var fotorama = $('#fotorama').fotorama();

    $('#arrow-prev').click(function(){
        fotorama.trigger('showimg', 'prev');
        return false;
    });

    $('#arrow-next').click(function(){
        fotorama.trigger('showimg', 'next');
        return false;
    });

})
