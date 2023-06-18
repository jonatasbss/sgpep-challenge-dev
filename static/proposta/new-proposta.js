$(document).ready(function () {

    const createPropostaURL = '{% url "proposta:create_proposta" %}';
    const csrftoken = Cookies.get('csrftoken');

    $('#propostaForm').on('submit', function (event) {
        event.preventDefault();

        let emailInput = $('#cliente-email');
        let emailValue = emailInput.val();
        let gmailSuffix = '@gmail.com';

        if (!emailValue.endsWith(gmailSuffix)) {
            emailValue += gmailSuffix;
            emailInput.val(emailValue);
        }

        let data = {
            cliente: {email: emailValue},
            nome_completo: $('#nome_completo').val(),
            cpf: $('#cpf').val(),
            endereco: $('#endereco').val(),
            valor_emprestimo: $('#valor_emprestimo').val(),
        };

        $.ajax({
            url: createPropostaURL,
            method: 'POST',
            dataType: 'json',
            data: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            success: function (response) {

                let toast = $('<div class="bs-toast toast fade show bg-success" role="alert" aria-live="assertive" aria-atomic="true">' +
                    '<div class="toast-header">' +
                    '<i class="bx bx-bell me-2"></i>' +
                    '<div class="me-auto fw-semibold">SGPEP</div>' +
                    '<button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>' +
                    '</div>' +
                    '<div class="toast-body">' +
                    'Proposta enviada com sucesso!' +
                    '</div>' +
                    '</div>');

                $('.toast-container').append(toast);
                toast.toast('show');


                $('#propostaForm')[0].reset();

                setTimeout(function () {
                    window.location.reload();
                }, 2000);
            },
            error: function (xhr, status, error) {
                // toastr.error('Ocorreu um erro ao enviar a proposta.', 'Erro');
                alert('Ocorreu um erro ao enviar a proposta.');
                console.log(xhr.responseText);
            }
        })
    })
})