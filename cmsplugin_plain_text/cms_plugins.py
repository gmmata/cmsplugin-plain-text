from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from .models import Plaintext


class PlaintextPlugin(CMSPluginBase):
    model = Plaintext
    name = _("Plaintext")
    render_template = "cms/plugins/plaintext.html"

    def render(self, context, instance, placeholder):
        context["body"] = instance.body
        return context


plugin_pool.register_plugin(PlaintextPlugin)
