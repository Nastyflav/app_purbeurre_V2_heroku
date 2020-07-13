function removeChar() {
    var query = document.getElementById("query").value;
    query = query.replace(/[^a-zA-Z0-9]/g, '');
    document.getElementById("query").value  = query;
}