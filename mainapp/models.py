from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# # Create your models here.
class User(AbstractUser):
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    has_filled_profile = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

# class Profile(models.Model):
#     profile_owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

class Unit(models.Model):
    unit_name = models.CharField(max_length=100)

class Business(models.Model):
    models.ManyToManyField(Unit)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    units = models.ManyToManyField('Unit', related_name='units')
    name = models.CharField(max_length=200)
    email = models.EmailField(verbose_name='business email', max_length=254)
    address  = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    about = models.TextField()
    services = models.CharField(max_length=500, help_text='Add services seperated by comma "," ')
    logo = models.ImageField(upload_to='logos', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = ('Business')
        verbose_name_plural = ('Businesses')

   
class BusinessImages(models.Model):
    owner = models.ForeignKey(Business, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = ('Business Image')
        verbose_name_plural = ('Business Images')


class Socials(models.Model):
    owner = models.OneToOneField(Business, on_delete=models.CASCADE)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    whatsapp = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = ('Social')
        verbose_name_plural = ('Socials')



#   USER_UPDATE_APPROVED = 'True'
#   USER_UPDATE_DISAPPROVED = 'False'
#   USER_UPDATE_PENDING = 'Pending'
#   # NOT_YET_UPDATED = 'None'

# #   id = db.Column(db.Integer, primary_key=True)
#   #db.backref fixes instrumentedlist error --- now fixed
# #   units = db.relationship("Unit", secondary=user_unit, backref=db.backref("unit_members", lazy=True), lazy=True, passive_deletes= True)
# #   username = db.Column(db.String(20), unique=True) # its really not needed.
# #   password = db.Column(db.String(60), nullable=False, default="12345678")
# #   date_registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#   role = db.Column(db.String(6), nullable=False, default="USER")
# #   _is_superadmin = db.Column("is_superadmin", db.Boolean, nullable=False, default=False)
#   current_salary = db.Column(db.String(60))
#   occupation = db.Column(db.String(60))
#   experience = db.Column(db.String(60))

#   experience = models.CharField()


#   # date_of_birth = db.Column(db.String(77), nullable=False, default=datetime.utcnow)


#   business_address = db.Column(db.String(120))
#   _is_suspended = db.Column("is_suspended", db.Boolean, nullable=False, default=False)
#   has_filled_profile = db.Column(db.Boolean(), default=False)

#   #newly added field to track whether the user's update is approved
#   update_is_approved = db.Column(db.String(50), nullable=False, default='NOT_YET_UPDATED')
#   business_name = db.Column(db.String(77))
#   business_email = db.Column(db.String(120), unique = True)
#   business_phone = db.Column(db.String(77), unique = True)
#   business_photo = db.Column(db.String(20), nullable = False, default='default.jpg')
#   business_about = db.Column(db.String(300))
#   business_services = db.Column(db.String(300))

#     # Model
#   business_facebook = db.Column(db.String(77))
#   business_website = db.Column(db.String(77))
#   business_twitter = db.Column(db.String(77))
#   business_linkedin = db.Column(db.String(77))
#   business_whatsapp = db.Column(db.String(77))

#   # Model
#   business_product_image_1 = db.Column(db.String(20), nullable=False, default='default.jpg')
#   business_product_image_2 = db.Column(db.String(20), nullable=False, default='default.jpg')
#   business_product_image_3 = db.Column(db.String(20), nullable=False, default='default.jpg')
#   business_product_image_4 = db.Column(db.String(20), nullable=False, default='default.jpg')
#   business_product_image_5 = db.Column(db.String(20), nullable=False, default='default.jpg')
#   business_product_image_6 = db.Column(db.String(20), nullable=False, default='default.jpg')


  
#   messages_sent = db.relationship('Message',
#                                     foreign_keys='Message.sender_id',
#                                     backref='author', lazy='dynamic')
#   messages_received = db.relationship('Message',
#                                       foreign_keys='Message.member_recipient_id',
#                                       backref='member_recipient', lazy='dynamic')
#   last_message_read_time = db.Column(db.DateTime)

  
  
#   def new_messages(self):
#     last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
    
#     #recipient should be units recieving
#     # count = 0
#     # for unit in self.units:
#     #   count += Message.query.filter_by(recipient=unit).filter(
#     #     Message.timestamp > last_read_time).count()

#     # return count

#     return Message.query.filter_by(recipient=self).filter(
#         Message.timestamp > last_read_time).count()

#   def display_units(self):
#     unit_names = []
#     # for unit in self.units.all():
#     for unit in self.units:
#       unit_names.append(unit.name)

#     return ", ".join(unit_names)

#   #for csv export
#   def unit_ids(self):
#     unit_ids = []
#     # for unit in self.units.all():
#     for unit in self.units:
#       unit_ids.append(str(unit.id))

#     return unit_ids

  
#   @property
#   def is_superadmin(self):
#       return self._is_superadmin

#   @property
#   def is_suspended(self):
#       return self._is_suspended

#   @is_superadmin.setter
#   def is_superadmin(self, s):
#     #this exists because of the csv fuction that inputs strings
#     if type(s) == type(str()):
#       #change string to boolean
#       if s.lower() == "true":
#         self._is_superadmin = True
#       elif s.lower() == "false":
#         self._is_superadmin = False
#     else:
#       #dont change anything if it's not a string
#       self._is_superadmin = s

#   @is_suspended.setter
#   def is_suspended(self, s):
#     #this exists because of the csv fuction that inputs strings
#     if type(s) == type(str()):
#       #change string to boolean
#       if s.lower() == "true":
#         self._is_suspended = True
#       elif s.lower() == "false":
#         self._is_suspended = False
#     else:
#       #dont change anything if it's not a string
#       self._is_suspended = s

# #   def get_reset_token(self, expires_sec=1800):
# #     s = Serializer(app.config['SECRET_KEY'], expires_sec)
# #     return s.dumps({'user_id': self.id}).decode('utf-8')

# #   @staticmethod
# #   def verify_reset_token(token):
# #       s = Serializer(app.config['SECRET_KEY'])
# #       try:
# #           user_id = s.loads(token)['user_id']
# #       except:
# #           return None
# #       return User.query.get(user_id)

# #   def __repr__(self):
# #     return f"User('{self.username} {self.business_phone}')"