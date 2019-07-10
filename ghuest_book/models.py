from django.db import models
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    username = models.CharField(_('username'), max_length=128)
    email = models.EmailField(_('email'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    text = models.TextField(_('text'), max_length=4096)

    def construct(self, username, email, text):
        self.username = username
        self.email = email
        self.text = text

        return self