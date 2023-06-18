let elementos = document.querySelectorAll('#status')


elementos.forEach(elemento => {
    if (elemento.innerHTML === 'Aprovado') {
        elemento.classList.add('bg-success');
    } else if (elemento.innerHTML === 'Reprovado') {
        elemento.classList.add('bg-danger');
    } else {
        elemento.classList.add('bg-warning');
    }
});