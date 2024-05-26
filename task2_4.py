import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load the CSV file
df = pd.read_csv('/Users/vardanvij/Desktop/BigBasket Products.csv')
df = df.fillna('')
df['combined_features'] = df['product'] + " " + df['category'] + " " + df['sub_category'] + " " + df['brand'] + " " + df['sale_price'].astype(str)
count_matrix = CountVectorizer().fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(count_matrix)
def get_recommendations(product_name, cosine_sim=cosine_sim):
    if product_name not in df['product'].values:
        return "Product not found in the dataset."
    idx = df[df['product'] == product_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 similar products
    product_indices = [i[0] for i in sim_scores]
    return df['product'].iloc[product_indices]
product_name = 'Some Product Name'  
recommendations = get_recommendations(product_name)
print("Recommendations for {}: ".format(product_name))
print(recommendations)