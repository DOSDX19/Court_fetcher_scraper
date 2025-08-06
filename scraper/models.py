from django.db import models

# Create your models here.

# scraper/models.py

class CaseQuery(models.Model):
    case_type = models.CharField(max_length=20)
    case_number = models.CharField(max_length=20)
    filing_year = models.CharField(max_length=10)
    raw_html = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.case_type}-{self.case_number}-{self.filing_year}"
