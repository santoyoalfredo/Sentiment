function confirmDelete(id, name) {
   if (confirm('Are you sure you want to remove the product?' + 
   	'\nProduct ID: ' + id +
   	'\nName: ' + name)) {
       return true;
   } else {
       return false;
   }
}