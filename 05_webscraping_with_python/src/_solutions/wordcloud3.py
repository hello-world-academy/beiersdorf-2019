
# Create and generate a word cloud image:
wordcloud = WordCloud(background_color="white",
                      max_words=80,
                      stopwords=stopwords,
                      mode="RGB",
                      relative_scaling=0.5,
                      random_state=42
                    ).generate(full_blog_texts)


# Display the generated image:
fig, ax = plt.subplots(figsize=(12,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off");
