# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="El6RJVvEot5RhvbgX7z6.7Z3cXrtfuogtw1TNNAW49G.g3i1XUW57muA5og3v9YU9KriZ5fzIABYUR9CcgSSMAs=")
cl.loginResult()
#海綿

ki = LINETCR.LINE()
ki.login(token="EljdBhjIpyymNQ2iMdU4.EHXdooy0k7Vdpz/JWPw31a.RJ+ND/knQqmufOobx17Ayy4be3hkmgII8UU8IeQU8fw=")
ki.loginResult()
#派大

ki2 = LINETCR.LINE()
ki2.login(token="Eli6mQsqZLJIa0EwiVU8.RtSrOhnYPzvBP13bYQ3U2a.KuFRaSQhQorY0YCTT5HafXsJ2RhQfHu8JVKiE2ZMx4g=")
ki2.loginResult()
#章魚

ki3 = LINETCR.LINE()
ki3.login(token="ElVveSrReW1r3M1fgFe2.sRqeFyjdHuvOeAl/K8LtGG.OvOPQBx5l+agUJi0RDXjZORdoYWJusY04Q0gVQnFP9E=")
ki3.loginResult()
#蟹老闆

ki4 = LINETCR.LINE()
ki4.login(token="EkUTvGSfGiJl7neSSY01.qmf+mG4qg58AVj7ARoBTuq.7zaTkwOMZslGg9hUAq+F6joM8+2gxN/GkA8FFhZm8U0=")
ki4.loginResult()
#

ki5 = LINETCR.LINE()
ki5.login(token="El3KdJJCZOqb7mghrRdb.IMj6l+lTvlZDBdTs8RLPgW.bXvLPScmdtmgHcxashs30mfxrjoTSnQ7YtyGs0b9Vug=")
ki5.loginResult()
#皮

ki6 = LINETCR.LINE()
ki6.login(token="ElitY4szw2pp5a58exS1.LV1zjEYReG6JjveFs1pBeq.Zo1o5IeEvF+Y5azZBOyznGhXCpKJhBTCZXQIxeaKJ7g=")
ki6.loginResult()
#泡芙

ki7 = LINETCR.LINE()
ki7.login(token="Elqogkd0Qgc1jWQGdcG7.OmBjf179LkLveZJhlwP9fW./QufjNTidU38rkqyStIwLUjku87wmEpaDQHJchrz298=")
ki7.loginResult()
#飛行

ki8 = LINETCR.LINE()
ki8.login(token="ElRv4rztCf0A5XjUrXSb.I/EPueUrHBP1i08VGrbPEW.PYqqYElEpJerTUhOl889jOSeflkwbHS8rMZOirCAXGY=")
ki8.loginResult()
#小蝸

ki9 = LINETCR.LINE()
ki9.login(token="El7SEgsY1dmlCTIrqFJf.pyykg7upILnMu7sucQqBVW.eF9xLrkT+ozFZZDjcUExp8OEqgPnRA7bPpzxRd6OrqU=")
ki9.loginResult()
#水母

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""-以下指令權限者使用-
[海綿指令]→查看指令
[/Author]→作者顯示
[/me]→ 顯示自己的友資
[/mid]→ 顯示自己mid
[/gid]→ 顯示群組gid
[Gn:]→ 更改群名
[/Ginfo]→ 顯示群組詳情
[海綿取消]→ 取消所有邀請
[/Url]→ 取得群組網址
[/Urlon]→ 開啟群組網址
[/Urloff]→ 關閉群組網址
[/Mid:@]→ 顯示被標註者的mid
[/mid:]→ 顯示mid的友資
[愛的禮物]→ 發送禮物
[/Time]→ 現在時間
[/Gc]→ 查看群長
[運勢]→ 看看今日運勢
[Nk:]→ 名字踢人
[Mk:@]→ 標註踢人
[Bl:@]→ 標註黑單
[Ban]→ 友資黑單
[Unban]→ 友資解除黑單
[Mban]→ mid黑單
[Munban]→ mid解除黑單
[Bl]→ 查看黑單
[/blk]→ 踢出黑單用戶
[權限者]→ 查看權限名單
[海綿加入]→ 增加防翻
[海綿退出]→ 防翻退出

-以下指令作者使用-
[Oa:@]→ 標註增加權限
[Od:@]→ 標註刪除權限

作者:戦神[Made In Taiwan]
http://line.me/ti/p/4-ZKcjagH0
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
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid]
admin = [mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,"uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","u40c17f320e101b9f1abc9edaace6ed51","u93c7dcf280c6730054e8ce0f8bdf5a97","u1e83e74785815f992611f32ac5b0b9b7","ud6e2c18ceeda02a8a21f8dd537378c55","uca42f2c5232e2ca4c86b7febc761fe7d","u2550fbb7947ab6c840def9905ac2a817","ub593dfce6c5276fe20f53a3ceea4a248","ubc3dae49b4bdd1d4e2b264d876bee267","ua7d7d88ae46e04468c089ccd14f271e8","ub19d0bd87bb361d8738ab432d6b12a10","uddf9714006a1010bb6551fc107f52390"]
staff = ["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","u40c17f320e101b9f1abc9edaace6ed51"]
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin2 = "ubecd98a04cbf74a830b6c95b67bd6b74"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"戦神Bot作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
    'message1':"戦神Bot作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
    'lang':"JP",
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
		if op.param2 in staff:
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
			G.preventJoinByTicket = True
                        cl.updateGroup(G)
		        try:
                            ginfo = cl.getGroup(op.param1)
			    try:
                                gCreator = ginfo.creator.displayName
                            except:
                                gCreator = ginfo.members[0].displayName
                            cl.sendText(op.param1,"防翻加入成功,請勿踢出任何機器!")
		        except:
			    cl.sendText(op.param1,"防翻加入成功,請勿踢出任何機器!")

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
                    cl.cancelGroupInvitation(op.param1, matched_list)
		    cl.kickoutFromGroup(op.param1, matched_list)
		
        if op.type == 13:
	    if op.param2 not in staff + admin + Bots:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
		    ki.kickoutFromGroup(op.param1,[op.param2])
		    ki3.cancelGroupInvitation(op.param1, matched_list)
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
		    ki2.kickoutFromGroup(op.param1, matched_list)
		
        if op.type == 13:
	    if op.param2 not in staff + admin + Bots:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki3.kickoutFromGroup(op.param1,[op.param2])
		    ki3.cancelGroupInvitation(op.param1, matched_list)
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
                    ki4.cancelGroupInvitation(op.param1, matched_list)
		    ki4.kickoutFromGroup(op.param1, matched_list)
		
        if op.type == 13:
	    if op.param2 not in staff + admin + Bots:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
		    ki5.kickoutFromGroup(op.param1,[op.param2])
		    ki6.cancelGroupInvitation(op.param1, matched_list)
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
		    ki7.kickoutFromGroup(op.param1, matched_list)
		
        if op.type == 13:
	    if op.param2 not in staff + admin + Bots:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki8.kickoutFromGroup(op.param1,[op.param2])
		    ki8.cancelGroupInvitation(op.param1, matched_list)
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
		    ki9.kickoutFromGroup(op.param1, matched_list)
		
        if op.type == 13:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
		    ki.sendText(msg.to,"請勿邀請黑單用戶")
		
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ki3.sendText(msg.to,msg.contentMetadata["displayName"] + " 已加入黑單成功")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ki3.sendText(msg.to,msg.contentMetadata["displayName"] + " 已加入黑單成功")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ki4.sendText(msg.to,msg.contentMetadata["displayName"] + " 已解除黑單成功")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        ki4.sendText(msg.to,msg.contentMetadata["displayName"] + " 已解除黑單成功")
			
            else:
		pass

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                    msg.contentType = 0
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
			if msg.contentMetadata["mid"] in wait["blacklist"]:
                             ki3.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu) + "\n[用戶狀況]:\n此用戶為黑名單用戶,不可邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        else:
			     ki3.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu) + "\n[用戶狀況]:\n此用戶為正常用戶\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ki3.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
            elif msg.contentType == 16:
                    msg.contentType = 0
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    if wait["lang"] == "JP":
                        msg.text = msg.contentMetadata["postEndUrl"] + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"] + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
                    ki4.sendText(msg.to,msg.text)
		

            elif msg.text is None:
                return
		
            if msg.text == "/Help":
              if msg.from_ in staff:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    ki.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)

		
            if msg.text == "/help":
              if msg.from_ in staff:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    ki.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)

            if msg.text == "/gid":
              if msg.from_ in staff:
                ki4.sendText(msg.to, msg.to)
            if msg.text == "/Gid":
              if msg.from_ in staff:
                ki4.sendText(msg.to, msg.to)
		
            elif msg.text in ["Groupid","所有群組","Allgid"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                ki3.sendText(msg.to,h)
              else:
		   pass
		
            elif ("Gn:" in msg.text):
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    random.choice(KAC).updateGroup(group)
                    ki2.sendText(msg.to,"群名: " + group.name)
                else:
                    ki2.sendText(msg.to,"><")
              else:
		pass
	
            elif msg.text in ["/mid","/Mid"]:
              if msg.from_ in staff:
                ki3.sendText(msg.to,msg.from_)
		
            elif msg.text in ["/me","/Me"]:
              if msg.from_ in staff:
		msg.contentType = 13
		X = msg.from_
                msg.contentMetadata = {"mid": X }
		ki4.sendMessage(msg)
                ki3.sendText(msg.to,msg.from_)
		
		
            elif msg.text in ["/tagall","/Tagall"]:
                if msg.from_ in admin:
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
                else:
		   pass

		

            elif msg.text in ["/test"]:
	       if msg.from_ in staff:
                profile = cl.getProfile()
                text = profile.displayName
                cl.sendText(msg.to, text)
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = profile.displayName
                ki7.sendText(msg.to, text)
                profile = ki8.getProfile()
                text = profile.displayName
                ki8.sendText(msg.to, text)
                profile = ki9.getProfile()
                text = profile.displayName
                ki9.sendText(msg.to, text)
	       else:
			pass
		

		


            elif msg.text in ["/Cancel","/cancel"]:
	       if msg.from_ in staff:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = ki5.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki5.cancelGroupInvitation(msg.to, gInviMids)
                        ki5.sendText(msg.to,"派大星取消了 "+ str(len(group.invitee)) + " 個邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        if wait["lang"] == "JP":
                            ki5.sendText(msg.to,"派大星找不到能取消的邀請吶\n(|||ﾟдﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        else:
                            ki5.sendText(msg.to,"派大星找不到能取消的邀請吶\n(|||ﾟдﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                        pass
			
            elif msg.text in ["/Cancel2","/cancel2"]:
	       if msg.from_ in staff:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = ki7.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki7.cancelGroupInvitation(msg.to, gInviMids)
                        ki7.sendText(msg.to,"取消了 "+ str(len(group.invitee)) + " 個邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        if wait["lang"] == "JP":
                            ki7.sendText(msg.to,"找不到能取消的邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        else:
                            ki7.sendText(msg.to,"找不到能取消的邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    pass

            elif msg.text in ["/author","/Author","/作者"]:
              if msg.from_ in staff:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
		cl.sendMessage(msg)
		cl.sendText(msg.to,"防翻作者:戦神\nMade In Taiwan\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			

            elif msg.text in ["/Urloff","/urloff"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(group)
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"關閉網址\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        ki2.sendText(msg.to,"關閉網址\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Urlon","/urlon"]:
                if msg.from_ in staff:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    gurl = cl.reissueGroupTicket(msg.to)
                    random.choice(KAC).updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"開啟網址\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        ki.sendText(msg.to,"開啟網址\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		else:
		   pass
            elif msg.text in ["/Time","/時刻","/time","/Now","/now"]:
              if msg.from_ in staff:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                ki4.sendText(msg.to, "海綿報時:" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Url","/url"]:
              if msg.from_ in staff:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                gurl = cl.reissueGroupTicket(msg.to)
                ki.sendText(msg.to,"群組網址...\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Groupcreator","/群長","/Gc","/gc","/groupcreator","群長"]:
             if msg.from_ in staff:
              if msg.toType == 2:
		 source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		 name = "".join([random.choice(source_str) for x in xrange(9)])
                 ginfo = cl.getGroup(msg.to)
                 try:
                        gCreator = ginfo.members[0].displayName
                 except:
                        gCreator = ginfo.members[0].displayName
		 ki4.sendText(msg.to,"[群長]\n->" + gCreator + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
              else:
		pass


            if msg.text == "/ginfo":
              if msg.from_ in staff:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
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
                        ki3.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        ki3.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    ki3.sendText(msg)
		
            if msg.text == "/Ginfo":
              if msg.from_ in staff:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    ginfo = cl.getGroup(msg.to)
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
                        ki3.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        ki3.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    ki3.sendText(msg)
		
            elif msg.text in ["/bgbye","/BGbye"]:
	       if msg.from_ in staff:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
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
		
            elif ("Oa:" in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff.append(target)
                                ki3.sendText(msg.to,target.displayName + "已加入權限名單")
                            except:
                                pass
                   print "[Command]Staff add executed"
                else:
                    pass
	
            elif ("Od:" in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                            try:
                                staff.remove(target)
                                ki4.sendText(msg.to,target.displayName + "已被解除權限")
                            except:
                                pass
                   print "[Command]Staff add executed"
                else:
                    pass
	
	
            elif msg.text in ["Owner"]:
              if msg.from_ in staff:
                if staff == []:
                    cl.sendText(msg.to,"沒有權限用戶")
                else:
                    cl.sendText(msg.to,"權限名單讀取中...")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki4.sendText(msg.to,"權限用戶:\n\n" + mc)
                    print "[Command]Stafflist executed"
              else:
                    pass
			
            elif ("Mk:" in msg.text):
		if msg.from_ in staff:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           random.choice(KAC).kickoutFromGroup(msg.to,[target])
                       except:
                           pass
		else:
                    pass

			
            elif "Nk:" in msg.text:
	      if msg.from_ in staff:
                if msg.toType == 2:
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
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
	      else:
                    pass
		
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		ki3.sendText(msg.to,midd.displayName + "已加入黑單")
            elif "Munban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = False
		ki4.sendText(msg.to,midd.displayName + "已解除黑單")
		
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])

		
            elif msg.text in ["77","ㄌㄑ"]:
	      if msg.from_ in staff:
		cl.sendText(msg.to,"ㄎㄩ的女人><")
		
            elif msg.text in ["戰神","ㄎㄩ"]:
	      if msg.from_ in staff:
		cl.sendText(msg.to,"ㄌㄑ的老公><")
		
            elif msg.text in ["Ban"]:
	      if msg.from_ in staff:
                wait["wblacklist"] = True
                ki.sendText(msg.to,"請傳送友資黑單")
            elif msg.text in ["Unban"]:
	      if msg.from_ in staff:
                wait["dblacklist"] = True
                ki2.sendText(msg.to,"請傳送友資解除黑單")
		
            elif msg.text in ["Bl","BL","bl"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"沒有黑名單")
                else:
                    cl.sendText(msg.to,"黑名單用戶讀取中...")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"黑名單用戶:\n\n" + mc)
		
            elif ("Bl:" in msg.text):
		if msg.from_ in staff:
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
                                ki4.sendText(msg.to,target.displayName + " 已加入黑單")
                            except:
                                ki4.sendText(msg.to,target.displayName + " 已是黑單")
				
            elif ("Ubl:" in msg.text):
		if msg.from_ in staff:
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
                                ki3.sendText(msg.to,target.displayName + " 已解除黑單")
                            except:
                                ki3.sendText(msg.to,target.displayName + " 已不是黑單")
		
            elif "Banlist" in msg.text:
                if msg.from_ in staff:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "->" +cl.getContact(mm).displayName + "\n"
                    ki.sendText(msg.to,cocoa + "以上為在本群的黑單用戶")
		
            elif "Ban:" in msg.text:  
		if msg.from_ in staff:
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
                           sendMessage(msg.to,"找不到此成員")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki3.sendText(msg.to,"已黑單")
                                except:
                                    ki3.sendText(msg.to,"錯誤")

            elif "Unban:" in msg.text:        
		if msg.from_ in staff:
                       nk0 = msg.text.replace("Unban","")
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
                           sendMessage(msg.to,"找不到此成員")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki3.sendText(msg.to,"已解除黑單")
                                except:
                                    ki3.sendText(msg.to,"錯誤")
		
            elif "/blk" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"群內沒有黑單用戶")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
                            pass
		
		
		
		
            elif msg.text in ["/helper","/Helper"]:
		if msg.from_ in staff:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
			ki.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
			

            elif msg.text in ["/checker","/Checker"]:
		if msg.from_ in staff:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
			ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki3.getGroup(msg.to)
                        ginfo = ki3.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
		
		
            elif msg.text in ["/bgbot","/BGbot"]:
		if msg.from_ in staff:
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
			cl.sendText(msg.to,"保護追加完成")
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
			

#--------------------------------------------------------
            elif "/mid:" in msg.text:
	      if msg.from_ in staff:
                mmid = msg.text.replace("/mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                ki3.sendMessage(msg)

#-----------------------------------------------------------

		
            elif ("/Mid:" in msg.text):
	      if msg.from_ in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   ki4.sendText(msg.to,"" +  key1)
			


#------------------------------------------------------------------------------------

        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    cl.sendText(op.param1,str(wait["message"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		    ki.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		    ki2.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		    ki3.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    ki4.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		    ki5.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		    ki6.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    ki7.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		    ki8.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		    ki9.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)


	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff:
		    G = ki9.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki9.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff:
		    G = ki8.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki8.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff:
		    G = ki7.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki7.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff:
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
	    else:
		pass
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff:
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff:
		    G = ki5.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki5.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff:
		    G = ki3.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki3.updateGroup(G)
	    else:
		pass
	
	if op.type == 19:
          if op.param2 not in Bots + staff + admin:
            print "someone was kicked"
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
          else:
		pass
	

				
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Bots + staff + admin:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
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
                        ki3.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = ki.getGroup(op.param1)

			ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
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
			jgs.append(op.param1)
			print "jgs.append13"
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                        
                elif op.param3 in kimid:
                    if op.param2 in Bots + staff + admin:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
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
                        ki8.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = ki2.getGroup(op.param1)

			ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
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
                        ki7.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in Bots + staff + admin:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
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
                        G = ki4.getGroup(op.param1)

                        
			ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki34.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
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
                        ki4.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in Bots + staff + admin:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
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
                        G = ki3.getGroup(op.param1)

                        
			ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
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
                        
                elif op.param3 in ki4mid:
                    if op.param2 in Bots + staff + admin:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
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
                        ki6.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
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
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in Bots + staff + admin:
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
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
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
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in Bots + staff + admin:
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
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
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
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in Bots + staff + admin:
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
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
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
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in Bots + staff + admin:
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
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
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
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in ki9mid:
                    if op.param2 in Bots + staff + admin:
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
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])
			ki5.kickoutFromGroup(op.param1,[op.param2])

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
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)


            except:
                pass

		
		

#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error

def nameUpdate():
    while True:
                profile = cl.getProfile()
		profile.displayName = "戦神保護V.7"
		cl.updateProfile(profile)
		profile = ki.getProfile()
		profile.displayName = "Helper"
		ki.updateProfile(profile)
		profile = ki2.getProfile()
		profile.displayName = "Helper"
		ki2.updateProfile(profile)
		profile = ki3.getProfile()
		profile.displayName = "Checker[K]"
		ki3.updateProfile(profile)
		profile = ki4.getProfile()
		profile.displayName = "Checker[N]"
		ki4.updateProfile(profile)
		profile = ki5.getProfile()
		profile.displayName = "Protection[A]"
		ki5.updateProfile(profile)
		profile = ki6.getProfile()
		profile.displayName = "Protection[D]"
		ki6.updateProfile(profile)
		profile = ki7.getProfile()
		profile.displayName = "Protection[E]"
		ki7.updateProfile(profile)
		profile = ki8.getProfile()
		profile.displayName = "Protection[G]"
		ki8.updateProfile(profile)
		profile = ki9.getProfile()
		profile.displayName = "Protection[S]"
		ki9.updateProfile(profile)
                
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
