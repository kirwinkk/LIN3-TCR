# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="EkukzJ7gWt0PnbcWKv33.MG8BtWFbb+oGXed0Fa9qWW.qZYhkFJC8pm3HM8aHJkga4YQot2OfFpBIrx7PydTNxk=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="Ekz3ZKEdUZe7qOuBiyTc.SeZ4ifzYZu4HyhgP47tpha.MNA2ssYmaL52m1EKgvAlkwyg0KXC66bvsfiGMPh9IRE=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EkzWgfXlPZ6rRiJIry3d.eem+p7zyhJGXULW/YtGNpq.fpm/Lku3gUiMX+HhQCGBe4L3mniaRP0WeaKjohRju7o=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EkyeKl3OcvOKJE3uZeV4.7RWlONtZ1Buiu1pRYoIM5a.xS4I9MgobgkkvFk2rmCNlcfyPMmkYy0wjAOESdjZqbI=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="Ek4voHXMJwNsenvYwJc0.EATCF6MzZ/kW4LEHLIslea.RPzK3aMIbgipRHrHLqpJ1yRWxWOUfiBEwRqI1xmtdmk=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EkBFUH2KRvooCziIe3K9.sZWYkriJsJf80xBKZDkbsq.kadwbKtdlV2Sv/yfxtAmdFHm3k0ymvMd68ZT98tM5Z0=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token=" El2e4tTG29CjOqKMB0h8.w0WR2OKO/canEpl7cVYAMa.6GMKEhlAD0dzu6xu8x4Wl+fSApjtztJ2saUz+UzRWnc=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="Ek8lJbO1TdtJ7IU59b9e.anot7ok1CmMlkurtH8BKxG.adpzKav+kBaG/ZR3T3184RjLfRC0LSqAHy8t+ekGDns=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="Ek5wMqt6tyVsBgaXIMJ4.WjRz5oW1/nfIsExC/cMSza.LojIUZZ9d/VRceEWCYtOUkfPxYIJm9/WQoWb+IftcQg=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EllH4TrW9b5WLGC1C6ce.WHByzKXoh0n3ljIXSlIvBG.lcNynhimCDzpiJ0pO7M5df1sNLDSd/lK8f0G6nbANQY=")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="Ekx78FlZHpDRydU5A5W0.bUWp6DHUJ5cshMkl5m0Aia.w9MLieeRDl2xBIa1ZbLI9F05sv7V3xdDA0PX6BaR8u0=")
ki10.loginResult()

ki11 = LINETCR.LINE()
ki11.login(token="ElGYaFC35VmWXRE6Phk6.QchB2dR6MW1R/GwBDLzYjG.8MWsEGSlUJfgXG4EZU8G4yV6YrwjTrAo9Riw+pn3HxI=")
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
[Nk:]→名字踢人
[Mk:@]→標註踢人
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
[Url]→取得群組網址
[Urlon]→開啟群組網址
[Urloff]→關閉群組網址
[Groupid]→目前加入的所有群組
[Mid:]→顯示被標註者的mid
[mid:]→顯示mid的友資
[Gift]→發送禮物
[TL:]→Po文
[Time]→現在時間
[Tagall]→標註所有人
[Say:]→保鑣講話
[BGbot]→追加kicker
[BGbye]→kicker退出
[Botmid]→查看Kicker友資
[Sp]→反應速度

作者:戦神
http://line.me/ti/p/4-ZKcjagH0"""
KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
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
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid]
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin = "uc216d8664c4e1f43772c98b1b0b8956e"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"戦神SelfBOT\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
    'lang':"JP",
    'comment':"戦神SelfBOT\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
    'commentOn':True,
    'commentBlack':{},
    'wblack':False,
    'dblack':False,
    'clock':True,
    'blacklist':{},
    'wblacklist':False,
    'dblacklist':False,
    'protect':True,
    'cancelprotect':True,
    'inviteprotect':True,
    'linkprotect':True,
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
                        ki4.updateGroup(G)
		        try:
                            cl.sendText(op.param1,"安安我是戦神^^\n......可以愛愛嗎?")
		        except:
			    pass
            if kimid in op.param3:
		if op.param2 in Bots:
                    ki.acceptGroupInvitation(op.param1)

            if ki2mid in op.param3:
		if op.param2 in Bots:
                    ki2.acceptGroupInvitation(op.param1)

            if ki3mid in op.param3:
		if op.param2 in Bots:
                    ki3.acceptGroupInvitation(op.param1)
			
            if ki4mid in op.param3:
		if op.param2 in Bots:
                    ki4.acceptGroupInvitation(op.param1)

            if ki5mid in op.param3:
		if op.param2 in Bots:
                    ki5.acceptGroupInvitation(op.param1)

            if ki6mid in op.param3:
		if op.param2 in Bots:
                    ki6.acceptGroupInvitation(op.param1)
			
            if ki2mid in op.param3:
		if op.param2 in Bots:
                    ki7.acceptGroupInvitation(op.param1)

            if ki3mid in op.param3:
		if op.param2 in Bots:
                    ki8.acceptGroupInvitation(op.param1)
			
            if ki4mid in op.param3:
		if op.param2 in Bots:
                    ki9.acceptGroupInvitation(op.param1)

            if ki5mid in op.param3:
		if op.param2 in Bots:
                    ki10.acceptGroupInvitation(op.param1)

            if ki6mid in op.param3:
		if op.param2 in Bots:
                    ki11.acceptGroupInvitation(op.param1)
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
                    cl.cancelGroupInvitation(op.param1, matched_list)
		
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
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "uc216d8664c4e1f43772c98b1b0b8956e":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
		
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
                             ki.sendText(msg.to,msg.contentMetadata["mid"])
                        else:
			     ki.sendText(msg.to,msg.contentMetadata["mid"])
		

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
		
            if msg.text == "Help":
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    random.choice(KAC).updateGroup(group)
                    ki.sendText(msg.to,"群名: " + group.name)
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
		

            elif "Botmid" == msg.text:
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
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
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
                    print "SUKSES -- SEND GINFO"
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl)
                    else:
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl)
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
                cl.sendText(msg.to,"[戦神SelfBOT代行]\nline://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])


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
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = False
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
				
            elif ("Mkk:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"因規制,無法踢出!")
				
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
                    _name = msg.text.replace("Nk:","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"找不到用戶")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"因規制,無法踢出!")
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
                                    cl.sendText(msg.to,"黑單成功")
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
                        try:
                            klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
                            cl.sendText(msg.to,"因規制,無法踢出!")


#-----------------------------------------------
            elif msg.text in ["tagall","Tagall"]:
			    group = cl.getGroup(msg.to)
			    nama = [contact.mid for contact in group.members]

			    cb = ""
			    cb2 = ""
			    strt = int(0)
			    akh = int(0)
			    for md in nama:
			        akh = akh + int(6)

			        cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

			        strt = strt + int(7)
			        akh = akh + 1
			        cb2 += "@nrik \n"

			    cb = (cb[:int(len(cb)-1)])
			    msg.contentType = 0
			    msg.text = cb2
			    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

			    try:
			        cl.sendMessage(msg)
			    except Exception as error:
			        print error
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
                        ginfo = ki2.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
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
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
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
                        wait["blacklist"][op.param2] = True


                        
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
                        G = ki2.getGroup(op.param1)
			ki2.kickoutFromGroup(op.param1,[op.param2])
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


                        
                elif op.param3 in ki2mid:
                    if op.param2 in Bots:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki3mid:
                    if op.param2 in Bots:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki4mid:
                    if op.param2 in Bots:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki5mid:
                    if op.param2 in Bots:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki6mid:
                    if op.param2 in Bots:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki7mid:
                    if op.param2 in Bots:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)
                        ki8.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
			cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki8mid:
                    if op.param2 in Bots:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
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
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)
                        ki9.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
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
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki9mid:
                    if op.param2 in Bots:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
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
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)
                        ki10.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
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
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki10mid:
                    if op.param2 in Bots:
                        G = ki11.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
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
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki11.getGroup(op.param1)
                        ki11.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
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
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			
                elif op.param3 in ki11mid:
                    if op.param2 in Bots:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
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
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
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
			ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

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

def nameUpdate():
    while True:
		profile = ki.getProfile()
		profile.displayName = "戦神☆01"
		ki.updateProfile(profile)
		profile = ki2.getProfile()
		profile.displayName = "戦神☆02"
		ki2.updateProfile(profile)
		profile = ki3.getProfile()
		profile.displayName = "戦神☆03"
		ki3.updateProfile(profile)
		profile = ki4.getProfile()
		profile.displayName = "戦神☆04"
		ki4.updateProfile(profile)
		profile = ki5.getProfile()
		profile.displayName = "戦神☆05"
		ki5.updateProfile(profile)
		profile = ki6.getProfile()
		profile.displayName = "戦神☆06"
		ki6.updateProfile(profile)
		profile = ki7.getProfile()
		profile.displayName = "戦神☆07"
		ki7.updateProfile(profile)
		profile = ki8.getProfile()
		profile.displayName = "戦神☆08"
		ki8.updateProfile(profile)
		profile = ki9.getProfile()
		profile.displayName = "戦神☆09"
		ki9.updateProfile(profile)
		profile = ki10.getProfile()
		profile.displayName = "戦神☆10"
		ki10.updateProfile(profile)
                
                time.sleep(600000)
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
