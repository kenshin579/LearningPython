# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet

from django.conf import settings
from django.db import models

class Record(models.Model):
    DEFAULT_ENCODING = 'utf-8'

    title = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=64)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=2048)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def encrypt_password(self):
        self.password = self.encrypt(self.password)

    def decrypt_password(self):
        self.password = self.decrypt(self.password)

    def encrypt(self, plaintext):
        return self.cypher('encrypt', plaintext)

    def decrypt(self, cyphertext):
        return self.cypher('decrypt', cyphertext)

    def cypher(self, cypher_func, text):
        fernet = Fernet(settings.ENCRYPTION_KEY)
        '''
        note: runtime에 cypher_func의 값을 알수 있기에 getattr를 사용해서 메서드를 원하는 메서드를 호출함
        cypher_func가 encrypt이면 fernet.encryt()를 호출하는 것과 같다!
        '''

        result = getattr(fernet, cypher_func)(self._to_bytes(text))
        return self._to_str(result)

    def _to_str(self, bytes_str):
        return bytes_str.decode(self.DEFAULT_ENCODING)

    def _to_bytes(self, s):
        return s.encode(self.DEFAULT_ENCODING)

    def __str__(self):
        return '{}'.format(self.title)
