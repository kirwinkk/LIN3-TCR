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
ki3.login(token="EkeIbgnKT7pYht2uGX68.iarQyHUgknIRni5Recj+Ea.LLGh4VA86sDoXEZO4LPKEPFcFSTUlmF1kvmk3+KsibA=")
ki3.loginResult()

ki16 = LINETCR.LINE()
ki16.login(token="ElbkOgQKx1hXMr5roFy4.bOTjwJ4IY6/M4ng+aUJmLa.dN4xvFyXKKAODlTFhQanytJlGRBvQaUNYcNbTaua3Lo=")
ki16.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

jgs = cl.getGroupIdsJoined()

helpMessage ="""=====[ℬᎶ戦神無料Bot]=====
--以下指令為基本功能--
[help]   查看指令
[ver]   查看版本以及說明
[Author]   作者顯示
[Mid]   顯示早就mid
[gid]   顯示群組
[Me]   顯示自己友資
--以下指令為設定用--
[Contocton/off]   友資詳情
[Autojoinon/off]   自動入群
[Autoleaveon/off]   自動離開副本
[Protecton/off]   禁止踢人,改群圖群名
[Urlprotecton/off]   網址保護
[Inviteprotecton/off]   禁止邀人
[Cancelprotecton/off]   禁止取消邀請
[set]   確認設定
[封鎖名單]   確認已封鎖用戶
--以下指令為群組使用--
[Ginfo]   顯示群組詳情
[cancel]   取消所有邀請
[Nk:]   名字踢人
[Mk:@]   標註踢人
[Bl:@]   標註黑單
[Ban]   友資黑單
[Unban]   友資解除黑單
[Mban:]   mid黑單
[Munban:]   mid解除黑單
[Bl]   查看黑單
[Banlist]   查看此群黑單
[Kill]   踢出黑單
[Cleanse]   踢出所有成員
--以下指令為kicker用--
[BGbot]   追加kicker
[死神]   追加死神
[BGbye]   kicker退出
[死神bye]   死神退出
[Test]   查看所有kicker
[Sp]   反應速度
[Url]   取得群組網址
[Urlon]   開啟群組網址
[Urloff]   關閉群組網址
[Show:]   顯示mid友資
[kick:]   踢出mid
[Invite:]   邀請mid
[Gift]   發送禮物
[Say:]   Kicker講話
-以下指令為額外功用-
[TL:]   Po文
[Time]   現在時間
部分指令前打[BG1/2/3]可指定kicker動作

作者:戦神
http://line.me/ti/p/4-ZKcjagH0
[Made In Taiwan]
"""
KAC=[cl,ki,ki2,ki3]
kIL=[ki16]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki16mid = ki16.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki16mid]
admsa = "u874fef535f73052006360261c26ea3f5"
admin = "u874fef535f73052006360261c26ea3f5"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"戦神代行SelfBOT\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
    'lang':"JP",
    'comment':"戦神代行SelfBOT\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
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
                            cl.sendText(op.param1,"[群組名稱]\n" + str(ginfo.name) + "\n\n[此群首位入群者]\n->" + gCreator)
		        except:
			    cl.sendText(op.param1,"OK")
                        jgs.append(op.param1)
			print "jgs.append"
			
	          else:
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
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"成功")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"成功")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"成功")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"成功")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"成功")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"成功")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"成功")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"成功")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"ℬᎶ戦神Bot-友資詳情\n[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個性簽名]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"ℬᎶ戦神Bot-友資詳情\n[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個性簽名]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "文章網址 URL\n" + msg.contentMetadata["postEndUrl"]
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
                    ki.updateGroup(group)
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
                cl.sendText(msg.to, "報時:" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S'))
		
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
                
            elif msg.text in ["BG1gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","i gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["BG2gift","Bot2gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["BG3gift","Bot3gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
           
            
            elif msg.text in ["BG1cancel","BG2cancel","BG3cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
			ki.sendText(msg.to,"取消了 "+ str(len(group.invitee)) + " 個邀請\n(´∀｀)♡")
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

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"取消了 "+ str(len(group.invitee)) + " 個邀請\n(´∀｀)♡")
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
                        msg.contentMetadata = {"mid":"ued7764f69b285c64c92f59b685cb0371"}
			cl.sendText(msg.to,"此機器作者↓")
                        cl.sendMessage(msg)
			
            elif msg.text in ["Groupid","所有群組","Allgid"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
		
            elif msg.text in ["Urlon"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        sendText(msg.to,"已開啟網址")
                    else:
                        kk.sendText(msg.to,"網址為開啟狀態")

            elif msg.text in ["Urloff"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉網址")
                    else:
                        cl.sendText(msg.to,"網址為關閉狀態")

            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    print "SUKSES -- SEND GINFO"
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "不存在"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"ℬᎶ戦神Bot-群組詳情\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中")
                    else:
                        cl.sendText(msg.to,"ℬᎶ戦神Bot-群組詳情\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"請在群中使用此功能")
                    else:
                        cl.sendText(msg.to,"請在群中使用此功能")
                cl.sendTextc
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
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])


#--------------------------------------------------------
            elif "mid:" in msg.text:
                mmid = msg.text.replace("mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Contacton':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OK")
                    else:
                        cl.sendText(msg.to,"OK")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OK")
                    else:
                        cl.sendText(msg.to,"OK")
            elif msg.text.lower() == 'Contactoff':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OK")
                    else:
                        cl.sendText(msg.to,"OK")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OK")
                    else:
                        cl.sendText(msg.to,"OK")
            elif msg.text in ["Protect on","Protecton"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"保護開啟")
                    else:
                        cl.sendText(msg.to,"保護開啟")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"保護開啟")
                    else:
                        cl.sendText(msg.to,"保護開啟")
            elif msg.text in ["Urlprotecton","Urlprotect on"]:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"網址保護開啟")
                    else:
                        cl.sendText(msg.to,"網址保護開啟")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"網址保護開啟")
                    else:
                        cl.sendText(msg.to,"網址保護開啟")
            elif msg.text in ["Inviteprotecton","Inviteprotect on"]:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"招待保護開啟")
                    else:
                        cl.sendText(msg.to,"招待保護開啟")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"招待保護開啟")
                    else:
                        cl.sendText(msg.to,"招待保護開啟")
            elif msg.text in ["Cancelprotecton","Cancelprotect on"]:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"取消保護開啟")
                    else:
                        cl.sendText(msg.to,"取消保護開啟")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"取消保護開啟")
                    else:
                        cl.sendText(msg.to,"取消保護開啟")
            elif msg.text in ["Autojoinon","autojoinon"]:
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
            elif msg.text.lower() == 'Autojoinoff':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Protectoff"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"保護關閉")
                    else:
                        cl.sendText(msg.to,"保護關閉")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"保護關閉")
                    else:
                        cl.sendText(msg.to,"保護關閉")
            elif msg.text in ["Urlprotectoff","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"網址保護關閉")
                    else:
                        cl.sendText(msg.to,"網址保護關閉")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"網址保護關閉")
                    else:
                        cl.sendText(msg.to,"網址保護關閉")
            elif msg.text in ["Inviteprotectoff"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"招待保護關閉")
                    else:
                        cl.sendText(msg.to,"招待保護關閉")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"招待保護關閉")
                    else:
                        cl.sendText(msg.to,"招待保護關閉")
            elif msg.text in ["Cancelprotectoff"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"取消保護關閉")
                    else:
                        cl.sendText(msg.to,"取消保護關閉")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"取消保護關閉")
                    else:
                        cl.sendText(msg.to,"取消保護關閉")

            elif msg.text in ["Autoleaveon","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OK")
                    else:
                        cl.sendText(msg.to,"OK")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OK")
                    else:
                        cl.sendText(msg.to,"OK")
            elif msg.text in ["Autoleaveoff","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OK")
                    else:
                        cl.sendText(msg.to,"OK")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OK")
                    else:
                        cl.sendText(msg.to,"OK")

            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+="友資情報:開啟\n"
                else: md+="友資情報:關閉\n"
                if wait["autoJoin"] == True: md+="自動入群:開啟\n"
                else: md +="自動入群:關閉\n"
                if wait["autoCancel"]["on"] == True:md+="自動取消:" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "自動取消:關閉\n"
                if wait["leaveRoom"] == True: md+="自動離開副本:開啟\n"
                else: md+="自動離開副本:關閉\n"
                if wait["timeline"] == True: md+="文章URL:開啟\n"
                else:md+="文章URL:關閉\n"
                if wait["autoAdd"] == True: md+="自動加好友:開啟\n"
                else:md+="自動加好友:關閉\n"
                if wait["commentOn"] == True: md+="自動留言:開啟\n"
                else:md+="自動留言:關閉\n"
                if wait["protect"] == True: md+="保護:開啟\n"
                else:md+="保護:關閉\n"
                if wait["linkprotect"] == True: md+="網址保護:開啟\n"
                else:md+="網址保護:關閉\n"
                if wait["inviteprotect"] == True: md+="招待保護:開啟\n"
                else:md+="招待保護:關閉\n"
                if wait["cancelprotect"] == True: md+="取消保護:開啟"
                else:md+="取消保護:關閉"
                cl.sendText(msg.to,md)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif "BGbyeall" in msg.text:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"已退出所有群組")
                else:
                    cl.sendText(msg.to,"已退出所有群組")

		
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"已黑單此用戶")
            elif "Munban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = False
		cl.sendText(msg.to,"已解除黑單")
		
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"0.0")
                    else:
                        cl.sendText(msg.to,"0.0")

            elif msg.text in ["Bl"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"沒人在黑單中0.0")
                else:
                    cl.sendText(msg.to,"黑單讀取中...")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "-»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

#-----------------------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "BG戦神Bot讀取中...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
		


            elif ("Mid:" in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"" +  key1)
				
            elif ("Mk:" in msg.text):
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
                           cl.sendText(msg.to,"Error")
				
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
                                klist=[ki,ki2,ki3]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"錯誤!!!!!!!!")
				
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
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

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
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")
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
            elif "Kill" in msg.text:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"0.0")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,ki2,ki3]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
                            pass


#-----------------------------------------------

#-----------------------------------------------
                       
#-----------------------------------------------
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
#-----------------------------------------------
#-----------------------------------------------
            elif "Bot2" in msg.text:
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
            elif "Bot3" in msg.text:
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
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------

#-----------------------------------------------
            elif msg.text in ["死神","死神bot"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
			ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki16.sendText(msg.to,"[" + str(ginfo.name) + "]\n死神参加成功!")
                        G = cl.getGroup(msg.to)
                        ginfo = ki16.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki16.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki16.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["/bgbye","/BGbye","/Bgbye"]:
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
		
#-----------------------------------------------
            elif msg.text in ["死神退出","死神bye"]:
                if msg.toType == 2:
                    ginfo = ki16.getGroup(msg.to)
                    try:
			ki16.sendText(msg.to,"死神退出")
                        ki16.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------

#-----------------------------------------------
            elif "Say:" in msg.text:
				bctxt = msg.text.replace("Say:","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
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
                        ki3.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                if op.param3 in kimid:
                    if op.param2 in mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)

                            
                        
                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])
			ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])
			ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])
			ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
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
                        

			
                elif op.param3 in ki16mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
			ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if op.param2 in admin + Bots:
		   try:
			random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
			G = ki16.getGroup(op.param1)
			G.preventJoinByTicket = True
			ki16.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
			    G = ki16.getGroup(op.param1)
			    G.preventJoinByTicket = True
			    ki16.updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    ki16.kickoutFromGroup(op.param1,[op.param2])
		else:
		    ki16.sendText(op.param1,"")
	    else:
		ki16.sendText(op.param1,"別在死神面前做壞事^^")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
                    ki16.kickoutFromGroup(op.param1,[op.param2])
		else:
		    ki16.sendText(op.param1,"別在死神面前做壞事^^")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    ki16.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    ki16.sendText(op.param1,"別在死神面前做壞事^^")
	    else:
		ki16.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    ki16.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    ki16.sendText(op.param1,"別在死神面前做壞事^^")
	    else:
		ki16.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    G = ki2.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki2.updateGroup(G)
		    ki16.kickoutFromGroup(op.param1,[op.param2])
		else:
		    ki16.sendText(op.param1,"別在死神面前做壞事^^")
	    else:
		ki16.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    ki.sendText(op.param1,str(wait["message"]))
                    ki2.sendText(op.param1,str(wait["message"]))
                    ki3.sendText(op.param1,str(wait["message"]))
                    ki16.sendText(op.param1,str(wait["message"]))
		
        if op.type == 19:
            try:
                if op.param3 in mid:
			jgs.remove(op.param1)
			print "jgs.remove"
		else:
                       pass
            except:
                       pass


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
	    if wait["clock"] == True:
                profile = ki16.getProfile()
                profile.displayName = "๑死神๑"
                ki16.updateProfile(profile)
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
