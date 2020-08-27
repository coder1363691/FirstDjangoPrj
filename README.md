# FirstDjangoPrj
Django@1.11.6 project practice



当传递多个参数时(2020/08/26)

views做的修改：
def node_list(request, prefix, node_name):
    fixed_nodename = prefix + '_' + node_name
    file_list = meta_dict[fixed_nodename]
    return render(request, 'polls/list.html', file_list)

urls做的修改（这里不建议使用/分割两个参数，这里使用的是-）：
url(r'^(?P<prefix>\S+)_(?P<node_name>\S+)/children/$', views.node_list, name="node")

模板做的修改：
<li><a href="{% url 'polls:node' file.prefix file.name %}">[   {{ file.contri|floatformat:6 }}   ]: {{ file.name }}</a></li>

