from django.db import models  
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# choices for user type
USER_TYPE = (("personal", "Personal"), ("company", "Company"))

# choices for category
CATEGORY = (("construction", "Construction"), ("i.t", "I.T"), ("photography", "Photography"), 
            ("design", "Design"), ("hair & beauty", "Hair & Beauty"), ("cooking", "Cooking"), 
            ("arts & crafts", "Arts & Crafts"), ("writing & copywriting", "Writing & Copywriting"), 
            ("other", "Other"))

class Profile(models.Model):
    """
    model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder', blank=True, null=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE, default="personal")

class Category(models.Model):
    """
    model for work category
    """
    name = models.CharField(max_length=50, choices=CATEGORY, default="construction")

    def __str__(self):
        return self.name

class Work(models.Model):
    """
    model for work posts
    """
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_posts")
    work_image = CloudinaryField('image', default='work_placeholder')
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name="work_category")
    sub_category = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, blank=True, related_name="work_likes" )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title   
    
    def number_of_likes(self):
        return self.likes.count()

class Rating(models.Model):
    """
    model for work ratings/comments
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="work_ratings", default=1)
    content = models.TextField()
    suggested_price = models.IntegerField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.content} by {self.user}"
