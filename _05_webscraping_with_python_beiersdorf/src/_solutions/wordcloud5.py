
from PIL import Image
mask = np.array(Image.open("../data/images/Hamburg_Umriss.png"))   #choose mask

# Create and generate a word cloud image:
wordcloud = WordCloud(
    background_color="white",
                    mask=mask,
                    max_words=150,
                    stopwords=stopwords,
                    width=800,
                    height=400,
                    mode="RGB",
                      random_state=42
                    ).generate(full_blog_texts)


# Display the generated image:
fig, ax = plt.subplots(figsize=(12,10))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off");
