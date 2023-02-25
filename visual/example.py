import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5, 6]
y1 = [2, 4, 6, 10, 16, 18]

x2 = [3, 4, 7, 9]
y2 = [7, 10, 16, 18]

plt.plot(x1, y1, linestyle='--')
plt.plot(x2, y2, linestyle='dotted')

plt.xlabel('X')
plt.ylabel('Y')

plt.title("Test", fontsize=20, color='red', backgroundcolor='black')
plt.show()
