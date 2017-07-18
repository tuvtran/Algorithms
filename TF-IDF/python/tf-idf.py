# try writing tfidf from scratch
import math
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

document_0 = "China has a strong economy that is growing at a rapid pace. However politically it differs greatly from the US Economy."
document_1 = "At last, China seems serious about confronting an endemic problem: domestic violence and corruption."
document_2 = "Japan's prime minister, Shinzo Abe, is working towards healing the economic turmoil in his own country for his view on the future of his people."
document_3 = "Vladimir Putin is working hard to fix the economy in Russia as the Ruble has tumbled."
document_4 = "What's the future of Abenomics? We asked Shinzo Abe for his views"
document_5 = "Obama has eased sanctions on Cuba while accelerating those against the Russian Economy, even as the Ruble's value falls almost daily."
document_6 = "Vladimir Putin was found to be riding a horse, again, without a shirt on while hunting deer. Vladimir Putin always seems so serious about things - even riding horses."

all_documents = [
    document_0, document_1, document_2, document_3,
    document_4, document_5, document_6]


def tokenize(doc):
    return doc.lower().split(" ")


def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)


def sublinear_term_frequency(term, tokenized_document):
    tf = term_frequency(term, tokenized_document)
    return 1 + math.log(tf) if tf > 0 else 0


def augmented_term_frequency(term, tokenized_document):
    max_count = max([term_frequency(t, tokenized_document)
                    for t in tokenized_document])
    return (0.5 + ((0.5 * term_frequency(term, tokenized_document))/max_count))


def inverse_document_frequencies(tokenized_documents):
    idf_values = {}
    all_token_sets = set([item for sublist in tokenized_documents
                          for item in sublist])
    for tok in all_token_sets:
        # generate a list of booleans, those with True contain tokens
        # and otherwise
        contains_token = map(lambda doc:  tok in doc, tokenized_documents)
        # call sum on a boolean list returns the sum of True elements
        idf_values[tok] = 1 + \
            math.log(len(tokenized_documents)/sum(contains_token))
    return idf_values


def tfidf(documents):
    tokenized_documents = [tokenize(d) for d in documents]
    idf = inverse_document_frequencies(tokenized_documents)
    tfidf_documents = []
    for document in tokenized_documents:
        doc_tfidf = []
        for term in idf.keys():
            tf = sublinear_term_frequency(term, document)
            doc_tfidf.append(tf * idf[term])
        tfidf_documents.append(doc_tfidf)
    return tfidf_documents


if __name__ == "__main__":
    tfidf_rep = tfidf(all_documents)

    countvec = CountVectorizer(stop_words='english', min_df=1)
    X = countvec.fit_transform(all_documents)

    text_df = pd.DataFrame(
        data=X.toarray(),
        columns=countvec.get_feature_names()
    )
    text_df = text_df.where(text_df > 1).dropna()
    print(text_df)
