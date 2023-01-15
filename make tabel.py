from tabulate import tabulate

data = [['name','man','age'],['ali','man','13'],
    ['hasan','man','15'],['sara','woman','20']
    ]

print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
