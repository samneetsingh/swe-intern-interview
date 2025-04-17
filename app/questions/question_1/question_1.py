"""
Question: Filter Symptoms by Severity and Sort by Frequency

Context:
You're building a backend service for a digital health assistant that tracks user-reported symptoms. 
Each symptom report includes the symptom name, its severity (on a 1-10 scale), and how often it has 
been mentioned historically by the user.

You are given a list of symptom entries, where each symptom entry is a dictionary with the following keys:
	•	"name": a string representing the symptom name
	•	"severity": an integer from 1 to 10
	•	"frequency": an integer representing how many times the user has mentioned this symptom before

Your goal is to filter out low-severity symptoms (any with severity < 4) and return a sorted list of symptom names, ordered by:
	1.	Highest frequency first
	2.	If frequencies are equal, sort alphabetically by name

-----------------------------------------------------------------------------------------------------------------------------------------
Example 1:

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
"""


def filter_and_sort_symptoms(symptoms: list[dict]) -> list[str]:
    pass