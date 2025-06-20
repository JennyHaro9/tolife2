function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const euCol = document.getElementById('eu-col');

  sidebar.classList.toggle('collapsed');

  if (sidebar.classList.contains('collapsed')) {
    euCol.classList.remove('col-5');
    euCol.classList.add('col-12');
  } else {
    euCol.classList.remove('col-12');
    euCol.classList.add('col-5');
  }
}
