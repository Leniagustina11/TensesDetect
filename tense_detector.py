# tense_detector.py
import re

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

    # Fallback jika tidak cocok apa pun
    return {
        "tense": "Tidak dikenali",
        "description": "Tidak cocok dengan pola tenses yang tersedia.",
        "example": None
    }
