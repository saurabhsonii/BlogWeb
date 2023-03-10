from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.
from PIL import Image
from gtts import gTTS
from bs4 import BeautifulSoup

# this modal for contact form
class Contact(models.Model):
      name = models.CharField(max_length=50)
      email = models.EmailField(max_length=100)
      subject = models.CharField(max_length=100)
      message = models.TextField()
      created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.name

# this modal for blog categorys form
class BlogCategory(models.Model):
      category = models.CharField(max_length=50)
      # category_img = models.ImageField(upload_to='pics')
      category_details = models.CharField(max_length=250, blank=True)
      slug = models.SlugField(max_length=100)
      created = models.DateTimeField(auto_now_add=True)

      def save(self, *args, **kwargs):
            if not self.id:
                  # Newly created object, so set slug
                  self.slug = slugify(self.category)

                  super(BlogCategory, self).save(*args, **kwargs)

      def __str__(self):
            return self.category


# this modal for blog form
class Blog(models.Model):
      category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
      snipit = models.CharField(max_length=50)
      title = models.CharField(max_length=100)
      img = models.ImageField(upload_to='pics')
      img_alt = models.CharField(max_length=100)
      description = models.TextField()
      blog_url = models.SlugField(max_length=100)
      author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
      title_meta = models.CharField(max_length=100)
      description_meta = models.CharField(max_length=500)
      keywords_meta = models.CharField(max_length=75)
      music = models.FileField(upload_to='music',null=True, blank=True)
      created = models.DateTimeField(auto_now_add=True)


      def save(self, *args, **kwargs):
            if not self.id:
                  # Newly created object, so set slug
                  self.blog_url = slugify(self.title)

                  super(Blog, self).save(*args, **kwargs)

      def image(self, *args, **kwargs):
            super().save(*args, **kwargs)
            img = Image.open(self.img.path)

            if img.height > 100 or img.weight > 100:
                  output_size = (100,100)
                  img.thumbnail(output_size)
                  img.save(self.img.path)

      # def music(self, *args, **kwargs):
      #
      #       title = self.title
      #       des = self.description
      #       des = BeautifulSoup(des)
      #       t = des.getText()
      #
      #       mytexts = (f' blog title is {title} and details is {t}')
      #
      #       language = 'en'
      #       myobj = gTTS(text=mytexts, lang=language, slow=False)
      #       music = myobj.save(f'media/audio/{title}.mp3')
      #       print(music)
      #
      #       mp = (f'media/audio/{title}.mp3')
      #
      #       d = self.music = mp
      #       print(d)
      #
      #       super(Blog, self).save(*args, **kwargs)



      def __str__(self):
            return self.title


class Subscribe(models.Model):

      name = models.CharField(max_length=50)
      email = models.EmailField(max_length=100, unique=True)

      def __str__(self):
            return self.name







