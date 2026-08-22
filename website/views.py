from django.views.generic import TemplateView

from tututuru.models import Circuito, Corrida, Equipe, Piloto

class IndexView(TemplateView):
    template_name = "website/modelo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.request.user.is_authenticated:
            return context

        usuario = self.request.user
        context.update(
            total_pilotos=Piloto.objects.filter(usuario=usuario).count(),
            total_equipes=Equipe.objects.filter(usuario=usuario).count(),
            total_corridas=Corrida.objects.filter(usuario=usuario).count(),
            total_circuitos=Circuito.objects.filter(usuario=usuario).count(),
            ultimos_pilotos=Piloto.objects.filter(usuario=usuario)
            .select_related("equipe")
            .order_by("-pk")[:5],
            proximas_corridas=Corrida.objects.filter(usuario=usuario)
            .select_related("circuito")
            .order_by("data")[:4],
        )
        return context

class ContatoView(TemplateView):
    template_name = "website/contato.html"

class SobreView(TemplateView):
    template_name = "website/sobre.html"
