            // Pobierz elementy
            const hamburger = document.querySelector('.hamburger');
        const menu = document.querySelector('.main-menu-inner');
        const menuLinks = document.querySelectorAll('.main-menu-item a');
    
        // Obsługa kliknięcia hamburgera
        hamburger.addEventListener('click', () => {
            menu.classList.toggle('active'); // Przełącz klasę 'active'
        });
    
        // Obsługa kliknięcia linków w menu
        menuLinks.forEach(link => {
            link.addEventListener('click', () => {
                menu.classList.remove('active'); // Ukryj menu
            });
        });