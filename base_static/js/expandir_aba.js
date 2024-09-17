// Função para alternar a visibilidade da aba e ajustar a posição se necessário
function toggleContent(buttonId, contentId) {
    const button = document.getElementById(buttonId);
    const content = document.getElementById(contentId);

    // Evento de clique no botão
    button.addEventListener('click', function(event) {
        event.stopPropagation(); // Evita fechar imediatamente

        const isVisible = content.style.display === 'block';
        document.querySelectorAll('.content').forEach(function(el) {
            el.style.display = 'none'; // Fecha todas as outras abas
        });

        if (!isVisible) {
            content.style.display = 'block'; // Mostra o conteúdo

            // Ajusta a posição do conteúdo para não ultrapassar o limite da página
            adjustPosition(content);
        }
    });
}

// Função para ajustar a posição da aba para não ultrapassar os limites da janela
function adjustPosition(content) {
    const rect = content.getBoundingClientRect();
    const windowHeight = window.innerHeight;

    // Se o conteúdo estiver saindo da tela, ajusta a posição
    if (rect.bottom > windowHeight) {
        const overflow = rect.bottom - windowHeight;
        content.style.top = `${-overflow}px`; // Move a aba para cima para caber na tela
    }
}

// Inicializa os botões e as abas
toggleContent('toggle-button-1', 'content-1');
toggleContent('toggle-button-2', 'content-2');
toggleContent('toggle-button-3', 'content-3');
toggleContent('toggle-button-4', 'content-4');
toggleContent('toggle-button-5', 'content-5');
toggleContent('toggle-button-6', 'content-6');
toggleContent('toggle-button-7', 'content-7');

// Fecha a aba ao clicar fora dela
document.addEventListener('click', function(event) {
    const contentElements = document.querySelectorAll('.content');
    contentElements.forEach(function(content) {
        if (!event.target.closest('.toggle-button') && !content.contains(event.target)) {
            content.style.display = 'none'; // Fecha a aba
        }
    });
});
