// renderIrregular.js
document.addEventListener("DOMContentLoaded", () => {
  const tableBody = document.getElementById("verbTableBody");
  const searchInput = document.getElementById("verbSearch");

  if (!tableBody || !searchInput) {
    console.error("Elemen tabel atau search tidak ditemukan");
    return;
  }

  function renderTable(data) {
    tableBody.innerHTML = "";
    data.forEach(verb => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${verb.base}</td>
        <td>${verb.past}</td>
        <td>${verb.pastParticiple}</td>
        <td>${verb.meaning}</td>
      `;
      tableBody.appendChild(row);
    });
  }

  // render awal
  renderTable(irregularVerbs);

  // fitur search
  searchInput.addEventListener("input", () => {
    const keyword = searchInput.value.toLowerCase();
    const filtered = irregularVerbs.filter(v =>
      v.base.includes(keyword) ||
      v.past.includes(keyword) ||
      v.pastParticiple.includes(keyword) ||
      v.meaning.includes(keyword)
    );
    renderTable(filtered);
  });
});
