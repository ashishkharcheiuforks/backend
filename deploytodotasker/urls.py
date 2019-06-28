from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_social_oauth2.views import RevokeTokenView

from deploytodotaskerapp import views, apis


class MyRevokeTokenView(RevokeTokenView):
    def post(self, request, *args, **kwargs):
        print('request', request)
        print('request.META', request.META)
        print('request.data', request.data)
        print('request._request.GET', request._request.GET)
        print('request._request.POST', request._request.POST)

        return super().post(request, *args, **kwargs)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    # Registration
    url(r'^registration/login/$', auth_views.LoginView.as_view(),
        {'template_name': 'registration/login.html'},
        name = 'registration-login'),
    url(r'^registration/sign-out', auth_views.LogoutView.as_view(),
        {'next_page': '/'},
        name = 'registration-sign-out'),
    url(r'^registration/sign-up', views.registration_sign_up,
        name = 'registration-sign-up'),
    url(r'^registration/$', views.registration_home, name = 'registration-home'),

    url(r'^registration/account/$', views.registration_account, name = 'registration-account'),
    url(r'^registration/meal/$', views.registration_meal, name = 'registration-meal'),
    url(r'^registration/meal/add/$', views.registration_add_meal, name = 'registration-add-meal'),


    url(r'^registration/meal/edit/(?P<meal_id>\d+)/$', views.registration_edit_meal, name = 'registration-edit-meal'),
    url(r'^registration/order/$', views.registration_order, name = 'registration-order'),
    url(r'^registration/report/$', views.registration_report, name = 'registration-report'),

    url(r'^api/social/revoke-token/?$', MyRevokeTokenView.as_view(), name="revoke_token"),

    # Sign In/ Sign Up/ Sign Out
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token (sign in/ sign up)
    # /revoke-token (sign out)
    url(r'^api/registration/order/notification/(?P<last_request_time>.+)/$', apis.registration_order_notification),


    # APIs for CUSTOMERS
    url(r'^api/customer/registrations/$', apis.customer_get_registrations),
    url(r'^api/customer/meals/(?P<registration_id>\d+)/$', apis.customer_get_meals),
    url(r'^api/customer/order/add/$', apis.customer_add_order),
    url(r'^api/paytm/response/', apis.response, name = 'responsetm'),
    url(r'^api/customer/order/latest/$', apis.customer_get_latest_order),
    url(r'^api/customer/driver/location/$', apis.customer_driver_location),


    # APIs for DRIVERS
    url(r'^api/driver/orders/ready/$', apis.driver_get_ready_orders),
    url(r'^api/driver/order/pick/$', apis.driver_pick_order),
    url(r'^api/driver/order/latest/$', apis.driver_get_latest_order),
    url(r'^api/driver/order/complete/$', apis.driver_complete_order),
    url(r'^api/driver/revenue/$', apis.driver_get_revenue),
    url(r'^api/driver/location/update/$', apis.driver_update_location),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
