# -*- coding: utf-8 -*-
import json
import random

import falcon

from quotes import quotes


class QuoteResource:
    def on_get(self, req, resp):
        quote = {
            'quote': random.choice(quotes),
            'author': 'The Buddha'
        }
        resp.body = json.dumps(quote)


api = falcon.API()
api.add_route('/quote', QuoteResource())

a = 10
b = 20
(a, b) = b, a

10, 20 = 20, 10
