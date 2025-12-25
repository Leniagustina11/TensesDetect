function highlightSentence(sentence, tense) {
  let regex;

  switch (tense) {
    case "Simple Present":
      regex = /\b(do|does)\s+\w+\b|\b\w+(s|es)\b/gi;
      break;
    case "Present Continuous":
      regex = /\b(am|is|are)\s+(not\s+)?\w+ing\b/gi;
      break;
    case "Present Perfect":
      regex = /\b(has|have)\s+(not\s+)?(been\s+)?\w+(ed|d|t|en|n)\b/gi;
      break;
    case "Present Perfect Continuous":
      regex = /\b(has|have)\s+(not\s+)?been\s+\w+ing\b/gi;
      break;
    case "Simple Past":
      regex = /\b(did)\s+(not\s+)?\w+\b|\b\w+(ed)\b|\b(went|saw|ate|took|came|was|were)\b/gi;
      break;
    case "Past Continuous":
      regex = /\b(was|were)\s+(not\s+)?\w+ing\b/gi;
      break;
    case "Past Perfect":
      regex = /\bhad\s+(not\s+)?\w+(ed|d|t|en|n)\b/gi;
      break;
    case "Past Perfect Continuous":
      regex = /\bhad\s+(not\s+)?been\s+\w+ing\b/gi;
      break;
    case "Simple Future":
      regex = /\b(will)\s+(not\s+)?\w+\b/gi;
      break;
    case "Future Continuous":
      regex = /\b(will)\s+(not\s+)?be\s+\w+ing\b/gi;
      break;
    case "Future Perfect":
      regex = /\b(will)\s+(not\s+)?have\s+\w+(ed|d|t|en|n)\b/gi;
      break;
    case "Future Perfect Continuous":
      regex = /\b(will)\s+(not\s+)?have\s+been\s+\w+ing\b/gi;
      break;
    case "Simple Past Future":
      regex = /\b(would)\s+(not\s+)?\w+\b/gi;
      break;
    case "Past Future Continuous":
      regex = /\b(would)\s+(not\s+)?be\s+\w+ing\b/gi;
      break;
    case "Past Future Perfect":
      regex = /\b(would)\s+(not\s+)?have\s+\w+(ed|d|t|en|n)\b/gi;
      break;
    case "Past Future Perfect Continuous":
      regex = /\b(would)\s+(not\s+)?have\s+been\s+\w+ing\b/gi;
      break;
    default:
      return sentence;
  }

  return sentence.replace(regex, match => `<span class="highlight">${match}</span>`);
}
