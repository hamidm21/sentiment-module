# **Twitter Preprocessing Unit**
# remove urls
# remove usernames
# remove hashtags
# character normalization
# Punctuation, special characters and numbers
# Lower casing
import preprocessor as p


def cleaner(content):
    clean = [0] * len(content)

    # forming a separate feature for cleaned tweets
    for i, v in enumerate(content['Text']):
        # tweets.loc[v,"Text"] = p.clean(i)
        clean[i] = p.clean(v)

    content['Clean'] = clean
    return content
