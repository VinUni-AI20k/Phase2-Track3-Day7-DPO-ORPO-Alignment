# Preference Alignment Experiment Report (Student Template)

*Instructions: Fill out this report as you complete the lab milestones. Replace all bracketed text `[like this]` with your own findings.*

## 1. Dataset Analysis & Cleaning

### Data Loading Summary
- **Total examples loaded**: `[count]`
- **Validation issues found**: `[e.g., Line 1 malformed JSON, unescaped quotes]`
- **Cleaning steps taken**: `[e.g., Fixed JSON syntax on line 1, implemented regex for quote escaping]`

### Split Strategy
- **Train/Val Ratio**: `[e.g., 80/20]`
- **Leakage Prevention**: `[Describe how you ensured same prompts didn't appear in both splits]`

## 2. Implementation: [DPO / ORPO]

### Objective Selection
- **Why this method?**: `[Rationale for choosing DPO or ORPO]`
- **Key Hyperparameters**:
    - `beta`: `[value]`
    - `lambda_orpo` (if applicable): `[value]`

### Numerical Stability
- **Challenges**: `[e.g., Handling log(0) or extreme logprob values]`
- **Solutions**: `[e.g., Clamping logprobs, using log1p]`

## 3. Evaluation Results

### Metrics
| Metric | Value |
|---|---|
| Pairwise Accuracy | `[%]` |
| Final Loss (Mock/Train) | `[value]` |

### Qualitative Review
- **Prompt**: `[Insert prompt]`
- **Chosen Response**: `[Text]`
- **Rejected Response**: `[Text]`
- **Model Preference**: `[Correct/Incorrect]`

## 4. Discussion & Failure Modes

- **What went well?**: `[observations]`
- **Observed Bias**: `[e.g., Did the model prefer shorter responses regardless of quality?]`
- **Safety**: `[How did the model handle the regression prompts in docs/regression_prompts.md?]`
