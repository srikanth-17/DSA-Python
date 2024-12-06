"""def con(s):
    d=[int(i) for i in str(s)]
    return sum(d)
def main():
    n=int(input())
    for i in range(n):
        a=[x for x in input().split()]
        for n in a:
            print(con(str(n)))
if __name__=="__main__":
    main()"""

"""l=[1,2,3,4,5]
x=l.pop(0)
print(l,x)"""

import matplotlib.pyplot as plt

# Define the metrics and their efficiency scores
metrics = [
    "Relevance to Academics",
    "User Trust and Transparency",
    "Community Engagement",
    "Resource Accessibility",
    "User Navigation and Usability"
]
scores = [9, 9.5, 8.5, 9, 8.8]

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(metrics, scores, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

# Adding labels and title
plt.title("Efficiency Metrics of Proposed System")
plt.xlabel("Efficiency Metrics")
plt.ylabel("Efficiency Score (0-10)")
plt.ylim(0, 10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
