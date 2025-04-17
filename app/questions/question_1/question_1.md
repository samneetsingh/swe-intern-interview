### Context

You're building a backend service for a digital health assistant that tracks user-reported symptoms. Each symptom report includes the symptom name, its severity (on a 1–10 scale), and how often it has been mentioned historically by the user.

---

You are given a list of symptom entries, where each symptom entry is a dictionary with the following keys:

- `name` : a string representing the symptom name  
- `severity` : an integer from 1 to 10  
- `frequency` : an integer representing how many times the user has mentioned this symptom before

Your goal is to filter out low-severity symptoms (any with severity < 4) and return a sorted list of symptom names, ordered by:
1. Highest frequency first  
2. If frequencies are equal, sort alphabetically by name

---

### Task

Write a function `filter_and_sort_symptoms` that:
1. Filters out symptoms with severity less than 4
2. Sorts by highest frequency, then by name alphabetically

### Example 1

```python
Input:
    symptoms = [
        {"name": "headache", "severity": 7, "frequency": 5},
        {"name": "fatigue", "severity": 3, "frequency": 2},
        {"name": "nausea", "severity": 5, "frequency": 5},
        {"name": "dizziness", "severity": 4, "frequency": 3},
        {"name": "blurred vision", "severity": 2, "frequency": 6}
    ]

Output:
    ["headache", "nausea", "dizziness"]
```

### Example 2
```python
Input:
    symptoms = [
        {"name": "fever", "severity": 8, "frequency": 2},
        {"name": "sore throat", "severity": 5, "frequency": 4},
        {"name": "cough", "severity": 6, "frequency": 4},
        {"name": "runny nose", "severity": 3, "frequency": 5},
        {"name": "muscle pain", "severity": 4, "frequency": 4}
    ]

Output:
    ["cough", "muscle pain", "sore throat", "fever"]
```       