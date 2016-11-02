
import pydotplus

def _to_node(n):
  name = n.get_name()
  attrs = n.get_attributes()

  r = dict(id=name, type='node', attrs=attrs)
  for inline in ['type','description']:
    if inline in attrs:
      r[inline] = attrs[inline]
      del attrs[inline]

  return r

def _resolve_name(args, f):
  if 'name' in args:
    return args['name']
  fn = f.filename
  import os.path
  name, ext = os.path.splitext(os.path.basename(fn))
  return name

def _to_edge(link):
  source = link.get_source()
  target = link.get_destination()
  attrs = link.get_attributes()

  r = dict(type='edge', attrs=attrs, source=source, target=target)
  for inline in ['type','description']:
    if inline in attrs:
      r[inline] = attrs[inline]
      del attrs[inline]

  return r

def parse_dot(args, files):
  if len(files) == 0:
    return None

  content = files[0].read()
  g = pydotplus.parse_dot_data(content)

  nodes = [_to_node(n) for n in g.get_nodes()]
  edges = [_to_edge(e) for e in g.get_edges()]

  return dict(name=_resolve_name(args, files[0]), nodes=nodes, edges=edges)