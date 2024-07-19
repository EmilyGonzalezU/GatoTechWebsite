document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('filtrosForm');

    if (form) {
        const inputs = form.querySelectorAll('input[type="checkbox"]');

        inputs.forEach(input => {
            input.addEventListener('change', function() {
                form.submit();
            });
        });
    }
});
