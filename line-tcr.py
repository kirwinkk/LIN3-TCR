# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="Elwqog7uvMTEiGRQER69.aLZN+GwDwgQS69XUBHE2Aq.w8FhrJeMLp0AbvHMIzIF2FTMfA9nbPP0gEfcDo19k+U=")
cl.loginResult()


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""想控制智乃嘛..

[help]...查看指令
[Author]...作者顯示
[gid]...顯示群組gid
[Ginfo]...顯示群組詳情
[Cancel]...取消所有邀請
[Urloff]...關閉群組網址
[Mid:@]...顯示被標註者的mid
[mid:]...顯示mid的友資
[Gift]...發送禮物
[Time]...現在時間
[Gc]...查看群長
[/botbye]...智乃退出

追加功能:
  1.分享文章時 顯示文章網址
  2.丟友資後 顯示友資詳情
  3.自動關閉網址

智乃作者:戦神[Made In Taiwan]
http://line.me/ti/p/4-ZKcjagH0
"""
KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
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
    'message':"智奶的創造者是戦神唷><\n邀我進群打  /help  查看ㄉ查看指令唷\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
    'lang':"JP",
    'comment':"智奶的創造者是戦神唷><\n邀我進群打  v  查看ㄉ查看指令唷\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
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


def ACCEPT_GROUP_INVITATION(op):
	try:
            cl.sendText(op.param1,"ss")
	except:
                pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
	  try:
            print op.param1
            G = cl.getGroup(op.param1)
            cl.acceptGroupInvitation(op.param1)
          except:
                pass

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                    msg.contentType = 0
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu)) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu)) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name
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
            if msg.text == "help":
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
            if msg.text == "Help":
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    cl.sendText(msg.to,helpMessage + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
            if msg.text == "/Help":
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

            if msg.text == "gid":
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                cl.sendText(msg.to, msg.to)
            if msg.text == "Gid":
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                cl.sendText(msg.to, msg.to)

            elif msg.text in ["Gift","i gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["Cancel","cancel"]:
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
            elif msg.text in ["author","Author","作者"]:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
		cl.sendMessage(msg)
		cl.sendText(msg.to,"智奶的創造者是戦神唷><👆\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			

            elif msg.text in ["Urloff"]:
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
			
            elif msg.text in ["Time","時刻","time","Now","now"]:
		source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		name = "".join([random.choice(source_str) for x in xrange(9)])
                cl.sendText(msg.to, "智乃報時:" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		
		
            elif cms(msg.text, ["Groupcreator","群長","Gc","gc","groupcreator"]):
		if msg.toType == 2:
		 source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		 name = "".join([random.choice(source_str) for x in xrange(9)])
                 ginfo = cl.getGroup(msg.to)
                 try:
                        gCreator = ginfo.creator.displayName
                 except:
                        gCreator = "Error"
		 cl.sendText(msg.to,"[創立群組者]\n->" + gCreator + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
		


            elif msg.text == "Ginfo":
		if msg.toType == 2:
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
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"請在群中使用此功能\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"請在群中使用此功能\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                cl.sendTextc
                cl.sendText(msg)
		
            elif "Gid" == msg.text:
                cl.sendText(msg.to,msg.to)
		
            elif msg.text in ["/botbye","/Botbye"]:
                if msg.toType == 2:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,""  +  str(ginfo.name)  + " 掰掰~\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
		
#--------------------------------------------------------
            elif "mid:" in msg.text:
                mmid = msg.text.replace("mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

#-----------------------------------------------------------

		
            elif ("Mid:" in msg.text):
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
        #while a2():
            #pass
            if wait["clock"] == True:
                nowT = datetime.datetime.today().strftime("☆%H:%M☆")
                profile = cl.getProfile()
                profile.displayName = "智乃" + nowT
                cl.updateProfile(profile)
            time.sleep(60)
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
