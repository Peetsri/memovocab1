from django.db import models

# Create your models here.
class memovocab_test1(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title


class  profile(models.Model):
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)


class  vocab(models.Model):
    vocab = models.CharField(max_length=20)
    meaning_vocab = models.CharField(max_length=200)
    type_vocab = models.CharField(max_length=200)

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}



class Vocab2(models.Model):
    vocab = models.CharField(max_length=20)
    meaning_vocab = models.CharField(max_length=200)
    VERB = 'VE'
    NOUN = 'NO'
    ADJECTIVE = 'AD'
    ADVERB = 'AV'

    Vocab_type = [
        (VERB, 'Verb'),
        (NOUN, 'Noun'),
        (ADJECTIVE, 'Adj'),
        (ADVERB, 'Adv'),
        
    ]
    vocab_all = models.CharField(
        max_length=2,
        choices=Vocab_type,
        default=VERB,
    )

    def is_vocab(self):
        return self.Vocab_type in {self.VERB, self.NOUN}
