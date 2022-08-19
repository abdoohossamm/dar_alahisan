from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from reports.models import SessionReporter,StudentReporter
from app.models import Session, Student
from django.contrib.auth.mixins import LoginRequiredMixin
from app.generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from django.urls import reverse_lazy
from reports.forms import SessionReporterForm, StudentReporterCreateForm, StudentReporterUpdateForm
from django.views import View
from reports.filters import SessionReporterFilter
from django.db.models import Q
from django.core.paginator import Paginator
from app.functions import ITEM_PER_PAGE
from django.http import HttpResponseRedirect
'''
functions to help in views
'''
def create_student_for_session_report(form, session):
    session_report = get_object_or_404(SessionReporter.objects.all().select_related('session', 'session__teacher', 'session__day'), session=session, session_date=form.cleaned_data['session_date']) 
    student_in_sessions = StudentSessions.objects.filter(session=form.cleaned_data['session']).select_related('student')
    for student in student_in_sessions:
        student_report = StudentReporter(student=student.student, session_report= session_report)
        student_report.save()
'''
Views
'''

# Create your views here.
class SessionReportView(LoginRequiredMixin, View):
    template = 'reports/session/session_report.html'
    success_url = reverse_lazy('reports:session_report')
    model = SessionReporter
    type = 'تقرير'
    myfilter = SessionReporterFilter
    
    def session_report_search(self,request, item:int=10):
        strval =  request.GET.get("search", False)
        page_number = request.GET.get('page')
        if strval :
            query = Q(report__icontains=strval) 
            query.add(Q(review_report__icontains=strval), Q.OR)
            session_report = SessionReporter.objects.filter(query).select_related(
                'session', 'session__teacher', 'session__day').order_by('-session_date')
            myfilter = SessionReporterFilter(request.GET, queryset=session_report)
            return {
                'search': strval,
                'session_reports': session_report,
                'page_obj': session_report,
                'filter': myfilter,
            }

        else :
            session_report = SessionReporter.objects.all().select_related(
                'session', 'session__teacher', 'session__day').order_by('-session_date')
        myfilter = SessionReporterFilter(request.GET, queryset=session_report)
        session_report = myfilter.qs
        paginator = Paginator(session_report, item) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)
        return {
                'search': strval,
                'session_reports': session_report,
                'page_obj': page_obj,
                'filter': myfilter,
        }
    # GET method response
    def get(self, request):
        
        search = self.session_report_search(request, ITEM_PER_PAGE)
        ctx={
            'session_reports': search['session_reports'],
            'search': search['search'],
            'page_obj':search['page_obj'],
            'type':self.type,
            'filter': search['filter'],
            'search_bar': True,
            'suc_url': self.success_url,
            
        }
        return render(request, self.template, ctx)


class StudentReportDetailView(LoginRequiredMixin, View):
    template = 'reports/session/session_report_detail.html'
    form = SessionReporterForm        
    def get(self, request, session_pk, month=None, year=None):
        session = get_object_or_404(Session, pk=session_pk)
        form = self.form(initial={'session':session_pk})
        success_url = reverse_lazy('reports:session_report', kwargs={'session_pk':session_pk})
        if month and year:
            session_report = SessionReporter.objects.filter(session=session, session_date__year=year, session_date__month=month).select_related('session', 'session__teacher', 'session__day')
        elif year:
            session_report = SessionReporter.objects.filter(session=session, session_date__year=year).select_related('session', 'session__teacher', 'session__day')
        else:
            session_report = SessionReporter.objects.filter(session=session).select_related('session', 'session__teacher', 'session__day')
        ctx={
            'session': session,
            'session_reports': session_report,
            'month': month,
            'year': year,
            'suc_url': success_url,
            'form': form,
        }
        return render(request, self.template, ctx)
    def post(self, request, session_pk, month=None, year=None):
        session = get_object_or_404(Session, pk=session_pk)
        success_url = reverse_lazy('reports:session_report', kwargs={'session_pk':session_pk})
        if month and year:
            session_report = SessionReporter.objects.filter(session=session, session_date__year=year, session_date__month=month).select_related('session', 'session__teacher', 'session__day')
        else:
            session_report = SessionReporter.objects.filter(session=session).select_related('session', 'session__teacher', 'session__day', 'session__name')
        form = self.form(request.POST)        
        if not form.is_valid():
            ctx = {
                'session': session,
                'session_reports': session_report,
                'month': month,
                'year': year,
                'suc_url': success_url,
                'form': form,
                }
            return render(request, self.template, ctx)
        form.save()
        create_student_for_session_report(form, session)
        return redirect(success_url)




from app.models import StudentSessions
from app.functions import check_suc_url
from reports.filters import StudentReporterFilter
from reports.forms import StudentAttendForm
class StudentAttendSessionView(LoginRequiredMixin,View):
    template = 'reports/session/student_attend_session.html'
    form = StudentReporterCreateForm
    type = 'طالب' 
    def get(self, request, session_report, next='', **kwargs):
        session_report = get_object_or_404(SessionReporter.objects.all().select_related(
            'session', 'session__teacher', 'session__day', 'session__name'),
                                        pk=session_report
                                        )
        students_report = StudentReporter.objects.filter(session_report=session_report).select_related(
            'session_report', 'student').order_by('pk')
        form = self.form(initial= {'session_report':session_report})
        success_url = reverse_lazy('reports:student_session_attend', kwargs={'session_report':session_report})
        ctx={
            'students_reports': students_report,
            'session_report': session_report,
            'suc_url': success_url,
            'form': form,
            'type':self.type,
        }
        return render(request, self.template, ctx)
    def post(self,request, session_report, next=''):
        success_url = reverse_lazy('reports:student_session_attend', kwargs={'session_report':session_report})
        session_report = get_object_or_404(SessionReporter.objects.all().select_related(
            'session', 'session__teacher', 'session__day', 'session__name'),
                                        pk=session_report
                                        )
        students_report = StudentReporter.objects.filter(session_report=session_report).select_related(
            'session_report', 'student').order_by('pk')
        # POST method conditions
        if 'attend_status' in request.POST: # Change attend status form
            instance_data = StudentReporter.objects.get(pk=request.POST['student_report'])
            instance_data.attend = request.POST['attend_status']
            instance_data.save()
        elif 'paybox' or 'uncheck' in request.POST: # Change pay status form
            instance_data = StudentReporter.objects.get(pk=request.POST['student_report'])
            if request.POST.get('paybox'):
                paybox = int(request.POST['paybox'])
                if paybox == 10:
                    instance_data.money = 10
            if request.POST.get('uncheck'):
                print('done')
                instance_data.money = None
            instance_data.save()
        else: # Add student Form
            form = self.form(request.POST, initial= {'session_report':session_report})
            if not form.is_valid():
                ctx = {
                    
                'students_reports': students_report,
                'session_report': session_report,
                'suc_url': success_url,
                'form': form,
                'type':self.type,
                    }
                return render(request, self.template, ctx)
            form.save()
        return redirect(success_url)

def change_student_attend_status(request, pk, change=0, next=''):
    print('function')
    model = StudentReporter
    
    # instance_data = get_object_or_404(model, pk=pk)
    instance_data = StudentReporter.objects.get(pk=pk)
    if change == 0:
        instance_data.update(attend='حضور')
        instance_data.save()
        print('done')
    elif change == 1:
        instance_data.attend = 'غياب'
        instance_data.save()
        print('done')
        
    return HttpResponseRedirect(next)
    
class StudentReportView(LoginRequiredMixin, View):
    template = 'reports/student/student_report.html'
    form = StudentReporterCreateForm
    type = 'طالب'
    def get(self, request, *args, **kwargs):
        student = kwargs.pop('student', None)
        next_url = kwargs.pop('next', None)
        student_report = StudentReporter.objects.filter(student=student).select_related(
            'student', 'session_report', 'session_report__session', 'session_report__session__name',
            'session_report__session__name', 'session_report__session__teacher').order_by(
                '-session_report__session_date'
                )
        myfilter = StudentReporterFilter(request.GET, initial= {"student":student}, queryset=student_report)
        student_report = myfilter.qs
        success_url = reverse_lazy('reports:student_report', kwargs={'student':student})
        success_url = check_suc_url(next_url, success_url)
        
        ctx={
            'student_report': student_report,
            'student': Student.objects.get(pk=student),
            'suc_url': success_url,
            'type':self.type,
            'filter': myfilter
        }
        return render(request, self.template, ctx)





'''
CRUD Views
'''


# Session report CRUD

class SessionReporterCreate(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('session')
    type='تقرير'
    form = SessionReporterForm

    def post(self, request, session,next=''):
        
        form = self.form(request.POST)
        self.success_url = check_suc_url(next, self.success_url)
        if not form.is_valid():
            
            ctx = {
                'form': form,
                'suc_url': self.success_url,
                'type':self.type
                }
            return render(request, self.template, ctx)
        form.save()
        create_student_for_session_report(form, session)
        return redirect(self.success_url)

class SessionReporterUpdate(LoginRequiredMixin, CRUDUpdate):
    model = SessionReporter
    success_url = reverse_lazy('session')
    template = 'add_update_form.html'
    form = SessionReporterForm
    type='تقرير'

class SessionReporterDelete(LoginRequiredMixin, CRUDDelete):
    model = SessionReporter
    success_url = reverse_lazy('session')
    form = SessionReporterForm
    template = 'make_confirm_delete.html'
    type = 'تقرير'
    



# Student Report CRUD Views


class StudentReportUpdateView(LoginRequiredMixin, CRUDUpdate):
    type='تقرير طالب'
    template = 'add_update_form.html'
    form = StudentReporterUpdateForm
    success_url = reverse_lazy('session_report') 
    model = StudentReporter       

class StudentReportCreateView(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('session')
    type='تقرير طالب'
    model = StudentReporter  
    form = StudentReporterCreateForm
    
class StudentReportDeleteView(LoginRequiredMixin, CRUDDelete):
    template = 'make_confirm_delete.html'
    success_url = reverse_lazy('session')
    type='تقرير طالب'
    model = StudentReporter  


