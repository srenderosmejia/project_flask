document.addEventListener('DOMContentLoaded', function() {
    const rowsPerPage = 5;
    const table = document.getElementById('datatable');
    const pagination = document.getElementById('pagination');
    const rows = table.querySelectorAll('tbody tr');
    const totalPages = Math.ceil(totalRegistros.length / rowsPerPage);

    function displayRows(page) {
        const start = (page - 1) * rowsPerPage;
        const end = start + rowsPerPage;
        rows.forEach((row, index) => {
            row.style.display = (index >= start && index < end) ? '' : 'none';
        });
    }

    function createPagination() {
        pagination.innerHTML = '';
        for (let i = 1; i <= totalPages; i++) {
            const button = document.createElement('button');
            button.textContent = i;
            button.addEventListener('click', () => {
                displayRows(i);
                updateButtons(i);
            });
            pagination.appendChild(button);
        }
    }

    function updateButtons(activePage) {
        const buttons = pagination.querySelectorAll('button');
        buttons.forEach((button, index) => {
            button.classList.toggle('disabled', index + 1 === activePage);
        });
    }

    displayRows(1);
    createPagination();
    updateButtons(1);
});
