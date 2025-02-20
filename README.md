# Motor Task Analysis Scripts

This repository contains four Python scripts designed to analyze motor task data (alternating between finger tapping and rest periods). When "TAP" appears on the screen, the participants are instructed to tap. During "REST," they stop tapping and relax their fingers. Each task contain 10 periods of tapping and 10 periods of rest. Each script processes reaction times, finger tapping sequences, and response patterns, providing insights into motor behavior. The experiments are executed using PsycoPy (v2024.1.1). The *.psyexp files can also be found in this repository. The output of PsycoPy is a .csv file. The codes are extracting relevant information from .csv files to assess reaction time and accuracy. 

## 📌 Motor Tasks Overview

### 1️⃣ Simple tapping analysis (`1. Simple tapping.docx`)

#### Task
Participants are instructed to tap the second button on the responce box with their index finger in response to auditory cues(1Hz-8Hz).
- 1st tapping block: 1HZ
- 2nd tapping block: 2HZ
- 3rd tapping block: 3HZ
- 4th tapping block: 4HZ
- 5th tapping block: 5HZ
- 6th tapping block: 6HZ
- 7th tapping block: 6.5HZ
- 8th tapping block: 7HZ
- 9th tapping block: 7.5HZ
- 10th tapping block: 8HZ
#### Outcome 
- reaction time (=auditory cue time - tap time)
- accuracy (each tap is assigned to the corresponding sound; if their is a tap matching the sound, the accuracy will be assigned to 1; if more then one tap is assigned to the sound, the accuracy will be assigned to 0.5; if no tap is assigned to the sound, the accuracy will be assigned to 0; the mean accuracy =sum(accurasy)/number of auditory cues per block)
 
### 2️⃣ Complex tapping analysis (`2. Complex tapping.docx`)

#### Task
Participants are instructed to tap the second button on the responce box with their index finger in response to auditory cues(1Hz-6Hz), while keeping the other 4 fingers on the corresponding buttons.The index finger taps are excluded, if any of the other 4 fingers were untapped.
- 1st tapping block: 1HZ
- 2nd tapping block: 2HZ
- 3rd tapping block: 2.5HZ
- 4th tapping block: 3HZ
- 5th tapping block: 3.5HZ
- 6th tapping block: 4HZ
- 7th tapping block: 4.5HZ
- 8th tapping block: 5HZ
- 9th tapping block: 5.5HZ
- 10th tapping block: 6HZ
#### Outcome 
- reaction time (=auditory cue time - tap time)
- accuracy (each tap is assigned to the corresponding sound; if their is a tap matching the sound, the accuracy will be assigned to 1; if more then one tap is assigned to the sound, the accuracy will be assigned to 0.5; if no tap is assigned to the sound, the accuracy will be assigned to 0; the mean accuracy =sum(accurasy)/number of auditory cues per block)

### 3️⃣ Simple Sequential Analysis (`3. Sequential simple.docx`)

#### Task
Participants are instructed to tap their fingers in sequence from the thumb to the pinky (Thumb → Index → Middle → Ring → Pinky) as quickly and accurately as possible, while keeping all the rest of their fingers on their corresponding buttons during the whole duration of the tapping block.
- Thumb index is 1
- Index index is 2
- Middle index is 3
- Ring index is 4
- Pinky index is 5
The correct pattern participants have to perform is [1,2,3,4,5]
#### Outcome 
- tapping pattern
- total errors (taps outside the main pattern)
- total taps
- error rate (total errors/total taps*100%)

### 4️⃣ Complex Sequential Analysis (`4. Sequential complex.docx`)

#### Task
Participants are instructed to tap their fingers in sequence from the thumb to the pinky (Thumb → Index → Middle → Ring → Pinky) as quickly and accurately as possible.
- Thumb index is 1
- Index index is 2
- Middle index is 3
- Ring index is 4
- Pinky index is 5
The correct pattern participants have to perform is [1,2,3,4,5].
The finger taps are excluded, if any of the other 4 fingers were untapped.
#### Outcome 
- tapping pattern
- total errors (taps outside the main pattern)
- total taps
- error rate (total errors/total taps*100%)

### 5️⃣ Index-Middle Sequential Analysis (`5. Index-Middle finger tapping.docx`)

#### Task
Participants are instructed to tap their fingers in sequence Index → Middle → Index → Middle... as quickly and accurately as possible.
- Index index is 2
- Middle index is 3
The correct pattern participants have to perform is [2,3].

#### Outcome 
- tapping pattern
- total errors (taps outside the main pattern)
- total taps
- error rate (total errors/total taps*100%)

## 🛠 Usage

1. Ensure you have Python installed (3.7 or later).
2. Ensure you have Anaconda Navigator installed.
3. Run Anaconda Navigator, from Anaconda GUI run Jypyter notebook.
4. Modify file paths in the scripts to match your dataset location.
5. Run the scripts by copy-pasting it to Jypyter notebook cell and press ctrl+enter

## 📊 Dependencies
- `pandas` for data manipulation.
- `numpy` for numerical computations.
- `matplotlib` for data visualization.

## 🤝 Contributions
Feel free to contribute by improving the analysis, adding visualization tools, or optimizing performance. Fork the repository, create a branch, and submit a pull request!

---

🚀 **Happy coding and data analyzing!**

