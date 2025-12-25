// === Tombol utama ===
document.getElementById("detectBtn").addEventListener("click", detectTense);

// Ambil elemen-elemen penting
const resultPanel = document.getElementById("resultPanel");
const resultDiv = document.getElementById("result");
const closeBtn = document.getElementById("closeResult");
const wrapper = document.querySelector(".wrapper");

// === Fungsi utama deteksi tense ===
async function detectTense() {
  const input = document.getElementById("inputSentence").value.trim();

  if (!input) {
    showResultHTML(`❗ Kalimat tidak boleh kosong!`, "not-found");
    return;
  }

  // Reset hasil lama dan tampilkan animasi loading
  showResultHTML(`
    <div class="loading-spinner"></div>
    <p><em>🧠 TenseBuddy is thinking...</em></p>
  `, "loading");

  try {
    const response = await fetch("http://localhost:8000/detect", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sentence: input })
    });

    const data = await response.json();
    console.log(data);

    // 🔹 Grammar check
    if (data.has_error) {
      showResultHTML(`
        <div class="grammar-result">
          <p><strong>🧠 Grammar Check:</strong></p>
          <p>${data.message}</p>
          ${
            data.suggestions && data.suggestions.length > 0
              ? `<p><strong>Perbaikan:</strong> ${data.suggestions.join(", ")}</p>`
              : ""
          }
        </div>
      `, "grammar-warning");
      return;
    }

    // 🔹 Jika tense tidak dikenali
    if (data.tense === "Tidak dikenali") {
      showResultHTML(`❗ Tense tidak dikenali.`, "not-found");
      return;
    }

    // 🔹 Deteksi bentuk kalimat
      const lower = input.toLowerCase();
      const negativeRegex = /(?:\bnot\b|\bnever\b|didn['’]?t|won['’]?t|hasn['’]?t|haven['’]?t|wasn['’]?t|weren['’]?t|isn['’]?t|aren['’]?t|don['’]?t|doesn['’]?t|can['’]?t|cannot|shan['’]?t|n['’]?t)/i;
      const auxStartRegex = /^[\s]*(?:do|does|did|will|would|have|has|had|is|are|am|was|were|can|could|should|shall)\b/i;

      let formType = "positive";
      if (negativeRegex.test(lower)) formType = "negative";
      else if (lower.trim().endsWith("?") || auxStartRegex.test(lower)) formType = "interrogative";

    // 🔹 Ambil data tense dari mapping
    const tenseBlock = tenseInfo[data.tense] || {};
    const info = tenseBlock[formType] || tenseBlock || { formula: "-", examples: [] };
    const highlighted = highlightSentence(input, data.tense);
    const imageFile = tenseToImage[data.tense] || "";

    // 🔹 Ubah contoh sesuai bentuk kalimat
let adjustedExamples = (info.examples || []).map(ex => {
  if (formType === "negative") {
    return ex
      .replace(/\b(do|does)\b/i, "$1 not")
      .replace(/\b(is|are|am|was|were|has|have|had|can|will|should|would)\b/i, "$& not")
      .replace(/\bnot not\b/g, "not");
  } else if (formType === "interrogative") {
    return ex.replace(/^([A-Za-z']+)/, "Do $1") + "?";
  }
  return ex;
});

// 🔹 Bangun hasil HTML akhir
const resultHTML = `
  <div class="card-result">
    <img src="tensesCard/${imageFile}" alt="${data.tense}" />
  </div>
  <h3>✅Hasil Deteksi Tense</h3>
  <strong>Tense:</strong> ${data.tense}<br/>
  <em>${data.description || ""}</em><br/>
  <strong>Bentuk Kalimat:</strong> ${formType}<br/>
  <em>Rumus:</em> ${info.formula || "-"} <br/>
  <strong>Kalimatmu:</strong> ${highlighted}<br/>
  <strong>Contoh Lain:</strong>
    <ul>
      ${adjustedExamples.map(ex => `<li>${ex}</li>`).join("")}
    </ul>
`;


    // 🔹 Tampilkan hasil dengan animasi slide
    setTimeout(() => showResultHTML(resultHTML, "show"), 400);

  } catch (error) {
    console.error("Error detail:", error);
    showResultHTML(`❗ Terjadi kesalahan: ${error.message}`, "not-found");
  }
}

// === Fungsi untuk menampilkan hasil di panel samping ===
function showResultHTML(html, className = "") {
  resultDiv.className = `result ${className}`;
  resultDiv.innerHTML = html;

  // Aktifkan animasi wrapper dan panel
  wrapper.classList.add("show-result");
  resultPanel.classList.add("show");
  resultPanel.setAttribute("aria-hidden", "false");
}

// === Tombol tutup panel hasil ===
closeBtn.addEventListener("click", () => {
  resultPanel.classList.remove("show");
  resultPanel.setAttribute("aria-hidden", "true");
  wrapper.classList.remove("show-result"); // input panel kembali ke tengah
});


