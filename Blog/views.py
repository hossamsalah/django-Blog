from django.shortcuts import render
from models import Blog, Category, UserProfile,Comment
from forms import UserForm, UserProFileForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import loader


def main(request):
    latest_blogs = Blog.objects.order_by('-creation_date')
    comment = Comment.objects.all
    user = UserProfile.objects.get(user=request.user)
    context = {
        'latest_blogs': latest_blogs,
        'user': user,
        'comment': comment,
        'categories': Category.objects.all()
    }
    return render(request, 'Blog/home.html', context)

def about(request, author_id):
    info = UserProfile.objects.filter(id=author_id)
    context = {'info': info}
    return render(request,'Blog/about.html', context)

# for adding a new bolg
def create(request):
    if request.user.is_authenticated():
        category = {'categories': Category.objects.all()}
        return render(request, 'Blog/addblog.html', category)
    else:
        return HttpResponse("You are not logged in.")


def add(request):
    if request.user.is_authenticated():
        category= get_object_or_404(Category, category=request.POST.get('category'))
        blog = Blog(title=request.POST.get('title'), body=request.POST.get('body'),
                author=request.user, category=category)
        blog.save()
        return HttpResponseRedirect(reverse('Blog:main'))
    else:
        return HttpResponse("You are not logged in.")


#for adding anew comment
def addcomment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {'blog': blog, }
    return render(request, 'Blog/comments.html', context)


def newcomment(request, blog_id):
    if request.user.is_authenticated():
        comment = Comment(comment=request.POST.get('comment'), blog=Blog(pk=blog_id) )
        comment.save()
        return HttpResponseRedirect(reverse('Blog:main'))
    else:
        return HttpResponse("You are not logged in.")


#the category views

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    blog = Blog.objects.filter(category=category_id)
    context = {'fun_blogs': blog,
               'category': Category.objects.all()}
    return render(request, 'Blog/category.html', context)



# the user system views
def register(request):
    registered = False
    if request.POST:
        user_form = UserForm(data=request.POST)
        profile_form = UserProFileForm(data=request.POST)
        if user_form.is_valid()and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user = authenticate(username=request.POST['username'] , password=request.POST['password'])
            if user:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/blog/')
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProFileForm()

    return render(request, 'blog/register.html', {'user_form': user_form,
                                                  'profile_form': profile_form, 'registerd': registered})


def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/blog/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print "Invalied log in details" #.formate(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'blog/login.html', {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/')
