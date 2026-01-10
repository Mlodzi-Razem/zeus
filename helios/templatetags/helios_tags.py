
from django import template
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe
import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

register = template.Library()


def _d_to_dl(d):
    html = "<dl>"
    for key in list(d.keys()):
        html += "<dt>%s</dt>" % _(key)
        value = d[key]
        if isinstance(value, dict):
            value = _d_to_dl(value)
        if isinstance(value, list):
            value = _l_to_table(value)

        html += "<dd>%s</dd>" % str(value)

    html += "</dl>"
    return html


def _l_to_table(l_):
    if not len(l_):
        return "<table></table>"

    html = "<table>"

    if isinstance(l_[0], dict):
        values = l_
        html += "<thead><tr>"
        for key in list(l_[0].keys()):
            html += "<th>%s</th>" % _(key)
        html += "</thead></tr>"
    else:
        values = [{'value': v} for v in l_]

    html += "<tbody>"
    for entry in values:
        html += "<tr>"
        for v in list(entry.values()):
            if isinstance(v, dict):
                v = _d_to_dl(v)
            html += "<td>%s</td>" % v
        html += "</tr>"

    html += "</tbody></table>"
    return html


@register.filter
def as_dl(d):
    return _d_to_dl(d)


as_dl.is_safe = True


@register.filter
def as_table(l_):
    return _l_to_table(l_)


as_dl.is_safe = True


class RemoveHeadingsProcessor(Treeprocessor):
    def run(self, root):
        for element in list(root):
            if element.tag in {"h1", "h2", "h3", "h4", "h5",}:
                element.tag = "p"


class RemoveHeadingsExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            RemoveHeadingsProcessor(md),
            "remove_headings",
            priority=15,
        )

@register.filter
def markdownify(value):
    return mark_safe(
        markdown.markdown(
            value or "",
            extensions=[RemoveHeadingsExtension()],
        )
    )