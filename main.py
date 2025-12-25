from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import re
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "TensesDetect API is running 🚀"
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentenceInput(BaseModel):
    sentence: str

# Ganti dengan API key kamu dari textgears.com
TEXTGEARS_API_KEY = "PxmT6jMbvybTNE9M"

# --------------------- GRAMMAR CHECK FUNCTION ---------------------
def check_grammar(sentence: str):
    """Cek grammar menggunakan TextGears API"""
    response = requests.get(
        "https://api.textgears.com/grammar",
        params={"text": sentence, "language": "en-US", "key": TEXTGEARS_API_KEY}
    )

    data = response.json()
    if data.get("response", {}).get("errors"):
        errors = data["response"]["errors"]
        corrected_sentence = sentence
        suggestions = []

        for err in errors:
            bad = err["bad"]
            better = err["better"][0] if err["better"] else bad
            corrected_sentence = corrected_sentence.replace(bad, better)
            suggestions.append(f"{bad} → {better}")

        return {
            "has_error": True,
            "original": sentence,
            "corrected": corrected_sentence,
            "suggestions": suggestions,
            "message": f"Mungkin maksud Anda: {corrected_sentence}"
        }
    else:
        return {"has_error": False}

# --------------------- DETEKSI TENSE ---------------------
MODAL = r"\b(would|should|could|might|may|must)(?:\s+not|n['’]t)?\b"
ING = r"\b[a-z]+ing\b"
V3 = r"\b(bought|built|gone|been|done|taken|made|run|eaten|drunk|come|become|felt|left|kept|forgotten|given|shown|read|written|known|won|put|sent|paid|cut|hurt|met|brought|thought)\b"


def detect_tense(sentence: str) -> dict:
    s = sentence.lower().strip()
    s = re.sub(r"\s+", " ", s)

  # 1) PAST FUTURE PERFECT CONTINUOUS
    if re.search(rf"{MODAL}(?:\s+\w+)*\s+have\s+been\s+\w+ing\b", s):
        return {
        "tense": "Past Future Perfect Continuous",
        "description": "Akan telah sedang berlangsung sebelum waktu di masa lalu.",
        "example": "I would have been studying."
    }


# 2) PAST FUTURE PERFECT
    elif re.search(rf"{MODAL}(?:\s+\w+)*\s+have\s+\w+(ed|en)\b", s):
        return {
        "tense": "Past Future Perfect",
        "description": "Akan telah selesai sebelum waktu tertentu di masa lalu.",
        "example": "She would have finished."
    }

# 3) PAST FUTURE CONTINUOUS  
    elif re.search(rf"{MODAL}(?:\s+\w+)*\s+be\s+\w+ing\b", s):
        return {
        "tense": "Past Future Continuous",
        "description": "Akan sedang berlangsung di masa lalu.",
        "example": "They would be traveling."
    }

# 4) SIMPLE PAST FUTURE
    elif (
        re.search(MODAL, s)
        and not re.search(r"\bhave\b", s)
        and not re.search(r"\bbeen\b", s)
        and not re.search(r"\bbe\s+\w+ing\b", s)
    ):
        return {
        "tense": "Simple Past Future",
        "description": "Akan melakukan sesuatu di masa lalu.",
        "example": "He would go."
    }

    # ============================
    # 🔵 FUTURE SERIES
    # ============================
# 🔵 FUTURE PERFECT CONTINUOUS  (FIXED FULL)
    if re.search(
        r"\bwill(?:\s+not|n['’]t)?(?:\s+\w+){0,3}?\s+have\s+been\b",
        s
    ) and re.search(r"\b\w+ing\b", s):
        return {
        "tense": "Future Perfect Continuous",
        "description": "Akan telah sedang berlangsung sebelum waktu tertentu di masa depan.",
        "example": "They will have been working."
    }

    elif re.search(
        r"\bwill(?:\s+not|n['’]t)?(?:\s+\w+){0,3}?\s+have\b",
        s
    ) and re.search(r"\b\w+(ed|en)\b", s):
        return {
        "tense": "Future Perfect",
        "description": "Akan telah selesai sebelum waktu tertentu di masa depan.",
        "example": "She will have finished."
    }

    elif re.search(
        r"\bwill(?:\s+not|n['’]t)?\s+be\s+\w+ing\b",
        s
    ):
        return {
        "tense": "Future Continuous",
        "description": "Akan sedang berlangsung di masa depan.",
        "example": "I will be sleeping."
    }


    elif re.search(r"\bwill\b", s):
        return {
        "tense": "Simple Future",
        "description": "Akan melakukan sesuatu di masa depan.",
        "example": "He will go."
    }
    
   # ============================
    # 🔵 PRESENT SERIES
    # ============================
# PRESENT PERFECT CONTINUOUS
    if (
        re.search(r"\b(has|have)(?:\s+not|n['’]t)?\s+been\b", s)
        and re.search(r"\b\w+ing\b", s)
        and not re.search(MODAL, s)
    ) or (
        # YES/NO question form:
        re.search(r"\b(has|have)\b\s+\w+\s+been\s+\w+ing\b", s)
        and not re.search(MODAL, s)
    ):
        return {
            "tense": "Present Perfect Continuous",
            "description": "Telah sedang berlangsung sampai sekarang.",
            "example": "They have been working."
        }



    elif (
        # core pattern
        re.search(r"\b(has|have)\b", s)
        and re.search(r"\b\w+(ed|en)\b", s)

        # BLOCK MODALS
        and not re.search(r"\b(would|should|could|might|may|must)\b", s)

        # BLOCK PERFECT CONTINUOUS
        and not re.search(r"\bhave been\b", s)

        # BLOCK would have been / should have been / etc
        and not re.search(r"\b(would|should|could|might|may|must)(?:\s+not|n't)?\s+have\b", s)
    ):
        return {
        "tense": "Present Perfect",
        "description": "Aksi telah selesai dan berpengaruh ke sekarang.",
        "example": "She has eaten."
    }



    elif (
    re.search(r"\b(is|am|are)\b", s)
    and re.search(r"\b\w+ing\b", s)
    and not re.search(MODAL, s)
):
        return {
        "tense": "Present Continuous",
        "description": "Aksi sedang berlangsung sekarang.",
        "example": "I am writing."
    }


    
    
# ============================
# 🔵 PAST SERIES (FINAL FIX)
# ============================

# 1) PAST PERFECT CONTINUOUS
    if re.search(
        r"\bhad(?:\s+not|n['’]t)?\s+been\s+\w+ing\b",
        s
    ):
        return {
        "tense": "Past Perfect Continuous",
        "description": "Sedang berlangsung sebelum kejadian lain di masa lalu.",
        "example": "She had been studying."
    }

# 2) PAST PERFECT
    elif (
        re.search(r"\bhad(?:\s+not|n['’]t)?\b", s)
        and (
            re.search(r"\b\w+(ed|en)\b", s)
            or re.search(V3, s)
        )
        and not re.search(r"\bhad(?:\s+not|n['’]t)?\s+been\b", s)   # <- cegah continuous
    ):
        return {
        "tense": "Past Perfect",
        "description": "Telah selesai sebelum waktu tertentu di masa lalu.",
        "example": "They had left."
    }

# 3) PAST CONTINUOUS
    elif re.search(r"\b(was|were)\b", s) and re.search(r"\b\w+ing\b", s):
        return {
        "tense": "Past Continuous",
        "description": "Sedang berlangsung di masa lalu.",
        "example": "I was eating."
    }

# 4) SIMPLE PAST
    elif (
    (
        # Affirmative
        re.search(r"\b\w+ed\b", s)
        or re.search(
            r"\b(went|saw|ate|slept|took|made|ran|bought|read|came|spoke|drank|wrote|felt|left|had|was|were)\b",
            s
        )
        # Negative
        or re.search(r"\b(did not|didn't)\s+\w+\b", s)
        # Interrogative
        or re.search(r"^did\s+\w+", s)
    )
    and not re.search(MODAL, s)
):
        return {
        "tense": "Simple Past",
        "description": "Aksi yang terjadi dan selesai di masa lalu",
        "example": "Did she go to school yesterday?"
    }


    # ============================
    # 🔵 SIMPLE PRESENT (SUPER FINAL)
    # ============================
    elif (
        # Pronoun plural (I, you, we, they) + verb dasar
        re.search(r"\b(i|you|we|they)\s+[a-z]+(?:\s|$)", s)
        # Pronoun singular (he/she/it) + verb + s/es
        or re.search(r"\b(he|she|it)\s+[a-z]+(?:s|es)(?:\s|$)", s)
        # Subjek benda tunggal umum
        or re.search(r"\b(the\s+)?(sun|water|bird|father|child)\s+[a-z]+(?:s|es)?(?:\s|$)", s)
        # Subjek jamak berakhiran s + verb dasar
        or re.search(r"\b[a-z]+s\s+[a-z]+(?:\s|$)", s)
        # do / does / don't / doesn't
        or re.search(r"\b(do|does|don’t|doesn’t|don't|doesn't)\b", s)
    ) and not re.search(r"\b(is|am|are|was|were|will|has|have|had|been|would)\b", s):

        return {
            "tense": "Simple Present",
            "description": "Fakta, rutinitas, atau kebiasaan sekarang (termasuk bentuk negatif).",
            "example": "They don’t speak Korean."
        }


    # Default
    return {"tense": "Tidak dikenali", "description": "Tense belum dikenali sistem.", "example": ""}
    
    
    # ====== DEFAULT ======
    return {"tense": "Tidak dikenali", "description": "Tense belum dikenali sistem.", "example": "Gunakan struktur kalimat yang lebih jelas."}

# --------------------- GENERATE RELATED TENSES ---------------------
def generate_related_tenses(base_tense: str, sentence: str):
    """
    Membuat versi kalimat lain berdasarkan tense yang sama (keluarga waktu yang sama)
    Misal: Simple Past -> Past Continuous, Past Perfect, Past Perfect Continuous
    """
    # Ambil kata kerja utama (sangat sederhana)
    words = sentence.split()
    if len(words) < 2:
        return []

    subject = words[0]
    # cari verb (sederhana): kata ke-2 atau yang mengandung 'ed', 'ing'
    verb = next((w for w in words if re.search(r"(ed|ing|go|see|eat|sleep|take|make|run|read|come|speak|drink|write|feel|leave|have|play)", w.lower())), "do")
    rest = " ".join(words[words.index(verb)+1:]) if verb in words else ""

    related = []

    if "Past" in base_tense:
        related = [
            {"tense": "Past Continuous", "sentence": f"{subject} was {verb}ing {rest}".strip()},
            {"tense": "Past Perfect", "sentence": f"{subject} had {verb}ed {rest}".strip()},
            {"tense": "Past Perfect Continuous", "sentence": f"{subject} had been {verb}ing {rest}".strip()}
        ]
    elif "Present" in base_tense:
        related = [
            {"tense": "Present Continuous", "sentence": f"{subject} is {verb}ing {rest}".strip()},
            {"tense": "Present Perfect", "sentence": f"{subject} has {verb}ed {rest}".strip()},
            {"tense": "Present Perfect Continuous", "sentence": f"{subject} has been {verb}ing {rest}".strip()}
        ]
    elif "Future" in base_tense:
        related = [
            {"tense": "Future Continuous", "sentence": f"{subject} will be {verb}ing {rest}".strip()},
            {"tense": "Future Perfect", "sentence": f"{subject} will have {verb}ed {rest}".strip()},
            {"tense": "Future Perfect Continuous", "sentence": f"{subject} will have been {verb}ing {rest}".strip()}
        ]
    else:
        related = []

    # Hilangkan duplikasi
    unique_related = {r["tense"]: r for r in related if r["tense"] != base_tense}
    return list(unique_related.values())


# --------------------- MAIN ENDPOINT ---------------------
@app.post("/detect")
def detect(sentence_input: SentenceInput):
    sentence = sentence_input.sentence.strip()

    # 🔹 Cek grammar dulu sebelum deteksi tense
    grammar_result = check_grammar(sentence)
    if grammar_result["has_error"]:
        return grammar_result  # kirim hasil koreksi ke user

    # 🔹 Jika grammar benar → lanjut deteksi tense
    main_tense = detect_tense(sentence)
    related = generate_related_tenses(main_tense["tense"], sentence)

    # 🔹 Gabungkan hasil
    main_tense["related"] = related
    return main_tense
