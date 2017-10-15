# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="ElDu2YnXzcSCGW9IJL47.1kyf4+QsP7krNDEVhERE5W.G2C9vbhttcWNvJp1mi7Zc4tRsrGXdPRrK0FxFahvpZQ=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="El5sszK6zNtf81vVvjv4.CJqd24edERcutbKcGz5hDa.+zgEZ0tooD0nfs4KQiKQQAmCZbEee7Mzc++G30bQv/0=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="ElL5SWJQbuKcLi9ePLEe.SrCSpiP/rYSAQZYxykGUBG.GdjtlfkpmsYsdhDFE/CUd3Yl1NZ7dl7kiZa9wqvrTJc=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Elrn6F9ra7rsFTYU0g3c.sXCxy0CKzb/86fdMQWIJNa.MV4pT5VumEcGJYZsOtD6g4SvLxc5XuTJM2XvoxIh5fk=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="ElDQG1DLc5Qo6X8Uwug0.WwqPm0ukL9ODJ0m39TY4Sa.RrzMcY05yddE3jbjbHX2DOtThkBX6a6ztWE/yM7Fwko=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="El8ZWksA0RZ1Ubdwrm0a.VRtkE8ldWOmWhFjp0ZIgMG.GcWssPMcEwL40kQ9PEdD9EO0izmc7tJ7TwthpANhdhg=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="ElXDgFI1GBPkORGIXsd4.bOTjwJ4IY6/M4ng+aUJmLa.0UJiAWJxe9wDqD6K1zzS4S7GY7jHlrPcoxGGqYGCgnE=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="El1XEUBmYDuAzDTYBMke.jDxhAGROvQjm1IFQHi4uxG.u+ngeXvfqRsoRLN0oqSqd20yg2kcXBHuroBQYweH6j4=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="ElZsHsDUkvalYyW5nW17.Vd2UsBs90DtISMtyDR7IzW.d4WGeSUy2YMb4DqGXlqMl+SMIKueRrzunTQZS+520AI=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EljrYo9So6Khmhdmt790.3d81No0uyJfmd61BOYIYCa.fXe+2O+h/CuP6/MDyk1NnG4kYsKkNM7EVquzc6qfN9U=")
ki9.loginResult()

ki15 = LINETCR.LINE()
ki15.login(token="ElDQ92ox8Ph7M0JYqQze.WHByzKXoh0n3ljIXSlIvBG.TjNkCixA8QYX8onbku8Obw1Ij+QEhpV+cQacCxomqr8=")
ki15.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""※指令Lv.1以上使用
[/help]...查看指令
[/Author]...作者顯示
[/mid]...顯示自己mid
[/me]...顯示友資,mid,權限狀況
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
[Gn:]...關閉群組網址
☆Lv.2以上才有被機器白單

※指令Lv.3以上使用
[/bg9bot]...增加防翻
[/bg9bye]...防翻退出
[/helper]...helper入群
[/checker]...helper入群
☆Lv.3以上才可邀請機器入群

※指令Lv.4以上使用
[Nk:]...名字踢人
[Mk:@]...標註踢人
[/kick:]...用mid踢人
[Ubl:@]...標註解除黑單
[Unban:]...友資解除黑單
[Munban:]...mid解除黑單
[Banlist]...查看本群黑單

※指令Lv.5以上使用
[Bl:@]...標註黑單
[Ban]...友資黑單
[Mban]...mid黑單
[/blk]...踢出黑單用戶
[/tagall]...標註所有人

※指令Lv.6使用
[Bl]...查看黑單
[/Level]...查看權限名單
[Lv1:@]...標註增加Lv0權限至Lv1
[Lvd1:@]...標註刪除Lv1權限至Lv0
[/test]...查看防翻狀態

※盡量少用指令,避免盪,謝謝※
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
ki15mid = ki15.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki15mid]
admin = [mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki15mid,"uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","u40c17f320e101b9f1abc9edaace6ed51","uef3dc2c514c550e1935b5b679dac38f6","u7a1c4338e6342bbbc33d9fa3c295b7d4","uad3b11a07372a5955ba75dc1caadeed8","u4ab4047d824385456811a2fe93c95382","u40c17f320e101b9f1abc9edaace6ed51","u8a627a2ff2ed54bcdd6c3b52f2b9691b","u96fd5925ecab120ea325511f4b53db11","ua0c6c9175efd94a9551338c72d6a7d17","u3d860a1bb50f8a536653b4940aa41bbf","u8be7a9504b9185ba75234f2f8110697b"]
staff = []
staff2 = []
staff3 = []
staff4 = []
staff5 = []
staff6 = ["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin2 = "ubecd98a04cbf74a830b6c95b67bd6b74"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"戦神公開保護V.9\n[使用方式]:\n邀請此機器進入群組,此機器為公開防翻。群內有機器,丟友資可查看是否黑單。\n\n[禁止事項]:\n\n$[不會]被黑單[不會]被踢:\n1.禁止開啟網址\n\n$[不會]被黑單[會]被踢:\n1.禁止邀請黑單用戶\n2.禁止踢任何群內成員\n\n$[會]被黑單[會]被踢\n1.踢出機器\n\n#注意:黑單無法解除!\n\n戦神Bot作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
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
		if op.param2 in admin + staff3 + staff4 + staff5 + staff6:
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
                            cl.sendText(op.param1,"戦神權限保護V.9\n\n[禁止事項]:\n\n$[不會]被黑單[不會]被踢:\n1.禁止開啟網址\n\n$[不會]被黑單[會]被踢:\n1.禁止邀請黑單用戶\n2.禁止踢任何群內成員\n\n$[會]被黑單[會]被踢\n1.踢出機器\n\n#注意:黑單無法解除!\n權限者才可使用指令,不過盡量少用指令,避免盪,謝謝\n\n戦神Bot作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0")
		        except:
			    pass
		else:
		  pass
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
                    random.choice(KAC).cancelGroupInvitation(op.param1, matched_list)
		
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

        if op.type == 13:
            if op.param2 not in admin + staff2 + staff3 + staff4 + staff5 + staff6:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			
        if op.type == 13:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
		    ki9.sendText(op.param1,"請勿邀請黑單用戶")
			
        if op.type == 13:
		Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    random.choice(KAC).updateGroup(G)
		
        if op.type == 13:
            if op.param2 not in admin + staff2 + staff3 + staff4 + staff5 + staff6:
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
                        ki.sendText(msg.to,msg.contentMetadata["displayName"] + " 已加入黑單")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ki.sendText(msg.to,msg.contentMetadata["displayName"] + " 已加入黑單")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ki.sendText(msg.to,msg.contentMetadata["displayName"] + " 已解除黑單")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        ki.sendText(msg.to,msg.contentMetadata["displayName"] + " 已解除黑單")
			
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
                             ki2.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu) + "\n[黑單狀況]:\n此用戶為黑名單用戶,不可邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        else:
			     ki2.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu) + "\n[黑單狀況]:\n此用戶並不是黑名單用戶,可以邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ki2.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
            elif msg.contentType == 16:
                    msg.contentType = 0
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    if wait["lang"] == "JP":
                        msg.text = msg.contentMetadata["postEndUrl"] + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"] + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
                    ki2.sendText(msg.to,msg.text)
		

            elif msg.text is None:
                return
		
            if msg.text == "/Help":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    ki.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)

		
            if msg.text == "/help":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    ki.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)

            if msg.text == "/gid":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                ki2.sendText(msg.to, msg.to)
            if msg.text == "/Gid":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                ki2.sendText(msg.to, msg.to)
		
            elif msg.text in ["Groupid","所有群組","Allgid"]:
              if msg.from_ in admin + staff6:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                ki.sendText(msg.to,h)
              else:
		   pass
		
            elif ("Gn:" in msg.text):
              if msg.from_ in admin + staff2 + staff3 + staff4 + staff5 + staff6:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    random.choice(KAC).updateGroup(group)
                    ki.sendText(msg.to,"群名: " + group.name)
                else:
                    ki.sendText(msg.to,"><")
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
		gid = ki15.getGroupIdsJoined()
                for i in gid:
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
                    ki15.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"已退出所有群組")
                else:
                    cl.sendText(msg.to,"已退出所有群組")
		
		
            elif msg.text in ["/mid","/Mid"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                ki2.sendText(msg.to,msg.from_)
		
            elif msg.text in ["/me","/Me"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		msg.contentType = 13
		X = msg.from_
                msg.contentMetadata = {"mid": X }
		ki2.sendMessage(msg)
                ki2.sendText(msg.to,msg.from_)
		if msg.from_ in staff:
			ki2.sendText(msg.to,"[權限狀況]:Lv.1")
                if msg.from_ in staff2:
			ki2.sendText(msg.to,"[權限狀況]:Lv.2")
		if msg.from_ in staff3:
			ki2.sendText(msg.to,"[權限狀況]:Lv.3")
                if msg.from_ in staff4:
			ki2.sendText(msg.to,"[權限狀況]:Lv.4")
                if msg.from_ in staff5:
			ki2.sendText(msg.to,"[權限狀況]:Lv.5")
		if msg.from_ in admin:
			ki2.sendText(msg.to,"[權限狀況]:Lv.6(最高)")
		
		
		
            elif msg.text in ["/tagall","/Tagall"]:
                if msg.from_ in admin + staff5 + staff6:
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
	       if msg.from_ in admin + staff6:
                profile = cl.getProfile()
                text = "[正常] " + profile.displayName
                cl.sendText(msg.to, text)
                profile = ki.getProfile()
                text = "[正常] " + profile.displayName
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = "[正常] " + profile.displayName
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = "[正常] " + profile.displayName
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = "[正常] " + profile.displayName
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = "[正常] " + profile.displayName
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = "[正常] " + profile.displayName
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = "[正常] " + profile.displayName
                ki7.sendText(msg.to, text)
                profile = ki8.getProfile()
                text = "[正常] " + profile.displayName
                ki8.sendText(msg.to, text)
                profile = ki9.getProfile()
                text = "[正常] " + profile.displayName
                ki9.sendText(msg.to, text)
	       else:
			pass
		

		


            elif msg.text in ["/Cancel","/cancel"]:
	       if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = ki5.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki5.cancelGroupInvitation(msg.to, gInviMids)
                        ki.sendText(msg.to,"取消了 "+ str(len(group.invitee)) + " 個邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"找不到能取消的邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        else:
                            ki.sendText(msg.to,"找不到能取消的邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                        pass
			
            elif msg.text in ["/Cancel2","/cancel2"]:
	       if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = ki7.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki7.cancelGroupInvitation(msg.to, gInviMids)
                        ki.sendText(msg.to,"取消了 "+ str(len(group.invitee)) + " 個邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"找不到能取消的邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        else:
                            ki.sendText(msg.to,"找不到能取消的邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    pass

            elif msg.text in ["/author","/Author","/作者"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
		cl.sendMessage(msg)
		cl.sendText(msg.to,"防翻作者:戦神\nMade In Taiwan\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			

            elif msg.text in ["/Urloff","/urloff"]:
              if msg.from_ in admin + staff2 + staff3 + staff4 + staff5 + staff6:
                if msg.toType == 2:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"關閉網址\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        ki.sendText(msg.to,"關閉網址\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Urlon","/urlon"]:
                if msg.from_ in admin + staff2 + staff3 + staff4 + staff5 + staff6:
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
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                ki.sendText(msg.to, "" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Url","/url"]:
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                gurl = cl.reissueGroupTicket(msg.to)
                ki.sendText(msg.to,"群組網址...\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Groupcreator","/群長","/Gc","/gc","/groupcreator","群長"]:
             if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
              if msg.toType == 2:
		 source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		 name = "".join([random.choice(source_str) for x in xrange(9)])
                 ginfo = cl.getGroup(msg.to)
                 try:
                        gCreator = ginfo.members[0].displayName
                 except:
                        gCreator = ginfo.members[0].displayName
		 ki.sendText(msg.to,"[群長]\n->" + gCreator + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
              else:
		pass


            if msg.text == "/ginfo":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
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
                        ki.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        ki.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    ki.sendText(msg)
		
            if msg.text == "/Ginfo":
              if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
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
                        ki.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        ki.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    ki.sendText(msg)
		
            elif msg.text in ["/bg9bye","/BG9bye"]:
	       if msg.from_ in admin + staff3 + staff4 + staff5 + staff6:
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
                if msg.from_ in admin:
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
                                ki.sendText(msg.to,"提升權限至Lv.1\n" + mi)
                            except:
                                pass
                   print "[Command]Staff1 add executed"
                else:
                    pass
	

	
            elif ("Lv2:" in msg.text):
                if msg.from_ in admin:
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
                                ki.sendText(msg.to,"提升權限至Lv.2\n" + mi)
                            except:
                                pass
                   print "[Command]Staff2 add executed"
                else:
                    pass
	

            elif ("Lv3:" in msg.text):
                if msg.from_ in admin:
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
                                staff3.append(target)
                                ki.sendText(msg.to,"提升權限至Lv.3\n" + mi)
                            except:
                                pass
                   print "[Command]Staff3 add executed"
                else:
                    pass
	
            elif ("Lv4:" in msg.text):
                if msg.from_ in admin:
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
                                staff4.append(target)
                                ki.sendText(msg.to,"提升權限至Lv.4\n" + mi)
                            except:
                                pass
                   print "[Command]Staff4 add executed"
                else:
                    pass
	
            elif ("Lv5:" in msg.text):
                if msg.from_ in admin:
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
                                staff5.append(target)
                                ki.sendText(msg.to,"提升權限至Lv.5\n" + mi)
                            except:
                                pass
                   print "[Command]Staff5 add executed"
                else:
                    pass

	

            elif ("Lvd1:" in msg.text):
                if msg.from_ in admin:
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
				ki.sendText(msg.to,"解除權限至Lv.0\n" + mi)
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
            elif ("Lvd2:" in msg.text):
                if msg.from_ in admin:
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
                                staff2.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + mi)
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
            elif ("Lvd3:" in msg.text):
                if msg.from_ in admin:
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
                                staff3.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + mi)
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
            elif ("Lvd4:" in msg.text):
                if msg.from_ in admin:
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
                                staff4.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + mi)
                            except:
                                pass
                   print "[Command]Staff remove executed"
                else:
                    pass
            elif ("Lvd5:" in msg.text):
                if msg.from_ in admin:
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
                                staff5.remove(target)
				ki.sendText(msg.to,"解除權限至Lv.0\n" + mi)
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
                    ki.sendText(msg.to,"權限用戶:\n\n€權限Lv.1\n" + mc + "\n€權限Lv.2\n" + mc2 + "\n€權限Lv.3\n" + mc3 + "\n€權限Lv.4\n" + mc4 + "\n€權限Lv.5\n" + mc5 + "\n€權限Lv.6(最高)\n" + mc6 + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    print "[Command]Stafflist executed"
              else:
                    pass
			
            elif ("Mk:" in msg.text):
		if msg.from_ in admin + staff4 + staff5 + staff6:
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
	      if msg.from_ in admin + staff4 + staff5 + staff6:
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
	      if msg.from_ in admin + staff5 + staff6:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		ki2.sendText(msg.to,"已加入黑單")
            elif "Munban:" in msg.text:
	      if msg.from_ in admin + staff4 + staff5 + staff6:
                midd = msg.text.replace("Munban:","")
                wait["blacklist"][midd] = False
		ki2.sendText(msg.to,"已解除黑單")
		
            elif "/kick:" in msg.text:
	      if msg.from_ in admin + staff4 + staff5 + staff6:
                midd = msg.text.replace("Kick:","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])

		
            elif msg.text in ["77","ㄌㄑ"]:
	      if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		cl.sendText(msg.to,"ㄎㄩ的女人><")
		
            elif msg.text in ["戰神","ㄎㄩ"]:
	      if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		cl.sendText(msg.to,"ㄌㄑ的老公><")
		
            elif msg.text in ["/Blhelp","/blhelp"]:
	      if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
		    cl.sendText(msg.to,"[黑單說明]\n\n踢機器者或是權限Lv5以上設定的用戶會被黑單。\n若邀請黑單用戶,則會被踢出群組,但邀請者並不會被黑單。\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
            elif msg.text in ["/wlhelp","/Wlhelp"]:
	      if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
		    cl.sendText(msg.to,"[白單說明]\n\n€白單用戶特權:\n1.開啟網址不會被關\n2.踢人不會被機器踢\n3.邀請黑單用戶不會被踢只會被取消\n4.踢機器不會被踢也不會被黑(別去踢機器^^)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
            elif msg.text in ["Ban"]:
	      if msg.from_ in admin + staff5 + staff6:
                wait["wblacklist"] = True
                ki2.sendText(msg.to,"請傳送友資黑單")
            elif msg.text in ["Unban"]:
	      if msg.from_ in admin + staff4 + staff5 + staff6:
                wait["dblacklist"] = True
                ki2.sendText(msg.to,"請傳送友資解除黑單")
		
            elif msg.text in ["Bl","BL","bl"]:
	      if msg.from_ in admin + staff6:
                if wait["blacklist"] == {}:
                    ki.sendText(msg.to,"沒有黑名單")
                else:
                    ki.sendText(msg.to,"黑名單用戶讀取中...")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,"黑名單用戶:\n\n" + mc)
		
            elif ("Bl:" in msg.text):
		if msg.from_ in admin + staff5 + staff6:
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
                                ki2.sendText(msg.to,"已加入黑單")
                            except:
                                ki2.sendText(msg.to,"已是黑單")
				
            elif ("Ubl:" in msg.text):
		if msg.from_ in admin + staff4 + staff5 + staff6:
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
                                ki2.sendText(msg.to,"已解除黑單")
                            except:
                                ki2.sendText(msg.to,"已不是黑單")
		
            elif "Banlist" in msg.text:
                if msg.from_ in admin + staff4 + staff5 + staff6:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "->" +cl.getContact(mm).displayName + "\n"
                    ki2.sendText(msg.to,cocoa + "以上為在本群的黑單用戶")
		
            elif "Ban:" in msg.text:  
		if msg.from_ in admin + staff5 + staff6:
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
                           ki2.sendText(msg.to,"找不到此成員")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki2.sendText(msg.to,"已黑單")
                                except:
                                    ki2.sendText(msg.to,"錯誤")

            elif "Unban:" in msg.text:        
		if msg.from_ in admin + staff4 + staff5 + staff6:
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
                           ki2.sendText(msg.to,"找不到此成員")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki2.sendText(msg.to,"已解除黑單")
                                except:
                                    ki2.sendText(msg.to,"錯誤")
		
            elif "/blk" in msg.text:
              if msg.from_ in admin + staff5 + staff6:
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
		if msg.from_ in admin + staff3 + staff4 + staff5 + staff6:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
			ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
			

            elif msg.text in ["/checker","/Checker"]:
		if msg.from_ in admin + staff3 + staff4 + staff5 + staff6:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
			ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki3.getGroup(msg.to)
                        ginfo = ki3.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
		
		
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
                   ki.sendText(msg.to,"" +  key1)
			


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
	    if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6:
		    G = ki9.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki9.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6:
		    G = ki8.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki8.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6:
		    G = ki7.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki7.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6:
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
	    else:
		pass
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6:
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6:
		    G = ki5.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki5.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6:
		    G = ki3.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki3.updateGroup(G)
	    else:
		pass
	
	if op.type == 19:
          if op.param2 not in Bots + admin + staff2 + staff3 + staff4 + staff5 + staff6:
            print "someone was kicked"
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
          else:
		pass
	

				
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                        ki9.updateGroup(G)
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
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        
                elif op.param3 in kimid:
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                        ki9.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                        ki5.updateGroup(G)
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
                        ki6.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                        ki5.updateGroup(G)
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
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                        ki6.updateGroup(G)
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
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
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
                        ki7.updateGroup(G)
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

                elif op.param3 in ki15mid:
                    if op.param2 in Bots + staff2 + staff3 + staff4 + staff5 + admin:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
			wait["blacklist"][op.param2] = True
                        G = ki8.getGroup(op.param1)
                        ki8.kickoutFromGroup(op.param1,[op.param2])
			ki6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
			
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
		profile.displayName = "戦神權限保護V.9.4.02"
		cl.updateProfile(profile)
		profile = ki.getProfile()
		profile.displayName = "戦神Helper"
		ki.updateProfile(profile)
		profile = ki2.getProfile()
		profile.displayName = "戦神Checker[A]"
		ki2.updateProfile(profile)
		profile = ki3.getProfile()
		profile.displayName = "Protection[F]"
		ki3.updateProfile(profile)
		profile = ki4.getProfile()
		profile.displayName = "Protection[G]"
		ki4.updateProfile(profile)
		profile = ki5.getProfile()
		profile.displayName = "Protection[H]"
		ki5.updateProfile(profile)
		profile = ki6.getProfile()
		profile.displayName = "Protection[I]"
		ki6.updateProfile(profile)
		profile = ki7.getProfile()
		profile.displayName = "Protection[J]"
		ki7.updateProfile(profile)
		profile = ki8.getProfile()
		profile.displayName = "Protection[K]"
		ki8.updateProfile(profile)
		profile = ki9.getProfile()
		profile.displayName = "Protection[L]"
		ki9.updateProfile(profile)
		profile = ki15.getProfile()
		profile.displayName = "戦神☆"
		ki15.updateProfile(profile)
                
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
