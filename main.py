#%%
from advertools import crawl
import pandas as pd
# crawl('https://www.nike.com/nike-by-you','nike.jl',follow_links=True)
# df = pd.read_json('nike.jl', lines=True)
df = pd.read_pickle('nike.pkl')
#%%