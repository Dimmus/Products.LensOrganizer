from Products.Five.browser import BrowserView
from zope.interface import implements
from Acquisition import aq_inner
from interfaces import *
from Products.CMFCore.utils import getToolByName

class LensOrganizersView(BrowserView):

    implements(ILensOrganizersView)

    def getLensOrganizers(self):
        """
            Returns all lens organizers for the current Member
        """
        ltool = self.context.lens_tool
        path = self.context.getPhysicalPath()
        pc = getToolByName(self.context, 'portal_catalog')
        return pc(portal_type='LensOrganizer', 
                  sort_on='created', 
                  sort_order='ascending',
                  path=path) 

    __call__ = getLensOrganizers

class SiyavulaBioView(BrowserView):

    implements(ISiyavulaBioView )

    def getBio(self):
        pms = getToolByName(self, 'portal_membership')
        member = pms.getMemberById('siyavula')

        if member is not None:
            return '<br/>'.join(member.getProperty('biography'))

        return ''

    __call__ = getBio
