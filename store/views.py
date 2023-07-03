from django.http import JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
import django
from.models import *
from.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, "store/index.html")

def dashboard(request):
    group = Group.objects.all()
    #print(group)
    context = {'group':group}
    return render(request,"store/dashboard.html", context)

@login_required(login_url='loginpage')
def dashboardview(request, slug):
    group = Group.objects.filter(slug=slug).first()
    branches = Branch.objects.filter(Group__slug=slug)
    context = {'branches': branches, 'group': group}
    return render(request, "store/branches/index.html", context)
    # if(Group.objects.filter(slug=slug)):
    #     branches = Branch.objects.filter(group__slug=slug)
    #     group = Group.objects.filter(slug=slug).first()
    #     context = {'branches': branches, 'group':group}
    #     return render(request, "store/branches/index.html",context)
    # else:
    #     messages.warning(request,"No such Group")
    #     return django.redirect('dashboard')


@login_required(login_url='loginpage')
def branchview(request, group_slug, branch_slug):
    group = Group.objects.get(slug=group_slug)
    branch = Branch.objects.get(Group=group, id=branch_slug)

    if request.method == 'POST':
        print("here")
        form = BranchForm(request.POST, instance=branch)
        #forms.dob = forms.DateField(input_formats=['%d/%m/%Y'])
        print(branch.student_image)
        if form.is_valid():
            student_image = request.POST.get('student_image')
            print(student_image)
            # Save the student_image value to the branch object instance
            form.student_image = student_image
            
            print("form")
            form.save()
            context={"branch_slug":branch_slug}
            return redirect('dashboardview',group.slug)
        else:
            print(form.errors)
    else:
        form = BranchForm(instance=branch)

    context = {
        'group': group,
        'name': branch.name,
        'dob': branch.dob,
        'email': branch.email,
        'mobile': branch.mobile,
        'status': branch.status,
        'Reg': branch.Reg,
        'gender': branch.gender,
        'address': branch.address,
        'form': form,
        "student_image": branch.student_image.url,
    }

    return render(request, 'store/branches/branchview.html', context)

    # branches =  Branch.
    # if(Group.objects.filter(slug=grou_slug, status=0)):
    #     if(Branch.objects.filter(slug=bran_slug, status=0)):
    #             branches = Branch.objects.filter(slug=bran_slug, status=0).first
    #             context = {'branches':branches}
    #     else:
    #         messages.error(request, "No such group")
    #         return django.redirect('dashboard')

    # else:
    #     messages.error(request, "No such group")
    #     return django.redirect('dashboard')
    # return render(request, "store/branches/view.html", context)

def branchlistAjax(request):
    branches = Branch.objects.filter(status=0).values_list('name',flat=True)
    branchesList = list(branches)
    return JsonResponse(branchesList, safe =False)

@login_required(login_url='loginpage')
def searchbranch(request):
    print("request is gotten")
    if request.method == 'POST':
        searchedterm = request.POST.get('branchsearch')
        #print(searchedterm)
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            branch = Branch.objects.filter(name__contains=searchedterm).first()

            if branch:
                return redirect('dashboard/{}/{}'.format(branch.Group.slug, branch.id))
            else:
                messages.info(request, "No branch matched your search.")
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='loginpage')
def studentReportPage(request):
    user = request.user.id
    print(user)
    user = get_object_or_404(User, id=user)
    #branch = get_object_or_404(Branch, name=user.username)
    branch_name = user.username.replace('_', ' ')
    #print(branch_name)
    branch = get_object_or_404(Branch, name=branch_name)
    context = {
        'user': user,
        'branch': branch,
        # Include any other data you want to pass to the template
    }
    return render(request, 'store/branches/studentReport.html', context)