from curses import A_VERTICAL
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView
from .models import Post
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.urls import reverse_lazy

#Function Based View template show
'''def indexView(request):
    return render(request, "index.html")'''


# function based view redirect

'''def redirectView(request):
    return redirect("https://aur.archlinux.org/")'''
class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "koth2"
        context["age"] = 20
        context["city"] = "koth-city"
        context["posts"] = Post.objects.all()
        return context
    # extra_context = {"name":"koth2"}

class RedirectViewAUR(RedirectView):
    url = "https://aur.archlinux.org/"
    # permanent = True

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs["pk"])
        print(post.title)
        return super().get_redirect_url(*args, **kwargs)
        

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = ["-created_at"]

    #queryset = Post.objects.all()
    #template_name = "post_list.html"

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"

    def get_object(self):
        return get_object_or_404(Post, id=self.kwargs["pid"])

class PostCreateView(FormView):
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)