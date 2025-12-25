// Data semua tenses + gambar
const tenseInfo = {
  "Simple Present": {
    positive: {
      formula: "Subject + Verb 1 (s/es)",
      examples: [
        "She writes a letter every day.",
        "I go to school at 7 AM.",
        "They play football every weekend."
      ]
    },
    negative: {
      formula: "Subject + do/does not + Verb 1",
      examples: [
        "She does not write a letter every day.",
        "I do not go to school at 7 AM.",
        "They do not play football every weekend."
      ]
    },
    interrogative: {
      formula: "Do/Does + Subject + Verb 1?",
      examples: [
        "Does she write a letter every day?",
        "Do you go to school at 7 AM?",
        "Do they play football every weekend?"
      ]
    }
  },

  "Present Continuous": {
    positive: {
      formula: "Subject + is/are/am + Verb-ing",
      examples: [
        "They are playing football.",
        "I am reading a book now.",
        "She is cooking in the kitchen."
      ]
    },
    negative: {
      formula: "Subject + is/are/am + not + Verb-ing",
      examples: [
        "They are not playing football.",
        "I am not reading a book now.",
        "She is not cooking in the kitchen."
      ]
    },
    interrogative: {
      formula: "Is/Are/Am + Subject + Verb-ing?",
      examples: [
        "Are they playing football?",
        "Am I reading a book now?",
        "Is she cooking in the kitchen?"
      ]
    }
  },

  "Present Perfect": {
    positive: {
      formula: "Subject + have/has + Verb 3",
      examples: [
        "I have finished my homework.",
        "She has visited Paris twice.",
        "They have already eaten dinner."
      ]
    },
    negative: {
      formula: "Subject + have/has not + Verb 3",
      examples: [
        "I have not finished my homework.",
        "She has not visited Paris twice.",
        "They have not eaten dinner."
      ]
    },
    interrogative: {
      formula: "Have/Has + Subject + Verb 3?",
      examples: [
        "Have you finished your homework?",
        "Has she visited Paris twice?",
        "Have they eaten dinner?"
      ]
    }
  },

  "Present Perfect Continuous": {
    positive: {
      formula: "Subject + have/has been + Verb-ing",
      examples: [
        "She has been studying for three hours.",
        "I have been waiting since morning.",
        "They have been playing games all day."
      ]
    },
    negative: {
      formula: "Subject + have/has not been + Verb-ing",
      examples: [
        "She has not been studying for three hours.",
        "I have not been waiting since morning.",
        "They have not been playing games all day."
      ]
    },
    interrogative: {
      formula: "Have/Has + Subject + been + Verb-ing?",
      examples: [
        "Has she been studying for three hours?",
        "Have you been waiting since morning?",
        "Have they been playing games all day?"
      ]
    }
  },

  "Simple Past": {
    positive: {
      formula: "Subject + Verb 2",
      examples: [
        "He visited Bali last year.",
        "I watched a movie yesterday.",
        "They bought a new car last week."
      ]
    },
    negative: {
      formula: "Subject + did not + Verb 1",
      examples: [
        "He did not visit Bali last year.",
        "I did not watch a movie yesterday.",
        "They did not buy a new car last week."
      ]
    },
    interrogative: {
      formula: "Did + Subject + Verb 1?",
      examples: [
        "Did he visit Bali last year?",
        "Did you watch a movie yesterday?",
        "Did they buy a new car last week?"
      ]
    }
  },

  "Past Continuous": {
    positive: {
      formula: "Subject + was/were + Verb-ing",
      examples: [
        "I was watching TV when she called.",
        "They were playing football at 5 PM.",
        "She was reading a book all evening."
      ]
    },
    negative: {
      formula: "Subject + was/were not + Verb-ing",
      examples: [
        "I was not watching TV when she called.",
        "They were not playing football at 5 PM.",
        "She was not reading a book all evening."
      ]
    },
    interrogative: {
      formula: "Was/Were + Subject + Verb-ing?",
      examples: [
        "Was I watching TV when she called?",
        "Were they playing football at 5 PM?",
        "Was she reading a book all evening?"
      ]
    }
  },

  "Past Perfect": {
    positive: {
      formula: "Subject + had + Verb 3",
      examples: [
        "They had left before the storm came.",
        "I had finished the task before the deadline.",
        "She had eaten before he arrived."
      ]
    },
    negative: {
      formula: "Subject + had not + Verb 3",
      examples: [
        "They had not left before the storm came.",
        "I had not finished the task before the deadline.",
        "She had not eaten before he arrived."
      ]
    },
    interrogative: {
      formula: "Had + Subject + Verb 3?",
      examples: [
        "Had they left before the storm came?",
        "Had you finished the task before the deadline?",
        "Had she eaten before he arrived?"
      ]
    }
  },

  "Past Perfect Continuous": {
    positive: {
      formula: "Subject + had been + Verb-ing",
      examples: [
        "He had been working there for 5 years.",
        "I had been studying for two hours before dinner.",
        "They had been waiting for an hour when the bus arrived."
      ]
    },
    negative: {
      formula: "Subject + had not been + Verb-ing",
      examples: [
        "He had not been working there for 5 years.",
        "I had not been studying for two hours before dinner.",
        "They had not been waiting for an hour when the bus arrived."
      ]
    },
    interrogative: {
      formula: "Had + Subject + been + Verb-ing?",
      examples: [
        "Had he been working there for 5 years?",
        "Had you been studying for two hours before dinner?",
        "Had they been waiting for an hour when the bus arrived?"
      ]
    }
  },

"Simple Future": {
  positive: {
    formula: "Subject + will + Verb1",
    examples: [
      "She will go to the market tomorrow.",
      "I will help you with your homework.",
      "They will arrive at 8 o’clock."
    ]
  },
  negative: {
    formula: "Subject + will not (won’t) + Verb1",
    examples: [
      "She will not go to the market tomorrow.",
      "I will not help you with your homework.",
      "They won’t arrive at 8 o’clock."
    ]
  },
  interrogative: {
    formula: "Will + Subject + Verb1?",
    examples: [
      "Will she go to the market tomorrow?",
      "Will you help me with my homework?",
      "Will they arrive at 8 o’clock?"
    ]
  }
},

"Future Continuous": {
  positive: {
    formula: "Subject + will be + Verb-ing",
    examples: [
      "I will be studying at 7 p.m.",
      "She will be cooking dinner when you arrive.",
      "They will be playing football tomorrow afternoon."
    ]
  },
  negative: {
    formula: "Subject + will not be + Verb-ing",
    examples: [
      "I will not be studying at 7 p.m.",
      "She will not be cooking dinner when you arrive.",
      "They will not be playing football tomorrow afternoon."
    ]
  },
  interrogative: {
    formula: "Will + Subject + be + Verb-ing?",
    examples: [
      "Will you be studying at 7 p.m.?",
      "Will she be cooking dinner when I arrive?",
      "Will they be playing football tomorrow afternoon?"
    ]
  }
},

"Future Perfect": {
  positive: {
    formula: "Subject + will have + Verb3",
    examples: [
      "I will have finished my work by 5 p.m.",
      "She will have graduated by next year.",
      "They will have arrived before the meeting starts."
    ]
  },
  negative: {
    formula: "Subject + will not have + Verb3",
    examples: [
      "I will not have finished my work by 5 p.m.",
      "She will not have graduated by next year.",
      "They will not have arrived before the meeting starts."
    ]
  },
  interrogative: {
    formula: "Will + Subject + have + Verb3?",
    examples: [
      "Will you have finished your work by 5 p.m.?",
      "Will she have graduated by next year?",
      "Will they have arrived before the meeting starts?"
    ]
  }
},

"Future Perfect Continuous": {
  positive: {
    formula: "Subject + will have been + Verb-ing",
    examples: [
      "By next month, I will have been working here for 3 years.",
      "She will have been studying for 5 hours by noon.",
      "They will have been traveling for two weeks by the time you see them."
    ]
  },
  negative: {
    formula: "Subject + will not have been + Verb-ing",
    examples: [
      "By next month, I will not have been working here for 3 years.",
      "She will not have been studying for 5 hours by noon.",
      "They will not have been traveling for two weeks by the time you see them."
    ]
  },
  interrogative: {
    formula: "Will + Subject + have been + Verb-ing?",
    examples: [
      "Will you have been working here for 3 years by next month?",
      "Will she have been studying for 5 hours by noon?",
      "Will they have been traveling for two weeks by the time you see them?"
    ]
  }
},

"Past Future": {
  positive: {
    formula: "Subject + would + Verb1",
    examples: [
      "He said he would call me tomorrow.",
      "I knew she would come to the party.",
      "They promised they would help us."
    ]
  },
  negative: {
    formula: "Subject + would not (wouldn’t) + Verb1",
    examples: [
      "He said he would not call me tomorrow.",
      "I knew she would not come to the party.",
      "They promised they wouldn’t help us."
    ]
  },
  interrogative: {
    formula: "Would + Subject + Verb1?",
    examples: [
      "Would he call you tomorrow?",
      "Would she come to the party?",
      "Would they help us?"
    ]
  }
},

"Past Future Perfect": {
  positive: {
    formula: "Subject + would have + Verb3",
    examples: [
      "He said he would have finished the task by yesterday.",
      "I knew she would have graduated by 2020.",
      "They promised they would have arrived on time."
    ]
  },
  negative: {
    formula: "Subject + would not have + Verb3",
    examples: [
      "He said he would not have finished the task by yesterday.",
      "I knew she would not have graduated by 2020.",
      "They promised they would not have arrived on time."
    ]
  },
  interrogative: {
    formula: "Would + Subject + have + Verb3?",
    examples: [
      "Would he have finished the task by yesterday?",
      "Would she have graduated by 2020?",
      "Would they have arrived on time?"
    ]
  }
},

"Past Future Perfect Continuous": {
  positive: {
    formula: "Subject + would have been + Verb-ing",
    examples: [
      "He said he would have been working for 5 hours by then.",
      "I knew she would have been studying all night.",
      "They said they would have been traveling for a week."
    ]
  },
  negative: {
    formula: "Subject + would not have been + Verb-ing",
    examples: [
      "He said he would not have been working for 5 hours by then.",
      "I knew she would not have been studying all night.",
      "They said they would not have been traveling for a week."
    ]
  },
  interrogative: {
    formula: "Would + Subject + have been + Verb-ing?",
    examples: [
      "Would he have been working for 5 hours by then?",
      "Would she have been studying all night?",
      "Would they have been traveling for a week?"
    ]
  }
},

"Simple Past Future": {
  positive: {
    formula: "Subject + should + Verb1",
    examples: [
      "He said I should go to school early.",
      "She told me I should take some rest.",
      "They said we should join them."
    ]
  },
  negative: {
    formula: "Subject + should not + Verb1",
    examples: [
      "He said I should not go to school early.",
      "She told me I should not take some rest.",
      "They said we should not join them."
    ]
  },
  interrogative: {
    formula: "Should + Subject + Verb1?",
    examples: [
      "Should I go to school early?",
      "Should I take some rest?",
      "Should we join them?"
    ]
  }
}
}


const tenseToImage = {
  "Simple Present": "simplePresent.png",
  "Present Continuous": "presentCon.png",
  "Present Perfect": "presentPerfect.png",
  "Present Perfect Continuous": "presentPerfectCon.png",
  "Simple Past": "simplePast.png",
  "Past Continuous": "pastCon.png",
  "Past Perfect": "pastPerfect.png",
  "Past Perfect Continuous": "pastPerfectCon.png",
  "Simple Future": "simpleFuture.png",
  "Future Continuous": "futureCon.png",
  "Future Perfect": "futurePerfect.png",
  "Future Perfect Continuous": "futurePerfectCon.png",
  "Simple Past Future": "simPastFut.png",
  "Past Future Continuous": "pastFutCon.png",
  "Past Future Perfect": "pastFutPerfect.png",
  "Past Future Perfect Continuous": "pastFutPerfectCon.png"
};
