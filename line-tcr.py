# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="EmiOc8nvbbvwfchX8eZc.WLRCsJRm0xoKELSKVXYJFa.TevkCPa1hjGh7N0VEa/XY3n6unFgp3JrmQtG5Rk2T1s=")
cl.loginResult()


ki = LINETCR.LINE()
ki.login(token="EmMqK1Iy4wOZSzF9Nz0e.MM/lmsWyPqaOXUzfmNLwpG.yknRCwQNcsYg9wg2rbmxsTQSKQ7sPgG7RkoeTm39/TA=")
ki.loginResult()


ki2 = LINETCR.LINE()
ki2.login(token="EmauyUM9i6tEmRzzRGd6.0FzcDg6DlE2Zzgh4jmXITG.cWPYFzTrFW7qykxnm88DgAasysFFhWlH3bvfFeqoKNY=")
ki2.loginResult()


ki3 = LINETCR.LINE()
ki3.login(token="EmHIeBTuMAiGUzzBR9fb.teS33yz1Gm5aDFKFPFCTsW.L5h02YfBGUDmMncKwcdVSJkp1Ii7mUfvT3L9zhBBs84=")
ki3.loginResult()


ki4 = LINETCR.LINE()
ki4.login(token="EmlJrZFzNxl05j3g2Y40.oVCSiGdNzkXHvuGyYsCf4a.RSSTi/03hrMFcAShaNU0Bqiu2HS1UWvgGuO0Vc8p2fY=")
ki4.loginResult()


ki5 = LINETCR.LINE()
ki5.login(token="EmC03j4ktIyT5OosKXTb.nd1EnvG4MSHUqjnC8eKYQW.lnJq6JV748Ml8YvV1Dej/7pVtQv0EvUzoCY34jMjl74=")
ki5.loginResult()


ki6 = LINETCR.LINE()
ki6.login(token="Ems1RSRAdsg2Wu69iJf3.uwjeJKNBljacc2UbuiYjGW.KLK7btiiIfFmOWORd3BNL2I1CebQWfYBKB1bIacmTm4=")
ki6.loginResult()


ki7 = LINETCR.LINE()
ki7.login(token="Emjt0Y4LJRYsE2MvZw94.Nyu3cmo7uwhUzrp8zQsoja.0tkPd5dRfJRNNlMVNrEZ2CLnqpG+SEX18hAUMrOYslk=")
ki7.loginResult()


ki8 = LINETCR.LINE()
ki8.login(token="EmKTFaKERF8GNAnv3t01.G+CFyIC/aZmNLw/a2ZdS0q.iPz4gGbB+VtueqKTdKJMAAt4v1vNY4QKX8Q5XxVOvNc=")
ki8.loginResult()


ki9 = LINETCR.LINE()
ki9.login(token="EmzgKE72ZP6B2EhEFa33.BY+PNmAwY2YOUw6R7E0qKW.PZyyXEujZJcDbkTrDbufvNmERyKMYdBwK9oIsW1/nfs=")
ki9.loginResult()


ki10 = LINETCR.LINE()
ki10.login(token="EmRpgzsjyWulpgDyrgd8.MzTc0trBAWQR3q7w6uHv6a.ukqvRZe3c6r7gyVmer/0i/mugK6nVmghqn+IGOdBvrE=")
ki10.loginResult()

ki11 = LINETCR.LINE()
ki11.login(token="Em55pBNdAcupX2AA6wK6.AMMZOO6GzAMI+1kaIF3D1G.QfuZXfzsgw4RjqwIRMt0kMIHZBK838BvREgk27JGdiU=")
ki11.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""[戦神SelfBOT]

[help]→查看指令
[Author]→作者顯示
[Me]→顯示自己友資
[Mid]→顯示自己mid
[Gid]→顯示群組
[封鎖名單]→確認已封鎖用戶
[Ginfo]→顯示群組詳情
[Cancel]→取消所有邀請
[Kick:]→mid踢人
[Invite:]→mid邀人
[BG1invite:]→mid kicker1邀人
[Inv:]→標註邀人
[BG1inv:]→標註kicker1邀人
[Nk:]→名字本帳踢人
[Nkk:]→名字kicker踢人
[Mk:@]→標註本帳踢人
[Mkk:@]→標註kicker踢人
[M1k:@]→標註指定kicker踢人
[Bl:@]→標註黑單
[Ubl:@]→標註解除黑單
[Ban:]→名字黑單
[Unban:]→名字解除黑單
[Ban]→友資黑單
[Unban]→友資解除黑單
[Mban:]→mid黑單
[Munban:]→mid解除黑單
[Bl]→查看黑單
[Banlist]→查看此群黑單
[Blk]→踢出黑單
[Wl:@]→標註白單
[Wld:@]→標註解除白單
[Wl]→查看白單
[Url]→取得群組網址
[Urlon]→開啟群組網址
[Urloff]→關閉群組網址
[Groupid]→目前加入的所有群組
[Mid:]→顯示被標註者的mid
[Mc:]→顯示被標註者的友資
[mid:]→顯示mid的友資
[Gift]→發送禮物
[TL:]→Po文
[Time]→現在時間
[Tagall]→標註所有人
[Say:]→保鑣講話
[BGbot]→追加kicker
[bot1]→追加kicker1
[BGbye]→kicker退出
[bot1bye]→kicker1退出
[Botcontact]→查看Kicker友資
[Botmid]→查看Kicker的mid
[Sp]→反應速度
[Point]→抓已讀者
[Read]→查看已讀名單
[Joinon/off]→自動入群開關
[Botjoinon/off]→kicker自動入群開關
[Leaveon/off]→自動退出副本開關
[set]→設定確認
[Pkickon/off]→踢人保護開關
[Pnameon/off]→群名保護開關
[Purlon/off]→網址保護開關
[Pinviteon/off]→招待保護開關
[Pallon/off]→所有保護開關
[Gset]→群組設定確認

作者:戦神
http://line.me/ti/p/4-ZKcjagH0"""
KAC=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
KAC3=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
ki11mid = ki11.getProfile().mid

Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid,"ubecd98a04cbf74a830b6c95b67bd6b74","ua1d924caa58666ee73d0625ca036a1b1","u8dc2983d2e3183303bc466f3283d44d8"]
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin = "uc216d8664c4e1f43772c98b1b0b8956e"
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
bgbot = []

wait = {
    'contact':True,
    'autoJoin':False,
    'urlJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"戦神SelfBOT\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
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
    'pnharfbot':{},
    'pname':{},
    'pro_name':{},  
    'pinvite':{},
    'pkick':{},  
    'purl':{},  
}

wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }
	
setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}


def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1



def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
                        ginfo = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
                        cl.updateGroup(G)
			invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
			G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
		        try:
                            cl.sendText(op.param1,"戦神☆style^^\n\n作者:戦神\nhttp://line.me/ti/p/4-ZKcjagH0")
		        except:
			    pass

        if op.param3 == "4":
            if op.param1 in wait['purl']:
		if op.param2 in Bots + bgbot:
			pass
		else:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					try:
						random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
						except:
							pass
					try:
						random.choice(KAC).updateGroup(group)
					except:
						try:
							random.choice(KAC).updateGroup(G)
                        			except:
							try:
								ki7.updateGroup(G)
							except:
							    try:
									ki8.updateGroup(G)
							    except:
								try:
									ki3.updateGroup(G)
								except:
							           try:
								     ki4.updateGroup(G)
							           except:
								     try:
									ki10.updateGroup(G)
								     except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															cl.updateGroup(G)
				else:
					pass
	
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
		  if op.param2 not in Bots + bgbot:
                    try:
                        G = cl.getGroup(op.param1)
			c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':op.param2}
                    except:
			try:
                        	G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
                        		random.choice(KAC).updateGroup(G)
				except:
					pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        random.choice(KAC).updateGroup(G)
                    except:
                        cl.updateGroup(G)
                    if op.param2 in Bots + bgbot:
                        pass
                    else:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
			    try:
				random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    except:
				pass
                    

        if op.type == 13:
                if op.param1 in wait['pinvite']:
			OWN = Bots
			if op.param2 in OWN + bgbot:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				try:
				    random.choice(KAC).cancelGroupInvitation(op.param1,InviterX)
				except:
				    try:
				        random.choice(KAC).cancelGroupInvitation(op.param1,InviterX)
				    except:
					try:
						ki6.cancelGroupInvitation(op.param1,InviterX)
					except:
						try:
							ki7.cancelGroupInvitation(op.param1,InviterX)
						except:
							try:
								ki9.cancelGroupInvitation(op.param1,InviterX)
							except:
								try:
									ki5.cancelGroupInvitation(op.param1,InviterX)
								except:
									try:
										ki4.cancelGroupInvitation(op.param1,InviterX)
									except:
										try:
											ki.cancelGroupInvitation(op.param1,InviterX)
										except:
											try:
												ki3.cancelGroupInvitation(op.param1,InviterX)
											except:
												try:
													ki2.cancelGroupInvitation(op.param1,InviterX)
												except:
													try:
														ki10.cancelGroupInvitation(op.param1,InviterX)
													except:
														try:
															cl.cancelGroupInvitation(op.param1,InviterX)
														except:
															pass
				try:
					try:
                             			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									a5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
														except:
															pass

				except:
                                    pass
        if op.type == 19:
             if op.param1 in wait['pkick']:
                    if op.param2 in Bots + bgbot:
                        pass
                    else:
                      if op.param3 not in Bots:
                        G = cl.getGroup(op.param1)
					
                        try:
				random.choice(KAC3).kickoutFromGroup(op.param1,[op.param2])
                        except:
				try:
                                	random.choice(KAC2).kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
					except:
						pass
				
                        G.preventJoinByTicket = True
			try:
				random.choice(KAC3).updateGroup(G)
                        except:
				try:
                                	random.choice(KAC2).updateGroup(G)
				except:
					try:
						random.choice(KAC).updateGroup(G)
					except:
						pass

			
			
             else:
                        pass
		

                        
			

		
		
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "uc216d8664c4e1f43772c98b1b0b8956e":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki2.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki3.acceptGroupInvitationByTicket(list_[1],list_[2])							
                            X = cl.getGroup(list_[1])
                            X = ki.getGroup(list_[1])
                            X = ki2.getGroup(list_[1])
                            X = ki3.getGroup(list_[1])							
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            ki.updateGroup(X)
                            ki2.updateGroup(X)
                            ki3.updateGroup(X)							
                        except:
                            cl.sendText(msg.to,"error")
        if op.type == 13:
	     if op.param2 not in Bots:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
				try:
				    random.choice(KAC).cancelGroupInvitation(op.param1, matched_list)
				except:
					try:
						random.choice(KAC).cancelGroupInvitation(op.param1, matched_list)
					except:
						try:
							random.choice(KAC).cancelGroupInvitation(op.param1, matched_list)
						except:
							try:
								ki9.cancelGroupInvitation(op.param1, matched_list)
							except:
								try:
									ki5.cancelGroupInvitation(op.param1, matched_list)
								except:
									try:
										ki4.cancelGroupInvitation(op.param1, matched_list)
									except:
										try:
											ki.cancelGroupInvitation(op.param1, matched_list)
										except:
											try:
												ki3.cancelGroupInvitation(op.param1, matched_list)
											except:
												try:
													ki2.cancelGroupInvitation(op.param1, matched_list)
												except:
													try:
														ki10.cancelGroupInvitation(op.param1, matched_list)
													except:
														try:
															cl.cancelGroupInvitation(op.param1, matched_list)
														except:
															pass
		
        if op.type == 13:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1, matched_list)

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
		
        if op.param3 == "4":
            if wait["blacklist"][op.param2] == True:
		if op.param2 in Bots + bgbot:
			pass
		else:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					try:
                                          random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			                except:
				             try:
					         random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
				             except:
						  try:
							ki.kickoutFromGroup(op.param1,[op.param2])
						  except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
														except:
															try:
																cl.kickoutFromGroup(op.param1,[op.param2])
															except:
																pass
															
					try:
						random.choice(KAC).updateGroup(group)
					except:
						try:
							random.choice(KAC).updateGroup(G)
                        			except:
							try:
								ki7.updateGroup(G)
							except:
							    try:
									ki8.updateGroup(G)
							    except:
								try:
									ki3.updateGroup(G)
								except:
							           try:
								     ki4.updateGroup(G)
							           except:
								     try:
									ki10.updateGroup(G)
								     except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															cl.updateGroup(G)
				else:
					pass

		
	if op.type == 17:
	    if wait["blacklist"][op.param2] == True:
		if op.param2 in Bots + bgbot:
		    pass
		else:
		   try:
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
														except:
															pass
			try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = random.choice(KAC).getGroup(op.param1)
				except:
					try:
						G = random.choice(KAC).getGroup(op.param1)
					except:
						try:
							G = ki8.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			G.preventJoinByTicket = True
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					random.choice(KAC).updateGroup(G)
				except:
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
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass
		   except:
			pass
			
            
		
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ki.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
			if msg.contentMetadata["mid"] in wait["blacklist"]:
                             cl.sendText(msg.to,msg.contentMetadata["mid"])
                        else:
			     cl.sendText(msg.to,msg.contentMetadata["mid"])

			
			

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n->" + Name
                        wait2['ROM'][op.param1][op.param2] = "->" + Name
                else:
                    cl.sendText
            except:
                  pass

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,msg.contentMetadata["displayName"] + " 已加入黑單")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,msg.contentMetadata["displayName"] + " 已加入黑單")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,msg.contentMetadata["displayName"] + " 已解除黑單")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,msg.contentMetadata["displayName"] + " 已解除黑單")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[戦神SelfBOT]\n[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個性簽名]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[戦神SelfBOT]\n[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個性簽名]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "[戦神SelfBOT]\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "文章網址 URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
		


            elif msg.text is None:
                return
            if msg.text == "help":
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)

            elif msg.text in ["Pkickon","pkickon"]:
                if msg.to in wait['pkick']:
                    cl.sendText(msg.to,"已開啟禁止踢人保護!")
                else:
                    cl.sendText(msg.to,"禁止踢人保護開啟!")
                    wait['pkick'][msg.to] = True
            elif msg.text in ["Pkickoff","pkickoff"]:
                if msg.to in wait['pkick']:
                    del wait['pkick'][msg.to]
                    cl.sendText(msg.to,"禁止踢人保護關閉!")
                else:
                    cl.sendText(msg.to,"已關閉禁止踢人保護!")
			      
            elif msg.text in ["Pnameon","pnameon"]:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"已開啟禁止更改群名保護!")
                else:
                    cl.sendText(msg.to,"禁止更改群名保護開啟!")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif msg.text in ["Pnameoff","pnameoff"]:
                if msg.to in wait['pname']:
                    del wait['pname'][msg.to]
                    cl.sendText(msg.to,"禁止更改群名保護關閉!")
                else:
                    cl.sendText(msg.to,"已關閉禁止更改群名保護!")
					
            elif msg.text in ["Pinviteon","pinviteon"]:
                if msg.to in wait['pinvite']:
                    cl.sendText(msg.to,"已開啟禁止邀人保護!")
                else:
                    cl.sendText(msg.to,"禁止邀人保護開啟!")
                    wait['pinvite'][msg.to] = True
            elif msg.text in ["Pinviteoff","pinviteoff"]:
                if msg.to in wait['pinvite']:
                    del wait['pinvite'][msg.to]
                    cl.sendText(msg.to,"禁止邀人保護關閉!")
                else:
                    cl.sendText(msg.to,"已關閉禁止邀人保護!")       
            elif msg.text in ["Purlon","purlon"]:
                if msg.to in wait['purl']:
                    cl.sendText(msg.to,"已開啟禁止開網址保護!")
                else:
                    cl.sendText(msg.to,"禁止開網址保護開啟!")
                    wait['purl'][msg.to] = True
            elif msg.text in ["Purloff","purloff"]:
                if msg.to in wait['purl']:
                    del wait['purl'][msg.to]
                    cl.sendText(msg.to,"禁止開網址保護關閉!")
                else:
                    cl.sendText(msg.to,"已關閉禁止開網址保護!")  
		
            elif msg.text in ["Pallon","pallon"]:
                try:
			wait['pkick'][msg.to] = True
		except:
			pass
                try:
			wait['pinvite'][msg.to] = True
		except:
			pass
                try:
			wait['purl'][msg.to] = True
		except:
			pass
                try:
			wait['pname'][msg.to] = True
			wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
		except:
			pass
                cl.sendText(msg.to,"已開啟所有保護!")

            elif msg.text in ["Palloff","palloff"]:
                try:
			del wait['pkick'][msg.to]
		except:
			pass
                try:
			del wait['purl'][msg.to]
		except:
			pass
                try:
			del wait['pinvite'][msg.to]
		except:
			pass
                try:
			del wait['pname'][msg.to]
		except:
			pass
                cl.sendText(msg.to,"已關閉所有保護!")

					
            elif msg.text in ["Gset","gset"]:
                md = ""
		if msg.to in wait['pkick']: md+="踢人保護:開啟\n"
                else: md +="踢人保護:關閉\n"
                if msg.to in wait["purl"]: md+="網址保護:開啟\n"
                else: md +="網址保護:關閉\n"
                if msg.to in wait["pname"]: md+="群名保護:開啟\n"
                else: md +="群名保護:關閉\n"
                if msg.to in wait["pinvite"]: md+="禁邀保護:開啟"
                else: md +="禁邀保護:關閉"
                cl.sendText(msg.to,"[戦神群組設定]\n\n" + md)
					
					
            elif msg.text in ["Tagall","tagall"]:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 					
            elif msg.text == "Help":
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
		
		

		
		
		
		
		
		
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    random.choice(KAC).updateGroup(group)
                    cl.sendText(msg.to,"群名: " + group.name)
                else:
                    cl.sendText(msg.to,"><")

            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "BG1invite:" in msg.text:
                midd = msg.text.replace("BG1invite:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
		
            elif "Mc:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                msg.contentType = 13
                msg.contentMetadata = {"mid":key1}
                cl.sendMessage(msg)
		
            elif "Inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.findAndAddContactsByMid(key1)
                cl.inviteIntoGroup(msg.to,[key1])
		
            elif "BG1inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki.findAndAddContactsByMid(key1)
                ki.inviteIntoGroup(msg.to,[key1])
		
            elif "BG2inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki2.findAndAddContactsByMid(key1)
                ki2.inviteIntoGroup(msg.to,[key1])
		
            elif "BG3inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki3.findAndAddContactsByMid(key1)
                ki3.inviteIntoGroup(msg.to,[key1])
		
            elif "BG4inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki4.findAndAddContactsByMid(key1)
                ki4.inviteIntoGroup(msg.to,[key1])
		
            elif "BG5inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki5.findAndAddContactsByMid(key1)
                ki5.inviteIntoGroup(msg.to,[key1])
		
            elif "BG6inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki6.findAndAddContactsByMid(key1)
                ki6.inviteIntoGroup(msg.to,[key1])
		
            elif "BG7inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki7.findAndAddContactsByMid(key1)
                ki7.inviteIntoGroup(msg.to,[key1])
		
            elif "BG8inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                midd = key["MENTIONEES"][0]["M"]
                ki8.findAndAddContactsByMid(midd)
                ki8.inviteIntoGroup(msg.to,[midd])
		
            elif "BG9inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                midd = key["MENTIONEES"][0]["M"]
                ki9.findAndAddContactsByMid(midd)
                ki9.inviteIntoGroup(msg.to,[midd])
		
            elif "BG10inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                midd = key["MENTIONEES"][0]["M"]
                ki10.findAndAddContactsByMid(midd)
                ki10.inviteIntoGroup(msg.to,[midd])
		
            elif "BG11inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                midd = key["MENTIONEES"][0]["M"]
                ki11.findAndAddContactsByMid(midd)
                ki11.inviteIntoGroup(msg.to,[midd])
		
				
		
		
            elif "BG11inv:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                midd = key["MENTIONEES"][0]["M"]
                kicker = random.choice(KAC2)
                kicker.findAndAddContactsByMid(midd)
                kicker.inviteIntoGroup(msg.to,[midd])
		
            elif "BG2invite:" in msg.text:
                midd = msg.text.replace("BG2invite:","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
		
            elif msg.text in ["Time","時刻","time","Now","now"]:
                cl.sendText(msg.to, "" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S'))
		
            elif "BG3invite:" in msg.text:
                midd = msg.text.replace("BG3invite:","")
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
		
            elif "BG4invite:" in msg.text:
                midd = msg.text.replace("BG4invite:","")
                ki4.findAndAddContactsByMid(midd)
                ki4.inviteIntoGroup(msg.to,[midd])
		
            elif "BG5invite:" in msg.text:
                midd = msg.text.replace("BG5invite:","")
                ki5.findAndAddContactsByMid(midd)
                ki5.inviteIntoGroup(msg.to,[midd])
		
		
            elif ("Wl:" in msg.text):
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
                                bgbot.append(target)
                                cl.sendText(msg.to,"加入白單\n" + mi)
                            except:
                                pass
                   print "[Command]bgbot add executed"
	

            elif ("Wld:" in msg.text):
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
                                bgbot.remove(target)
				cl.sendText(msg.to,"刪除白單\n" + mi)
                            except:
                                pass
                   print "[Command]bgbot remove executed"

	
            elif msg.text in ["wl","Wl"]:
                if bgbot == []:
                    cl.sendText(msg.to,"沒有白單")
                else:
                    cl.sendText(msg.to,"白單讀取中...")
                    m1 = ""
		    
                    for mi_d in bgbot:
                        m1 += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"機器名單:\n\n" + m1)

		
		
		
		
		
		
            elif "BG6invite:" in msg.text:
                midd = msg.text.replace("BG6invite:","")
                ki6.findAndAddContactsByMid(midd)
                ki6.inviteIntoGroup(msg.to,[midd])
		
            elif "BG7invite:" in msg.text:
                midd = msg.text.replace("BG7invite:","")
                ki7.findAndAddContactsByMid(midd)
                ki7.inviteIntoGroup(msg.to,[midd])
		
            elif "BG8invite:" in msg.text:
                midd = msg.text.replace("BG8invite:","")
                ki8.findAndAddContactsByMid(midd)
                ki8.inviteIntoGroup(msg.to,[midd])
		
            elif "BG9invite:" in msg.text:
                midd = msg.text.replace("BG9invite:","")
                ki9.findAndAddContactsByMid(midd)
                ki9.inviteIntoGroup(msg.to,[midd])
		
            elif "BG10invite:" in msg.text:
                midd = msg.text.replace("BG10invite:","")
                ki10.findAndAddContactsByMid(midd)
                ki10.inviteIntoGroup(msg.to,[midd])
		
            elif "BG11invite:" in msg.text:
                midd = msg.text.replace("BG11invite:","")
                ki11.findAndAddContactsByMid(midd)
                ki11.inviteIntoGroup(msg.to,[midd])
		

		
            elif "Botcontact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
		msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki11mid}
                cl.sendMessage(msg) 
                
            elif msg.text in ["BG1gift","Bot1gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["BG2gift","Bot2gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki2.sendMessage(msg)



			
            elif msg.text in ["leaveon","Leaveon"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"自動退出副本開啟")
                    else:
                        cl.sendText(msg.to,"自動退出副本開啟")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"自動退出副本開啟")
                    else:
                        cl.sendText(msg.to,"自動退出副本開啟")
            elif msg.text in ["leaveoff","Leaveoff"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"自動退出副本關閉")
                    else:
                        cl.sendText(msg.to,"自動退出副本關閉")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"自動退出副本關閉")
                    else:
                        cl.sendText(msg.to,"自動退出副本關閉")
			
            elif msg.text in ["Joinon","joinon"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"自動入群開啟")
                    else:
                        cl.sendText(msg.to,"自動入群開啟")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"自動入群開啟")
                    else:
                        cl.sendText(msg.to,"自動入群開啟")
			
            elif msg.text in ["Joinoff","joinoff"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"自動入群關閉")
                    else:
                        cl.sendText(msg.to,"自動入群關閉")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"自動入群關閉")
                    else:
                        cl.sendText(msg.to,"自動入群關閉")
			
            elif msg.text in ["Botjoinon","botjoinon"]:
                if wait["urlJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kicker自動入群開啟")
                    else:
                        cl.sendText(msg.to,"kicker自動入群開啟")
                else:
                    wait["urlJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kicker自動入群開啟")
                    else:
                        cl.sendText(msg.to,"kicker自動入群開啟")
			
            elif msg.text in ["Botjoinoff","botjoinoff"]:
                if wait["urlJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kicker自動入群關閉")
                    else:
                        cl.sendText(msg.to,"kicker自動入群關閉")
                else:
                    wait["urlJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kicker自動入群關閉")
                    else:
                        cl.sendText(msg.to,"kicker自動入群關閉")	


            elif msg.text.lower() == 'set':
                md = ""
		if wait["autoJoin"] == True: md+="自動入群:開啟\n"
                else: md +="自動入群:關閉\n"
                if wait["urlJoin"] == True: md+="kicker自動入群:開啟\n"
                else: md+="kicker自動入群:關閉\n"
                if wait["leaveRoom"] == True: md+="自動離開副本:開啟"
                else: md+="自動離開副本:關閉"
                cl.sendText(msg.to,"[戦神SelfBOT]\n\n" + md)
		


            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n取消了 "+ str(len(group.invitee)) + " 個邀請\n(´∀｀)♡")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"邀請中沒人><")
                        else:
                            cl.sendText(msg.to,"邀請中沒人><")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"邀請中沒人><")
                    else:
                        cl.sendText(msg.to,"邀請中沒人><")

            elif msg.text in ["author","Author","作者"]:
			msg.contentType = 13
                        msg.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
			cl.sendText(msg.to,"此機器作者↓")
                        cl.sendMessage(msg)
			
            elif msg.text in ["Groupid","所有群組","Allgid"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
		
            elif msg.text in ["Urlon","urlon"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)

            elif msg.text in ["Boturlon","boturlon"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(group)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
            elif msg.text in ["Urloff","urloff"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉網址")
                    else:
                        cl.sendText(msg.to,"已關閉網址")
            elif msg.text in ["Ginfo","ginfo"]:
                    ginfo = cl.getGroup(msg.to)
                    gurl = cl.reissueGroupTicket(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = ginfo.members[0].displayName
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
		    try:
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl)
                    except:
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nerror" + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl)
                    cl.sendText(msg)



            elif "Mid1" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Mid2" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Mid3" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Botmid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
		ki4.sendText(msg.to,ki4mid)
		ki5.sendText(msg.to,ki5mid)
		ki6.sendText(msg.to,ki6mid)
		ki7.sendText(msg.to,ki7mid)
		ki8.sendText(msg.to,ki8mid)
		ki9.sendText(msg.to,ki9mid)
		ki10.sendText(msg.to,ki10mid)
		ki11.sendText(msg.to,ki11mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"[戦神SelfBOT代行]\nline://home/post?userMid="  +mid + "&postId=" + cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])


#--------------------------------------------------------
            elif "mid:" in msg.text:
                mmid = msg.text.replace("mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)


            elif msg.text.lower() == '封鎖名單':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "讀取中...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="已封鎖用戶:\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\n總共 %i 位被我封鎖" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)


		
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"已黑單此用戶")
            elif "Munban:" in msg.text:
                midd = msg.text.replace("Munban:","")
		del wait["blacklist"][midd]
		cl.sendText(msg.to,"已解除黑單")
		
            elif ("Mid:" in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"" +  key1)
		
            elif msg.text in ["url","Url"]:
                    g = cl.getGroup(msg.to)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)

            elif msg.text in ["Bl","BL","bl"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"沒有黑名單")
                else:
                    cl.sendText(msg.to,"黑名單用戶讀取中...")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"[戦神SelfBOT代行]\n黑名單用戶:\n\n" + mc)

#-----------------------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "BG戦神Bot讀取中...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki6.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki7.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki8.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki9.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki10.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki11.sendText(msg.to, "%sseconds" % (elapsed_time))
		
		

				
            elif ("Mk:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[cl]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M1k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M2k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki2]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M3k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki3]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M4k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki4]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki4.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M5k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki5]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M6k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki6]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki6.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M7k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki7]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki7.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M8k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki8]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki8.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M9k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki9]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki9.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M10k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki10]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki10.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("M11k:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki11]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           ki11.sendText(msg.to,"因規制,無法踢出!")
				
            elif ("Mkk:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
		     if target not in Bots:
                       try:
                           klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
				
            elif ("Bl:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"已黑單此用戶")
                            except:
                                cl.sendText(msg.to,"此用戶已是黑單")
				
            elif ("Ubl:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"已解除黑單")
                            except:
                                cl.sendText(msg.to,"此用戶並不是黑單")
				
            elif "Nk:" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nk:","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"找不到用戶")
                    else:
                        for target in targets:
			  if target not in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"因規制,無法踢出!")
				
				

				
            elif "Nkk:" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nkk:","")
                    gs = cl.getGroup(msg.to)
		    gs = ki.getGroup(msg.to)
		    gs = ki2.getGroup(msg.to)
		    gs = ki3.getGroup(msg.to)
		    gs = ki4.getGroup(msg.to)
		    gs = ki5.getGroup(msg.to)
		    gs = ki6.getGroup(msg.to)
		    gs = ki7.getGroup(msg.to)
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
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
#-----------------------------------------------------------

#-----------------------------------------------------------

				

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"找不到用戶0.0")
                           pass
                       else:
                           for target in targets:
			     if target not in Bots:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"黑單成功")
                                except:
                                    cl.sendText(msg.to,"黑單成功")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"找不到用戶0.0")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"解黑成功")
                                except:
                                    cl.sendText(msg.to,"解黑成功")
#-----------------------------------------------------------
#-----------------------------------------------------------

#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

#-----------------------------------------------------------
            elif "Test" in msg.text:
                profile = ki.getProfile()
                text = profile.displayName + ""
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + ""
                ki2.sendText(msg.to, text)
		profile = ki3.getProfile()
                text = profile.displayName + ""
                ki3.sendText(msg.to, text)
		profile = ki4.getProfile()
                text = profile.displayName + ""
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + ""
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName + ""
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = profile.displayName + ""
                ki7.sendText(msg.to, text)
                profile = ki8.getProfile()
                text = profile.displayName + ""
                ki8.sendText(msg.to, text)
                profile = ki9.getProfile()
                text = profile.displayName + ""
                ki9.sendText(msg.to, text)
                profile = ki10.getProfile()
                text = profile.displayName + ""
                ki10.sendText(msg.to, text)
                profile = ki11.getProfile()
                text = profile.displayName + ""
                ki11.sendText(msg.to, text)

#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"請傳送友資")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"請傳送友資")

            elif "Banlist" in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "->" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "以上為在本群的黑單用戶")
            elif "Blk" in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"群內沒有黑單用戶")
                        return
                    for jj in matched_list:
		      if jj not in Bots:
                        try:
                            klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
                            cl.sendText(msg.to,"因規制,無法踢出!")


#-----------------------------------------------

#-----------------------------------------------
                       
#-----------------------------------------------
            elif msg.text in ["BGbot","Bgbot"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki2.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC3).updateGroup(G)
			except:
				try:
					random.choice(KAC2).updateGroup(G)
				except:
					try:
						random.choice(KAC).updateGroup(G)
					except:
						pass
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["bot2","Bot2"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["bot1","Bot1"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text in ["bot3","Bot3"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
            elif msg.text in ["bot4","Bot4"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki4.updateGroup(G)
            elif msg.text in ["bot5","Bot5"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
            elif msg.text in ["bot6","Bot6"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
            elif msg.text in ["bot7","Bot7"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
            elif msg.text in ["bot8","Bot8"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
            elif msg.text in ["bot9","Bot9"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
            elif msg.text in ["bot10","Bot10"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
            elif msg.text in ["bot11","Bot11"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki11.updateGroup(G)
#-----------------------------------------------
            elif msg.text == "Point":
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.datetime.today().strftime("%H:%M")
                wait2['ROM'][msg.to] = {}
		cl.sendText(msg.to, "[戦神SelfBOT]\n已讀設定OK")

            elif msg.text == "Read":
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to,"[戦神SelfBOT]\n已讀者\n%s"  % (wait2['readMember'][msg.to]))
	          else:
	            cl.sendText(msg.to, "請先設定已讀點")
#-----------------------------------------------

#-----------------------------------------------
            elif msg.text in ["BGbye","Bgbye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
			ki3.leaveGroup(msg.to)
			ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                    except:
                        pass
		

            elif msg.text in ["Bot1bye","bot1bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot2bye","bot2bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot3bye","bot3bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot4bye","bot4bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot5bye","bot5bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot6bye","bot6bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot7bye","bot7bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot8bye","bot8bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot9bye","bot9bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot10bye","bot10bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot11bye","bot11bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki11.leaveGroup(msg.to)
                    except:
                        pass
		
#-----------------------------------------------

#-----------------------------------------------

#-----------------------------------------------
            elif "Say:" in msg.text:
				bctxt = msg.text.replace("Say:","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki11.sendText(msg.to,(bctxt))
				
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
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki10.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki8.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki6.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
														except:
															pass
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki7.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki8.reissueGroupTicket(op.param1)
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
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
			
			
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki7.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
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
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki10.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki4.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki6.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki8.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
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
						ki4.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki6.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki7.updateGroup(G)
										except:
											try:
												ki8.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki2.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki4.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki8.reissueGroupTicket(op.param1)
							except:
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki6.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki7.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
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
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki2.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki10.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki5.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki2.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki8.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki6.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
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
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki7.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki9.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki11.reissueGroupTicket(op.param1)
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
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki8.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki4.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki3.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki7.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
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
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki10.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki3.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki6.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki8.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
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
						ki11.updateGroup(G)
					except:
						try:
							ki5.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki7.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki8.updateGroup(G)
													except:
														try:
															ki3.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki6.reissueGroupTicket(op.param1)
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
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki8.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki3.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki11.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki7.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass

			
                elif op.param3 in ki4mid:
                    if op.param2 in Bots:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki7.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki10.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki10.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki3.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki6.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki8.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
														except:
															pass
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki10.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki7.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki2.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki4.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki8.reissueGroupTicket(op.param1)
							except:
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki4.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki7.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass

			
                elif op.param3 in ki5mid:
                    if op.param2 in Bots:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki8.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki10.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki10.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki11.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki8.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki6.kickoutFromGroup(op.param1,[op.param2])
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
						ki5.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki7.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki8.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki7.reissueGroupTicket(op.param1)
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
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki8.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki6.updateGroup(G)
				except:
					try:
						ki9.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki7.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki8.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass

			
                elif op.param3 in ki6mid:
                    if op.param2 in Bots:
                        wait["blacklist"][op.param2] = True
                        G = ki7.getGroup(op.param1)
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki7.kickoutFromGroup(op.param1,[op.param2])
				except:
					print ("["+op.param1+"]の["+op.param2+"]")
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki8.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki4.getGroup(op.param1)
										except:
											try:
												G = ki10.getGroup(op.param1)
											except:
												try:
													G = ki7.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki10.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki2.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki8.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki11.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki6.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki7.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki9.kickoutFromGroup(op.param1,[op.param2])
														except:
															pass
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki11.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki5.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki7.updateGroup(G)
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
						Ticket = ki4.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki8.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki2.reissueGroupTicket(op.param1)
							except:
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki9.updateGroup(G)
				except:
					try:
						ki10.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki8.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki7.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass

			
                elif op.param3 in ki7mid:
                    if op.param2 in Bots:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki6.getGroup(op.param1)
				except:
					try:
						G = ki.getGroup(op.param1)
					except:
						try:
							G = ki10.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki11.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki2.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki6.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki8.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
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
						ki5.updateGroup(G)
					except:
						try:
							ki6.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki7.updateGroup(G)
									except:
										try:
											ki3.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki8.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki4.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki8.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki2.reissueGroupTicket(op.param1)
							except:
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki11.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki3.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki7.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass

			
                elif op.param3 in ki8mid:
                    if op.param2 in Bots:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki3.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki10.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki11.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki8.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki6.kickoutFromGroup(op.param1,[op.param2])
														except:
															pass
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki9.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki7.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki2.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki4.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki8.reissueGroupTicket(op.param1)
							except:
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki5.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki11.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki3.updateGroup(G)
													except:
														try:
															ki7.updateGroup(G)
														except:
															pass

			
                elif op.param3 in ki9mid:
                    if op.param2 in Bots:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki9.getGroup(op.param1)
				except:
					try:
						G = ki4.getGroup(op.param1)
					except:
						try:
							G = ki3.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki6.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki10.getGroup(op.param1)
													except:
														try:
															ki11.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki11.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki6.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki8.kickoutFromGroup(op.param1,[op.param2])
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
						ki6.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki7.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki8.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki8.reissueGroupTicket(op.param1)
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
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki11.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki10.updateGroup(G)
				except:
					try:
						ki11.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki7.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki8.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass

			
                elif op.param3 in ki10mid:
                    if op.param2 in Bots:
                        G = ki11.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki5.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki4.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki10.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki3.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki11.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki8.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki6.kickoutFromGroup(op.param1,[op.param2])
														except:
															pass
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki9.updateGroup(G)
				except:
					try:
						ki2.updateGroup(G)
					except:
						try:
							ki6.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki3.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki10.updateGroup(G)
										except:
											try:
												ki8.updateGroup(G)
											except:
												try:
													ki7.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki11.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki2.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki4.reissueGroupTicket(op.param1)
							except:
								try:
									Ticket = ki3.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki10.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki8.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki2.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki7.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
														except:
															pass
			
                elif op.param3 in ki11mid:
                    if op.param2 in Bots:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki10.getGroup(op.param1)
				except:
					try:
						G = ki11.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki5.getGroup(op.param1)
								except:
									try:
										G = ki3.getGroup(op.param1)
									except:
										try:
											G = ki7.getGroup(op.param1)
										except:
											try:
												G = ki8.getGroup(op.param1)
											except:
												try:
													G = ki.getGroup(op.param1)
												except:
													try:
														ki9.getGroup(op.param1)
													except:
														try:
															ki4.getGroup(op.param1)
														except:
															pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki8.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki6.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki4.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki10.kickoutFromGroup(op.param1,[op.param2])
													except:
														try:
															ki11.kickoutFromGroup(op.param1,[op.param2])
														except:
															pass
                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki5.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki7.updateGroup(G)
														except:
															pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki10.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki11.reissueGroupTicket(op.param1)
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
										Ticket = ki5.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki6.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki7.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki8.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = ki9.reissueGroupTicket(op.param1)
													except:
														try:
															Ticket = ki4.reissueGroupTicket(op.param1)
														except:
															pass
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki7.updateGroup(G)
				except:
					try:
						ki8.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki10.updateGroup(G)
								except:
									try:
										ki.updateGroup(G)
									except:
										try:
											ki6.updateGroup(G)
										except:
											try:
												ki2.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														ki11.updateGroup(G)
													except:
														try:
															ki5.updateGroup(G)
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
def autolike():
			for zx in range(0,20):
				hasil = cl.activity(limit=20)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki7.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki7.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki8.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki8.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						ki9.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki9.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						
						ki10.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki10.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						
						ki11.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
						ki11.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
						
					except:
							pass
				else:
						pass
			time.sleep(50)
thread3 = threading.Thread(target=autolike)
thread3.daemon = True
thread3.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
