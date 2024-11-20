/// ========== Variables ==========

#let name = "{}"
#let username = "{}"
#let stats = (
  Anxiety: {},
  Normal: {},
  Depression: {},
  Suicidal: {},
  Stress: {},
)

/// ========== Evaluation ==========

#let maxVal = calc.max(..stats.values())      
#let diagnosis = stats.pairs().filter(x => x.at(1) == maxVal).at(0).at(0)

#let dataset = (
  Anxiety: (
    points: ("Practice deep breathing exercises or mindfulness meditation daily to calm your mind.", "Break tasks into smaller, manageable steps to reduce overwhelm.", "Engage in physical activities, like yoga or walking, to release tension and stress."),
    links: ("https://youtu.be/iX6qn9fuxY4?si=sl45-oSnChkuQau-", "https://www.youtube.com/watch?v=_KuUXz5gjgw", "https://adaa.org/"),
    response: "Signs of anxiety are evident, characterized by feelings of restlessness and unease."
  ),
  Normal: (
    points: ("Maintain a balanced routine that includes work, leisure, and relaxation.", "Practice gratitude by noting three positive things each day.", "Stay socially connected by spending time with friends or loved ones."),
    links: ("https://youtu.be/v7AYKMP6rOE?si=whsUZfjZ5Ys2TmEL", "https://www.ted.com/"),
    response: "Responses indicate a balanced emotional state without significant signs of distress."
  ),
  Depression: (
    points: ("Seek support from a trusted friend or a mental health professional.", "Set small, achievable goals to regain a sense of accomplishment.", "Incorporate physical exercise or hobbies you once enjoyed into your routine.I"),
    links: ("https://youtu.be/I_AxR-aHKaQ?si=-T3G1wxEKLCOMF3m", "https://www.youtube.com/watch?v=d96akWDnx0w", "https://www.youtube.com/watch?v=Xm_2zmX6Akc"),
    response: "Traits of depression are demonstrated, including persistent low mood and a lack of interest in activities."
  ),
  Suicidal: (
    points: ("Reach out to a crisis hotline or trusted individual immediately for support.", "Remove any means of self-harm from your surroundings and focus on your safety.", "Engage in grounding activities, such as listening to music or writing your thoughts, to shift focus."),
    links: ("https://www.youtube.com/watch?v=ZebSXPUCPFc", "https://www.ted.com/", "https://discord.com/"),
    response: "The analysis suggests critical levels of distress with potential suicidal ideation."
  ),
  Stress: (
    points: ("Identify and prioritize tasks using techniques like to-do lists or time management.", "Dedicate 15-30 minutes daily to relaxation exercises, such as progressive muscle relaxation.", "Take short breaks during the day to recharge your energy."),
    links: ("https://youtu.be/tYddPTEfS_8?si=w_35X1kmjlKaTQit", "https://www.youtube.com/watch?v=_KuUXz5gjgw", "https://adaa.org/"),
    response: "Indications of stress are present, likely caused by overwhelming pressure or external challenges."
  ),
)

#let data = dataset.at(diagnosis)

/// ========== Template ==========
#let today = datetime.today()
#let reportDate = str(today.day()) + " / " + str(today.month()) + " / " + str(today.year())

#set page(
  fill: rgb("#F1F0EF"),
  margin: (
    x: 0pt,
    y: 10pt
  )
)

#let bg = rgb("#2C2A32")
#let fg = rgb("235347")

#let bar(title, value) = [
  #box(width: 100pt, height: 210pt)[
    #text(size: 20pt)[#title]
    #align(bottom + center)[
      #rect(width: 80pt, height: value * 1.5pt, fill: fg, inset: 10pt)
      #text(size: 16pt)[#value%]
    ]
  ]
]

#stack(
  dir: ltr,
  spacing: 1fr,
  box(fill: bg, height: 100pt, width: 150pt, inset: 20pt)[
    #align(right)[
      #text(fill: white, size: 15pt)[Virtual Assistant]
    ]
    #align(center)[
      #image(
        "logo.png",
        height: 50pt
      )
    ]
  ],
  box(inset: 30pt)[
    #align(center)[
      #text(fill: fg, size: 60pt)[User Report]
    ]
  ]
)

#box(inset: 30pt, width: 100%)[
  #stack(
    dir: ltr,
    spacing: 1fr,
    text(fill: fg, size: 30pt)[#name],
    text(fill: fg, size: 30pt)[\@#username]
  )
]

#box(inset: 30pt, width: 100%)[
  #align(center)[
    #text(fill: black, size: 30pt)[Analysis Report]
  ]
]

#align(center)[
  #stack(
    dir: ltr,
    spacing: 30pt,
    for each in stats.keys() [
      #bar(each, stats.at(each))
    ]
  )
]

/// ========== Diagnosis ==========

#align(center)[
  #text(size: 20pt)[*#dataset.at(diagnosis).at("response")*]
]

#box(inset: 20pt)[
  #for point in data.at("points") [
    + #point
  ]
  = Refer these links:
  #for eachLink in data.at("links") [
    - #link(eachLink)[#eachLink]
  ]
]

#align(center)[Report generated on *#reportDate*]