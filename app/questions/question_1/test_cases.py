TEST_CASES = [{        
    "input": [
            {"name": "headache", "severity": 7, "frequency": 5},
            {"name": "fatigue", "severity": 3, "frequency": 2},
            {"name": "nausea", "severity": 5, "frequency": 5},
            {"name": "dizziness", "severity": 4, "frequency": 3},
            {"name": "blurred vision", "severity": 2, "frequency": 6}
        ],
        "expected": ["headache", "nausea", "dizziness"]
    },
    {
        "input": [
            {"name": "fever", "severity": 8, "frequency": 2},
            {"name": "sore throat", "severity": 5, "frequency": 4},
            {"name": "cough", "severity": 6, "frequency": 4},
            {"name": "runny nose", "severity": 3, "frequency": 5},
            {"name": "muscle pain", "severity": 4, "frequency": 4}
        ],
        "expected": ["cough", "muscle pain", "sore throat", "fever"]
    },
    {
        "input": [
            {"name": "insomnia", "severity": 6, "frequency": 1},
            {"name": "anxiety", "severity": 2, "frequency": 3},
            {"name": "irritability", "severity": 5, "frequency": 2}
        ],
        "expected": ["irritability", "insomnia"]
    },
    {
        "input": [
            {"name": "fatigue", "severity": 3, "frequency": 3},
            {"name": "drowsiness", "severity": 2, "frequency": 2}
        ],
        "expected": []
    }
]