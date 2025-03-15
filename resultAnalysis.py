# import matplotlib.pyplot as plt

# # Data: Replace these with actual results
# attacks = ["Phishing", "Malware Injection", "SQL Injection", "Ransomware", "DDoS"]
# detection_accuracy = [90, 80, 72, 66, 70]  # Example data

# plt.figure(figsize=(8,5))
# plt.bar(attacks, detection_accuracy, color='blue')

# # Labels and title
# plt.xlabel("Types of Cyber Attacks", fontsize=12, fontweight='bold')
# plt.ylabel("Detection Accuracy (%)", fontsize=12, fontweight='bold')
# plt.title("FRONESIS Detection Accuracy for Different Cyber Attacks", fontsize=14, fontweight='bold')

# # Show graph
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Cyber attacks
attacks = ["Phishing", "Malware Injection", "SQL Injection", "Ransomware", "DDoS"]

# Performance metrics (Example values, replace with actual results)
detection_accuracy = [92, 85, 78, 70, 75]  # Percentage (%)
response_time = [200, 250, 300, 350, 400]  # Time in milliseconds (ms)
false_positive_rate = [5, 7, 10, 12, 8]  # Percentage (%)
computational_overhead = [20, 25, 30, 35, 28]  # Percentage (%)
threat_coverage = [95, 90, 85, 80, 88]  # Percentage (%)

# Bar width
bar_width = 0.15
x = np.arange(len(attacks))

# Creating the bar chart
plt.figure(figsize=(10, 6))

plt.bar(x - 2 * bar_width, detection_accuracy, width=bar_width, label="Detection Accuracy (%)", color="blue")
plt.bar(x - bar_width, response_time, width=bar_width, label="Response Time (ms)", color="red")
plt.bar(x, false_positive_rate, width=bar_width, label="False Positive Rate (%)", color="orange")
plt.bar(x + bar_width, computational_overhead, width=bar_width, label="Computational Overhead (%)", color="purple")
plt.bar(x + 2 * bar_width, threat_coverage, width=bar_width, label="Threat Coverage (%)", color="green")

# Labels and title
plt.xlabel("Cyber Attacks", fontsize=12, fontweight='bold')
plt.ylabel("Performance Metrics", fontsize=12, fontweight='bold')
plt.title("FRONESIS Cyber Attack Detection Performance", fontsize=14, fontweight='bold')

# X-axis labels and legend
plt.xticks(x, attacks, fontsize=10, fontweight='bold')
plt.legend()

# Display the graph
plt.show()
