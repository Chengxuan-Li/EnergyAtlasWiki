from types import SimpleNamespace

import hooks.wiki_metadata as wiki_metadata


def test_flatten_nav_pages_uses_nested_nav_order():
    first = SimpleNamespace(title="Home", url="index.html", meta={})
    second = SimpleNamespace(title="Guide", url="guide/", meta={})
    third = SimpleNamespace(title="API", url="api/", meta={})
    section = SimpleNamespace(children=[second, third])
    external_link = SimpleNamespace(title="External", url="https://example.com")

    pages = wiki_metadata.flatten_nav_pages([first, section, external_link])

    assert pages == [first, second, third]


def test_on_nav_sets_previous_and_next_article_metadata():
    first = SimpleNamespace(title="Home", url="index.html", meta={})
    second = SimpleNamespace(title="Guide", url="guide/", meta={})
    third = SimpleNamespace(title="API", url="api/", meta={})
    nav = SimpleNamespace(items=[first, SimpleNamespace(children=[second, third])])

    result = wiki_metadata.on_nav(nav, config={}, files=[])

    assert result is nav
    assert first.meta["previous_article"] is None
    assert first.meta["next_article"] == {"title": "Guide", "url": "guide/"}
    assert second.meta["previous_article"] == {"title": "Home", "url": "index.html"}
    assert second.meta["next_article"] == {"title": "API", "url": "api/"}
    assert third.meta["previous_article"] == {"title": "Guide", "url": "guide/"}
    assert third.meta["next_article"] is None


def test_on_page_context_sets_current_page_article_metadata_by_file_key():
    first = SimpleNamespace(title="Home", url="index.html", meta={}, file=SimpleNamespace(src_uri="index.md"))
    second = SimpleNamespace(title="Guide", url="guide/", meta={}, file=SimpleNamespace(src_uri="guide.md"))
    render_page = SimpleNamespace(title="Guide", url="guide/", meta={}, file=SimpleNamespace(src_uri="guide.md"))
    nav = SimpleNamespace(items=[first, second])

    context = wiki_metadata.on_page_context({}, page=render_page, config={}, nav=nav)

    assert context == {}
    assert render_page.meta["previous_article"] == {"title": "Home", "url": "index.html"}
    assert render_page.meta["next_article"] is None
