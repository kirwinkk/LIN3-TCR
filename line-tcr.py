# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="EkeIbgnKT7pYht2uGX68.iarQyHUgknIRni5Recj+Ea.LLGh4VA86sDoXEZO4LPKEPFcFSTUlmF1kvmk3+KsibA=")
cl.loginResult()


reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""請使用新版免費BOT
取得方式:打[Newbot]

紗霧作者:戦神
http://line.me/ti/p/4-ZKcjagH0
[Made In Taiwan]"""
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
    'message':"ℬᎶ戦神Bot\n\nBot作者:http://line.me/ti/p/4-ZKcjagH0\n\n(Made In Taiwan)",
    'lang':"JP",
    'comment':"ℬᎶ戦神Bot\n\nBot作者:http://line.me/ti/p/4-ZKcjagH0\n\n(Made In Taiwan)",
    'commentOn':True,
    'commentBlack':{},
    'clock':True,
    'cName':"戦神BOT[公開中]",
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
	  try:
            print op.param1
            G = cl.getGroup(op.param1)
            cl.acceptGroupInvitation(op.param1)
	  except:
                pass
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
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
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
            elif msg.contentType == 16:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)

            if msg.text == "gid":
                cl.sendText(msg.to, msg.to)
            if msg.text == "Gid":
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
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
			cl.sendText(msg.to,"嘿嘿...紗霧取消了 "+ str(len(group.invitee)) + " 個邀請")
                        cl.sendText(msg.to,"你說 紗霧有沒有好棒(´∀｀)♡")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"明明沒有邀請 別騙紗霧啦")
                        else:
                            cl.sendText(msg.to,"明明沒有邀請 別騙紗霧啦")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"明明沒有邀請 別騙紗霧啦")
                    else:
                        cl.sendText(msg.to,"明明沒有邀請 別騙紗霧啦")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["author","Author","作者"]:
			cl.sendText(msg.to,"紗霧作者:\nhttp://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]")
			


            elif msg.text in ["Urloff"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"紗霧已關閉網址")
                    else:
                        cl.sendText(msg.to,"紗霧已關閉網址")

		
            elif "Gid" == msg.text:
                cl.sendText(msg.to,msg.to)
		
            elif "Newbot" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {"mid":"ued7764f69b285c64c92f59b685cb0371"}
		cl.sendText(msg.to,"NEW!!公開BOT:")
                cl.sendMessage(msg)

				

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


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
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
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
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
