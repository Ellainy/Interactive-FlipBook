def identidade_visual(request):
    from livro3d.models import IdentidadeVisual
    identidade = IdentidadeVisual.objects.first()
    return {'identidade_visual' : identidade}