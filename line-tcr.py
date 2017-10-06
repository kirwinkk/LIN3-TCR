# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="ElLfLh1FoJej5kJLCi1d.VSu/lwQt0BfHIYFV2IIO3q.eX3RwkxpP60a7VWGhmmlylbXj2IcYgR5yPWNXXQnuzw=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ElCkxC0ty8IIFHi5J5Wc.u6kB6lCxZNreCdd3sRm+ha.zyXY0IRL81SYWuDaSGbAo7Jc4YyQfbPQuvAF5XBuQiA=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="ElpfCEBttwuXeMEshcA2.e4ZI31Q97N5EAzwpc+/hSG.UMLvXWR3dooUPYPaLvehECVCNZpIaami2ylznkRBFe8=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="ElhhqMHKmadxMyLVdsle.iT+8/7l878DR2aicLAjOFG.bAEl2O+0GPOLFG2MozptfmieGgYaoBVkIpPqNLAY564=")
ki3.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

jgs = cl.getGroupIdsJoined()
print "getGroupIdsJoined success"



helpMessage ="""[天線寶寶指令]...查看指令
[/Author]...作者顯示
[/gid]...顯示群組gid
[/Ginfo]...顯示群組詳情
[/Cancel]...取消所有邀請
[/Url]...取得群組網址
[/Urloff]...關閉群組網址
[/Mid:@]...顯示被標註者的mid
[/mid:]...顯示mid的友資
[/Gift]...發送禮物
[/Time]...現在時間
[/Gc]...查看群長
[天線寶寶加入]...BOT退出
[天線寶寶退出]...BOT退出

作者:戦神[Made In Taiwan]
http://line.me/ti/p/4-ZKcjagH0
"""
KAC=[cl,ki,ki2,ki3]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
mid1 = "uc216d8664c4e1f43772c98b1b0b8956e"
mid2 = "ubecd98a04cbf74a830b6c95b67bd6b74"
Bots=[mid,mid1,kimid,ki2mid,ki3mid,mid2]
admin = ["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
staff = ["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
adminMID = ["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
admsa = ["uc216d8664c4e1f43772c98b1b0b8956e"]

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"ℬᎶ戦神Bot*天線寶寶系列*\n此為權限機\n作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
    'message1':"ℬᎶ戦神Bot*天線寶寶系列*\n作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
    'lang':"JP",
    'linkprotect':True,
}


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
		if op.param2 in staff:
		  if op.param1 not in jgs:
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
			G.preventJoinByTicket = True
                        cl.updateGroup(G)
		        try:
                            ginfo = cl.getGroup(op.param1)
			    try:
                                gCreator = ginfo.creator.displayName
                            except:
                                gCreator = ginfo.members[0].displayName
                            cl.sendText(op.param1,"跟天線寶寶說你好^^\n[群組名稱]\n" + str(ginfo.name) + "\n\n[群長]\n->" + gCreator)
		        except:
			    cl.sendText(op.param1,"OK")
                        jgs.append(op.param1)
			print "jgs.append13"
			
	          else:
                       pass
		else:
			cl.acceptGroupInvitation(op.param1)
			cl.leaveGroup(op.param1)



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
                        cl.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
            elif msg.contentType == 16:
                    msg.contentType = 0
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    if wait["lang"] == "JP":
                        msg.text = msg.contentMetadata["postEndUrl"] + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"] + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
                    cl.sendText(msg.to,msg.text)
		
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
            elif msg.text is None:
                return
		
            if msg.text == "/Help":
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
            if msg.text == "天線寶寶指令":
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
            if msg.text == "/help":
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)

            if msg.text == "/gid":
                cl.sendText(msg.to, msg.to)
            if msg.text == "/Gid":
                cl.sendText(msg.to, msg.to)

            elif msg.text in ["/Gift","/gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["/運勢"]:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                a1, a2, a3, a4, a5, a6, a7, b1, b2, b3, b4, b5 = "大吉！", "中吉！", "小吉！", "吉！", "末凶！", "凶！", "大吉！", "中吉！", "小吉！", "吉！", "末凶！", "凶！"
                omikujilist = [a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5]
                cl.sendText(msg.to, random.choice(omikujilist) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
            elif msg.text in ["天線寶寶你好"]:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
		name2 = "".join([random.choice(source_str) for x in xrange(9)])
		name3 = "".join([random.choice(source_str) for x in xrange(9)])
		name4 = "".join([random.choice(source_str) for x in xrange(9)])
                cl.sendText(msg.to,"丁丁跟你說你好\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		ki.sendText(msg.to,"迪西跟你說你好\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name2)
		ki2.sendText(msg.to,"拉拉跟你說你好\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name3)
		ki3.sendText(msg.to,"小波跟你說你好\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name4)
		
            elif msg.text in ["智乃禮物","愛的禮物"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["/Cancel","/cancel","天線寶寶取消","天線寶寶cancel","天線寶寶Cancel"]:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"取消了 "+ str(len(group.invitee)) + " 個邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"找不到能取消的邀請吶(ノﾟДﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        else:
                            cl.sendText(msg.to,"找不到能取消的邀請吶(ノﾟДﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"(ノﾟДﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"(ノﾟДﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)

            elif msg.text in ["/author","/Author","/作者"]:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
		cl.sendMessage(msg)
		cl.sendText(msg.to,"創造者是戦神唷><👆\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			

            elif msg.text in ["/Urloff"]:
                if msg.toType == 2:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"關閉網址了≧∇≦\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"關閉網址了≧∇≦\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Urlon"]:
                if msg.from_ in staff:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"開啟網址了≧∇≦\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"開啟網址了≧∇≦\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		else:
		   pass
            elif msg.text in ["/Time","/時刻","/time","/Now","/now"]:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                cl.sendText(msg.to, "報時:" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Url","/url"]:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                gurl = cl.reissueGroupTicket(msg.to)
                cl.sendText(msg.to,"群組網址...\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Groupcreator","/群長","/Gc","/gc","/groupcreator","群長"]:
              if msg.toType == 2:
		 source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		 name = "".join([random.choice(source_str) for x in xrange(9)])
                 ginfo = cl.getGroup(msg.to)
                 try:
                        gCreator = ginfo.members[0].displayName
                 except:
                        gCreator = ginfo.members[0].displayName
		 cl.sendText(msg.to,"[群長]\n->" + gCreator + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
              else:
		pass


            if msg.text == "/ginfo":
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
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    cl.sendText(msg)
		
            if msg.text == "/Ginfo":
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
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    cl.sendText(msg)
		
            elif msg.text in ["/bgbye","/BGbye","天線寶寶再見","天線寶寶bye","天線寶寶退出"]:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    ginfo = cl.getGroup(msg.to)
                    try:
			jgs.remove(msg.to)
			print "jgs.remove"
                        cl.sendText(msg.to,""  +  str(ginfo.name)  + " 掰掰~\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			cl.leaveGroup(msg.to)
			ki.leaveGroup(msg.to)
			ki2.leaveGroup(msg.to)
			ki3.leaveGroup(msg.to)
                    except:
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
                                cl.sendText(msg.to,"已將此用戶加入權限名單")
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
                                cl.sendText(msg.to,"已將此用戶解除權限")
                            except:
                                pass
                   print "[Command]Staff add executed"
                else:
                    pass
	
	
            elif msg.text in ["Owner","權限","權限名單","權限者"]:
              if msg.from_ in staff:
                if staff == []:
                    cl.sendText(msg.to,"沒有權限用戶")
                else:
                    cl.sendText(msg.to,"權限名單讀取中...")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"權限者:\n" + mc)
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
                           klist=[cl,ki,ki2,ki3]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
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
                        cl.sendText(msg.to,"找不到用戶")
                    else:
                        for target in targets:
                            try:
                                klist=[cl,ki,ki2,ki3]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
	      else:
                    pass
		
            elif msg.text in ["/bgbot","/BGbot","天線寶寶bot","天線寶寶加入"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
			ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
			cl.sendText(msg.to,"天線寶寶們到齊囉")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#--------------------------------------------------------
            elif "/mid:" in msg.text:
                mmid = msg.text.replace("/mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

#-----------------------------------------------------------

		
            elif ("/Mid:" in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"" +  key1)
				

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
		

#------------------------------------------------------------------------------------

	if op.type == 11:
	    if op.param2 not in Bots:
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots:
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots:
		    G = ki2.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki2.updateGroup(G)
	    else:
		pass
	
	if op.type == 11:
	    if op.param2 not in Bots:
		    G = ki3.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki3.updateGroup(G)
	    else:
		pass
	

        if op.type == 19:
            try:
                if op.param3 in mid:
		    jgs.remove(op.param1)
		    print "jgs.remove19"
                    if op.param2 in Bots:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
			jgs.append(op.param1)
			print "jgs.append19"
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
			ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        wait["blacklist"][op.param2] = True
			jgs.append(op.param1)
			print "jgs.append19"

                if op.param3 in kimid:
                    if op.param2 in Bots:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
			ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        


                elif op.param3 in ki3mid:
                    if op.param2 in Bots:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
			ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
			cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        


            except:
                pass
        if op.type == 59:
            print op


    except Exception as error:
        print error

def nameUpdate():
    while True:
        try:
                profile = cl.getProfile()
                profile.displayName = "丁丁"
                cl.updateProfile(profile)
		profile1 = ki.getProfile()
                profile1.displayName = "迪西"
                ki.updateProfile(profile1)
		profile2 = ki2.getProfile()
                profile2.displayName = "拉拉"
                ki2.updateProfile(profile2)
		profile3 = ki3.getProfile()
                profile3.displayName = "小波"
                ki3.updateProfile(profile3)
                time.sleep(6000)
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
