# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="ElhhqMHKmadxMyLVdsle.iT+8/7l878DR2aicLAjOFG.bAEl2O+0GPOLFG2MozptfmieGgYaoBVkIpPqNLAY564=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ElCkxC0ty8IIFHi5J5Wc.u6kB6lCxZNreCdd3sRm+ha.zyXY0IRL81SYWuDaSGbAo7Jc4YyQfbPQuvAF5XBuQiA=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="ElpfCEBttwuXeMEshcA2.e4ZI31Q97N5EAzwpc+/hSG.UMLvXWR3dooUPYPaLvehECVCNZpIaami2ylznkRBFe8=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="ElLfLh1FoJej5kJLCi1d.VSu/lwQt0BfHIYFV2IIO3q.eX3RwkxpP60a7VWGhmmlylbXj2IcYgR5yPWNXXQnuzw=")
ki3.loginResult()


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

jgs = cl.getGroupIdsJoined()
print "getGroupIdsJoined success"



helpMessage ="""想控制智乃嘛..

[/help]...查看指令
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
[/botbye]...智乃退出

追加功能:
  1.分享文章時 顯示文章網址
  2.丟友資後 顯示友資詳情
  3.自動關閉網址

智乃作者:戦神[Made In Taiwan]
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
Botss=[kimid,ki2mid,ki3mid]
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
    'message':"ℬᎶ戦神Bot\n邀我進群打 /help 查看指令唷\n作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
    'message1':"ℬᎶ戦神Bot\n作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
    'lang':"JP",
    'comment':"ℬᎶ戦神Bot\n邀我進群打 /help 查看指令唷\n作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
    'commentOn':True,
    'commentBlack':{},
    'clock':True,
    'cName':"智乃",
    'linkprotect':True,
}

d = datetime.datetime.today()


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

        if op.type == 19:
            try:
                if op.param3 in mid:
			jgs.remove(op.param1)
			print "jgs.remove"
		else:
                       pass
            except:
                       pass
        if op.type == 13:
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
                                gCreator = "Error"
                            cl.sendText(op.param1,"[群組名稱]\n" + str(ginfo.name) + "[群組創立者]\n->" + gCreator)
		        except:
			    cl.sendText(op.param1,"OK")
                        jgs.append(op.param1)
			
	          else:
                       pass

        if op.type == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)

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
                        msg.text = "智乃給你文章網址哦(๑ơ ₃ ơ)\n" + msg.contentMetadata["postEndUrl"] + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
                    else:
                        msg.text = "智乃給你文章網址哦(๑ơ ₃ ơ)\n" + msg.contentMetadata["postEndUrl"] + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
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
		
            if msg.text == "智乃指令":
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
		
            elif cmi(msg.text, ["/Allgroup","analyze"]):
                if msg.from_ in admin:
                    All = cl.getGroupIdsJoined()
                    MemIn,MemInv = 0, 0
                    for var in range(0, len(All)):
                        try:
                            Gid = random.choice(All)
                            All.remove(Gid)
                            group = cl.getGroup(Gid)
                            MemIn = (MemIn) + (len(group.members))
                            if group.invitee is not None:
                                MemInv = MemInv + (len(group.invitee))
                            else:
                                pass
                        except:
                            print "e"
                            pass
                    cl.sendText(msg.to, "現在参加しているグループ数: " + str(len(cl.getGroupIdsJoined())) + "\n招待されているグループ数: " + str(len(kongou.getGroupIdsInvited())) + "\n参加中のグループにいるメンバーは総計" + str(MemIn) + "人\n招待中の人数は" + str(MemInv) + "人ﾃﾞｰｽ！")
		
            elif msg.text in ["智乃禮物","愛的禮物"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["/Cancel","/cancel","智乃取消","智乃cancel","智乃Cancel"]:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"姆...智乃取消了 "+ str(len(group.invitee)) + " 個邀請\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"智乃找不到能取消的邀請吶(ノﾟДﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        else:
                            cl.sendText(msg.to,"智乃找不到能取消的邀請吶(ノﾟДﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"智乃找不到能取消的邀請吶(ノﾟДﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"智乃找不到能取消的邀請吶(ノﾟДﾟ)\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["/author","/Author","/作者"]:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
		cl.sendMessage(msg)
		cl.sendText(msg.to,"智乃的創造者是戦神唷><👆\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			

            elif msg.text in ["/Urloff"]:
                if msg.toType == 2:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"智乃幫你關閉網址了≧∇≦\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"姆...網址本來就是關的咩ヽ(｀⌒´)ノ\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			
            elif msg.text in ["/Time","/時刻","/time","/Now","/now"]:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                cl.sendText(msg.to, "智乃報時:" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif msg.text in ["/Url","/url"]:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                gurl = cl.reissueGroupTicket(msg.to)
                cl.sendText(msg.to,"智乃找到的群組網址...\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
            elif cms(msg.text, ["/Groupcreator","/群長","/Gc","/gc","/groupcreator","群長"]):
		if msg.toType == 2:
		 source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		 name = "".join([random.choice(source_str) for x in xrange(9)])
                 ginfo = cl.getGroup(msg.to)
                 try:
                        gCreator = ginfo.creator.displayName
                 except:
                        gCreator = "Error"
		 cl.sendText(msg.to,"[創立群組者]\n->" + gCreator + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		 


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
		
            elif msg.text in ["/bgbye","/BGbye","/Bgbye"]:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    ginfo = cl.getGroup(msg.to)
                    try:
			jgs.remove(msg.to)
                        cl.sendText(msg.to,""  +  str(ginfo.name)  + " 掰掰~\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			cl.leaveGroup(msg.to)
			ki.leaveGroup(msg.to)
			ki2.leaveGroup(msg.to)
			ki3.leaveGroup(msg.to)
                    except:
                        pass
		
            elif msg.text in ["/bgbot","/BGbot","/Bgbot"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
			ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
			try:
                            cl.sendText(op.param1,"TESTOK")
		        except:
			    cl.sendText(op.param1,"TESTOK")
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
		    ki.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		    ki.sendText(op.param1,str(wait["message1"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		

#------------------------------------------------------------------------------------

	if op.type == 11:
	    if op.param2 not in Bots:
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
	    else:
		pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    nowT = datetime.datetime.today().strftime("%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
                profile = cl.getProfile()
                profile.displayName = "TEST001"
                cl.updateProfile(profile)
                time.sleep(6000)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
		profile = ki.getProfile()
		profile.displayName = "TEST002"
		ki.updateProfile(profile)
		time.sleep(6000)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
		profile = ki2.getProfile()
		profile.displayName = "TEST003"
		ki2.updateProfile(profile)
                time.sleep(6000)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


def nameUpdate():
    while True:
        try:
		profile = ki3.getProfile()
		profile.displayName = "TEST004"
		ki3.updateProfile(profile)
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
