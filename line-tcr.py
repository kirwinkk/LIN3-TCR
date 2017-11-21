# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="EmbdaDwm2FzUKtrmz3h0.Z3UPvSwklykyvs15/Bopua.pRstNgi9ZtyCL+bQ2wRZ9o7275MZxVQThwIkIYfDrHs=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmTeeIYLrFRyCoCcMFn4.zLcxKZ4RJTbDzSDVqAkmva.FrF2i3m+cxHWDIphbM3yK6wY6Tp+WVc+cxCowCYDGTY=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="Em42jIzNbjWR537iSxv3.IyVZW2pcvY6KpyfY05FmSW.UJv2fc713HYC2nHTqxYPYzqxjhPndk7NJMPGx9eIyco=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Emllq2opZT2mH5qLrrdd.y5uKOl5vkdH88JG96gA/3q.yu9EcjVPabbbXQsWSbhCHK5eGjr1EAYUAdgwwGa+cOo=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="Em87uCyt37quq8p5dZe6.R909ux0qpOXLDpe8GYM7nG.P2S6wOhWM3x2b5iMgPq8u6sRVaifjtMQxuyuxCgaMYQ=")
ki4.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')


KAC=[ki,ki2,ki3,ki4]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,"uc216d8664c4e1f43772c98b1b0b8956e","u8dc2983d2e3183303bc466f3283d44d8","ubecd98a04cbf74a830b6c95b67bd6b74","u9378246da17ae7914b0a9a27da4802a0","ufdd4dbee33a2af45c13a72444277298d","ub5497e219585e4dad3373f25696c85fc","u58623d8e816b2dbf9cc8dc15b243e313","u6c81c99cb7ae718754ceb7db1718e7dd","u32f0dc24e048a1e357f655aff0a5fa33","u444a6355bfdc40238d3509e161458916","ud4b30af2044227c281d5d3ec69a584be","ufd9bec46aabcba3cdd9271f0db4b4ac8","u0bd59b43cef104e8e8f0c771d46689f4"]
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin = ["uc216d8664c4e1f43772c98b1b0b8956e"]
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
			try:
                            G = cl.getGroup(op.param1)
                        except:
                            G = cl.getGroup(op.param1)
                        G.name = "戦神☆style"
                        try:
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
						random.choice(KAC).updateGroup(group)
					except:
						pass
					random.choice(KAC).updateGroup(group)
				else:
					pass
	
        if op.type == 11:
            if op.param3 == '1':
		if op.param2 in Bots + admin + staff6:
			pass
		else:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        G = random.choice(KAC).getGroup(op.param1)
                    G.name = "戦神☆style"
                    try:
                        random.choice(KAC).updateGroup(G)
                    except:
                        cl.updateGroup(G)



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
				    group.preventJoinByTicket = True
				    random.choice(KAC).updateGroup(group)
				except:
				    group.preventJoinByTicket = True
                                    random.choice(KAC).updateGroup(group)
        if op.type == 19:
                    if op.param2 not in Bots:
                        G = cl.getGroup(op.param1)	
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)


			


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
                                cl.sendText(msg.to,"提升權限\n" + mi)
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
		
		
            elif ("Mkk:" in msg.text):
              if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
		     if target not in Bots:
                       try:
                           klist=[ki,ki2,ki3,ki4]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           klist=[ki,ki2,ki3,ki4]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
				
            elif "Nkk:" in msg.text:
              if msg.from_ in admin + staff6:
                    _name = msg.text.replace("Nkk:","")
                    gs = cl.getGroup(msg.to)
		    gs = ki.getGroup(msg.to)
		    gs = ki2.getGroup(msg.to)
		    gs = ki3.getGroup(msg.to)
		    gs = ki4.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"找不到用戶")
                    else:
                        for target in targets:
			  if target not in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                klist=[ki,ki2,ki3,ki4]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
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
			try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki.getGroup(op.param1)
				except:
					try:
						G = ki2.getGroup(op.param1)
					except:
						try:
							G = ki3.getGroup(op.param1)
						except:
							try:
								G = ki4.getGroup(op.param1)
							except:
								pass

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki3.updateGroup(G)
				except:
					try:
						ki4.updateGroup(G)
					except:
						try:
							ki.updateGroup(G)
						except:
							try:
								ki2.updateGroup(G)
							except:
								pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki4.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki3.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki2.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki.reissueGroupTicket(op.param1)
							except:
								pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki.updateGroup(G)
				except:
					try:
						ki2.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								pass
                        


                        
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
			try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki2.getGroup(op.param1)
				except:
					try:
						G = ki3.getGroup(op.param1)
					except:
						try:
							G = ki4.getGroup(op.param1)
						except:
							try:
								G = ki.getGroup(op.param1)
							except:
								pass

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki4.updateGroup(G)
				except:
					try:
						ki.updateGroup(G)
					except:
						try:
							ki2.updateGroup(G)
						except:
							try:
								ki3.updateGroup(G)
							except:
								pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki2.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki3.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki4.reissueGroupTicket(op.param1)
							except:
								pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki2.updateGroup(G)
				except:
					try:
						ki3.updateGroup(G)
					except:
						try:
							ki4.updateGroup(G)
						except:
							try:
								ki.updateGroup(G)
							except:
								pass


                        
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
			try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki3.getGroup(op.param1)
				except:
					try:
						G = ki4.getGroup(op.param1)
					except:
						try:
							G = ki.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								pass

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki.updateGroup(G)
				except:
					try:
						ki2.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki2.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki3.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki4.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki.reissueGroupTicket(op.param1)
							except:
								pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki3.updateGroup(G)
				except:
					try:
						ki4.updateGroup(G)
					except:
						try:
							ki.updateGroup(G)
						except:
							try:
								ki2.updateGroup(G)
							except:
								pass

			
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
			try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki4.getGroup(op.param1)
				except:
					try:
						G = ki.getGroup(op.param1)
					except:
						try:
							G = ki2.getGroup(op.param1)
						except:
							try:
								G = ki3.getGroup(op.param1)
							except:
								pass

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki2.updateGroup(G)
				except:
					try:
						ki3.updateGroup(G)
					except:
						try:
							ki4.updateGroup(G)
						except:
							try:
								ki.updateGroup(G)
							except:
								pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki3.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki4.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki2.reissueGroupTicket(op.param1)
							except:
								pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki4.updateGroup(G)
				except:
					try:
						ki.updateGroup(G)
					except:
						try:
							ki2.updateGroup(G)
						except:
							try:
								ki3.updateGroup(G)
							except:
								pass
                        
			
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
			try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki.getGroup(op.param1)
				except:
					try:
						G = ki2.getGroup(op.param1)
					except:
						try:
							G = ki3.getGroup(op.param1)
						except:
							try:
								G = ki4.getGroup(op.param1)
							except:
								pass

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki3.updateGroup(G)
				except:
					try:
						ki4.updateGroup(G)
					except:
						try:
							ki.updateGroup(G)
						except:
							try:
								ki2.updateGroup(G)
							except:
								pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki4.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki3.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki2.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki.reissueGroupTicket(op.param1)
							except:
								pass
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki.updateGroup(G)
				except:
					try:
						ki2.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								pass
                        

            except:
                pass

        if op.type == 5:
            if wait["autoAdd"] == True:
		cl.findAndAddContactsByMid(op.param1)
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




def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
			try:
                                cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"] + "\n\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
			except:
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()

def nameUpdate():
    while True:
        try:
		profile = cl.getProfile()
		profile = ki.getProfile()
		profile = ki2.getProfile()
		profile = ki3.getProfile()
		profile = ki4.getProfile()
		profile.displayName = "戦神@tester"
		profile.statusMessage = "TESTING..."
                cl.updateProfile(profile)
		profile.displayName = "A"
                ki.updateProfile(profile)
		profile.displayName = "B"
                ki2.updateProfile(profile)
		profile.displayName = "C"
                ki3.updateProfile(profile)
		profile.displayName = "D"
                ki4.updateProfile(profile)

                time.sleep(600000)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
