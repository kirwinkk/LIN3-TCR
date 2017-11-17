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



helpMessage2 ="""[戦神SelfBOT]

[#help]→查看指令
[#author]→作者顯示
[#me]→顯示自己友資
[#mid]→顯示自己mid
[#gid]→顯示群組
[#ginfo]→顯示群組詳情
[#url]→取得群組網址
[#cancel]→取消所有邀請
[#mid:]→顯示mid的友資
[#Mid:@]→顯示被標註者的mid
[#mc:@]→顯示被標註者的友資
[#user:@]→查看標註者詳情
[#point]→抓已讀者
[#read]→查看已讀名單
[#tagall]→標註所有人
[#gift]→發送禮物
[#time]→現在時間
[#sp]→反應速度
[#bangset:]→設定內容
[#bang:@]→密標註者
[#say:]→保鏢說話
[#banlist]→查看此群黑單

作者:戦神
http://line.me/ti/p/4-ZKcjagH0"""

helpMessage ="""[戦神SelfBOT]

[help]→指令表
[Author]→作者
[Me]→自己友資
[Mid]→自己的mid
[Gid]→群組gid
[封鎖名單]→確認已封鎖用戶
[Ginfo]→群組詳情
[Cancel]→取消所有邀請
[Mid:@]→被標註者的mid
[mid:]→mid查看友資
[Mc:@]→標註查看友資
[User:@]→查看標註者詳情
[TL:]→Po文
[Gift]→發送禮物
[Time]→現在時間
[Sp]→反應速度
[Point]→設定已讀點
[Read]→查看已讀名單
[Tagall]→標註所有人

[Url]→取得群組網址
[Urlon]→開啟群組網址
[Urloff]→關閉群組網址
[BGbot]→追加kicker
[bot1]→追加kicker1
[BGbye]→kicker退出
[bot1bye]→kicker1退出
[Botcontact]→kicker友資
[Botmid]→kicker的mid
[Kick:]→mid踢人
[Invite:]→mid邀人
[BG1invite:]→mid kicker1邀人
[Inv:@]→標註邀人
[BG1inv:@]→標註kicker1邀人
[Nk:]→名字本帳踢人
[Nkk:]→名字kicker踢人
[Mk:@]→標註本帳踢人
[Mkk:@]→標註kicker踢人
[M1k:@]→標註kicker1踢人

[Bl:@]→標註黑單
[Ubl:@]→標註解除黑單
[Ban:]→名字黑單
[Unban:]→名字解除黑單
[Ban]→友資黑單
[Unban]→友資解除黑單
[Mban:]→mid黑單
[Munban:]→mid解除黑單
[Unbanall]→解除所有黑單
[Bl]→查看黑單用戶名字
[Blmid]→查看黑單用戶mid
[Banlist]→查看此群黑單
[Blk]→踢出黑單
[Wl:@]→標註白單
[Wld:@]→標註解除白單
[Wl]→查看白單
[Lv:@]→標註增加權限名單
[Lvd:@]→標註解除權限名單
[Level]→查看權限名單

[Glist]→所有群組
[Groupid]→所有群組gid
[名字更改:]→更改本帳名字
[名字更改1:]→更改kicker1名字
[個簽更改:]→更改本帳個簽
[個簽更改1:]→更改kicker1個簽
[Joinon/off]→自動入群開關
[Botjoinon/off]→kicker自動入群開關
[Leaveon/off]→自動退副本開關
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

Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid,"u8dc2983d2e3183303bc466f3283d44d8","ubecd98a04cbf74a830b6c95b67bd6b74","ua1d924caa58666ee73d0625ca036a1b1","u8dc2983d2e3183303bc466f3283d44d8"]
admsa = ["uc216d8664c4e1f43772c98b1b0b8956e"]
admin = ["uc216d8664c4e1f43772c98b1b0b8956e","u8dc2983d2e3183303bc466f3283d44d8"]
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
bgbot = ["uc216d8664c4e1f43772c98b1b0b8956e","u8dc2983d2e3183303bc466f3283d44d8","ubecd98a04cbf74a830b6c95b67bd6b74","u9378246da17ae7914b0a9a27da4802a0","ufdd4dbee33a2af45c13a72444277298d","ub5497e219585e4dad3373f25696c85fc","u58623d8e816b2dbf9cc8dc15b243e313","u6c81c99cb7ae718754ceb7db1718e7dd","u32f0dc24e048a1e357f655aff0a5fa33","u444a6355bfdc40238d3509e161458916","ud4b30af2044227c281d5d3ec69a584be","ufd9bec46aabcba3cdd9271f0db4b4ac8","u0bd59b43cef104e8e8f0c771d46689f4"]
staff = []

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
    'bang':{},
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
	             if wait["urlJoin"] == True:
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
                     else:
			pass
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
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
			if msg.contentMetadata["mid"] in wait["blacklist"]:
                             cl.sendText(msg.to,msg.contentMetadata["mid"])
                        else:
			     cl.sendText(msg.to,msg.contentMetadata["mid"])
			
            if msg.text == "#help":
                if msg.from_ in admin + staff:
                    ki.sendText(msg.to,helpMessage2)

		
            if msg.text == "#Help":
                if msg.from_ in admin + staff:
                    ki.sendText(msg.to,helpMessage2)

			
            elif msg.text in ["#me","#Me"]:
              if msg.from_ in admin + staff:
		msg.contentType = 13
		X = msg.from_
                msg.contentMetadata = {"mid": X }
		ki.sendMessage(msg)
                ki.sendText(msg.to,msg.from_)

		
            elif msg.text in ["#author","#Author","#作者"]:
              if msg.from_ in admin + staff:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
		ki.sendMessage(msg)
		ki.sendText(msg.to,"防翻作者:戦神\nMade In Taiwan")
		
            elif msg.text in ["#mid","#Mid"]:
              if msg.from_ in admin + staff:
                ki.sendText(msg.to,msg.from_)
		
            elif msg.text in ["#Gid","#gid"]:
              if msg.from_ in admin + staff:
                ki.sendText(msg.to, msg.to)
		
            elif msg.text in ["#Ginfo","#ginfo"]:
              if msg.from_ in admin + staff:
                    ginfo = ki.getGroup(msg.to)
                    gurl = ki.reissueGroupTicket(msg.to)
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
                            u = "關閉"
                        else:
                            u = "開啟"
		    try:
                        ki.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl)
                    except:
                        ki.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nerror" + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl)
                    ki.sendText(msg)

		
            elif msg.text in ["#Point","#point"]:
              if msg.from_ in admin + staff:
		cl.sendText(msg.to, "[戦神SelfBOT]\n已讀設定OK")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['ROM'][msg.to] = {}
		

            elif msg.text in ["#read","#Read"]:
              if msg.from_ in admin + staff:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                chiya += rom[1] + "\n"

	            ki.sendText(msg.to,"[戦神SelfBOT]\n已讀者\n%s"  % (wait2['readMember'][msg.to]))
	          else:
	            ki.sendText(msg.to, "請先設定已讀點")
		
            elif "#mid:" in msg.text:
              if msg.from_ in admin + staff:
                mmid = msg.text.replace("#mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                ki.sendMessage(msg)
		
            elif ("#Mid:" in msg.text):
              if msg.from_ in admin + staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = ki.getContact(key1)
                   ki.sendText(msg.to,"" +  key1)
		
            elif "#Mc:" in msg.text:
              if msg.from_ in admin + staff:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                msg.contentType = 13
                msg.contentMetadata = {"mid":key1}
                ki.sendMessage(msg)
            elif "#mc:" in msg.text:
              if msg.from_ in admin + staff:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                msg.contentType = 13
                msg.contentMetadata = {"mid":key1}
                ki.sendMessage(msg)
		

            elif "#User:" in msg.text:
              if msg.from_ in admin + staff:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    ki.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[頭貼網址]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]\n" + str(cu))
                except:
                    ki.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[封面網址]\n" + str(cu))
		
            elif "#user:" in msg.text:
              if msg.from_ in admin + staff:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    ki.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[頭貼網址]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]\n" + str(cu))
                except:
                    ki.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[封面網址]\n" + str(cu))
		
		
		
            elif msg.text in ["#gift","#Gift"]:
              if msg.from_ in admin + staff:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki.sendMessage(msg)
		
            elif "#gift:" in msg.text:
              if msg.from_ in admin + staff:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
		msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
		msg.text = None
		msg = Message(to=key1)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki.sendText(msg.to, "成功")
			
            elif "#Gift:" in msg.text:
              if msg.from_ in admin + staff:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
		msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
		msg.text = None
		msg = Message(to=key1)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki.sendText(msg.to, "成功")
		
            elif msg.text in ["#Time","#時刻","#time","#Now","#now"]:
              if msg.from_ in admin + staff:
                ki.sendText(msg.to, "" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f'))


            elif msg.text in ["#Tagall","#tagall"]:
              if msg.from_ in admin + staff:
                group = ki.getGroup(msg.to)
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
                    ki.sendMessage(msg) 
		
		

            elif msg.text in ["#Sp","#Speed","#speed","#sp"]:
              if msg.from_ in admin + staff:
                start = time.time()
                ki.sendText(msg.to, "BG戦神Bot讀取中...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
		
            elif msg.text in ["#Cancel","#cancel"]:
              if msg.from_ in admin + staff:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                        ki.sendText(msg.to,"[戦神SelfBOT代行]\n取消了 "+ str(len(group.invitee)) + " 個邀請\n(´∀｀)♡")
                    else:
                            ki.sendText(msg.to,"邀請中沒人><")
				
				
            elif "#Bangset:" in msg.text:
              if msg.from_ in admin + staff:
                c = msg.text.replace("#Bangset:","")
		del wait["bang"]
                wait["bang"] = c
                ki.sendText(msg.to,"更改內容:\n" + c)
		
            elif "#bangset:" in msg.text:
              if msg.from_ in admin + staff:
                c = msg.text.replace("#bangset:","")
		del wait["bang"]
                wait["bang"] = c
                ki.sendText(msg.to,"更改內容:\n" + c)
		
            elif "#Bang:" in msg.text:
              if msg.from_ in admin + staff:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki.sendText(key1,wait["bang"])
                ki2.sendText(key1,wait["bang"])
                ki3.sendText(key1,wait["bang"])
                ki4.sendText(key1,wait["bang"])
                ki5.sendText(key1,wait["bang"])
                ki6.sendText(key1,wait["bang"])
                ki7.sendText(key1,wait["bang"])
                ki8.sendText(key1,wait["bang"])
                ki9.sendText(key1,wait["bang"])
                ki10.sendText(key1,wait["bang"])
                ki11.sendText(key1,wait["bang"])
                ki.sendText(msg.to, "成功")
		
            elif "#bang:" in msg.text:
              if msg.from_ in admin + staff:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                ki.sendText(key1,wait["bang"])
                ki2.sendText(key1,wait["bang"])
                ki3.sendText(key1,wait["bang"])
                ki4.sendText(key1,wait["bang"])
                ki5.sendText(key1,wait["bang"])
                ki6.sendText(key1,wait["bang"])
                ki7.sendText(key1,wait["bang"])
                ki8.sendText(key1,wait["bang"])
                ki9.sendText(key1,wait["bang"])
                ki10.sendText(key1,wait["bang"])
                ki11.sendText(key1,wait["bang"])
                ki.sendText(msg.to, "成功")
		
            elif "#Say:" in msg.text:
              if msg.from_ in admin + staff:
				bctxt = msg.text.replace("#Say:","")
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
		
            elif "#say:" in msg.text:
              if msg.from_ in admin + staff:
				bctxt = msg.text.replace("#say:","")
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
				

		
		
            elif msg.text in ["#Banlist","#banlist"]:
              if msg.from_ in admin + staff:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "->" +ki.getContact(mm).displayName + "\n"
                    ki.sendText(msg.to,cocoa + "以上為在本群的黑單用戶")
		
		
            elif msg.text in ["#url","#Url"]:
              if msg.from_ in admin + staff:
                    g = ki.getGroup(msg.to)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
			
			



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
                cl.sendText(msg.to, "" + datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S.%f'))
		
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
		    num=1
                    for mi_d in bgbot:
                        m1 += "[%i] %s\n" % (num,cl.getContact(mi_d).displayName)
			num=(num+1)
                    cl.sendText(msg.to,"戦神SelfBOT白單用戶:\n\n" + m1 + "\n總共: " + str(len(bgbot)) +"人")
		


		
		
		
		
		
		
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
		
            elif "名字更改:" in msg.text:
                string = msg.text.replace("名字更改:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改1:" in msg.text:
                string = msg.text.replace("名字更改1:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"[1]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改2:" in msg.text:
                string = msg.text.replace("名字更改2:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"[2]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改3:" in msg.text:
                string = msg.text.replace("名字更改3:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"[3]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改4:" in msg.text:
                string = msg.text.replace("名字更改4:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"[4]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改5:" in msg.text:
                string = msg.text.replace("名字更改5:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"[5]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改6:" in msg.text:
                string = msg.text.replace("名字更改6:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"[6]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改7:" in msg.text:
                string = msg.text.replace("名字更改7:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"[7]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改8:" in msg.text:
                string = msg.text.replace("名字更改8:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"[8]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改9:" in msg.text:
                string = msg.text.replace("名字更改9:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"[9]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改10:" in msg.text:
                string = msg.text.replace("名字更改10:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"[10]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "名字更改11:" in msg.text:
                string = msg.text.replace("名字更改11:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki11.getProfile()
                    profile.displayName = string
                    ki11.updateProfile(profile)
                    ki11.sendText(msg.to,"[11]名字更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改:" in msg.text:
                string = msg.text.replace("個簽更改:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改1:" in msg.text:
                string = msg.text.replace("個簽更改1:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"[1]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改2:" in msg.text:
                string = msg.text.replace("個簽更改2:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"[2]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改3:" in msg.text:
                string = msg.text.replace("個簽更改3:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"[3]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改4:" in msg.text:
                string = msg.text.replace("個簽更改4:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"[4]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改5:" in msg.text:
                string = msg.text.replace("個簽更改5:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"[5]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改6:" in msg.text:
                string = msg.text.replace("個簽更改6:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"[6]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改7:" in msg.text:
                string = msg.text.replace("個簽更改7:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"[7]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改8:" in msg.text:
                string = msg.text.replace("個簽更改8:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"[8]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改9:" in msg.text:
                string = msg.text.replace("個簽更改9:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"[9]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改10:" in msg.text:
                string = msg.text.replace("個簽更改10:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"[10]個簽更改成功:\n" + string + "")
		else:
			pass
		
            elif "個簽更改11:" in msg.text:
                string = msg.text.replace("個簽更改11:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki11.getProfile()
                    profile.statusMessage = string
                    ki11.updateProfile(profile)
                    ki11.sendText(msg.to,"[11]個簽更改成功:\n" + string + "")
		else:
			pass
		

		
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
		

            elif "User:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[頭貼網址]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[封面網址]\n" + str(cu))
		
		
            elif "user:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[頭貼網址]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[封面網址]\n" + str(cu))
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
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
                    pass

            elif msg.text in ["author","Author","作者"]:
			msg.contentType = 13
                        msg.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
			cl.sendText(msg.to,"此機器作者↓")
                        cl.sendMessage(msg)
			
            elif msg.text in ["mid","Mid"]:
                cl.sendText(msg.to,msg.from_)
		
            elif msg.text in ["Gid","gid"]:
                cl.sendText(msg.to, msg.to)
		

		
            elif msg.text in ["Glist","glist"]:
                gs = cl.getGroupIdsJoined()
                L = "[戦神SelfBOT全部群組]\n"
		num=1
                for i in gs:
                    L += "[%i]  %s\n" % (num,"" + str(len (cl.getGroup(i).members)) + "人\n " + cl.getGroup(i).name + "")
                    num=(num+1)
                cl.sendText(msg.to, L + "\n總共:" + str(len(gs)) +"群")
			
            elif msg.text in ["Groupid","Allgid"]:
                gid = cl.getGroupIdsJoined()
		k = len(gid)//50
                h = ""
		for j in xrange(k+1):
		    msg = Message(to=msg.to)
                    for i in gid[j*50 : (j+1)*50]:
                        h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
			msg.text = h
                cl.sendMessage(msg) 
		


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
                    gurl = random.choice(KAC).reissueGroupTicket(msg.to)
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
                            u = "關閉"
                        else:
                            u = "開啟"
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
                    num=1
                    for mi_d in wait["blacklist"]:
                        mc += "[%i] %s\n" % (num,cl.getContact(mi_d).displayName)
			num=(num+1)
                    cl.sendText(msg.to,"戦神SelfBOT黑單用戶\n\n" + mc + "\n總共: " + str(len(wait["blacklist"])) +"人")
		
            elif msg.text in ["Blmid","blmid"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"沒有黑名單")
                else:
                    cl.sendText(msg.to,"黑名單用戶讀取中...")
                    mc = ""
                    num=1
                    for mi_d in wait["blacklist"]:
                        mc += "[%i] %s\n" % (num,mi_d)
			num=(num+1)
                    cl.sendText(msg.to,"戦神SelfBOT黑單MID\n\n" + mc + "\n總共: " + str(len(wait["blacklist"])) +"人")
		
            elif msg.text in ["Unbanall","unbanall"]:
             try:
	      for target in wait["blacklist"]:
		try:
			wait["blacklist"] = {}
		except:
			cl.sendText(msg.to,"失敗")
	      cl.sendText(msg.to,"已解除所有黑單")
             except:
			cl.sendText(msg.to,"沒有黑單用戶")
			
		

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
				
				
            elif "Bangset:" in msg.text:
                c = msg.text.replace("Bangset:","")
		del wait["bang"]
                wait["bang"] = c
                cl.sendText(msg.to,"更改內容:\n" + c)
		
		
		
		
            elif "Bang:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(key1,wait["bang"])
                ki.sendText(key1,wait["bang"])
                ki2.sendText(key1,wait["bang"])
                ki3.sendText(key1,wait["bang"])
                ki4.sendText(key1,wait["bang"])
                cl.sendText(key1,wait["bang"])
                cl.sendText(msg.to, "成功")
		
            elif ("Lvd:" in msg.text):
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
                                staff.remove(target)
				cl.sendText(msg.to,"解除權限\n" + mi)
                            except:
                                pass



            elif ("Lv:" in msg.text):
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
                                staff.append(target)
                                cl.sendText(msg.to,"提升權限\n" + mi)
                            except:
                                pass

	
            elif msg.text in ["Level","level"]:
                if staff == []:
                    cl.sendText(msg.to,"沒有權限用戶")
                else:
                    cl.sendText(msg.to,"權限名單讀取中...")
                    mc = ""
		    num=1
                    for mi_d in staff:
                        mc += "[%i] %s\n" % (num,cl.getContact(mi_d).displayName)
			num=(num+1)
                    cl.sendText(msg.to,"戦神SelfBOT權限用戶\n\n" + mc + "\n總共: " + str(len(staff)) +"人")
				

				
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
            elif msg.text in ["Test","test"]:
		try:
                 profile = cl.getProfile()
                 text = "[正常] " + profile.displayName
                 cl.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki.getProfile()
                 text = "[正常1] " + profile.displayName
                 ki.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki2.getProfile()
                 text = "[正常2] " + profile.displayName
                 ki2.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki3.getProfile()
                 text = "[正常3] " + profile.displayName
                 ki3.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki4.getProfile()
                 text = "[正常4] " + profile.displayName
                 ki4.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki5.getProfile()
                 text = "[正常5] " + profile.displayName
                 ki5.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki6.getProfile()
                 text = "[正常6] " + profile.displayName
                 ki6.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki7.getProfile()
                 text = "[正常7] " + profile.displayName
                 ki7.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki8.getProfile()
                 text = "[正常8] " + profile.displayName
                 ki8.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki9.getProfile()
                 text = "[正常9] " + profile.displayName
                 ki9.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki10.getProfile()
                 text = "[正常10] " + profile.displayName
                 ki10.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki11.getProfile()
                 text = "[正常11] " + profile.displayName
                 ki11.sendText(msg.to, text)
		except:
			pass



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


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
