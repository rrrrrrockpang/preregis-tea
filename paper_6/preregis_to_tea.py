import pandas as pd
import tea

## Preregistration: https://osf.io/bmer9/
## Split Dataset at https://github.com/jhofman/visual-effects-chi2020/tree/master
# df = pd.read_csv('data/df.csv', index_col=0)
# for i, g in df.groupby('text_condition'):
#     name = 'data/' + i + '.csv'
#     g.to_csv(name)
#################################################

## Run Tea on separate conditions
tea.data("data.csv")

variables = [
    # Dependent Variables
    {
        'name': 'NASA-TLX',
        'data type': 'interval'
    },
    {
        'name': 'UEQ',
        'data type': 'interval'
    },
    {
        'name': 'pleasure_item',
        'data type': 'interval'
    },

    # Independent Variables
    {
        'name': 'dh',
        'data type': 'nominal',
        'categories': ['0', '1']
    },
    {
        'name': 'vis',
        'data type': 'nominal',
        'categories': ['0', '1']
    },
    {
        'name': 'ch',
        'data type': 'nominal',
        'categories': ['0', '1']
    }
]

tea.define_variables(variables)

study_design = {
    'study_type': 'experiment',
    'independent variables': ['dh', 'vis', 'ch'],
    'dependent variables': ['NASA-TLX', 'UEQ', 'pleasure_item']
}

tea.define_study_design(study_design)

assumptions = {
    'Type I (False Positive) Error Rate': 0.05
}

tea.assume(assumptions)

tea.hypothesize(['NASA-TLX', 'dh', 'vis'], ['NASA-TLX ~ dh * vis'])
