# -*- coding: utf-8 -*-
from math import ceil
from random import sample
from string import ascii_lowercase, ascii_uppercase, digits

punctuation = '!#$%&()*+-?@_|'
allchars = ''.join(
    (ascii_lowercase, ascii_uppercase, digits, punctuation))

class PasswordValidator:
    def __init__(self, password):
        self.password = password.strip()

    def is_valid(self):
        return (len(self.password) > 0 and
                all(char in allchars for char in self.password))

    def score(self):
        result = {
            'length': self._score_length(),
            'case': self._score_case(),
            'numbers': self._score_numbers(),
            'special': self._score_special(),
            'ratio': self._score_ratio(),
        }
        result['total'] = sum(result.values())
        return result

    def _score_length(self):
        scores_list = ([0] * 4) + ([1] * 4) + ([3] * 4) + ([5] * 4)
        scores = dict(enumerate(scores_list))
        print("scores", scores)
        return scores.get(len(self.password), 7)

    def _score_case(self):
        lower = bool(set(ascii_lowercase) & set(self.password)) #2 세트에 intersection이 있는 경우에만 true임 (결국 lower인지 확인)
        upper = bool(set(ascii_uppercase) & set(self.password))
        return int(lower or upper) + 2 * (lower and upper)

    def _score_numbers(self):
        return 2 if (set(self.password) & set(digits)) else 0

    def _score_special(self):
        return 4 if (
            set(self.password) & set(punctuation)) else 0

    def _score_ratio(self):
        alpha_count = sum(
            1 if c.lower() in ascii_lowercase else 0
            for c in self.password)
        digits_count = sum(
            1 if c in digits else 0 for c in self.password)
        if digits_count == 0:
            return 0
        return min(ceil(alpha_count / digits_count), 7)

class PasswordGenerator:
    @classmethod # instance 생성없이 호출할 수 있도록 해줌
    def generate(cls, length, bestof=10):
        candidates = sorted([
            cls._generate_candidate(length)
            for k in range(max(1, bestof))
        ])
        return candidates[-1] #password의 score가 best인 것을 반환함

    @classmethod
    def _generate_candidate(cls, length):
        password = cls._generate_password(length)
        score = PasswordValidator(password).score()
        return (score['total'], password)

    @classmethod
    def _generate_password(cls, length):
        chars = allchars * (ceil(length / len(allchars)))
        return ''.join(sample(chars, length))
