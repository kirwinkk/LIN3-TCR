# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token='Ekz4TgKpeSWkDvNsetY0.3FLXqaAHaqU2vr+bb+uJKa.5/52TwKOUdn8x2wWxkc2sBYihCNVQVO0/L+nx6GKNao=')
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token='EkeIbgnKT7pYht2uGX68.iarQyHUgknIRni5Recj+Ea.LLGh4VA86sDoXEZO4LPKEPFcFSTUlmF1kvmk3+KsibA=')
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token='EkUTvGSfGiJl7neSSY01.qmf+mG4qg58AVj7ARoBTuq.7zaTkwOMZslGg9hUAq+F6joM8+2gxN/GkA8FFhZm8U0=')
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token='EkFxBRmXkbP3J3mAZPM3.vy5yDd4vkH13GPwq582miW.yquPVYw1Q9FjnJjTEECpQ3AU0xiNsriNsUFWw0B2TVA=')
kc.loginResult()

ky = LINETCR.LINE()
ky.login(token='Eky0a6tUTzgY4zAzVKY7.lsg729+o8geYYbTPFd32PW.oQSMtWz0MjwWuTOmqKO6U7mImAXqBj8CuDjpTAoxYMQ=')
ky.loginResult()

kl = LINETCR.LINE()
kl.login(token='EkN92i8fe4PQXh1vVbje.WHByzKXoh0n3ljIXSlIvBG.Hfz37sRHcafxFBbbWn/A6Kia/Wj1H5sJ3XBVovnhm1c=')
kl.loginResult()

kg = LINETCR.LINE()
kg.login(token='EkbtaEs6ecRBDHY2GAO5.O5vYqaA4b24ldPRYl/Uifq.8SiDO7eBi4Lp7jTOu/fTepjjfT8YF2DgU26tUuWyexY=')
kg.loginResult()

kh = LINETCR.LINE()
kh.login(token='EkSuazYXrX9MUmQrqnvb.JGXi37xKf5CbOC+nc/LtgW.khGEAlboJI1eag04hIc7036RMz9bXSWWDis6yenczOY=')
kh.loginResult()

ko = LINETCR.LINE()
ko.login(token='Ek3OYxaByvgnrvrZGCOc.a5njsIjkYmhnIxHDMAEHBa.OHLH1yI9feT4JExNdeU22jVLQptyVxarfQ1B/rgA/Lk=')
ko.loginResult()

kj = LINETCR.LINE()
kj.login(token='EkENC4R1oazaYwD3IEde.anot7ok1CmMlkurtH8BKxG.cCsFQzxbtd2HxKcIeH7BFA9X01yGwKNcIAZWuVs4p+s=')
kj.loginResult()

ka = LINETCR.LINE()
ka.login(token='EkBFUH2KRvooCziIe3K9.sZWYkriJsJf80xBKZDkbsq.kadwbKtdlV2Sv/yfxtAmdFHm3k0ymvMd68ZT98tM5Z0=')
ka.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

KAC=[cl,ki,kk,kc,ky,kl]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Lmid = ky.getProfile().mid
Umid = kl.getProfile().mid
Hmid = kh.getProfile().mid
Imid = ko.getProfile().mid
Jmid = kj.getProfile().mid
Pmid = ka.getProfile().mid
admin = ["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
staff = ["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","ua5246fb6c9e7fce0cf982776298b709b"]
Bots=[mid,Amid,Bmid,Cmid,Lmid,admin,staff,Umid,Hmid,Imid,Jmid,Pmid]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"ℬᎶ戦神Bot 作者:http://line.me/ti/p/4-ZKcjagH0",
    "lang":"JP",
    "comment":"ℬᎶ戦神Family",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"ℬᎶ戦神Bot",
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
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
			
                if op.param3 in Umid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kl.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
			
                if op.param3 in Hmid:
                    if op.param2 in mid:
                        X = ka.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
			
                if op.param3 in Imid:
                    if op.param2 in mid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ko.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
			
                if op.param3 in Jmid:
                    if op.param2 in mid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        kj.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
			
                if op.param3 in Pmid:
                    if op.param2 in mid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
			

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
			    cl.sendText(msg.to,"此機器作者↓")
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}
                            cl.sendMessage(msg)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
		
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:
                    klist=[ki,kk,kc]
                    fuck=random.choice(klist) 
                    G = fuck.getGroup(op.param1)
                    ginfo = fuck.getGroup
                    G.preventJoinByTicket = True
                    Ticket = ki.reissueGroupTicket(op.param1)
                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki.updateGroup(G)
                    ky.kickoutFromGroup(op.param1,[op.param2])  
                    G = fuck.getGroup(op.param1)   
                    G.preventJoinByTicket = True
                    fuck.updateGroup(G)
                    ky.leaveGroup(op.param1)
                 except Exception, e:
                           print e
			
        if op.type == 11:
            if cancelinvite["autoCancelUrl"] == True:
                if cl.getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        cl.reissueGroupTicket(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        print "Url Opened, Autokick on"
                else:
                    print "random group update"
            else:
                pass
	

			
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        gs = kc.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
			kk.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kk.updateGroup(G)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Umid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
			ki.kickoutFromGroup(op.param1,[op.param2])
			cl.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
			
		if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
			ka.kickoutFromGroup(op.param1,[op.param2])
			kj.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ko.updateGroup(G)
                    Ti = ko.reissueGroupTicket(op.param1)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
			
		if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
			ko.kickoutFromGroup(op.param1,[op.param2])
			ka.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"
                    G = kj.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kj.updateGroup(G)
                    Ti = kj.reissueGroupTicket(op.param1)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
			
		if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
			kh.kickoutFromGroup(op.param1,[op.param2])
			ka.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ka.updateGroup(G)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

		if Pmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
			kj.kickoutFromGroup(op.param1,[op.param2])
			kh.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"
                    G = kj.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kj.updateGroup(G)
                    Ti = kj.reissueGroupTicket(op.param1)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kj.updateGroup(X)
                    Ti = kj.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
			
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
			cl.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
		    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
			cl.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
			ki.kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    except:
			print "kicker kicked"
			
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
			
               

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

            elif ("Gn:" in msg.text):
                if msg.from_ in staff:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")

            elif msg.text in ["cancel","Cancel","C","c"]:
                if msg.from_ in staff:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
			ki.cancelGroupInvitation(msg.to, gInviMids)
			kk.cancelGroupInvitation(msg.to, gInviMids)
			kc.cancelGroupInvitation(msg.to, gInviMids)
			cl.sendText(msg.to, str(len(group.invitee)) + "人 已被戦神取消(´∀｀)♡")
			ki.sendText("[戦神" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"邀請中沒人啊..." + "\n[戦神" + datetime.datetime.today().strftime('%H:%M:%S') + "]")
                        else:
                            cl.sendText(msg.to,"邀請中沒人啊..." + "\n[戦神" + datetime.datetime.today().strftime('%H:%M:%S') + "]")

            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)

            elif msg.text in ["urlon","Urlon"]:
                if msg.from_ in staff:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已開啟網址")
                    else:
                        cl.sendText(msg.to,"網址為開啟狀態")
            elif msg.text in ["BG1urlon"]:
                if msg.from_ in staff:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"已開啟網址")
                    else:
                        ki.sendText(msg.to,"網址為開啟狀態")

            elif msg.text in ["BG2urlon"]:
                if msg.from_ in staff:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"已開啟網址")
                    else:
                        kk.sendText(msg.to,"網址為開啟狀態")

            elif msg.text in ["BG3urlon"]:
                if msg.from_ in staff:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"已開啟網址")
                    else:
                        kc.sendText(msg.to,"網址為開啟狀態")

            elif msg.text in ["urloff","Urloff"]:
                if msg.from_ in staff:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉網址")
                    else:
                        cl.sendText(msg.to,"網址為關閉狀態")
            elif msg.text in ["BG1urloff"]:
                if msg.from_ in staff:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"已關閉網址")
                    else:
                        ki.sendText(msg.to,"網址為關閉狀態")
            elif msg.text in ["BG2urloff"]:
                if msg.from_ in staff:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"已關閉網址")
                    else:
                        kk.sendText(msg.to,"網址為關閉狀態")
            elif msg.text in ["BG3urloff"]:
                if msg.from_ in staff:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"已關閉網址")
                    else:
                        kc.sendText(msg.to,"網址為關閉狀態")

            elif msg.text in ["author","Author","作者"]:
                if msg.from_ in staff:
			msg.contentType = 13
			cl.sendText(msg.to,"此機器作者↓")
                        msg.contentMetadata = {'mid': "uc216d8664c4e1f43772c98b1b0b8956e"}
                        cl.sendMessage(msg)
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["BGurl"]:
                if msg.from_ in staff:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
            elif msg.text in ["BG1url"]:
                if msg.from_ in staff:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
            elif msg.text in ["BG2url"]:
                if msg.from_ in staff:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
            elif msg.text in ["BG3url"]:
                if msg.from_ in staff:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)

#----------------------------------------------
            elif "Ownera:@" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Ownera:@","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"找不到此用戶")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"已提升權限")
                            except:
                                pass
                    print "[Command]Staff add executed"

            elif "Ownerd:@" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Ownerd:@","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"找不到此用戶")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"已刪除權限")
                            except:
                                pass
                    print "[Command]Staff remove executed"

            elif msg.text in ["權限名單","Owner","owner","Ownerlist"]:
              if msg.from_ in staff:
                if staff == []:
                    cl.sendText(msg.to,"尚無權限者")
                else:
                    cl.sendText(msg.to,"權限者:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +random.choice(KAC).getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"

            elif msg.text in ["BGbot","BG bot","BG Bot"]:
		if msg.from_ in staff:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
			kh.acceptGroupInvitationByTicket(msg.to,Ticket)
			ko.acceptGroupInvitationByTicket(msg.to,Ticket)
			kj.acceptGroupInvitationByTicket(msg.to,Ticket)
			ka.acceptGroupInvitationByTicket(msg.to,Ticket)
			kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
                else:
                        cl.sendText(msg.to,"權限不足 作者加入!")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kl.acceptGroupInvitationByTicket(msg.to,Ticket)
			G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["BGbye"]:
                if msg.from_ in staff:
                    ginfo = cl.getGroup(msg.to)
                    try:
			cl.sendText(msg.to,"掰掰~")
                        cl.leaveGroup(msg.to)
			ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
			ko.leaveGroup(msg.to)
                        kj.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.from_ in staff:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"沒有黑單在此群")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,kj,kh,ko,ka]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                            cl.sendText(msg.to,"已踢出黑單")
                        except:
                            pass
		
            elif "Nk:" in msg.text:
                if msg.from_ in staff:
                    print "ok"
                    _name = msg.text.replace("Nk:","")
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"找不到用戶")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,kk,kc,kj,kh,ko,ka]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
				cl.sendText(msg.to,"已踢出用戶")
                            except:
                                cl.sendText(msg.to,"錯誤!!!!!!!!")
		
		
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Cleanse","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
			ki.sendText(msg.to,"ℬᎶ戦神Bot降臨~")
                        kk.sendText(msg.to,"ℬᎶ戦神Bot降臨~")
                        kc.sendText(msg.to,"ℬᎶ戦神Bot降臨~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"ℬᎶ戦神Bot降臨~")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,kk,kc,kj,kh,ko,ka]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"ℬᎶ戦神Bot降臨~")
                                    kk.sendText(msg.to,"ℬᎶ戦神Bot降臨~")
                                    kc.sendText(msg.to,"ℬᎶ戦神Bot降臨~")

            elif "Mk:@" in msg.text:
                  if msg.from_ in staff:
                       nk0 = msg.text.replace("Mk:@","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"找不到用戶")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[ki,kk,kc,kj,kh,ko,ka]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"已成功踢出用戶")
				
            elif "Bl:@" in msg.text:
                if msg.from_ in staff:
                    print "[Ban]ok"
                    _name = msg.text.replace("Bl:@","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"沒有找到用戶")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"已黑單此用戶")
                            except:
                                cl.sendText(msg.to,"已黑單此用戶")
            elif "Ubl:@" in msg.text:
                if msg.from_ in staff:
                    print "[Unban]ok"
                    _name = msg.text.replace("Ubl:@","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"沒有找到用戶")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"已解除黑單")
                            except:
                                cl.sendText(msg.to,"已解除黑單")
#-----------------------------------------------
            elif msg.text in ["Test"]:
	      if msg.from_ in staff:
		cl.sendText(msg.to,"ℬᎶ戦神Bot主機")
                ki.sendText(msg.to,"ℬᎶ戦神Bot  1")
                kk.sendText(msg.to,"ℬᎶ戦神Bot  2")
                kc.sendText(msg.to,"ℬᎶ戦神Bot  3")
#-----------------------------------------------
            elif msg.text in ["愛"]:
	      if msg.from_ in staff:
		cl.sendText(msg.to,"戰神愛貓咪")
                ki.sendText(msg.to,"貓咪愛戰神")
                kk.sendText(msg.to,"ㄎㄩ愛ㄌㄑ")
                kc.sendText(msg.to,"ㄌㄑ愛ㄎㄩ")

#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
	      if msg.from_ in staff:
                start = time.time()
                cl.sendText(msg.to, "BG戦神Bot讀取中...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                kc.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["ban","Ban"]:
                if msg.from_ in staff:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"請傳送友資")
                    print "[Command]Ban executed"
            elif msg.text in ["Unban","unban"]:
                if msg.from_ in staff:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"請傳送友資")
                    print "[Command]Unban executed"
            elif msg.text in ["Bl","BL","bl"]:
              if msg.from_ in staff:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"戦神Bot-BLACKLIST\n\n尚無")
                else:
                    cl.sendText(msg.to,"黑名單用戶如下:")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.from_ in staff:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Blk"]:
                if msg.from_ in staff:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"[ℬᎶ戦神Bot]\n沒有黑單在此群")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"[ℬᎶ戦神Bot]\n黑單用戶已踢出!")
		
            elif "album:" in msg.text:
                try:
                    albumtags = msg.text.replace("album:","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fake:" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fake:","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","40","45","50","55","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(60)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
                try:    
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ky.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"ℬᎶ台灣戦神Style\nhttp://line.me/ti/p/4-ZKcjagH0")
                    print "Like"
                except:
                    pass
        else:
                print "Not Admin or staff"

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
