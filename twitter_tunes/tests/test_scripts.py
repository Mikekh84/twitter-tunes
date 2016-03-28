import pytest

TEST_TRENDS = [
    (u'#EasterEggRoll', u'EasterEggRoll'),
    (u'#ArianaGrade', u'ArianaGrade'),
    (u'#mondaymotivation', u'mondaymotivation'),
    (u'Nick Swisher', u'Nick Swisher')
]


@pytest.mark.parametrize('trend, query', TEST_TRENDS)
def test_parse_trend(trend, query):
    from twitter_tunes.scripts import parser
    assert parser.parse_trend(trend) == query


def test_camel_trend():
    """Test Camel Case is correctly split."""
    from twitter_tunes.scripts import parser
    assert parser.parse_camel_trend(u'MyHotTrend') == u'My Hot Trend'


def test_camel_trend_acronym():
    """Test Acronyms are still grouped and split correctly."""
    from twitter_tunes.scripts import parser
    assert parser.parse_camel_trend(u'MTVEMA') == u'MTVEMA'
