from zope.interface import Interface
from zope.app.publisher.interfaces.browser import IBrowserView

class ILensOrganizersView(IBrowserView):
    """ 
    LensOrganizers view
    """

    def getLensOrganizers(self):
        """
            Returns all lens organizers for the current Member
        """

class ISiyavulaBioView(IBrowserView):
    """ 
    SiyavulaBioView view
    """

    def getBio(self):
        """
        Return bio of siyavula member
        """
