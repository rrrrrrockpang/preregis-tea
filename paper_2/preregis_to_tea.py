import tea

## Preregistration: https://aspredicted.org/ek2bm.pdf

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
        'name': 'confidence_reading_vis',
        'data type': 'ordinal',
        'categories': [1, 2, 3, 4, 5, 6, 7]
    },
    {
        'name': 'confidence_in_the_tool',
        'data type': 'ordinal',
        'categories': [1, 2, 3, 4, 5, 6, 7]
    },
    {
        'name': 'confidence_reading_model',
        'data type': 'ordinal',
        'categories': [1, 2, 3, 4, 5, 6, 7]
    },
    {
        'name': 'cognitive_load',
        'data type': 'interval',
        'range': [0, 100]
    },
    {
        'name': 'deployment_score',
        'data type': 'ordinal',
        'categories': [1, 2, 3, 4, 5, 6, 7]
    },
    {
        'name': 'suspicion_data',
        'data type': 'nominal',
        'categories': ['0', '1']
    },
    {
        'name': 'suspicion_tool',
        'data type': 'nominal',
        'categories': ['0', '1']
    },

    # Independent Variables
    {
        'name': 'interpretability_tool',
        'data type': 'nominal',
        'categories': ['SHAP', 'GAMs']
    },
    {
        'name': 'explanations',
        'data type': 'nominal',
        'categories': ['normal', 'manipulated']
    }
]

tea.define_variables(variables)

study_design = {
    'study type': 'experiment',
    'independent variables': ['interpretability_tool', 'explanations'],
    'dependent variables': ['accuracy', 'confidence_reading_vis', 'confidence_in_the_tool', 'confidence_reading_vis',
                            'cognitive_load', 'deployment_score', 'suspicion_data', 'suspicion_tool']
}

tea.define_study_design(study_design)

tea.hypothesize(['explanations', 'accuracy'], ['explanations:normal != manipulated'])
