

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),   # This is homepage i.e., local host port 8000 with index view
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),   # The url will have the
    # slug of this object, and we are capturing it in detailed view
    path('blog/', views.BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),  # same for this slug too
]
