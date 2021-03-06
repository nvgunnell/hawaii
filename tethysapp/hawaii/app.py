from tethys_sdk.base import TethysAppBase, url_map_maker


class Hawaii(TethysAppBase):
    """
    Tethys app class for Hawaii.
    """

    name = 'Hawaii'
    index = 'hawaii:home'
    icon = 'hawaii/images/island.jpg'
    package = 'hawaii'
    root_url = 'hawaii'
    color = '#003366'
    description = 'An app to estimate mass flux on the Hawaiian Islands'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hawaii',
                controller='hawaii.controllers.home'
            ),
            UrlMap(
                name='background',
                url='background',
                controller='hawaii.controllers.background'
            ),
            UrlMap(
                name='mockups',
                url='mockups',
                controller='hawaii.controllers.mockups'
            ),
            UrlMap(
                name='proposal',
                url='proposal',
                controller='hawaii.controllers.proposal'
            ),
            UrlMap(
                name='Geoprocess',
                url='Geoprocess',
                controller='hawaii.controllers.Geoprocess'
            ),
            UrlMap(
                name='teambios',
                url='teambios',
                controller='hawaii.controllers.teambios'
            ),
            UrlMap(
                name='data',
                url='data',
                controller='hawaii.controllers.data'
            )
        )

        return url_maps
