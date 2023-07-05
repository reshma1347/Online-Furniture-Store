from app import forms
from app.forms import LoginForm
from django.contrib import auth
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordConfirmForm, MyPasswordResetForm

urlpatterns = [
   
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
    

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password__reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MyPasswordConfirmForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('chair/', views.chair, name='chair'),
    path('chair/<slug:data>', views.chair, name='chairdata'),
    path('table/', views.table, name='table'),
    path('table/<slug:data>', views.table, name='tabledata'),
    path('sofa/', views.sofa, name='sofa'),
    path('sofa/<slug:data>', views.sofa, name='sofadata'),
    path('officechair/', views.officechair, name='officechair'),
    path('officechair/<slug:data>', views.officechair, name='officechairdata'),
    path('officetable/', views.officetable, name='officetable'),
    path('officetable/<slug:data>', views.officetable, name='officetabledata'),
    path('officesofa/', views.officesofa, name='officesofa'),
    path('officesofa/<slug:data>', views.officesofa, name='officesofadata'),
    path('kidsbed/', views.kidsbed, name='kidsbed'),
    path('kidsbed/<slug:data>', views.kidsbed, name='kidsbeddata'),
    path('kidsseating/', views.kidsseating, name='kidsseating'),
    path('kidsseating/<slug:data>', views.kidsseating, name='kidsseatingdata'),
    path('kidsstudy/', views.kidsstudy, name='kidsstudy'),
    path('kidsstudy/<slug:data>', views.kidsstudy, name='kidsstudydata'),
    

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login' ),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('customerregistration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.payment_done, name='paymentdone'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
