from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    FormView,
)
from .models import *
from .forms import *
from django.urls import reverse_lazy
from apps.comments.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.objects.all().order_by("-created_at")

        category = self.request.GET.get("category", "")
        q = self.request.GET.get("q", "")

        if category:
            queryset = queryset.filter(Q(category__slug=category))

        if q:
            qset = (
                Q(title__icontains=q)
                | Q(author__first_name__icontains=q)
                | Q(category__name__icontains=q)
            )

            queryset = queryset.filter(qset)
            
        order_by = self.request.GET.get("order_by", "")
        
        if order_by == "featured":
            queryset = queryset.order_by("-featured")
            
        if order_by == "date-asc":
            queryset = queryset.order_by("created_at")
            
        if order_by == "date-desc":
            queryset = queryset.order_by("-created_at")

        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["postcomment_form"] = PostCommentForm()
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        post = self.get_object()
        visited = self.request.COOKIES.get('visited_' + str(post.slug))

        if not visited:

            post.views += 1
            post.save()
            response.set_cookie('visited_' + str(post.slug), 'true')

        return response


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostForm

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts:index")

    def test_func(self):
        return self.request.user.is_staff


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    success_url = reverse_lazy("posts:index")
    form_class = PostForm

    def test_func(self):
        return self.request.user.is_staff


class PostCommentCreateView(LoginRequiredMixin, FormView):
    form_class = PostCommentForm
    template_name = "posts/post_detail.html"

    def form_valid(self, form):
        post = Post.objects.get(slug=self.kwargs["slug"])
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("posts:view", args=[self.kwargs["slug"]])


class PostCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostComment
    template_name = "posts/comments/delete.html"
    pk_url_kwarg = "cpk"

    def get_success_url(self):
        return reverse("posts:view", args=[self.kwargs["slug"]])

    def test_func(self):
        cpk = self.kwargs["cpk"]
        comment = PostComment.objects.get(pk=cpk)
        return self.request.user == comment.author or self.request.user.is_staff


class PostCommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostComment
    template_name = "posts/comments/update.html"
    form_class = PostCommentForm
    pk_url_kwarg = "cpk"

    def get_success_url(self):
        return reverse("posts:view", args=[self.kwargs["slug"]])

    def test_func(self):
        cpk = self.kwargs["cpk"]
        comment = PostComment.objects.get(pk=cpk)
        return self.request.user == comment.author


@login_required
def like_post(request, slug):
    if request.method == "POST":
        post = Post.objects.get(slug=slug)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return redirect("posts:view", slug)


class PostCategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    template_name = 'posts/categories/create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('posts:index')

    def test_func(self):
        return self.request.user.is_staff


class PostCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    template_name = 'posts/categories/update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('posts:index')

    def test_func(self):
        return self.request.user.is_staff


class PostCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = "posts/categories/delete.html"
    success_url = reverse_lazy('posts:index')

    def test_func(self):
        return self.request.user.is_staff
