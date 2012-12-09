#!/usr/bin/env python
#
#   replace relative urls to absolute in string
#

import re
import urlparse

ACCEPTABLE_TAGS = ( 
    'a', 'applet', 'area', 'blockquote', 'body', 'del', 'form', 'longdesc', 'frame', 
    'iframe', 'head', 'img', 'input', 'ins', 'link', 'object', 'q', 'script',
)

ACCEPTABLE_TAG_ATTRS = (
    'href', 'codebase', 'cite', 'background', 'action', 'longdesc', 'src', 'profile',
    'usemap', 'classid', 'data',
)

tags_pattern = re.compile(r'<(.+?)(?:/)?>', re.I)
tag_attrs_patters = re.compile(r'(\w+)\s*=\s*[\'"](.+?)[\'"]', re.I)

def _rel2abs(chunk, base_uri):
    ''' return chunk where relative urls replaced by absolute
    '''    
    for tag in tags_pattern.findall(chunk):
        try:
            tag_name, tag_attrs = tag.split(' ', 1)
        except ValueError:
            continue
        if tag_name not in ACCEPTABLE_TAGS:
            continue
        
        for attr in tag_attrs_patters.finditer(tag_attrs):
            attr_name, attr_value = attr.groups()
            if attr_name not in ACCEPTABLE_TAG_ATTRS:
                continue
            prev_uri = attr_value
            res_uri = urlparse.urljoin(base_uri, prev_uri)
            attr_pos = attr.start()
            if attr_pos == 0:
                chunk = chunk.replace(prev_uri, res_uri, 1)
            else:
                chunk = ''.join((chunk[:attr_pos],chunk[attr_pos:].replace(prev_uri, res_uri, 1)))
    return chunk

def rel2abs(html_code, base_uri):
    ''' return html code where relative urls replaced by absolute
    '''    
    result = ''
    while True:
        pos = html_code.find('>') + 1
        if pos > 0:
            chunk = html_code[:pos]
            html_code = html_code[pos:]
        else:
            chunk = html_code
            html_code = ''
        if not chunk:
            break
        chunk = _rel2abs(chunk, base_uri)
        result = ''.join((result, chunk))
    return result
        
    
if __name__ == '__main__':

    assert rel2abs(
                    '<a href="http://www.example.com"> tag_a_1 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com"> tag_a_1 </a>'
    
    assert rel2abs(
                    "<a href='http://www.example.com'> tag_a_1 </a>", 
                    'http://www.exampe.com'
    ) == "<a href='http://www.example.com'> tag_a_1 </a>"

    assert rel2abs(
                    '<a name="tag_a" href="http://www.example.com"> tag_a_2 </a>', 
                    'http://www.exampe.com'
    ) == '<a name="tag_a" href="http://www.example.com"> tag_a_2 </a>'

    assert rel2abs(
                    "<a name='tag_a' href='http://www.example.com'> tag_a_2 </a>", 
                    'http://www.exampe.com'
    ) == "<a name='tag_a' href='http://www.example.com'> tag_a_2 </a>"

    assert rel2abs(
                    '<a href="http://www.example.com" name="tag_a" > tag_a_3 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com" name="tag_a" > tag_a_3 </a>'

    assert rel2abs(
                    "<a href='http://www.example.com' name='tag_a' > tag_a_3 </a>", 
                    'http://www.exampe.com'
    ) == "<a href='http://www.example.com' name='tag_a' > tag_a_3 </a>"

    assert rel2abs(
                    '<a href="http://www.example.com/"> tag_a_4 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com/"> tag_a_4 </a>'

    assert rel2abs(
                    '<a href="http://www.example.com/1"> tag_a_4 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com/1"> tag_a_4 </a>'

    assert rel2abs(
                    '<a href="http://www.example.com/pages"> tag_a_5 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com/pages"> tag_a_5 </a>'

    assert rel2abs(
                    '<a href="http://www.example.com/page/1"> tag_a_6 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com/page/1"> tag_a_6 </a>'

    assert rel2abs(
                    '<a href="http://www.example.com/page/1?sort=true"> tag_a_6 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com/page/1?sort=true"> tag_a_6 </a>'

    assert rel2abs(
                    '<a href="http://www.example.com/page/1?k1=v1&k2=v2&k3=v3"> tag_a_7 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com/page/1?k1=v1&k2=v2&k3=v3"> tag_a_7 </a>'

    assert rel2abs(
                    '<a href="http://www.example.com/page/1?k1=v1&k2=v2&k3=v3"> tag_a_8 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.example.com/page/1?k1=v1&k2=v2&k3=v3"> tag_a_8 </a>'

    assert rel2abs(
                    '<a href="/"> tag_a_10 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/"> tag_a_10 </a>'

    assert rel2abs(
                    '<a href="/" type="text/html"> tag_a_10 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/" type="text/html"> tag_a_10 </a>'

    assert rel2abs(
                    '<a type="text/html" href="/"> tag_a_10 </a>', 
                    'http://www.exampe.com'
    ) == '<a type="text/html" href="http://www.exampe.com/"> tag_a_10 </a>'

    assert rel2abs(
                    '<a href="/1"> tag_a_11 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/1"> tag_a_11 </a>'

    assert rel2abs(
                    '<a href="/pages"> tag_a_11 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/pages"> tag_a_11 </a>'

    assert rel2abs(
                    '<a href="/page/1"> tag_a_12 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/page/1"> tag_a_12 </a>'

    assert rel2abs(
                    '<a href="/page/1"> tag_a_13 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/page/1"> tag_a_13 </a>'

    assert rel2abs(
                    '<a href="/page/1?sort=true"> tag_a_14 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/page/1?sort=true"> tag_a_14 </a>'

    assert rel2abs(
                    '<a href="/page/1?k1=v1&k2=v2&k3=v3"> tag_a_14 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/page/1?k1=v1&k2=v2&k3=v3"> tag_a_14 </a>'

    assert rel2abs(
                    '<a href="/page/1?k1=v1&k2=v2&k3=v3"> tag_a_14 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/page/1?k1=v1&k2=v2&k3=v3"> tag_a_14 </a>'


    assert rel2abs(
                    '<a href="/page/1"> page 1 </a> <a href="/page/2"> page 2 </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.exampe.com/page/1"> page 1 </a> <a href="http://www.exampe.com/page/2"> page 2 </a>'
    
    assert rel2abs(
                    '<a href="http://www.google.com/"> Google </a>', 
                    'http://www.exampe.com'
    ) == '<a href="http://www.google.com/"> Google </a>'

