document.addEventListener('DOMContentLoaded', () => {
    const sidebar   = document.getElementById('sidebar');
    const openBtn   = document.getElementById('hamburger-toggle');
    const closeBtn  = document.getElementById('sidebar-close');
  
    function toggleSidebar() {
      sidebar.classList.toggle('open');
    }
  
    openBtn.addEventListener('click', toggleSidebar);
    closeBtn.addEventListener('click', toggleSidebar);
  });
  