from scrapy.item import Item, Field


class ScrapiesItem(Item):
    cast = Field()
    consumption_type = Field()
    content_type = Field()
    description = Field()
    director = Field()
    episode_count = Field()
    genre = Field()
    has_subtitles = Field()
    i_d = Field()
    languages = Field()  #
    meta_vendor = Field()
    meta_site = Field()
    meta_geo = Field()
    meta_pull_date = Field()
    network = Field()
    original_country = Field()  #
    original_title = Field()
    rating = Field()
    release_year = Field()
    request_url = Field()
    rights_holder = Field()  #
    season_count = Field()
    site_language = Field()
    studio = Field()
    tags = Field()  #
    title = Field()
    translated_title = Field()  #
    user_rating_average = Field()
    user_rating_max = Field()
    user_rating_count = Field()
