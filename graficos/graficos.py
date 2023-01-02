import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200,14,120]
    fig, ax = plt.subplots()
    plt.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
