from django.urls import path


from . import views

urlpatterns = [
    # path('', views.allblogs, name='allblogs'),
    # path('<int:blog_id>/', views.detail, name = 'detail'),
    # path('', views.webcv ,name = 'webcv')
    # path('', )
    path('', views.graph, name='graph'),

    path("starter/", views.starter, name="starter"),
    path("combo/", views.combo, name="combo"),
    path("programming/", views.programming, name="programming"),
    path("multi_plot/", views.multi_plot, name="multi_plot"),
    path("products/", views.products, name="products"),
    path("pie/", views.pie, name="pie"),
    path("test_html/", views.test_html, name="test_html"),
]