from django.urls import path

from . import views
urlpatterns = [
    path('addEmpPage',views.addEmpPage,name='addEmpPage'),
    path('insert',views.insert,name='insert'),
    path('show',views.show,name='show'),
    path('editEmp/<int:eid>',views.editEmp,name="editEmp"),
    path('updateEmp/<int:eid>',views.updateEmp,name="updateEmp"),
    path('deleteEmp/<int:eid>',views.deleteEmp,name="deleteEmp"),
]