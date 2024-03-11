from django.shortcuts import render
from rembg import remove
import base64



def bgremover( request):
        if request.method == 'POST':
            image_file = request.FILES.get('image')
            if image_file:
                # Lógica para remover o fundo da imagem
                try:
                    result = remove(image_file)
                    result_base64 = base64.b64encode(result).decode('utf-8')
                    result_image = f'data:image/png;base64,{result_base64}'
                except Exception as e:
                    print(e)  # Lidar com erros de remoção de fundo
                    result_image = None

                return render(request, 'bgremover.html', {'result_image': result_image})

        return render(request, 'bgremover.html')
