function removeCharNavBar() {
    var query = document.getElementById("query-navbar").value;
    query = query.normalize("NFD").replace(/[^a-zA-Z0-9]/g, '');
    document.getElementById("query-navbar").value = query;
}

function removeCharMain() {
    var query = document.getElementById("query-main").value;
    query = query.normalize("NFD").replace(/[^a-zA-Z0-9]/g, '');
    document.getElementById("query-main").value = query;
}