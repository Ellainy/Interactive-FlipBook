def identidade_visual(request):
    from .models import IdentidadeVisual
    identidade = IdentidadeVisual.objects.first()
    return {'identidade_visual' : identidade}