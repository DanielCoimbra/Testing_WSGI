# Get a compiler
from pybars import Compiler
compiler = Compiler()

# Compile the template
source = u"{{>header}}{{#list people}}{{firstName}} {{lastName}}{{/list}}"
template = compiler.compile(source)

# Add any special helpers
def _list(this, options, items):
    result = [u'<ul>']
    for thing in items:
        result.append(u'<li>')
        result.extend(options['fn'](thing))
        result.append(u'</li>')
    result.append(u'</ul>')
    return result
helpers = {'list': _list}

# Add partials
header = compiler.compile(u'<h1>People</h1>')
partials = {'header': header}

# Render the template
output = template({
    'people': [
        {'firstName': "Yehuda", 'lastName': "Katz"},
        {'firstName': "Carl", 'lastName': "Lerche"},
        {'firstName': "Alan", 'lastName': "Johnson"}
    ]}, helpers=helpers, partials=partials)

print(output)