from aethernetapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated user
    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    try:
        user = User.objects.get(uid=uid)

    # If authentication was successful, respond with their token
        data = {
            'id': user.id,
            'uid': user.uid,
            'email': user.email,
        }
        print(data)
        return Response(data)
    except:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the aethernetapi user table
    user = User.objects.create(
        uid=request.data['uid'],
        profile_image_url = request.data['profile_image_url'],
        email = request.data['email'],
        last_login = request.data['last_login'],
    )

    # Return the user info to the client
    data = {
            'id': user.id,
            'uid': user.uid,
            'bio': user.bio
    }
    return Response(data)
