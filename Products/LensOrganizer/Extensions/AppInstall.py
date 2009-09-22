from Products.CMFCore.utils import getToolByName

def install(self):
    # Re-purpose hack from LensMaker to disable the State tab for LensOrganizer
    pa = getToolByName(self, 'portal_actions') 
    action = pa.getActionObject('object_tabs/content_status_history')
    if action.condition.text.find('Lens Organizer') == -1:
        action.edit(condition=action.condition.text + " and object.Type() != 'Lens Organizer'")
