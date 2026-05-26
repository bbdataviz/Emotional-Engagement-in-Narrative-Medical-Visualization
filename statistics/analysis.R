library(tidyverse)
library(lsr)
library(effsize)
library(psych)
library(epitools)

# story level
Eda_summary = read.csv("https://raw.githubusercontent.com/bbdataviz/Emotional-Engagement--Biometric-Data-Analysis/refs/heads/main/data/Eda-summary-arousalmean-HG.csv")

# filter
# ALL
summary_all_ind <- Eda_summary %>%
  filter(story == "ind")

summary_all_gen <- Eda_summary %>%
  filter(story == "xgen")

# STORY 1 (between-subjects)
summary_story1 <- Eda_summary %>%
  filter((Group == "A" & story == "ind") | (Group == "B" & story == "xgen"))

summary_story1_ind <- Eda_summary %>%
  filter(Group == "A" & story == "ind")

summary_story1_gen <- Eda_summary %>%
  filter(Group == "B" & story == "xgen")

# STORY 2 (between-subjects)
summary_story2 <- Eda_summary %>%
  filter((Group == "A" & story == "xgen") | (Group == "B" & story == "ind"))

summary_story2_ind <- Eda_summary %>%
  filter(Group == "A" & story == "xgen")

summary_story2_gen <- Eda_summary %>%
  filter(Group == "B" & story == "ind")

# Groups (between groups)
summary_A <- Eda_summary %>%
  filter(Group == "A")

summary_B <- Eda_summary %>%
  filter(Group == "B")

# Group A (inbetween groups)
summary_A_ind <- summary_A %>%
  filter(story == "ind")

summary_A_gen <- summary_A %>%
  filter(story == "xgen")

# Group B (inbetween-subjects)
summary_B_ind <- summary_B %>%
  filter(story == "ind")

summary_B_gen <- summary_B %>%
  filter(story == "xgen")

# H1: Electrodermal Activity Data (Individual vs General Story)

# STORY 1 (Normal distribution test (shapiro))
shapiro.test(summary_story1$amp_per_min) # p-value = 0.02054 *
shapiro.test(summary_story1$max_peak) # p-value = 0.08115 normal
shapiro.test(summary_story1$max_amp_sum) # p-value = 0.2534 normal
shapiro.test(summary_story1$viewtime_sec) # p-value = 0.3665 normal

# amp_per_min
wilcox.test(amp_per_min ~ story, data = summary_story1, exact=FALSE, alternative="greater") # p-value = 0.1383
effsize::cliff.delta(summary_story1_ind$amp_per_min, summary_story1_gen$amp_per_min) # (small) * Cliff's delta = 0.28 [-0.23, 0.67]
t.test(amp_per_min ~ story, data = summary_story1) # mean(ind) = 2.210499 > mean(gen) = 1.357255

# max_peak
t.test(max_peak ~ story, data = summary_story1, alternative="greater") # p-value = 0.03945 *, mean(ind) = 1.0544647 > mean(gen) = 0.7275706
cohensD(summary_story1_ind$max_peak, summary_story1_gen$max_peak) # 0.7769332 (medium) ** 
cohen.d(max_peak ~ story, data = summary_story1) # 0.81 (large) *** Cohen's d = 0.81, 95% CI [-0.07, 1.68]

# max_sum of amplitudes in a story piece
t.test(max_amp_sum ~ story, data = summary_story1, alternative="greater") # p-value = 0.03002 *, mean(ind) = 3.000319 > mean(gen) = 1.741413
cohensD(summary_story1_ind$max_amp_sum, summary_story1_gen$max_amp_sum) # 0.8228378 (large) ***
cohen.d(max_amp_sum ~ story, data = summary_story1) # 0.86 (large) *** Cohen's d = 0.86, 95% CI [-0.03, 1.73]

# view_time
t.test(viewtime_sec ~ story, data = summary_story1, alternative="greater") # p-value = 0.09556, mean(ind) = 519 > mean(gen) = 441
cohensD(summary_story1_ind$viewtime_sec, summary_story1_gen$viewtime_sec) # 0.5882119 (medium) **
cohen.d(viewtime_sec ~ story, data = summary_story1) # Cohen's d = 0.62, 95% CI [-0.25, 1.47]

describe(summary_story1_ind)
describe(summary_story1_gen)

# Story elements analysis (Eye-Tracking)

story_element = read.csv("https://raw.githubusercontent.com/bbdataviz/Emotional-Engagement--Biometric-Data-Analysis/refs/heads/main/data/story-element_char_illu.csv")

story_element_ind <- story_element %>%
  filter(Group == 'char_ind')

story_element_genx <- story_element %>%
  filter(Group == 'char_genx')

chisq.test(story_element$Group, story_element$value) # p-value = 0.001232
riskratio(story_element$Group, story_element$value, conf.level = 0.95)

describe(story_element_ind) # M = 0.21, SD = 0.4
describe(story_element_genx) # M = 0.1, SD = 0.29 

###
# H2: Negative empathic emotions (Self-reported on a multiple-choice questionnaire with 20 emotions)

emotions <- read.csv("https://raw.githubusercontent.com/bbdataviz/Emotional-Engagement--Biometric-Data-Analysis/refs/heads/main/data/emotions-valence-sad-depressed-miserable-anxious.csv")
emotions_ind <- emotions %>%
  filter(story == "ind")
emotions_gen <- emotions %>%
  filter(story == "xgen")

wilcox.test(value ~ story, data = emotions, exact=FALSE, alternative="greater") # p-value = 0.009357**
effsize::cliff.delta(emotions_ind$value, emotions_gen$value) # 0.2758291 (small)
t.test(value ~ story, data = emotions) # 3.035714 > 1.517857
describe(emotions_ind)
describe(emotions_gen)

# curious
emotions <- read.csv("https://raw.githubusercontent.com/bbdataviz/Emotional-Engagement--Biometric-Data-Analysis/refs/heads/main/data/emotions-storypieces-first.csv")
emotions_ind <- emotions %>%
  filter(story == "ind")
emotions_gen <- emotions %>%
  filter(story == "xgen")

wilcox.test(curious ~ story, data = emotions, exact=FALSE, alternative="greater") # p-value = 0.029
effsize::cliff.delta(emotions_ind$curious, emotions_gen$curious) # large Cliff's delta = 0.42, 95% CI [-0.03, 0.73]
t.test(curious ~ story, data = emotions) # 16.78 > 12.14
describe(emotions_ind) # sd = 6.58
describe(emotions_gen) # sd = 5.46

###
# H3: Priming Effects (Electrodermal Activity)
shapiro.test(Eda_summary$amp_per_min) # p-value = 0.005452 **
shapiro.test(Eda_summary$max_peak) # p-value = 0.008969 **
shapiro.test(Eda_summary$max_amp_sum) # p-value = 0.1516 normal
shapiro.test(Eda_summary$viewtime_sec) # p-value = 0.7293 normal

# amp_per_min
wilcox.test(amp_per_min ~ Group, data = Eda_summary, exact=FALSE, alternative="greater") # p-value = 0.1321
effsize::cliff.delta(summary_A$amp_per_min, summary_B$amp_per_min) # delta estimate: 0.2077295 (small) Cliff's delta = 0.20, 95% CI [-0.15, 0.52]
t.test(amp_per_min ~ Group, data = Eda_summary) # mean(A) = 2.350317 > mean(B) = 1.539308

# max_peak
wilcox.test(max_peak ~ Group, data = Eda_summary, exact=FALSE, alternative="greater") # p-value = 0.01153 *
effsize::cliff.delta(summary_A$max_peak, summary_B$max_peak) # delta estimate: 0.4202899 (medium) ** Cliff's delta = 0.42, 95% CI [0.05, 0.68]
t.test(max_peak ~ Group, data = Eda_summary) # mean(A) = 1.10 > mean(B) = 0.81
describe(summary_A) # sd = 0.39
describe(summary_B) # sd = 0.38

# max_sum of amplitudes in a story piece
t.test(max_amp_sum ~ Group, data = Eda_summary, alternative="greater") # p-value = 0.005*, mean(A) = 2.83 > mean(B) = 1.76
cohensD(summary_A$max_amp_sum, summary_B$max_amp_sum) # 0.8077011 (large) ***
cohen.d(max_amp_sum ~ Group, data = Eda_summary) # Cohen's d = 0.83, 95% CI [0.18, 1.47]

# view_time
t.test(viewtime_sec ~ Group, data = Eda_summary, alternative="greater") # p-value = 0.04585 *, mean(A) = 453 > mean(B) = 370
cohensD(summary_A$viewtime_sec, summary_B$viewtime_sec) # 0.5494011 (medium) **
cohen.d(viewtime_sec ~ Group, data = Eda_summary) # Cohen's d = 0.56, 95% CI [-0.07, 1.19]
