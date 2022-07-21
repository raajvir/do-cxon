from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Discussion, Message, Post, Category, Profile  
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#def home(request):
#   return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class LandView(ListView):
    model = Post
    template_name = 'landing.html'

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class BrowseView(ListView):
    model = Post
    template_name = 'browse_post.html'
    cats = Category.objects.all()
     #ordering = ['-post_date']
    ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BrowseView, self).get_context_data(*args, **kwargs)
        #stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        #total_likes = stuff.total_likes() 

        context["cat_menu"] = cat_menu
        #context["total_likes"] =  total_likes
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list}) 
    
    

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts }) 
    

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes() 

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True


        context["total_likes"] =  total_likes
        context["liked"] = liked 
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url  = reverse_lazy('my_ideas')




class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url  = reverse_lazy('my_ideas')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url  = reverse_lazy('my_ideas')
   

class MyIdeasView(ListView):
    model = Post
    template_name = 'my_ideas.html'
    cats = Category.objects.all()
    ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(MyIdeasView, self).get_context_data(*args, **kwargs)
        post_lists = context['object_list']
        context['object_list'] = post_lists.filter(author=self.request.user)

        context["cat_menu"] = cat_menu
        return context


def request_collaborate(request,post_id):
    is_exist = Post.objects.filter(id=post_id)
    result = {'msg':'There is no valid article'}
    if is_exist:
        if request.method == 'POST':
            message = request.POST['msg']
            post = Post.objects.get(id=post_id)

            message_obj = Message.objects.create(user=request.user,message=message)
            discussion = Discussion.objects.create(sender=request.user,post=post)
            discussion.messages.add(message_obj)
            return redirect('article-detail',pk=post_id)
        
        result = {"postID":post_id}

    return render(request,'create_discussion.html',result)

def discussion_lists(request):
    list_disc = []
    discussions = Discussion.objects.all()
    for item in discussions:
        if (item.sender.id == request.user.id ) or (item.post.author.id == request.user.id):
            list_disc.append(item)
    
    return render(request,'discussion_lists.html',{"discussions":list_disc})

def messages_details(request,disc_id):
    is_exist = Discussion.objects.filter(id=disc_id)
    result = {'msg':'There is no valid discussion'}
    if is_exist:
        result = {"discussion":is_exist[0]}
        if request.method == 'POST':
            reply = request.POST['rply']
            disc_obj = Discussion.objects.get(id=disc_id)
            msgObj = Message.objects.create(user=request.user,message=reply)

            disc_obj.messages.add(msgObj)
            return redirect('messages',disc_id=disc_id)


    return render(request,'messages.html',result)


def connection_details(request,post_id):
    post = Post.objects.get(id=post_id)
    result = {"cat_1":[],"cat_2":[],"cat_3":[]}

    profiles = Profile.objects.all()

    for item in profiles:
        if item.user.id != request.user.id:
            if (post.category == item.interest):
                result['cat_1'].append(f'{item.user.username} ({item.interest})')
            if post.category2 == item.interest:
                result['cat_2'].append(f'{item.user.username} ({item.interest})')
            if post.category3 == item.interest:
                result['cat_3'].append(f'{item.user.username} ({item.interest})')
            if (post.category == item.interest2):
                result['cat_1'].append(f'{item.user.username} ({item.interest2})')
            if post.category2 == item.interest2:
                result['cat_2'].append(f'{item.user.username} ({item.interest2})')
            if post.category3 == item.interest2:
                result['cat_3'].append(f'{item.user.username} ({item.interest2})')
            if (post.category == item.interest3):
                result['cat_1'].append(f'{item.user.username} ({item.interest3})')
            if post.category2 == item.interest3:
                result['cat_2'].append(f'{item.user.username} ({item.interest3})')
            if post.category3 == item.interest3:
                result['cat_3'].append(f'{item.user.username} ({item.interest3})')
                

    return render(request,'connections.html',{"result":result})