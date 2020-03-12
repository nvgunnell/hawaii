from tethys_sdk.base import TethysAppBase, url_map_maker


class Hawaii(TethysAppBase):
    """
    Tethys app class for Hawaii.
    """

    name = 'Hawaii'
    index = 'hawaii:home'
    icon = 'hawaii/images/icon.gif'
    package = 'hawaii'
    root_url = 'hawaii'
    color = '#f39c12'
    description = ''
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
                name='proposal',
                url='proposal',
                controller='hawaii.controllers.proposal'
            )
        )

        return url_maps
