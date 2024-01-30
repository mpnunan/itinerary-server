from itineraryapi.models import Admin
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    admin = Admin.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if admin is not None:
        data = {
            'id': admin.id,
            'uid': admin.uid,
            'name': admin.name,
            'bio': admin.bio
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the levelupapi_gamer table
    admin = Admin.objects.create(
        uid=request.data['uid'],
        name=request.data['name'],
        bio=request.data['bio'],
        
    )

    # Return the gamer info to the client
    data = {
        'id': admin.id,
        'uid': admin.uid,
        'name': admin.name,
        'bio': admin.bio
    }
    return Response(data)
