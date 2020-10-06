from unittest import TestCase

import pdfkit

from service import ReportsGeneratorServer


class TestReportsGenerator(TestCase):
    def test_html_to_pdf(self):
        options = {
            "margin-top": "0",
            "margin-left": "0",
            "--quiet": None
        }
        pdfkit.api.configuration()
        pdfkit.from_file("/home/xu/xy/topgen-server/workplace/tmp/9813bf9a-8e6e-42b8-9b9a-0a8544885d4a/report.html",
                         "/home/xu/xy/topgen-server/pdfkit-test.pdf", options)
