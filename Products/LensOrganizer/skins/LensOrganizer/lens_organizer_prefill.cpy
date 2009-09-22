## Script (Python) "lens_prefill"
##parameters=
##
## Inject values into the request based on selected type, title, and creator (if available)

REQUEST = context.REQUEST
title = REQUEST.get('title', '')
#lenses = REQUEST.get('lensUID', None)

REQUEST.set('title', title)
#REQUEST.set('lenses', [lenses])

return state.set(status='success')
