# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="EmKUkREuwG9katcijZWa.qRHtLeMrYRtDtWS8Gd3XUG.bZccCqSezzSOOmmpTaR4Cs/0TPnLNys0l7mJ3E0sRMU=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmuDbTqEzubaPQ54hNed.RPlFPNCz9GMhPhBdqO90tq.9dVQXB2KujWkCvJEQvDpXDYcSClin/Cq/3ZsnBzvzak=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EmG54gejzghjQIh42G35.rDcaNym6DpBGSUxr9n2Vbq.jbR8xK9mVsslTh3YZpGC/0VFTSWanJ//zVJdgQ0V5+s=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EmR416XVjFlBUZgB7Vl6.v+K1KGPh4LeOeOJEMER+fG.UH3iIhhSxc/TZNiB/cpmRyZ1lswTYmDDkZPkc4Dt5LU=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EmUjXndELGkJl2Ob86db.fESunGlkMJmWdmTqsPzUoW.aCLA52BcAspEXqEulPnOCal+cNhut+2ObLbD6Mqo6Fs=")
ki4.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')


KAC=[cl,ki,ki2,ki3,ki4]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,"uc216d8664c4e1f43772c98b1b0b8956e"]
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin = "uc216d8664c4e1f43772c98b1b0b8956e"
staff6 = ["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","ua1d924caa58666ee73d0625ca036a1b1"]

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"戦神代行SelfBOT\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
    'lang':"JP",
    'comment':"戦神☆style",
    'commentOn':True,
    'commentBlack':{},
    'wblack':False,
    'dblack':False,
    'likeOn':True,
    'blacklist':{},
    'wblacklist':False,
    'dblacklist':False,
    'protect':False,
    'cancelprotect':False,
    'inviteprotect':False,
    'linkprotect':False,
}


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
	      if op.param2 in admin + staff6:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			try:
				G.name = "万由里☆style"
				cl.updateGroup(G)
			except:
				pass
			G.preventJoinByTicket = False
                        cl.updateGroup(G)
			invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
			
	      else:
		  cl.acceptGroupInvitation(op.param1)
                  cl.leaveGroup(op.param1)


		
        if op.param3 == "4":
		if op.param2 in Bots + admin + staff6:
			pass
		else:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					try:
						random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
					except:
						pass
					try:
						random.choice(KAC).updateGroup(group)
					except:
						pass
					random.choice(KAC).updateGroup(group)
				else:
					pass
	
        if op.type == 11:
            if op.param3 == '1':
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        G = random.choice(KAC).getGroup(op.param1)
                    G.name = "万由里☆style"
                    try:
                        random.choice(KAC).updateGroup(G)
                    except:
                        cl.updateGroup(G)
                    if op.param2 in Bots + admin + staff6:
                        pass
                    else:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
        if op.type == 32:
            if op.param2 not in Bots + admin + staff6:
		G = cl.getGroup(op.param1)
		G.preventJoinByTicket = True
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])  
		kicker = random.choice(KAC)
		kicker2 = random.choice(KAC)
		key1 = "uc216d8664c4e1f43772c98b1b0b8956e"
		key2 = "ua1d924caa58666ee73d0625ca036a1b1"
		kicker.findAndAddContactsByMid(key1)
                kicker.inviteIntoGroup(op.param1,[key1])
		kicker2.findAndAddContactsByMid(key2)
                kicker2.inviteIntoGroup(op.param1,[key2])

        if op.type == 13:
			if op.param2 in Bots + admin + staff6:
				pass
			else:
				group = cl.getGroup(op.param1)
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				try:
				    random.choice(KAC).cancelGroupInvitation(op.param1,InviterX)
				except:
				    cl.cancelGroupInvitation(op.param1,InviterX)
				try:
				    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
				    group.preventJoinByTicket = True
				    random.choice(KAC).updateGroup(group)
				except:
				    group.preventJoinByTicket = True
                                    random.choice(KAC).updateGroup(group)
        if op.type == 19:
                    if op.param2 not in Bots:
                      if op.param3 not in Bots:
                        G = cl.getGroup(op.param1)
					
                        try:
				random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
				
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)

        if op.type == 19:
                    if op.param3 in admin + staff6:
                        kicker = random.choice(KAC)
			kicker2 = random.choice(KAC)
		        key1 = "uc216d8664c4e1f43772c98b1b0b8956e"
			key2 = "ua1d924caa58666ee73d0625ca036a1b1"
		        kicker.findAndAddContactsByMid(key1)
                        kicker.inviteIntoGroup(op.param1,[key1])
			kicker2.findAndAddContactsByMid(key2)
                        kicker2.inviteIntoGroup(op.param1,[key2])
			


        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
				
			
			
			
        if op.type == 26:
            msg = op.message
            if msg.text is None:
                return
            if ("Lv1:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   mi = ""
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   mi += "\n->" + cl.getContact(key1).displayName
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff6.append(target)
                                cl.sendText(msg.to,"提升權限至Lv.1\n" + mi)
                            except:
                                pass
                   print "[Command]Staff1 add executed"
                else:
                    pass
	

            elif ("Lvd1:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   mi = ""
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   mi += "\n->" + cl.getContact(key1).displayName
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff6.remove(target)
				cl.sendText(msg.to,"解除權限至Lv.0\n" + mi)
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
	
	
            elif msg.text in ["/Level","/level"]:
              if msg.from_ in admin + staff6:
                if staff6 == []:
                    cl.sendText(msg.to,"沒有權限用戶")
                else:
                    cl.sendText(msg.to,"權限名單讀取中...")
                    mc = ""
                    for mi_d in staff6:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"權限用戶:\n\n€權限Lv.1\n" + mc)
                    print "[Command]Stafflist executed"
              else:
                    pass
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Bots:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = ki.getGroup(op.param1)
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki.kickoutFromGroup(op.param1,[op.param2])
				except:
					print ("["+op.param1+"]の["+op.param2+"]")
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        


                        
                elif op.param3 in kimid:
                    if op.param2 in Bots:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = ki2.getGroup(op.param1)
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki2.kickoutFromGroup(op.param1,[op.param2])
				except:
					print ("["+op.param1+"]の["+op.param2+"]")
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)


                        
                elif op.param3 in ki2mid:
                    if op.param2 in Bots:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = ki3.getGroup(op.param1)
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki3.kickoutFromGroup(op.param1,[op.param2])
				except:
					print ("["+op.param1+"]の["+op.param2+"]")
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

			
                elif op.param3 in ki3mid:
                    if op.param2 in Bots:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = ki4.getGroup(op.param1)
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki4.kickoutFromGroup(op.param1,[op.param2])
				except:
					print ("["+op.param1+"]の["+op.param2+"]")
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        
			
                elif op.param3 in ki4mid:
                    if op.param2 in Bots:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = cl.getGroup(op.param1)
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					cl.kickoutFromGroup(op.param1,[op.param2])
				except:
					print ("["+op.param1+"]の["+op.param2+"]")
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        

            except:
                pass


        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error







while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
