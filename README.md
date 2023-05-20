# Flow-interview
 

You are building a simple blog application and you need to create a Django view and template that displays a list of blog posts. Implement the following:

# Requirements:

    Create a model named BlogPost that has the following fields:

        title: CharField

        content: TextField

        author: ForeignKey to the built-in User model

        created_at: DateTimeField

    Create a Django view that lists all blog posts. The view should:

        Retrieve all BlogPost objects from the database

        Pass the list of blog posts to a template named blog_post_list.html

        Order the posts by created_at in descending order

    Create a template named blog_post_list.html that displays a list of blog posts. The template should:

        Iterate over the list of blog posts and display the title, content, author, and created_at fields for each post

        Use the {% url %} template tag to generate a URL for each post that points to a detail view for that post

# Hints:

    Use Django's built-in ListView and DetailView generic views to simplify your implementation

    Use Django's built-in template tags and filters to format dates and display content safely
    
# =====================================================================
# Running instruction:
1.Clone the porject and open with vscode
2.Then change the directory to blogPost using command ```cd blogPost```
3.Then run server by using ```python3 manage.py runserver```
4.To add a new blog post open admin view on any browser at ```localhost:8000/admin```. The username and password is ```minhle```
5.To view all blog post open the url on any browser at ```localhost:8000/blogpostlist```
