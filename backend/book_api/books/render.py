# books/render.py

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .callbacks import link_callback
import xhtml2pdf.pisa as pisa


class Render:
    """
    Class responsible to convert the HTML to PDF
    """

    @staticmethod
    def render(path: str, params: dict, file_name: str):
        """
        This static method receive the html template paramenters and
        conver it to PDF
        """

        # template = get_template(path)
        # html = template.render(params)
        # response = BytesIO()

        # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        #
        # if not pdf.err:
        #     return HttpResponse(response.getvalue(), content_type='application/pdf')
        # else:
        #     return HttpResponse("sorry an error occurred while processing your request (PDF rendering error)", status=400)

        template_path = path
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(params)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
            html, dest=response, link_callback=link_callback)

        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

