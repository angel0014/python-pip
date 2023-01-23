import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  plt.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()


def generate_pie_chart(labels, values):
  plt.pie(values, labels=labels)
  #plt.axis('equal')
  plt.savefig('chart_pie_final.png')
  plt.close()


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  generate_pie_chart(labels, values)