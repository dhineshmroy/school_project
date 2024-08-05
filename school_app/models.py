from django.db import models

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Assessment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Award(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class ClassModel(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    subject_score = models.FloatField()

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answers = models.CharField(max_length=255)
