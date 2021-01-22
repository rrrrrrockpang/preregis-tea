import tea

## Preregistration: https://aspredicted.org/blind.php?x=tf7y5r
## Fisher r-toz transformation

## Run Tea on separate conditions
tea.data("data.csv")

variables = [
    # Dependent Variables
    {
        'name': 'recognize_website',
        'data type': 'ordinal',
        'range': [0, 1]
    },
    {
        'name': 'trust_score',
        'data type': 'ordinal',
        'categories': [1, 2, 3, 4, 5]
    },
    {
        'name': 'added_line',
        'data type': 'nominal',
        'categories': ['0', '1']
    },
    {
        'name': 'sources',
        'data type': 'nominal',
        'categories': ['mainstream', 'partisan', 'fake']
    }
]

tea.define_variables(variables)

study_design = {
    'study type': 'experiment',
    'independent variables': ['added_line', 'sources'],
    'dependent variables': 'trust_score'
}

tea.define_study_design(study_design)

# Question to ask Eunice. Is this the right way to specify multiple variables?
tea.hypothesize(['added_line', 'sources', 'trust_score'], ['trust_score ~ added_line + sources + added_line*sources'])  #with interaction
