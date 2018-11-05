from pathlib import Path

def SaveArticle(article, url):
    art_id = url.rstrip('/').split('/')[-1]
    # Rudimentary sanity check on the article ID
    ### REMOVED THIS LINE FROM ORIGINAL SCRIPT TODO rewrite if needed
    # TODO: rewrite the below possibly to use ticker and date in path
    art_file = Path('../content', art_id + '.html')
    with open(art_file, 'w') as f:
        s = []
        for node in article.contents:
            # TODO: rewrite to prune results
            s.append(str(node))
        f.write('\n'.join(s))
    return
