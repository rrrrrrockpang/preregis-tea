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
tea.data("data/show_both_stats.csv", key="worker_id")

variables = [
    {
        'name': 'condition',
        'data type': 'nominal',
        'categories': ['SE', 'SD']
    },
    {
        'name': 'wtp_final',
        'data type': 'interval'
    },
    {
        'name': 'superiority_special',
        'data type': 'ratio',
        'range': [0, 1]
    }
]

tea.define_variables(variables)

study_design = {
    'study_type': 'experiment',
    'independent variables': ['condition', 'text_condition'],
    'dependent variables': ['wtp_final', 'superiority_special']
}

tea.define_study_design(study_design)

assumptions = {
    'Statistical Test': "Student's T Test",
    'Type I (False Positive) Error Rate': 0.05
}

tea.assume(assumptions)

tea.hypothesize(['condition', 'wtp_final'], ['condition: SE > SD'])
# tea.hypothesize(['condition', 'superiority_special'], ['condition: SE > SD'])
