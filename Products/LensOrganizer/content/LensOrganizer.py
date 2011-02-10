"""
LensOrganizer.py - AT Content type that represents a Lens Organizer

Author: Johan Beyers , Francois Lubbe 
(C) 2008 Rice University

This software is subject to the provisions of the GNU Lesser General
Public License Version 2.1 (LGPL).  See LICENSE.txt for details.

"""

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.LensOrganizer.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import DisplayList
##/code-section module-header

schema = Schema((

    ReferenceField(
        name='lenses',
        widget=MultiSelectionWidget(
            format="checkbox",
            label='Lenses',
            label_msgid='LensOrganizer_label_lenses',
            i18n_domain='LensOrganizer',
        ),  
        multiValued=True,
        relationship="lenses_lensorganizers",
        vocabulary='lensesVocab',
        default=[]
    ), 

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

LensOrganizer_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
field = LensOrganizer_schema['description']
field.schemata = 'default'
##/code-section after-schema

class LensOrganizer(BaseContent):
    """
    Lens Organizer Archetype

    Contains references to Lenses and is situated in the member's
    lensfolder
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'Lens Organizer'

    meta_type = 'LensOrganizer'
    portal_type = 'LensOrganizer'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'LensOrganizer.gif'
    immediate_view = 'lensorganizer_view'
    default_view = 'lensorganizer_view'
    suppl_views = ()
    typeDescription = "LensOrganizer"
    typeDescMsgId = 'description_edit_lensorganizer'

    _at_rename_after_creation = True

    schema = LensOrganizer_schema

    ##code-section class-header #fill in your manual code here
    aliases = {
        '(Default)'  : PROJECTNAME.lower() + '_view',
        'base_view'  : PROJECTNAME.lower() + '_view',
        'view'       : PROJECTNAME.lower() + '_view',
        'edit'       : 'base_edit',
        }

    ##/code-section class-header

    # Methods
    def getPublicOpenLenses(self):
        """
        Return a list of all Open Public lenses
        """
        wftool = getToolByName(self, 'portal_workflow')
        lenses = []
        for lens in self.getLenses():
            if wftool.getInfoFor(lens, 'review_state') == 'published_open':
                lenses.append(lens)
        return lenses

    def lensesVocab(self):
        """
        Build a vocabulary from the member's lenses
        """
        tool = getToolByName(self, 'lens_tool')
        li = []
        for brain in tool.getListsOwned():
            # We must fetch the object since the brains do not have 
            # UID as metadata.
            li.append((brain.getObject().UID(), brain.Title))
        return DisplayList(li)

    def showEditableBorder(self, *args, **kwargs):
        """
        Never show edit controls
        """
        return False

    def getIcon(self, *args, **kwargs):
        return 'transparent.gif'

registerType(LensOrganizer, PROJECTNAME)
# end of class LensOrganizer

##code-section module-footer #fill in your manual code here
def modify_fti(fti):
    for a in fti['actions']:
        if a['id'] not in ('view', 'edit'):
            a['visible'] = 0 
    return fti
##/code-section module-footer



