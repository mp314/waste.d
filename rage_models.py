from google.appengine.ext import ndb

class Rage(ndb.Model):
    date = ndb.DateTimeProperty()
    channel = ndb.StringProperty()
    title = ndb.StringProperty()

    # System stuff
    idate = ndb.DateTimeProperty(auto_now_add=True)
    udate = ndb.DateTimeProperty(auto_now=True)
    
    def __unicode__(self):
      if not self.title:
        return self.date.strftime("%Y-%m-%d %H:%M")
      else:
        return self.title
        
    def __str__(self):
      return unicode(self).encode('utf-8')

class Panel(ndb.Model):
    count = ndb.IntegerProperty()
    nick = ndb.StringProperty()
    face = ndb.StringProperty()
    msg = ndb.StringProperty()
    
    rage = ndb.KeyProperty(kind=Rage)

    # System stuff
    idate = ndb.DateTimeProperty(auto_now_add=True)
    udate = ndb.DateTimeProperty(auto_now=True)
    
    def __unicode__(self):
      return self.msg
        
    def __str__(self):
      return unicode(self).encode('utf-8')

