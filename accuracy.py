import csv
from tense_detector import detect_tense

def evaluate():
    correct = 0
    total = 0
    mistakes = []

    with open("tense.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Jika ada baris kosong atau kolom salah → skip
            if not row.get("sentence") or not row.get("tense"):
                continue

            sentence = row["sentence"].strip()
            true_tense = row["tense"].strip().lower()

            predicted = detect_tense(sentence)
            predicted_tense = predicted.get("tense", "").strip().lower()

            total += 1

            if predicted_tense == true_tense:
                correct += 1
            else:
                mistakes.append({
                    "sentence": sentence,
                    "true": true_tense,
                    "predicted": predicted_tense
                })

    accuracy = (correct / total * 100) if total > 0 else 0

    print(f"Total data : {total}")
    print(f"Benar      : {correct}")
    print(f"Akurasi    : {accuracy:.2f}%")
    print(f"Salah      : {len(mistakes)}")

    print("\n=== 20 CONTOH SALAH ===")
    for err in mistakes[:5]:
        print(f"- Kalimat : {err['sentence']}")
        print(f"  Benar   : {err['true']}")
        print(f"  Prediksi: {err['predicted']}\n")

    # Simpan semua kesalahan
    with open("mistakes.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=["sentence", "true", "predicted"])
        writer.writeheader()
        writer.writerows(mistakes)

    print("📁 Semua kesalahan disimpan ke mistakes.csv")


if __name__ == "__main__":
    evaluate()
