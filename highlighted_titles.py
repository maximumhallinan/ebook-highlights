def get_titles(highlights):
    titles = []

    for highlight in highlights:
        t = {}
        t['title'] = highlight['title']
        t['authors'] = highlight['authors']
        titles.append(t)

    return titles