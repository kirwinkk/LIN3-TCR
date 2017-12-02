# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob


cl = LINETCR.LINE()
cl.login(token="EmkPXa3rElh9xxo27Hl0.K3GKBAf655flcPON2KGcOa.+wxllliT31HTi7sF8nXHMIuuJyckj+fW5LOZOcIGXzY=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmbVHOm5cWoAo9celPed.+DtB7JoIR0xboNjeqNCPJq.d+ZVtHTXcFaoz3wThyhbJj6zx1VIXCCP1owqKCu6dOQ=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EmCwlDXpqEXBK8UqVe8c.TuL/izwf5nRtnZ8LAwYf+a.FAC91hn3KH9vnBPtFvXbt/xrOaLU2FBkDksAzS4TTaY=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EmcJTeQiWdPEiWOjpp93.wgi9JOfRlB/CYnWvSKpJeW.It0hgnBvZqbDJHurVaRbdd3EL9TRfAamiLe7F+VMILA=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EmarjXV7m5cQwWyo8Pod.BihjNlEUCyDuZRFBfXJN3q.IN+siEaP3/d3U+l1mYxSbBgNtD1v/T0MqzwhosV6NFE=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EmBgCAx9w1tag2K1SBJ3.mVdCjobiOEnx9LwV8kx6mW.27lhbyuPUmQte4k0Ebe4U/38zia8coLpogDzuBh9X4U=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EmrcHGFUD7gVrnh0RAZ6.rePJvB+CqconnqNHyuwjfG.iVeTQp92Hsm34VmShKvDjV6slczDD9XlRfol7DdU72I=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="Emzl6IsoC0bTUEGNYOPe.1lmk8Grcj8kb1DpSAAweVG.+ddNsTzf2VSDcLWZbJmv4jlIrpOILpm867zYMRu+eQQ=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EmyShHpdt7Y8JQOR0k48.+zVSrQQ8UJZDKNhW20TkYa.mFr+Cw3nHEP6cus++BN9wTxPsgPxAGTNKKqFCSN0YW4=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EmjgiqlHAbwJP33huQL4.c9wBq87XboJO8mDX1gAj9a.jmVKytUynnsLLgcz7hPI+m2s2e9zZLPXYATVWe/CsF8=")
ki9.loginResult() 

ki15 = LINETCR.LINE()
ki15.login(token="EmrSf4cWnlnWUJih5VSe.WHByzKXoh0n3ljIXSlIvBG.fqYI2YP2szowpHgytc/MCE7biiONwj+73PPSTeKRX8Y=")
ki15.loginResult()


reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""※指令Lv.1以上使用
[/help]...查看指令
[/Author]...作者顯示
[/me]...顯示友資,mid,權限狀況
[/mid]...顯示自己mid
[/gid]...顯示群組gid
[/Ginfo]...顯示群組詳情
[/cancel]...取消所有邀請
[/Url]...取得群組網址
[/Mid:@]...顯示被標註者的mid
[/mid:]...顯示mid的友資
[/Time]...現在時間
[/Gc]...查看群長
[/blhelp]...查看黑單說明
[/wlhelp]...查看白單說明

※指令Lv.2以上使用
[/Urlon]...開啟群組網址
[/Urloff]...關閉群組網址
[Gn:]...更改群組群名
☆Lv.2以上才有被機器白單

※指令Lv.3以上使用
[/bg9bot]...防翻回群
☆Lv.3以上才可邀請機器入群

※指令Lv.4以上使用
[/bg9bye]...防翻退出
[Banlist]...查看本群黑單

※指令Lv.5以上使用
[Bl:]...查看黑單用戶
[Banlist]...查看此群黑單用戶
[Ubl:@]...標註解除黑單
[Unban]...友資解除黑單
[Unban:]...名字解除黑單
[/Munban:]...mid解除黑單
[/Pnameon/off]→群名保護開關

作者:戦神[Made In Taiwan]
https://line.me/R/ti/p/%40cld3625n
"""

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9]
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
ki15mid = ki15.getProfile().mid

Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki15mid]
admin = [mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki15mid,"uddf9714006a1010bb6551fc107f52390","ua1d924caa58666ee73d0625ca036a1b1","u8dc2983d2e3183303bc466f3283d44d8","uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","u40c17f320e101b9f1abc9edaace6ed51","uef3dc2c514c550e1935b5b679dac38f6","u7a1c4338e6342bbbc33d9fa3c295b7d4","uad3b11a07372a5955ba75dc1caadeed8","u4ab4047d824385456811a2fe93c95382","u40c17f320e101b9f1abc9edaace6ed51","u8a627a2ff2ed54bcdd6c3b52f2b9691b","u96fd5925ecab120ea325511f4b53db11","ua0c6c9175efd94a9551338c72d6a7d17","u3d860a1bb50f8a536653b4940aa41bbf","u8be7a9504b9185ba75234f2f8110697b"]
staff = []
staff2 = []
staff3 = []
staff4 = []
staff5 = ["ufa38cdb1f6c60532d332cd1feb2811de","u8b07f7b099be4007077725f2159aa3ed","u34f1c3444e6a70f00fa1aa5502917800","ufa6c8088780a26834e335ae948ae1b42","u67f77712583c341c2624a1b3aa38e4a0"]
staff6 = ["uc216d8664c4e1f43772c98b1b0b8956e","uddf9714006a1010bb6551fc107f52390","ubecd98a04cbf74a830b6c95b67bd6b74","u8dc2983d2e3183303bc466f3283d44d8","ua1d924caa58666ee73d0625ca036a1b1"]
bgbot = ["u27a2e1c6d2067d3c644c3a04efc00b80","ua3f3e627b3f06be52532e5b6f6d328cf","uddf9714006a1010bb6551fc107f52390"]
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin2 = "ubecd98a04cbf74a830b6c95b67bd6b74"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"[權限取得方式]:\nLv3. NT300/月\nLv4. NT400/月\nLv5. NT500/月\n\nBot作者:戦神 Made In Taiwan\nhttps://line.me/R/ti/p/%40cld3625n",
    'message1':"戦神Bot作者:戦神 Made In Taiwan\nhttps://line.me/R/ti/p/%40cld3625n",
    'lang':"JP",
    'pname':{},
    'pro_name':{},  
    'linkprotect':True,
    'blacklist':{},
    'wblacklist':False,
    'dblacklist':False,
}


def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)

        if op.type == 13:
           if mid in op.param3:
		if op.param2 in admin + staff3 + staff4 + staff5 + staff6 + bgbot:
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
			ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
			G.preventJoinByTicket = True
                        cl.updateGroup(G)
		        try:
                            cl.sendText(op.param1,"戦神權限保護V.9\n\n[權限取得方式]:\nLv3. NT300/月\nLv4. NT400/月\nLv5. NT500/月\n\nBot作者:戦神 Made In Taiwan\nhttps://line.me/R/ti/p/%40cld3625n")
		        except:
			    pass
		else:
		  cl.acceptGroupInvitation(op.param1)
                  cl.leaveGroup(op.param1)
           else:
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
			try:
					random.choice(KAC).cancelGroupInvitation(op.param1, matched_list)
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
			try:
				try:
					random.choice(KAC).kickoutFromGroup(op.param1, matched_list)
				except:
					try:
						random.choice(KAC).kickoutFromGroup(op.param1, matched_list)
					except:
						try:
							ki4.kickoutFromGroup(op.param1, matched_list)
						except:
							try:
								ki9.kickoutFromGroup(op.param1, matched_list)
							except:
								try:
									ki5.kickoutFromGroup(op.param1, matched_list)
								except:
									try:
										ki6.kickoutFromGroup(op.param1, matched_list)
									except:
										try:
											ki.kickoutFromGroup(op.param1, matched_list)
										except:
											try:
												ki3.kickoutFromGroup(op.param1, matched_list)
											except:
												try:
													ki2.kickoutFromGroup(op.param1, matched_list)
												except:
													try:
														ki7.kickoutFromGroup(op.param1, matched_list)
													except:
														ki8.sendText(op.param1,"注意!!\n偵測到黑單用戶加入!\n\n由於機器遭到鎖踢,因此無法踢出!")
			except:
				pass
		


        if op.type == 13:
            if op.param2 not in admin + staff2 + staff3 + staff4 + staff5 + staff6 + bgbot:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
		        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			


     
			

		

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ki.sendText(msg.to,msg.contentMetadata["displayName"] + " 已加入黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ki.sendText(msg.to,msg.contentMetadata["displayName"] + " 已加入黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ki.sendText(msg.to,msg.contentMetadata["displayName"] + " 已解除黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        ki.sendText(msg.to,msg.contentMetadata["displayName"] + " 已解除黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
			
            else:
		pass
	

	



	
				    
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
			if msg.contentMetadata["mid"] in wait["blacklist"]:
			   try:
                             ki2.sendText(msg.to,"[mid]:\n" + msg.contentMetadata["mid"] + "\n[黑單狀況]:\n此用戶為黑名單用戶><,不可邀請" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                           except:
			     ki2.sendText(msg.to,"[mid]:\n" + msg.contentMetadata["mid"] + "\n[黑單狀況]:\n此用戶為黑名單用戶><,不可邀請" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
			else:
			   try:
			     ki2.sendText(msg.to,"[mid]:\n" + msg.contentMetadata["mid"] + "\n[黑單狀況]:\n並不是黑名單用戶,可以邀請" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		           except:
			     ki2.sendText(msg.to,"[mid]:\n" + msg.contentMetadata["mid"] + "\n[黑單狀況]:\n並不是黑名單用戶,可以邀請" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
            elif msg.contentType == 16:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = msg.contentMetadata["postEndUrl"] + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]"
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"] + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]"
                    ki2.sendText(msg.to,msg.text)
		

            elif msg.text is None:
                return
		
            if msg.text == "/Help":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                    ki.sendText(msg.to,helpMessage + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")

		
            if msg.text == "/help":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                ki.sendText(msg.to,helpMessage + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")

            if msg.text == "/gid":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                ki2.sendText(msg.to, msg.to + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
            if msg.text == "/Gid":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                ki2.sendText(msg.to, msg.to + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["Glist","glist"]:
              if msg.from_ in admin + staff6:
                gs = cl.getGroupIdsJoined()
                L = "[戦神SelfBOT全部群組]\n"
		num=1
                for i in gs:
                    L += "[%i]  %s\n" % (num,"" + str(len (cl.getGroup(i).members)) + "人\n " + cl.getGroup(i).name + "")
                    num=(num+1)
                cl.sendText(msg.to, L + "\n總共:" + str(len(gs)) +"群" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
			
            elif msg.text in ["Groupid","Allgid"]:
              if msg.from_ in admin + staff6:
                gid = cl.getGroupIdsJoined()
		k = len(gid)//50
                h = ""
		for j in xrange(k+1):
		    msg = Message(to=msg.to)
                    for i in gid[j*50 : (j+1)*50]:
                        h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
			msg.text = h
                cl.sendMessage(msg)
		
            elif ("Gn:" in msg.text):
              if msg.from_ in admin + staff2 + staff3 + staff4 + staff5 + staff6:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    random.choice(KAC).updateGroup(group)
                    ki.sendText(msg.to,"群名: " + group.name + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
                    pass
              else:
		pass

	
            elif "BGbyeall" in msg.text:
              if msg.from_ in admin + staff6:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
		gid = ki7.getGroupIdsJoined()
		gid = ki8.getGroupIdsJoined()
		gid = ki9.getGroupIdsJoined()
                for i in gid:
		    cl.sendText(msg.to,"作者:戦神 Made In Taiwan\nhttps://line.me/R/ti/p/%40cld3625n")
                    cl.leaveGroup(i)
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)
                    ki9.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"已退出所有群組" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
                    cl.sendText(msg.to,"已退出所有群組" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/sp","/Speed","/speed","/Sp"]:
               if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "BG戦神Bot讀取中..." + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s秒" % (elapsed_time) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
            elif msg.text in ["/mid","/Mid"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                ki2.sendText(msg.to,msg.from_ + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif "個簽:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("個簽:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"完成" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/me","/Me"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		msg.contentType = 13
		X = msg.from_
                msg.contentMetadata = {"mid": X }
		ki2.sendMessage(msg)
		if msg.from_ in staff:
			ki2.sendText(msg.to,"[權限狀況]:Lv.1" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                if msg.from_ in staff2:
			ki2.sendText(msg.to,"[權限狀況]:Lv.2" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		if msg.from_ in staff3:
			ki2.sendText(msg.to,"[權限狀況]:Lv.3" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                if msg.from_ in staff4:
			ki2.sendText(msg.to,"[權限狀況]:Lv.4" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                if msg.from_ in staff5:
			ki2.sendText(msg.to,"[權限狀況]:Lv.5" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		if msg.from_ in staff6:
			ki2.sendText(msg.to,"[權限狀況]:Lv.6(最高)" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
		
		
            elif msg.text in ["/tagall","/Tagall"]:
                if msg.from_ in admin + staff6:
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
                else:
		   pass

		

            elif msg.text in ["/test"]:
	       if msg.from_ in admin + staff6:
		try:
                 profile = cl.getProfile()
                 text = "[正常] " + profile.displayName 
                 cl.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki.getProfile()
                 text = "[正常] " + profile.displayName
                 ki.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki2.getProfile()
                 text = "[正常] " + profile.displayName
                 ki2.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki3.getProfile()
                 text = "[正常] " + profile.displayName
                 ki3.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki4.getProfile()
                 text = "[正常] " + profile.displayName
                 ki4.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki5.getProfile()
                 text = "[正常] " + profile.displayName
                 ki5.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki6.getProfile()
                 text = "[正常] " + profile.displayName
                 ki6.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki7.getProfile()
                 text = "[正常] " + profile.displayName
                 ki7.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki8.getProfile()
                 text = "[正常] " + profile.displayName
                 ki8.sendText(msg.to, text)
		except:
			pass
		try:
                 profile = ki9.getProfile()
                 text = "[正常] " + profile.displayName
                 ki9.sendText(msg.to, text)
		except:
			pass
	       else:
			pass
		

		


            elif msg.text in ["/Cancel","/cancel"]:
	       if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                        ki.sendText(msg.to,"取消了 "+ str(len(group.invitee)) + " 個邀請" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"找不到能取消的邀請\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                        else:
                            ki.sendText(msg.to,"找不到能取消的邀請\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
                        pass
			


            elif msg.text in ["/author","/Author","/作者"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"u85a9b62af4ce6248cfe05324e474e226"}
		cl.sendMessage(msg)
		cl.sendText(msg.to,"防翻作者:戦神\nMade In Taiwan\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
			

            elif msg.text in ["/Urloff","/urloff"]:
              if msg.from_ in admin + staff2 + staff3 + staff4 + staff5 + staff6:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"關閉網址\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    else:
                        ki.sendText(msg.to,"關閉網址\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
		
            elif msg.text in ["/Urlon","/urlon"]:
                if msg.from_ in admin + staff2 + staff3 + staff4 + staff5 + staff6:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"開啟網址" + "\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    else:
                        ki.sendText(msg.to,"開啟網址" + "\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		else:
		   pass
            elif msg.text in ["/Time","/時刻","/time","/Now","/now"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                ki.sendText(msg.to, "" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
		
		
            elif msg.text in ["/Url","/url"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                gurl = random.choice(KAC).reissueGroupTicket(msg.to)
		ginfo = ki.getGroup(msg.to)
                ki.sendText(msg.to,"[群組名稱]" + str(ginfo.name) + "[群組網址]\nline://ti/g/" + gurl + "\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
		
            elif msg.text in ["/Groupcreator","/群長","/Gc","/gc","/groupcreator","群長"]:
             if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 try:
                        gCreator = ginfo.creator.displayName
                 except:
                        gCreator = ginfo.members[0].displayName
		 
		 msg.contentType = 13
		 try:
                        gCreator1 = ginfo.creator.mid
                 except:
                        gCreator1 = ginfo.members[0].mid
		 msg.contentMetadata={'mid':gCreator1}
		 ki.sendMessage(msg)
		 ki.sendText(msg.to,"[群長]\n->" + gCreator + "\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
              else:
		pass
	
	
	
            elif msg.text in ["/Pnameon","/pnameon"]:
              if msg.from_ in admin + staff4 + staff5 + staff6:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"已開啟禁止更改群名保護!" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
                    cl.sendText(msg.to,"禁止更改群名保護開啟!" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
		
		
		
            elif msg.text in ["/Pnameoff","/pnameoff"]:
              if msg.from_ in admin + staff4 + staff5 + staff6:
                if msg.to in wait['pname']:
                    del wait['pname'][msg.to]
                    cl.sendText(msg.to,"禁止更改群名保護關閉!" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
                    cl.sendText(msg.to,"已關閉禁止更改群名保護!" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")


            elif msg.text in ["/ginfo","/Ginfo"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                    ginfo = cl.getGroup(msg.to)
                    gurl = random.choice(KAC).reissueGroupTicket(msg.to)
                    print "SUKSES -- SEND GINFO"
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
                        ki.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中" + "\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    except:
                        ki.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nerror" + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中" + "\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    ki.sendText(msg)
		

		
            elif msg.text in ["/bg9bye","/BG9bye"]:
	       if msg.from_ in admin + staff4 + staff5 + staff6:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
			cl.sendText(msg.to,"作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0")
			cl.leaveGroup(msg.to)
			ki.leaveGroup(msg.to)
			ki2.leaveGroup(msg.to)
			ki3.leaveGroup(msg.to)
			ki4.leaveGroup(msg.to)
			ki5.leaveGroup(msg.to)
			ki6.leaveGroup(msg.to)
			ki7.leaveGroup(msg.to)
			ki8.leaveGroup(msg.to)
			ki9.leaveGroup(msg.to)
                    except:
                        pass
	       else:
                    pass
		

		
		
		

            elif ("Lv1:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff.append(target)
                                ki.sendText(msg.to,"提升權限至Lv.1" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                else:
                    pass
	
            elif "Add:" in msg.text:
              if msg.from_ in admin + staff6:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.findAndAddContactsByMid(key1)
		cl.sendText(msg.to,"追加好友成功")
		ki.findAndAddContactsByMid(key1)
		ki.sendText(msg.to,"追加好友成功")
		ki2.findAndAddContactsByMid(key1)
		ki2.sendText(msg.to,"追加好友成功")
		ki3.findAndAddContactsByMid(key1)
		ki3.sendText(msg.to,"追加好友成功")
		ki4.findAndAddContactsByMid(key1)
		ki4.sendText(msg.to,"追加好友成功")
		ki5.findAndAddContactsByMid(key1)
		ki5.sendText(msg.to,"追加好友成功")
		ki6.findAndAddContactsByMid(key1)
		ki6.sendText(msg.to,"追加好友成功")
		ki7.findAndAddContactsByMid(key1)
		ki7.sendText(msg.to,"追加好友成功")
		ki8.findAndAddContactsByMid(key1)
		ki8.sendText(msg.to,"追加好友成功")
		ki9.findAndAddContactsByMid(key1)
		ki9.sendText(msg.to,"追加好友成功")
		
	
            elif ("Lv2:" in msg.text):
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
                                staff2.append(target)
                                ki.sendText(msg.to,"提升權限至Lv.2" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff2 add executed"
                else:
                    pass

		
            elif "Botinvite:" in msg.text:
               if msg.from_ in admin + staff6:
                midd = msg.text.replace("Botinvite:","")
		kicker = random.choice(KAC)
                kicker.findAndAddContactsByMid(midd)
                kicker.inviteIntoGroup(msg.to,[midd])

            elif ("Lv3:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff3.append(target)
                                ki.sendText(msg.to,"提升權限至Lv.3\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff3 add executed"
                else:
                    pass
	
            elif ("Lv4:" in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff4.append(target)
                                ki.sendText(msg.to,"提升權限至Lv.4\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff4 add executed"
                else:
                    pass
	
            elif ("Lv5:" in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff5.append(target)
                                ki.sendText(msg.to,"提升權限至Lv.5\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff5 add executed"
                else:
                    pass
	
	
            elif ("Bot:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                bgbot.append(target)
                                ki.sendText(msg.to,"加入機器名單\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]bgbot add executed"
                else:
                    pass	

            elif ("Bot:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                bgbot.remove(target)
				ki.sendText(msg.to,"刪除機器名單\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]bgbot remove executed"
                else:
                    pass

            elif ("Lvd1:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
            elif ("Lvd2:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff2.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
            elif ("Lvd3:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff3.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
            elif ("Lvd4:" in msg.text):
                if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff4.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
            elif ("Lvd5:" in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   key1 = key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff5.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
	
            elif msg.text in ["/Level","/level"]:
              if msg.from_ in admin + staff6:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if staff6 == []:
                    ki.sendText(msg.to,"沒有權限用戶")
                else:
                    ki.sendText(msg.to,"權限名單讀取中...")
                    mc = ""
		    mc2 = ""
		    mc3 = ""
		    mc4 = ""
		    mc5 = ""
                    mc6 = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    for mi_d in staff2:
                        mc2 += "->" +cl.getContact(mi_d).displayName + "\n"
                    for mi_d in staff3:
                        mc3 += "->" +cl.getContact(mi_d).displayName + "\n"
                    for mi_d in staff4:
                        mc4 += "->" +cl.getContact(mi_d).displayName + "\n"
                    for mi_d in staff5:
                        mc5 += "->" +cl.getContact(mi_d).displayName + "\n"
                    for mi_d in staff6:
                        mc6 += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,"權限用戶:\n\n€權限Lv.1\n" + mc + "\n€權限Lv.2\n" + mc2 + "\n€權限Lv.3\n" + mc3 + "\n€權限Lv.4\n" + mc4 + "\n€權限Lv.5\n" + mc5 + "\n€權限Lv.6(最高)\n" + mc6 + "\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")

              else:
                    pass
            elif msg.text in ["/Bot","/bot"]:
              if msg.from_ in admin + staff6:
                if bgbot == []:
                    ki.sendText(msg.to,"沒有機器名單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
                  try:
                    m1 = ""
		    
                    for mi_d in bgbot:
                        m1 += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,"機器名單:\n\n" + m1 + "\n" + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                  except:
				ki.sendText(msg.to,"錯誤")

              else:
                    pass
			
            elif ("/Mk:" in msg.text):
		if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
		     if target not in Bots + bgbot:
                       try:
                           random.choice(KAC).kickoutFromGroup(msg.to,[target])
                       except:
                            ki.sendText(msg.to,"錯誤")

			
            elif "/Nk:" in msg.text:
	      if msg.from_ in admin + staff6:
                    _name = msg.text.replace("/Nk:","")
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"找不到用戶")
                    else:
                        for target in targets:
			 if target not in Bots + bgbot:
			  try:
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                          except:
				ki.sendText(msg.to,"錯誤")
		
            elif "/Mban:" in msg.text:
	      if msg.from_ in admin + staff6:
                midd = msg.text.replace("/Mban:","")
                wait["blacklist"][midd] = True
		ki2.sendText(msg.to,"已加入黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
            elif "/Munban:" in msg.text:
	      if msg.from_ in admin + staff5 + staff6:
                midd = msg.text.replace("/Munban:","")
		del wait["blacklist"][midd]
		ki2.sendText(msg.to,"已解除黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif "/kick:" in msg.text:
	      if msg.from_ in admin + staff6:
                midd = msg.text.replace("/kick:","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])

		

		
            elif msg.text in ["/Blhelp","/blhelp"]:
	      if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		    cl.sendText(msg.to,"[黑單說明]\n\n踢機器者或是權限Lv5以上設定的用戶會被黑單。\n若邀請黑單用戶,則會被踢出群組,但邀請者並不會被黑單。\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/wlhelp","/Wlhelp"]:
	      if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		    cl.sendText(msg.to,"[白單說明]\n\n€白單用戶特權:\n1.開啟網址不會被關\n2.踢人不會被機器踢\n3.邀請黑單用戶不會被踢只會被取消\n\n" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["Ban"]:
	      if msg.from_ in admin + staff6:
                wait["wblacklist"] = True
                ki2.sendText(msg.to,"請傳送友資黑單" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
            elif msg.text in ["Unban"]:
	      if msg.from_ in admin + staff5 + staff6:
                wait["dblacklist"] = True
                ki2.sendText(msg.to,"請傳送友資解除黑單" + "[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["Bl","BL","bl"]:
	      if msg.from_ in admin + staff5 + staff6:
                if wait["blacklist"] == {}:
                    ki.sendText(msg.to,"沒有黑名單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
                  try:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,"黑名單用戶:\n\n" + mc + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                  except:
				ki.sendText(msg.to,"錯誤")
		
            elif ("Bl:" in msg.text):
		if msg.from_ in admin + staff6:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
			if target not in Bots + bgbot:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki2.sendText(msg.to,"已加入黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                ki2.sendText(msg.to,"已是黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
				
            elif ("Ubl:" in msg.text):
		if msg.from_ in admin + staff5 + staff6:
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
                                ki2.sendText(msg.to,"已解除黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                            except:
                                ki2.sendText(msg.to,"已不是黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif "Banlist" in msg.text:
                if msg.from_ in admin + staff5 + staff6:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "->" +cl.getContact(mm).displayName + "\n"
                    ki2.sendText(msg.to,cocoa + "以上為在本群的黑單用戶" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["Blmid","blmid"]:
              if msg.from_ in admin + staff5 + staff6:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"沒有黑名單")
                else:
                    cl.sendText(msg.to,"黑名單用戶讀取中...")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "" + mi_d + "\n\n"
                    cl.sendText(msg.to,"[戦神SelfBOT代行]\n黑名單用戶m_i_d:\n\n" + mc + "\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/Unbanall","/unbanall"]:
              if msg.from_ in admin + staff6:
		if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"沒有黑名單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
			wait["blacklist"] = {}
		        cl.sendText(msg.to,"已解除所有黑單" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif "Ban:" in msg.text:          
              if msg.from_ in admin + staff6:
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
                           cl.sendText(msg.to,"找不到用戶0.0" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                           pass
                       else:
                           for target in targets:
			     if target not in Bots + bgbot:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"黑單成功" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                                except:
                                    cl.sendText(msg.to,"黑單成功" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")

            elif "Unban:" in msg.text:      
              if msg.from_ in admin + staff6:
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
                           cl.sendText(msg.to,"找不到用戶0.0" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"解黑成功" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                                except:
                                    cl.sendText(msg.to,"解黑成功" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		

		
            elif "/blk" in msg.text:
              if msg.from_ in admin + staff6:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"群內沒有黑單用戶" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                        return
                    for jj in matched_list:
		      if jj not in Bots:
                        try:
                            klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
				pass
                            
		
		
		
		
		
            elif msg.text in ["/bg9bot","/BG9bot","/BGbot9"]:
		if msg.from_ in admin + staff3 + staff4 + staff5 + staff6:
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
			cl.sendText(msg.to,"保護追加完成" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
			
			

#--------------------------------------------------------
            elif "/mid:" in msg.text:
	      if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                mmid = msg.text.replace("/mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                ki.sendMessage(msg)

#-----------------------------------------------------------

		
            elif ("/Mid:" in msg.text):
	      if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   ki.sendText(msg.to,"" +  key1 + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif "名字:" in msg.text:
              if msg.from_ in admin + staff6:
                string = msg.text.replace("名字:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"成功:" + string + "" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		else:
			pass
		
            elif "名字9:" in msg.text:
              if msg.from_ in admin + staff6:
                string = msg.text.replace("名字9:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"成功:" + string + "" + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		else:
			pass
			


#------------------------------------------------------------------------------------

        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		    ki.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		    ki2.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		    ki3.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    ki4.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		    ki5.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		    ki6.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    ki7.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		    ki8.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		    ki9.sendText(op.param1,str(wait["message1"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")


	
	
        if op.param3 == "4":
		if op.param2 in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6 + bgbot:
			pass
		else:
					group = cl.getGroup(op.param1)
					try:
						G = cl.getGroup(op.param1)
						G.preventJoinByTicket = True
						random.choice(KAC).updateGroup(G)
						random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
					except:
						G = cl.getGroup(op.param1)
						G.preventJoinByTicket = True
						random.choice(KAC).updateGroup(G)
						random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
	
        if op.type == 19:
                    if op.param2 in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6 + bgbot:
                        pass
                    else:
                      if op.param3 not in Bots + staff3 + staff4 + staff5 + staff6 + bgbot:
                        G = cl.getGroup(op.param1)
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
						random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki5.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki2.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki4.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki7.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki8.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														ki3.kickoutFromGroup(op.param1,[op.param2])
													except:
														pass
				
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)



			
        if op.type == 19:
                    if op.param2 in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6 + bgbot:
                        pass
                    else:
                      if op.param3 in staff3 + staff4 + staff5 + staff6:
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
						random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki8.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
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
														ki7.kickoutFromGroup(op.param1,[op.param2])
													except:
														ki4.kickoutFromGroup(op.param1,[op.param2])
			
			
			
        if op.type == 19:
		if op.param2 not in Bots + bgbot:
                    if op.param3 in staff3 + staff4 + staff5 + staff6:
			try:
				kicker = random.choice(KAC)
				kicker.findAndAddContactsByMid(op.param3)
                                kicker.inviteIntoGroup(op.param1,[op.param3])
									    
			except:
				kicker = random.choice(KAC)
				kicker.findAndAddContactsByMid(op.param3)
                                kicker.inviteIntoGroup(op.param1,[op.param3])
				
        if op.type == 17:
		if op.param2 in staff:
			ki9.sendText(op.param1,"歡迎權限Lv.1用戶加入!\n(´▽｀)")
				
        if op.type == 17:
		if op.param2 in staff2:
			ki9.sendText(op.param1,"歡迎權限Lv.2用戶加入!\n(๑•̀ㅁ•́๑)✧")
			
        if op.type == 17:
		if op.param2 in staff3:
			ki9.sendText(op.param1,"歡迎權限Lv.3用戶加入!\nヾ(*´∀｀*)ﾉ")
				
        if op.type == 17:
		if op.param2 in staff4:
			ki9.sendText(op.param1,"歡迎權限Lv.4用戶加入!\n(●´ϖ`●)")
			
        if op.type == 17:
		if op.param2 in staff5:
			ki9.sendText(op.param1,"歡迎權限Lv.5用戶加入!\n(≧▽≦)")
				
        if op.type == 17:
		if op.param2 in staff6:
			ki9.sendText(op.param1,"歡迎權限Lv.6用戶加入!\nʕ•̀ω•́ʔ✧")
				
	if op.type == 17:
	    if wait["blacklist"][op.param2] == True:
		if op.param2 in Bots + bgbot:
		    pass
		else:
		   ki9.sendText(op.param1,"危險!\n黑單用戶加入!請踢出!")
			
			
			
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                  if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6 + bgbot:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        G = random.choice(KAC).getGroup(op.param1)	
                    G.name = wait['pro_name'][op.param1]
                    try:
                        random.choice(KAC).updateGroup(G)
                    except:
                        cl.updateGroup(G)
                    
                    if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6 + bgbot:
                        try:
				kicker = random.choice(KAC)
				kicker.kickoutFromGroup(op.param1,[op.param2])
                        except:
				kicker = random.choice(KAC)
				kicker.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Bots:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki9.updateGroup(G)
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
													pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki7.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki4.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki8.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
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
													pass
								

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki6.updateGroup(G)
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
									ki5.updateGroup(G)
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
													pass
			try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki7.reissueGroupTicket(op.param1)
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
									Ticket = ki5.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki6.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki8.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki9.reissueGroupTicket(op.param1)
												except:
													pass
                        
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
                        
                elif op.param3 in kimid:
                    if op.param2 in Bots:
                        G = ki2.getGroup(op.param1)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
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
							try:
								Ticket = ki4.reissueGroupTicket(op.param1)
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
													pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
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
													G = ki9.getGroup(op.param1)
												except:
													try:
														G = cl.getGroup(op.param1)
													except:
														pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki2.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki3.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki4.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki7.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki8.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki9.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														cl.kickoutFromGroup(op.param1,[op.param2])
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
			try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki9.reissueGroupTicket(op.param1)
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
													Ticket = ki.reissueGroupTicket(op.param1)
												except:
													try:
														Ticket = cl.reissueGroupTicket(op.param1)
													except:
														pass
                        
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
					ki7.updateGroup(G)
				except:
					try:
						ki6.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki2.updateGroup(G)
									except:
										try:
											ki.updateGroup(G)
										except:
											try:
												ki8.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														cl.updateGroup(G)
													except:
														pass

                elif op.param3 in ki3mid:
                    if op.param2 in Bots:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki8.updateGroup(G)
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
													G = ki9.getGroup(op.param1)
												except:
													try:
														G = cl.getGroup(op.param1)
													except:
														pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki3.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki2.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki6.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki4.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki7.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki8.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki9.kickoutFromGroup(op.param1,[op.param2])
												except:
													try:
														cl.kickoutFromGroup(op.param1,[op.param2])
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
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
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
							Ticket = ki.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki2.reissueGroupTicket(op.param1)
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
														Ticket = cl.reissueGroupTicket(op.param1)
													except:
														pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
					ki8.updateGroup(G)
				except:
					try:
						ki7.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
									except:
										try:
											ki2.updateGroup(G)
										except:
											try:
												ki.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														cl.updateGroup(G)
													except:
														pass
                        
                elif op.param3 in ki2mid:
                    if op.param2 in Bots:
                        G = ki3.getGroup(op.param1)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
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
							Ticket = ki3.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki2.reissueGroupTicket(op.param1)
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
														Ticket = cl.reissueGroupTicket(op.param1)
													except:
														pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki6.updateGroup(G)
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
													G = ki9.getGroup(op.param1)
												except:
													pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki3.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki2.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki4.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki8.kickoutFromGroup(op.param1,[op.param2])
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
					ki6.updateGroup(G)
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
									ki5.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki5.reissueGroupTicket(op.param1)
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
														Ticket = cl.reissueGroupTicket(op.param1)
													except:
														pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
                        
                elif op.param3 in ki4mid:
                    if op.param2 in Bots:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
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
													G = ki9.getGroup(op.param1)
												except:
													pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki9.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki2.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki7.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki4.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki8.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki3.kickoutFromGroup(op.param1,[op.param2])
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
						ki2.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki5.reissueGroupTicket(op.param1)
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
														Ticket = cl.reissueGroupTicket(op.param1)
													except:
														pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
					ki3.updateGroup(G)
				except:
					try:
						ki2.updateGroup(G)
					except:
						try:
							ki.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass

                elif op.param3 in ki5mid:
                    if op.param2 in Bots:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki5.updateGroup(G)
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
													pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki9.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki4.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki8.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki7.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
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
													pass
								

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki6.updateGroup(G)
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
									ki5.updateGroup(G)
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
													pass
			try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki7.reissueGroupTicket(op.param1)
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
									Ticket = ki5.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki6.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki8.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki9.reissueGroupTicket(op.param1)
												except:
													pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
					ki4.updateGroup(G)
				except:
					try:
						ki2.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
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
											ki7.updateGroup(G)
										except:
											try:
												ki8.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														cl.updateGroup(G)
													except:
														pass

                elif op.param3 in ki6mid:
                    if op.param2 in Bots:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki5.updateGroup(G)
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
													pass
								

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki6.updateGroup(G)
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
									ki5.updateGroup(G)
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
													pass
			try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki7.reissueGroupTicket(op.param1)
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
									Ticket = ki5.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki6.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki8.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki9.reissueGroupTicket(op.param1)
												except:
													pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
					ki7.updateGroup(G)
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
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
									except:
										try:
											ki.updateGroup(G)
										except:
											try:
												ki8.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														cl.updateGroup(G)
													except:
														pass

                elif op.param3 in ki7mid:
                    if op.param2 in Bots:
                        G = ki8.getGroup(op.param1)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
                    else:
			wait["blacklist"][op.param2] = True
			try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki5.getGroup(op.param1)
				except:
					try:
						G = ki4.getGroup(op.param1)
					except:
						try:
							G = ki6.getGroup(op.param1)
						except:
							try:
								G = ki2.getGroup(op.param1)
							except:
								try:
									G = ki9.getGroup(op.param1)
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
													pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki3.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki4.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki8.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki7.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki2.kickoutFromGroup(op.param1,[op.param2])
												except:
													pass
								

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki8.updateGroup(G)
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
									ki5.updateGroup(G)
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
													ki6.updateGroup(G)
												except:
													pass
			try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki7.reissueGroupTicket(op.param1)
				except:
					try:
						Ticket = ki8.reissueGroupTicket(op.param1)
					except:
						try:
							Ticket = ki3.reissueGroupTicket(op.param1)
						except:
							try:
								Ticket = ki4.reissueGroupTicket(op.param1)
							except:
								try:
									Ticket = ki5.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki6.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki2.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki9.reissueGroupTicket(op.param1)
												except:
													pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass

                elif op.param3 in ki8mid:
                    if op.param2 in Bots:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki8.updateGroup(G)
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
													pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki2.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki4.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki8.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki9.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki3.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													ki7.kickoutFromGroup(op.param1,[op.param2])
												except:
													pass
								

                        G.preventJoinByTicket = False
			try:
				random.choice(KAC).updateGroup(G)
                        except:
				try:
					ki6.updateGroup(G)
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
									ki5.updateGroup(G)
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
													pass
			try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki7.reissueGroupTicket(op.param1)
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
									Ticket = ki5.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki6.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki8.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki9.reissueGroupTicket(op.param1)
												except:
													pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass

                elif op.param3 in ki9mid:
                    if op.param2 in Bots:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki7.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        try:
                             G = random.choice(KAC).getGroup(op.param1)
			except:
				try:
					G = ki3.getGroup(op.param1)
				except:
					try:
						G = ki2.getGroup(op.param1)
					except:
						try:
							G = ki.getGroup(op.param1)
						except:
							try:
								G = ki4.getGroup(op.param1)
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
													G = ki9.getGroup(op.param1)
												except:
													pass
			try:
                             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki9.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki2.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ki3.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki4.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki6.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki7.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki8.kickoutFromGroup(op.param1,[op.param2])
											except:
												try:
													cl.kickoutFromGroup(op.param1,[op.param2])
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
						ki7.updateGroup(G)
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
										ki6.updateGroup(G)
									except:
										try:
											ki2.updateGroup(G)
										except:
											try:
												ki8.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														cl.updateGroup(G)
													except:
														pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki7.reissueGroupTicket(op.param1)
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
									Ticket = ki5.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki6.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki8.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki9.reissueGroupTicket(op.param1)
												except:
													pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
					ki8.updateGroup(G)
				except:
					try:
						ki3.updateGroup(G)
					except:
						try:
							ki2.updateGroup(G)
						except:
							try:
								ki4.updateGroup(G)
							except:
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
									except:
										try:
											ki7.updateGroup(G)
										except:
											try:
												ki.updateGroup(G)
											except:
												try:
													ki9.updateGroup(G)
												except:
													try:
														cl.updateGroup(G)
													except:
														pass

                elif op.param3 in ki15mid:
                    if op.param2 in Bots:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
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
													G = ki9.getGroup(op.param1)
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
							ki3.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ki4.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ki5.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ki.kickoutFromGroup(op.param1,[op.param2])
										except:
											try:
												ki8.kickoutFromGroup(op.param1,[op.param2])
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
					ki9.updateGroup(G)
				except:
					try:
						ki4.updateGroup(G)
					except:
						try:
							ki3.updateGroup(G)
						except:
							try:
								ki2.updateGroup(G)
							except:
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
									except:
										try:
											ki8.updateGroup(G)
										except:
											try:
												ki7.updateGroup(G)
											except:
												try:
													ki.updateGroup(G)
												except:
													try:
														cl.updateGroup(G)
													except:
														pass
                        try:
				Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
				try:
					Ticket = ki7.reissueGroupTicket(op.param1)
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
									Ticket = ki5.reissueGroupTicket(op.param1)
								except:
									try:
										Ticket = ki6.reissueGroupTicket(op.param1)
									except:
										try:
											Ticket = ki8.reissueGroupTicket(op.param1)
										except:
											try:
												Ticket = ki.reissueGroupTicket(op.param1)
											except:
												try:
													Ticket = ki9.reissueGroupTicket(op.param1)
												except:
													pass
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
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
								try:
									ki5.updateGroup(G)
								except:
									try:
										ki6.updateGroup(G)
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
														cl.updateGroup(G)
													except:
														pass
            except:
		pass
			
	

		

        if op.type == 59:
            print op


    except Exception as error:
        print error





def nameUpdate():
    while True:
        try:
		profile = ki.getProfile()
		profile = ki2.getProfile()
		profile = ki3.getProfile()
		profile = ki4.getProfile()
		profile = ki5.getProfile()
		profile = ki6.getProfile()
		profile = ki7.getProfile()
		profile = ki8.getProfile()
		profile = ki9.getProfile()
		profile.displayName = "戦神Helper"
                ki.updateProfile(profile)
		profile.displayName = "Checker_Bot"
                ki2.updateProfile(profile)
		profile.displayName = "Python2.13"
                ki3.updateProfile(profile)
		profile.displayName = "Visual Basic"
                ki4.updateProfile(profile)
		profile.displayName = "JavaScript"
                ki5.updateProfile(profile)
		profile.displayName = "HTML DOM"
                ki6.updateProfile(profile)
		profile.displayName = "SQL Server"
                ki7.updateProfile(profile)
		profile.displayName = "CSS Selectors"
                ki8.updateProfile(profile)
		profile.displayName = "戦神☆Group-Protector"
                ki9.updateProfile(profile)
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
