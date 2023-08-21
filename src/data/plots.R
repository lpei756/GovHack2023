plot.df <- read.csv("C:/Users/adamg/some_Gov_Hack/predicted_sentiments_plot_data - predicted_sentiments.csv.csv")
head(plot.df)

library(ggplot2)

install.packages("RColorBrewer")
library(RColorBrewer)

display.brewer.all()



# Define the colors from the Set1 palette
my_colors <- brewer.pal(10, "Pastel1")

# Map them to your sentiments. Ensure the order matches.
color_mapping <- c("negative" = my_colors[1], "neutral" = my_colors[5], "positive" = my_colors[3])

# Create the plot
ggplot(data = plot.df, aes(x = platform, fill = Predicted_Sentiment)) +
  geom_bar(position = "dodge") +
  labs(x = "Platform", y = "Count", title = "Sentiment Distribution by Platform", fill = "Sentiment") +
  scale_fill_manual(values = color_mapping) +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5))


