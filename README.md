# Emotional Engagement in Narrative Medical Visualization

Quantitative analysis of electrodermal activity (EDA), eye-tracking, and questionnaire data investigating emotional engagement in narrative medical visualization.

The project analyzes physiological and behavioral responses to two interactive Hyperemesis gravidarum (HG) data stories:

- an individual character-driven narrative
- a generalized population-focused narrative

The repository contains selected preprocessing workflows, statistical analysis scripts, and summary datasets related to the accompanying master’s thesis.

---

## 💡 Research Goal

This project investigates how personalization and narrative framing influence emotional engagement in medical visualization.

The study explores whether including an individual protagonist representing a patient’s lived experience increases:

- physiological emotional arousal
- empathic emotional responses
- narrative engagement

compared to a generalized explanatory narrative.

---

## 🧪 Study Design

### Hypotheses

- H1: Including a fictitious individual protagonist increases emotional arousal.
- H2: The individual story elicits stronger negative empathic emotions.
- H3: Viewing order influences emotional engagement and physiological responses.

### Methodology

![Methodology workflow](./visualizations/methodology-workflow.png)

A mixed-methods study (N=26) combined:

- electrodermal activity (EDA)
- eye tracking
- questionnaires
  
to investigate emotional engagement dynamics, viewing behavior, and self-reported emotional responses.

Participants viewed two closely matched narrative visualization prototypes differing primarily in narrative framing:

- individual first-person perspective
- generalized third-person perspective

Time-resolved physiological analysis was used to identify emotionally salient story segments and visualization elements.

---

## ⚙️ Analysis Workflow

The project workflow follows four main stages:

1. data preparation
2. preprocessing and signal analysis
3. statistical evaluation
4. result visualization

### Electrodermal Activity (EDA)
- signal preprocessing
- phasic signal extraction
- peak detection
- temporal response aggregation
- summary metric generation

### Eye Tracking
- fixation analysis
- gaze behavior analysis
- area-of-interest evaluation

### Questionnaire Analysis
- emotional valence analysis
- engagement comparison
- statistical hypothesis testing

Statistical analysis was conducted in R using comparative statistical and mixed-effects approaches.

---

## 📊 Repository Contents

/data
/scripts
/statistics
/results

Included:

- summary-level EDA data
- questionnaire data
- selected preprocessing scripts
- statistical analysis workflows

Not included:

- raw biometric recordings
- identifiable participant data

--- 

## 📈 Results Overview

The results indicate stronger physiological responses associated with the individual character-driven narrative, particularly in peak-based EDA measures.

Questionnaire responses further suggest increased curiosity and negative empathic emotions for the individual story version.

Participants who viewed the individual story first tended to exhibit stronger overall emotional engagement responses.

---

## 📸 Visualizations

### EDA-related plots


<table>
  <tr>
    <td align="center">
      <img src="./results/eda_plots/ind-vs-gen.png" width="400"><br>
      <sub>Story perspective</sub>
    </td>
    <td align="center">
      <img src="./results/eda_plots/groups.png" width="400"><br>
      <sub>Participant groups</sub>
    </td>
  </tr>

  <tr>
    <td align="center">
      <img src="./results/eda_plots/gender.png" width="400"><br>
      <sub>Gender differences</sub>
    </td>
    <td align="center" style="background-color: white">
      <img src="./results/eda_plots/groups-parallelCoords.png" width="400"><br>
      <sub>Emotional arousal trajectories</sub>
    </td>
  </tr>
</table>

<br>

<p align="center">
  <img src="./results/eda_plots/matrix-ind+gen-first.png" width="600"><br>
  <sub>Aggregated emotional arousal during each story piece (slide) per participants</sub>
</p>


### Eye-tracking
[coming soon]

### Questionnaires
[coming soon]

---

## 🛠 Tech Stack

- Python
- R
- tidyverse, incl. ggplot2
- R statistics packages, e.g., stats, effectsize

---

## 🔬 Related Work

- [Master’s Thesis PDF](https://www.vismd.de/wp-content/uploads/2026/01/Beatrice-Budich_Masters-Thesis_2025.pdf)
- [Narrative Visualization Prototype Repository](https://github.com/bbdataviz/Visualizing-Untold-Stories-Through-a-Human-Lens)

---

## 🧠 What I Learned

[coming soon]

---

## 🔒 Data & Repository Scope

Due to participant privacy considerations and ethical restrictions, this repository contains:
- summary-level biometric data
- selected preprocessing scripts
- statistical analysis workflows

Raw eye-tracking recordings, physiological recordings, and identifiable participant data are not publicly distributed.

---

## 📄 License

This project is licensed under the MIT License. Copyright (c) 2026 Beatrice Budich
