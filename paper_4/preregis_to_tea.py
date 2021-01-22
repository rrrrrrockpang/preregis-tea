import tea

## Preregistration: https://osf.io/tdby5
## Fisher r-toz transformation
## didn't use NHST. used interval estimation instead.

## Run Tea on separate conditions
tea.data("data.csv")

variables = [
    # Dependent Variables
    {
        'name': 'accuracy_rate',
        'data type': 'radio',
        'range': [0, 1]
    },
    {
        'name': 'time',
        'data type': 'interval'
    },
    # Independent Variables
    {
        'name': 'visualizations',
        'data type': 'nominal',
        'categories': ['single_map', 'small-multiples', 'animated']
    },
    {
        'name': 'tasks',
        'data type': 'nominal',
        'categories': ['distance', 'direction', 'spatial_continuity', 'speed', 'peak']
    }
]

tea.define_variables(variables)

study_design = {
    'study type': 'experiment',
    'independent variables': ['visualizations', 'tasks'],
    'dependent variables': ['accuracy_rate', 'time']
}

tea.define_study_design(study_design)

# Question to ask Eunice. Is this the right way to specify multiple variables?
tea.hypothesize(['visualizations', 'accuracy'], ['visualizations: single_map > small-multiples',
                                                 'visualizations: single_map > animated',
                                                 'visualizations: small-multiples > animated'])  #with interaction
