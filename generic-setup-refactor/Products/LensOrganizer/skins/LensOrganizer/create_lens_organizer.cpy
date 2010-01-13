## create_lens_organizer.py : Driver to create a new lens organizer
##parameters=

from AccessControl import Unauthorized

REQUEST = context.REQUEST

ltool = context.lens_tool
namedfolder = ltool.getIndividualFolder()
member = context.portal_membership.getAuthenticatedMember()
if str(member) == 'Anonymous User':
    raise Unauthorized

if not context.restrictedTraverse('@@siyavula-account')():
    raise Unauthorized

type_name = "LensOrganizer"
tmpid = context.generateUniqueId(type_name)

fullname = member.getProperty('fullname', None)
if fullname: 
    REQUEST.set('title' , "%s's Lens Organizer" % fullname)

o = namedfolder.restrictedTraverse('portal_factory/' + type_name + '/' + tmpid )
return state.set(context=o)
