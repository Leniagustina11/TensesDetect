  const tenseData = {
    simplePresent: {
      title: "Simple Present Tense",
      description: "Digunakan untuk menyatakan fakta, kebiasaan, atau rutinitas.",
      formula: "S + V1 (s/es untuk he/she/it)",
      example: "She drinks tea every morning."
    },
    presentPerfect: {
      title: "Present Perfect Tense",
      description: "Digunakan untuk aksi yang sudah terjadi dan masih relevan sekarang.",
      formula: "S + have/has + V3",
      example: "I have finished my homework."
    },
    presentContinuous: {
      title: "Present Continuous Tense",
      description: "Digunakan untuk aksi yang sedang berlangsung sekarang.",
      formula: "S + am/is/are + V-ing",
      example: "They are watching a movie."
    },
    presentPerfectContinuous: {
      title: "Present Perfect Continuous",
      description: "Digunakan untuk menyatakan aksi yang dimulai di masa lalu dan masih berlangsung.",
      formula: "S + have/has been + V-ing",
      example: "She has been studying for two hours."
    }
  };

  function openModal(key) {
    const data = tenseData[key];
    document.getElementById("modal-title").innerText = data.title;
    document.getElementById("modal-description").innerText = data.description;
    document.getElementById("modal-formula").innerText = data.formula;
    document.getElementById("modal-example").innerText = data.example;
    document.getElementById("modal").style.display = "block";
  }

  function closeModal() {
    document.getElementById("modal").style.display = "none";
  }
