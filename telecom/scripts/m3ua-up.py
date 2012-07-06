#!/usr/bin/env python
#
#   parse PDML data (tshark output), only M3UA protocol messages selected
#
#
__version__ = '0.1'
__author__ = 'Andrey Usov <http://devel.ownport.net>'
__url__ = 'https://github.com/ownport/my-notes/tree/master/telecom/scripts/m3ua-up.py'
__license__ = '''
Copyright (c) 2012, Andrey Usov <http://devel.ownport.net>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import re
import sys
from lxml import etree
from pprint import pprint

IGNORED_PROTOCOLS = ['geninfo', 'frame', 'eth', 'ip', 'sctp', 'h248',]


def handle_packet(packet):
    ''' handle packet '''
    r_packet = etree.fromstring(packet)    
    msg = list()
    for protocol in r_packet:
        if protocol.tag == 'proto':
            for protocol_res in handle_protocol(protocol):
                if protocol_res['name'] == 'm3ua' and len(msg) > 0:
                    yield msg
                else:
                    msg.append(protocol_res)
    if len(msg) > 0:
        yield msg

def handle_protocol(protocol):
    ''' handle protocol '''
    name = protocol.attrib.get('name', None)
    descr = protocol.attrib.get('showname', None)
    fields = list()

    if not name or not descr:
        return

    if name in IGNORED_PROTOCOLS:
        return
    
    for raw_field in protocol:
        for field in handle_field(raw_field):
            fields.append(field)

    if len(fields) == 0:
        return
            
    yield {'name': name, 'descr': descr, 'fields': fields, }

def handle_field(field):
    ''' handle field '''
    
    fdetails = {'name': None, 'value': None, 'name_ext': None, 'value_ext': None}
    fdetails['name'] = field.attrib['name']
    
    if fdetails['name']:
        
        fdetails['value'] = field.attrib.get('show', None)
        fdescr = field.attrib.get('showname', None)
        
        fdescr = fdescr.split('=')
        if len(fdescr) > 1:
            fdescr = ''.join(fdescr[1:])
        fdescr = ''.join(fdescr)
            
        fdescr = fdescr.split(':')
        if len(fdescr) == 2:
            fdetails['name_ext'] = fdescr[0].strip()
            fdetails['value_ext'] = fdescr[1].strip()
            
        yield fdetails

    for emb_field in field:
        for field in handle_field(emb_field):
            yield field

def main():
    ''' main (select <packet> .. </packet> section)'''
    msg_count = 0
    msg_size = 0
    is_packet = False
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        
        # handle packet
        if line.startswith('<packet>'):
            packet = line
            is_packet = True
        elif line.startswith('</packet>'):
            packet += line
            is_packet = False
            for msg in handle_packet(packet):
                # pprint(msg, width=150)
                msg_count += 1
                msg_size += len(str(msg))
                sys.stdout.write("%s/%s\r" % (msg_count, msg_size))
            packet = ''
        elif is_packet:
            packet += line

if __name__ == '__main__':
    # TODO make analysis for command line agruments
    main()            
            


