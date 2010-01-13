## addtolensorganizer.cpy : Driver to add a lens to a lens organizer
##parameters=
from Products.CMFCore.utils import getToolByName

REQUEST = context.REQUEST

organizer_uid = REQUEST.get('organizeruid' , 'NEW')

if organizer_uid == 'NEW':
    REQUEST.RESPONSE.redirect( context.absolute_url() + '/create_lens_organizer?lenses:list=' + context.UID())
else:
    pc = getToolByName(context, 'portal_catalog')
    query = {'UID' : organizer_uid }
    brains = pc(query)
    if brains:
        ob = brains[0].getObject()
        lenses = ob.getLenses()
        lenses.append(context.UID())
        ob.setLenses(lenses)
        REQUEST.RESPONSE.redirect(ob.absolute_url())

