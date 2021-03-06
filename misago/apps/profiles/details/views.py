from misago.apps.profiles.decorators import profile_view
from misago.apps.profiles.template import RequestContext

@profile_view('user_details')
def details(request, user):
    return request.theme.render_to_response('profiles/details.html',
                                            context_instance=RequestContext(request, {
                                             'profile': user,
                                             'tab': 'details',
                                             }));
