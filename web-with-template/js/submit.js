$('form.predectionForm').on('submit', function(){

    var data = $('#data').val();
    $('.error').fadeOut();
    $('.prediction').text('');

    // Validation

    if (data.trim() === '') {

            $('#data').focus();

            $('.error').fadeIn();

            return false;

    }

    else {

        $('.error').fadeOut();



        var that = $(this),

                url  = that.attr('action'), // action link

                type = that.attr('method'),

                data = {}; // to hold the user commming data





        that.find('[name]').each(function(index,value){ // will fetch each input with attribute name

            var that = $(this),

                    name  = that.attr('name'),

                    value = that.val();

            data[name] = value; // store the data in the data object to be sent over the php file without reloading

        });


        $.ajax({

            url: url,

            type: type,

            data: data,

            success: function(response){

                $('.prediction').text(response);
            }

        });

        return false;

    }



});