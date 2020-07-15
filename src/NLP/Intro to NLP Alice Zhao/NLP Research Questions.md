# NLP Research questions

|Question|Technique|Finding|
|---:|---|---|
|What are the most common words/terms in each text document?|Document-Term Matrix (DTM) & Term-Document Matrix (TDM)||
||`top50words_dict = {}`||
||`for each_document in tdm.columns:`||
||`top-n_list = tdm[each_document].sort_values(ascending=False).head(top-n)`||
||`top-n_dict[each_document] = list(zip(top-n_list.index, toptop-n_list.values))`||
||`top-n_dict.items()`||
|Does a particular word appear in any book?|`for each_document, top-n_list in top-n_dict.items():`|E.g., *book* appears in all but seven books|
||`print(each_document)`||
||`print(tdm.loc["word", :].sort_values(ascending=False))`||
||`print("Top 25 words: " + ', '.join([word for word, count in top50words[0:24]])`||
|What is the underlying theme of each book?|||
|What is the overarching sentiment of each book|||
|How rich is each book's vocabulary?|||
|How many sentences in each book?|||
|What are the most common words in each book?|||
