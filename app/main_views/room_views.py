from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Room
from ..forms import RoomForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete

'''
Room views
4 views for detials, create, update and delete
'''
class RoomDetailsView(LoginRequiredMixin,View):
    template = 'room/room_details.html'
    form = RoomForm
    success_url = reverse_lazy('room')
    type='غرفة'
    def get(self, request):
        room = Room.objects.all()
        ctx = {
            'rooms': room,
            'form': self.form(),
            'suc_url': self.success_url,
            'type': self.type
            }
        return render(request, self.template, ctx)
    def post(self, request):
        form = self.form(request.POST)

        print(request.POST)
        if not form.is_valid():
            ctx = {
                'form': form,
                'suc_url': self.success_url,
                'type':self.type
                }
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

class RoomCreate(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('room')
    type='غرفة'
    form = RoomForm
class RoomUpdate(LoginRequiredMixin, CRUDUpdate):
    model = Room
    success_url = reverse_lazy('room')
    template = 'add_update_form.html'
    form = RoomForm
    type='غرفة'
class RoomDelete(LoginRequiredMixin, CRUDDelete):
    model = Room
    success_url = reverse_lazy('room')
    form = RoomForm
    template = 'make_confirm_delete.html'
    type = 'غرفة'