from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from regular_exam_project.profiles.form import ProfileForm
from .models import Profile

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            request.session['profile_id'] = profile.id
            return redirect('car_catalogue')
    else:
        form = ProfileForm()
    return render(request, 'profiles/profile-create.html', {'form': form})


def profile_details(request):
    profile = request.user
    return render(request, 'profiles/profile-details.html', {'profile': profile})

@login_required
def profile_details(request):
    profile = request.user
    return render(request, 'profiles/profile-details.html', {'profile': profile})



@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile_details')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile-edit.html', {'form': form})

@login_required
def profile_delete(request):
    user = request.user
    user.delete()
    return redirect('/')

