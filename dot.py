
import pydotplus

def to_node(n):
  name = n.get_name()
  attrs = n.get_attributes()

  if 'type' in attrs:
    t = attrs['type']
    del attrs['type']
  else:
    t = 'node'

  return dict(id=name, type=t, attrs=attrs)

def to_edge(link, nodes):
  source = link.get_source()
  target = link.get_destination()
  attrs = link.get_attributes()

  if 'type' in attrs:
    t = attrs['type']
    del attrs['type']
  else:
    t = 'node'

  return dict(type=t, attrs=attrs, source=nodes[source], target=nodes[target])

def parse_dot(args, files):
  if len(files) == 0:
    return None

  content = files[0].read()
  g = pydotplus.parse_dot_data(content)

  nodes = { n['id'] : n for n in (to_node(n) for n in g.get_nodes()) }
  edges = [to_edge(e,nodes) for e in g.get_edges()]

  return dict(nodes=nodes.values(), edges=edges)