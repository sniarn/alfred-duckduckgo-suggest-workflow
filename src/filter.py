# encoding: utf-8

import sys
from workflow import Workflow3, web
from workflow.util import utf8ify

SUGGEST_URL = "https://duckduckgo.com/ac/"
GITHUB_SLUG = "sniarn/alfred-duckduckgo-suggest-workflow"


def retrieve_suggestions(query):
    r = web.get(url=SUGGEST_URL, params={'q': query})
    r.raise_for_status()
    return r.json()


def add_suggestion(suggestion):
    suggestion = utf8ify(suggestion)
    wf.add_item(
        title=suggestion,
        subtitle='Search DuckDuckGo for "{}"'.format(suggestion),
        arg=suggestion,
        valid=True,
        largetext=suggestion)


def main(wf):
    query = wf.args[0]
    suggestions = retrieve_suggestions(query)
    for suggestion in suggestions:
        add_suggestion(suggestion['phrase'])
    if not suggestions:
        add_suggestion(query)
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow3(
        update_settings={'github_slug': GITHUB_SLUG},
        help_url='https://github.com/{}'.format(GITHUB_SLUG))
    if wf.update_available:
        wf.start_update()
    else:
        sys.exit(wf.run(main))
