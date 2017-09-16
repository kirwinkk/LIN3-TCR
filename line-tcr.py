# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

setTime = {}
setTime = wait["setTime"]

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    cl._client.sendMessage(messageReq[to], mes)

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
	if op.type == 13:
           cl.getGroup(op.param1)
           cl.acceptGroupInvitation(op.param1)
	   group = cl.getGroup(op.param1)
           gMembMids = [contact.mid for contact in group.invitee]
           for _mid in gMembMids:
               cl.cancelGroupInvitation(op.param1,[_mid])
           sendMessage(op.param1, "ℬᎶ戦神Cancel Bot 作者↓")
	   sendMessage(op.param1, text=None, contentMetadata={'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}, contentType=13)
	   cl.leaveGroup(op.param1)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return

def NOTIFIED_ADD_CONTACT(op):
    try:
        sendMessage(op.param1, "ℬᎶ戦神Cancel Bot 作者↓")
        sendMessage(op.param1, text=None, contentMetadata={'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}, contentType=13)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    if not op.param2 in ["uc216d8664c4e1f43772c98b1b0b8956e"]:
	try:
	   if op.type == 19:
	      cl.kickoutFromGroup(op.param1,[op.param2])
	      cl.inviteIntoGroup(op.param1,[op.param3])
	except Exception, e:
	   print 'failed'
