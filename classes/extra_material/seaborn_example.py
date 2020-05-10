import seaborn as sns


# How does seaborn know how to compute the confidence interval
# for a line plot?

# Observe this data carefully
fmri = sns.load_dataset("fmri")

sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data=fmri)

# Let's see what each group contains
fmri.groupby(["region", "event"])["timepoint"].get_group(("frontal", "stim"))
# Many samples per x value, so seaborn simply calculates the STD for us
