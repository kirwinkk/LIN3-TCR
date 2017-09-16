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

KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"ℬᎶ戦神Bot 作者↓",
    "lang":"JP",
    "comment":"ℬᎶ戦神Family",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
cancelinvite = {
    'autoCancel':True,
    'autoCancelUrl':True
}

setTime = {}
setTime = wait2["setTime"]


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    if not op.param2 in ["uc216d8664c4e1f43772c98b1b0b8956e"]:
	try:
	   if op.type == 19:
              klist=[ki,kk,kc,cl,kg]
              kicker=random.choice(klist)
              kicker.kickoutFromGroup(msg.to,[target])
              Glist=[ki,kk,kc,cl,kg]
              Gicker=random.choice(Glist)
	      Gicker.inviteIntoGroup(op.param1,[op.param3])
	except Exception, e:
	   print 'failed'

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}
                    cl.sendMessage(msg)
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
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
