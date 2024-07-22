import matplotlib.pyplot as plt

causes = ["Lack of study and preparation", "Poor time management", "Lack of understanding of course material", "Procrastination", "Poor attendance", "Inadequate test-taking skills", "Distractions from social media and technology", "Lack of interest in the subject", "Personal/family issues", "Health problems"]
frequencies = [25, 20, 15, 10, 8, 7, 5, 4, 3, 3]

cumulative_frequencies = []
cumulative_frequency = 0

for frequency in frequencies:
    cumulative_frequency += frequency
    cumulative_frequencies.append(cumulative_frequency)

total = cumulative_frequency
percentages = [100 * freq / total for freq in frequencies]
cumulative_percentages = [100 * cfreq / total for cfreq in cumulative_frequencies]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(causes, frequencies, color="C0")
ax1.set_ylabel("Frequency", color="C0")
ax1.tick_params(axis="y", labelcolor="C0")

ax2 = ax1.twinx()

ax2.plot(causes, cumulative_percentages, color="C1", marker="o")
ax2.set_ylabel("Cumulative Percentage", color="C1")
ax2.tick_params(axis="y", labelcolor="C1")

ax1.set_xticklabels(causes, rotation=90)

plt.title("Pareto Chart of Possible Causes for a Student to Fail a Final Examination in a University Course")
plt.show()
