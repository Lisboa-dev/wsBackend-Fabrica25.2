
from .models import Books
from .serializer import serializerBook
from django.views.decorators.http import require_http_methods
from django.http import  JsonResponse
import json 
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView




# Create your views here.

class BookApi(APIView):
    @require_http_methods(["GET"])
    def BookAPI_Consult(request):
        query=request.GET.get('q',None)
        page=int(request.GET.get('page',1))
        limit=int(request.GET.get('limit',10))
   
        if query is None:
            return JsonResponse({'error': 'error: Envie um consult valido'}, status=404)   
        else:
            try:
              data=populate_books_from_openlibrary(query, page, limit)
              return JsonResponse(data, status=200)
            except ValueError as e:
              return JsonResponse({'error':f'message: {e}', 'status':500})
        

    permission_classes = [IsAuthenticated] 
    @require_http_methods(["Post"])
    def BookAPI_Save(request):

        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            title=body.get('title', None)
            author=body.get('author', None)
            genres=body.get('genres', None)
            url=body.get('urls', None)
            date_publi=body.get('date_publi', None)
            image=body.get('custo', None)
            format=body.get('format', None)
            avaliability=body.get('availability', None)
            number_pages=body.get('number_pages', None)
            publisher=body.get('publisher', None)
            language=body.get('language', None)
            cluster=body.get('cluster_id', None)

            if title is None or author is None or genres is None or url is None or date_publi is None or format is None or avaliability is None or publisher is None or language is None or cluster is None or image is None:
                return JsonResponse({'error': 'error: Envie todos os campos'}, status=404)   
            
            book=Books.objects.create(
                title=title[:255],
                author=author[:500],
                genres=genres[:500],
                urls=url[:500],
                date_publi=date_publi,
                image_url=image[:500],
                format=format[:200],
                availability=avaliability[:100],
                number_pages=number_pages,
                publisher=publisher[:500],
                language=language[:250],
                cluster_id=cluster,
            )
            book.save()
            book=serializerBook(book)
            return JsonResponse({'data':book},status=200, safe=False)
        
        except ValueError as e:
            return JsonResponse({'error':f'message: {e}', 'status':500})
        


    permission_classes = [IsAuthenticated] 
    @require_http_methods(["Post"])
    def BookAPI_Delete(resquest, id):
        try:
            book=Books.objects.get(id=id)
            book.delete()
            return JsonResponse({'data':f'Book {id} deletado com sucesso'},status=200, safe=False)
        except Books.DoesNotExist:
            return JsonResponse({'error': 'error: Book nao encontrado'}, status=404)   
        except ValueError as e:
            return JsonResponse({'error':f'message: {e}', 'status':500})








def populate_books_from_openlibrary(query, page, limit):

    offset = (page - 1) * limit

    url =(  f'https://openlibrary.org/search.json?q={query}&mode=everything'
           f'&fields=key,title,author_name,subject,cover_i,first_publish_year,'
           f'number_of_pages_median,publisher,language,availability,physical_format_s,edition_key'
           f'&limit={limit}&offset={offset}'
    )
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar OpenLibrary:", response.status_code)
        return({'error':"Erro ao acessar OpenLibrary"}, {'status':response.status_code})

    data = response.json()
    docs = data.get("docs", [])
    books_data = []
   
    for doc in docs:
        
        if doc.get("cover_i") or doc.get("author_name"):
           
            book_info = {
                    'title': doc.get("title", "Indefinido"),
                    'author': ", ".join(doc.get("author_name", ["Indefinido"])), 
                    'genres': ", ".join(doc.get("subject", ["Indefinido"])), 
                    'date_publi': doc.get("first_publish_year", None),
                    'number_pages': doc.get("number_of_pages_median", None),
                    'publisher': ", ".join(doc.get("publisher", ["Indefinido"])), 
                    'language': ", ".join(doc.get("language", ["Indefinido"])),
                    'urls': f"https://openlibrary.org{doc.get('key')}" if doc.get('key') else None,
                    'image_url': f"http://covers.openlibrary.org/b/olid/{doc.get("cover_i")}-M.jpg" if doc.get("cover_i") else None,
                    'availability': doc.get("availability", {} ).get("status", "Indefinido"), 
                    'format': ",".join(doc.get("physical_format_s", ["Indefinido"])),
                }
            books_data.append(book_info)


       
    return({'data':books_data})
    
        
    
  
            




        