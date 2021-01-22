import pandas as pd
import tea

## Preregistration: https://osf.io/rup7x/

## Run Tea on separate conditions
tea.data("data.csv")

variables = [
    # Dependent Variables
    {
        'name': 'accuracy',
        'data type': 'ratio',
        'range': [0, 1]
    },
    {
        'name': 'completion_time',
        'data type': 'interval'
    },
    {
        'name': 'confidence',
        'data type': 'ordinal',
        'range': [1, 2, 3, 4, 5]
    },

    # Independent Variables
    {
        'name': 'channel',
        'data type': 'nominal',
        'categories': ['scent_type', 'intensity', 'temperature', 'airflow']
    },
    {
        'name': 'data_type',
        'data type': 'nominal',
        'categories': ['ordinal', 'nominal', 'quantitative']
    }
]

tea.define_variables(variables)

study_design = {
    'study_type': 'experiment',
    'independent variables': ['data_type', 'channel'],
    'dependent variables': ['accuracy', 'completion_time', 'confidence']
}

tea.define_study_design(study_design)

assumptions = {
    'Type I (False Positive) Error Rate': 0.05
}

tea.assume(assumptions)

tea.hypothesize(['data_type', 'accuracy'], ['data_type: nominal > ordinal', 'data_type: nominal > quantitative'])
