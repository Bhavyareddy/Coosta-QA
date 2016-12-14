from rest_framework import routers
from coosta_users import views as user_views
from properties import views as property_views

router = routers.DefaultRouter()

# Users Router
router.register(r'users', user_views.UserViewSet)
router.register(r'user_profile', user_views.UserProfileViewSet, 'userprofile')

# Property Router
router.register(r'property', property_views.PropertyViewSet, 'property')
router.register(r'property_image', property_views.PropertyImagesViewSet, 'property_image')

# Groups Router
router.register(r'groups', user_views.GroupViewSet)
