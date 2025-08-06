from django.shortcuts import render

# Create your views here.
# scraper/views.py

from .forms import CaseSearchForm
from .models import CaseQuery
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def home(request):
    data = None
    error = None

    if request.method == 'POST':
        form = CaseSearchForm(request.POST)
        if form.is_valid():
            case_type = form.cleaned_data['case_type']
            case_number = form.cleaned_data['case_number']
            filing_year = form.cleaned_data['filing_year']
            try:
                driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
                driver.get('https://delhihighcourt.nic.in/case.asp')
                time.sleep(2)

                driver.find_element(By.NAME, 'case_type').send_keys(case_type)
                driver.find_element(By.NAME, 'case_no').send_keys(case_number)
                driver.find_element(By.NAME, 'case_year').send_keys(filing_year)

                driver.find_element(By.NAME, 'B1').click()
                time.sleep(3)

                html = driver.page_source
                driver.quit()

                # Save to database
                CaseQuery.objects.create(
                    case_type=case_type,
                    case_number=case_number,
                    filing_year=filing_year,
                    raw_html=html
                )

                # ⚠️ Replace this with real scraping logic from `html`
                data = {
                    'parties': 'Sample Party A vs Party B',
                    'filing_date': '2023-01-01',
                    'next_hearing': '2025-08-15',
                    'latest_pdf': 'https://example.com/sample_order.pdf'
                }

            except Exception as e:
                error = str(e)
    else:
        form = CaseSearchForm()

    return render(request, 'form.html', {'form': form, 'data': data, 'error': error})
