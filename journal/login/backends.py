from login.models import CustomUser
from django.contrib.auth.backends import ModelBackend

class CustomBackend(ModelBackend):
    def authenticate(request, username, password):
        try:
            user = CustomUser.objects.get(email = username)
            success = user.check_password(password)
            if success:
                return user
            
        except CustomUser.DoesNotExist:
            pass
        return None
    
    def get_user(request, uid):
        try:
            return CustomUser.objects.get(pk = uid)
        
        except:
            return None