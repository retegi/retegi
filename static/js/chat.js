$(document).ready(function () {
    $('#send-button').click(function () {
        let userMessage = $('#user-message').val();
        if (userMessage.trim() !== '') {
            $('#chat-box').append(`<p><strong>Tú:</strong> ${userMessage}</p>`);
            $('#user-message').val('');

            $.ajax({
                type: 'POST',
                url: '/api/get_response/',
                data: {
                    'message': userMessage,
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function (response) {
                    if (response.reply) {
                        $('#chat-box').append(`<p><strong>Bot:</strong> ${response.reply}</p>`);
                    } else {
                        $('#chat-box').append('<p><strong>Error:</strong> Algo salió mal.</p>');
                    }
                },
                error: function () {
                    $('#chat-box').append('<p><strong>Error:</strong> No se pudo conectar con el servidor.</p>');
                }
            });
        }
    });
});
