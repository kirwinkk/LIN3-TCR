# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="Ekz4TgKpeSWkDvNsetY0.3FLXqaAHaqU2vr+bb+uJKa.5/52TwKOUdn8x2wWxkc2sBYihCNVQVO0/L+nx6GKNao=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EkFxBRmXkbP3J3mAZPM3.vy5yDd4vkH13GPwq582miW.yquPVYw1Q9FjnJjTEECpQ3AU0xiNsriNsUFWw0B2TVA=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EkBFUH2KRvooCziIe3K9.sZWYkriJsJf80xBKZDkbsq.kadwbKtdlV2Sv/yfxtAmdFHm3k0ymvMd68ZT98tM5Z0=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EkeIbgnKT7pYht2uGX68.iarQyHUgknIRni5Recj+Ea.LLGh4VA86sDoXEZO4LPKEPFcFSTUlmF1kvmk3+KsibA=")
ki3.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""=====[ℬᎶ戦神Bot]=====
--以下指令為基本功能--
[Help]   查看指令
[Author]   作者顯示
[Mid]   顯示自己mid
[Gid]   顯示群組
[Me]   顯示自己友資
--以下指令為群組使用--
[Ginfo]   顯示群組詳情
[Cancel]   取消所有邀請
[Mid:@]   差看被標註者的mid
[Nk:]   名字踢人(空白為全踢)
[Mk:@]   標註踢人
[Bl:@]   標註黑單
[Ubl:@]   標註解除黑單
[Ban]   友資黑單
[Unban]   友資解除黑單
[Bl]   查看總黑單
[Banlist]   查看本群黑單
[Kill]   踢出黑單
[Owner]   查看權限名單
--以下指令為kicker用--
[BGbot]   追加kicker
[BGbye]   kicker退出
[Test]   查看所有kicker
[Url]   取得群組網址
[Urlon]   開啟群組網址
[Urloff]   關閉群組網址
[mid:]   顯示mid友資
[kick:]   踢出mid
[Invite:]   邀請mid
[Gift]   發送禮物
[set]   確認設定
--以下指令為作者用--
[Protecton/off]   禁止踢人
[Urlprotecton/off]   禁止開關網址
[Inviteprotecton/off]   禁止邀請
[Cancelprotecton/off]   禁止取消邀請
[Ownera:@]   提升標註者權限
[Ownerd:@]   刪除標註者權限
[Sp]   反應速度
[Groupid]   查看所有群組
[BGbyeall]   退出所有群組


作者:http://line.me/ti/p/4-ZKcjagH0
(Made In Taiwan)
"""
KAC=[cl,ki,ki2,ki3]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid]
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
    'wblack':False,
    'dblack':False,
    'clock':True,
    'cName':"戦神BOT[公開中]",
    'blacklist':{},
    'wblacklist':False,
    'dblacklist':False,
    'protect':True,
    'cancelprotect':False,
    'inviteprotect':False,
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
                        try:
                            cl.acceptGroupInvitation(op.param1)
			    try:
			       G = cl.getGroup(msg.to)
                               ginfo = cl.getGroup(msg.to)
                               G.preventJoinByTicket = False
                               cl.updateGroup(G)
                               invsend = 0
                               Ticket = cl.reissueGroupTicket(msg.to)
                               ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                               ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                               ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                               G = ki.getGroup(msg.to)
                               ginfo = ki.getGroup(msg.to)
                               G.preventJoinByTicket = True
                               ki.updateGroup(G)
                               print "kicker ok"
                               G.preventJoinByTicket(G)
                               ki.updateGroup(G)
			    except:
				pass

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
                  if msg.from_ in staff:
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
              if msg.from_ in staff:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "ℬᎶ戦神Bot-文章網址 URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "ℬᎶ戦神Bot-文章網址 URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
              if msg.from_ in staff:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif ("Gn:" in msg.text):
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"><")
            elif ("Gn " in msg.text):
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"><")
            if msg.text == "gid":
              if msg.from_ in staff:
                cl.sendText(msg.to, msg.to)
            if msg.text == "Gid":
              if msg.from_ in staff:
                cl.sendText(msg.to, msg.to)
            elif "Kick:" in msg.text:
              if msg.from_ in staff:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
              if msg.from_ in staff:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Gift","i gift"]:
              if msg.from_ in staff:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
		ki.sendMessage(msg)
		ki2.sendMessage(msg)
		ki3.sendMessage(msg)
		
            elif msg.text in ["Protect on","Protecton"]:
              if msg.from_ in admin:
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
              if msg.from_ in admin:
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
              if msg.from_ in admin:
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
              if msg.from_ in admin:
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

            elif msg.text in ["Protectoff"]:
              if msg.from_ in admin:
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
              if msg.from_ in admin:
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
              if msg.from_ in admin:
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
              if msg.from_ in admin:
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
			
            elif msg.text.lower() == 'set':
              if msg.from_ in staff:
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


            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"戦神已取消邀請")
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
		if msg.from_ in staff:
			msg.contentType = 13
                        msg.contentMetadata = {'mid': admsa}
			cl.sendText(msg.to,"此機器作者↓")
                        cl.sendMessage(msg)
			
            elif msg.text in ["Groupid","所有群組","Allgid"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
		
            elif msg.text in ["Urlon"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        sendText(msg.to,"已開啟網址")
                    else:
                        kk.sendText(msg.to,"網址為開啟狀態")

            elif msg.text in ["Urloff"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"已關閉網址")
                    else:
                        cl.sendText(msg.to,"網址為關閉狀態")

            elif msg.text == "Ginfo":
              if msg.from_ in staff:
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
            elif "Mid" == msg.text:
              if msg.from_ in staff:
                cl.sendText(msg.to,msg.contentMetadata["mid"])

            elif "TL:" in msg.text:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])


            elif "Oa:@" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Oa:@","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"找不到此用戶><")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"已提升權限")
                            except:
                                pass

            elif "Ownera:@" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Ownera:@","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"找不到此用戶><")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"已提升權限")
                            except:
                                pass

            elif "Ownerd:@" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Ownerd:@","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"找不到此用戶><")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"已刪除權限")
                            except:
                                pass

            elif "Od:@" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Od:@","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"找不到此用戶><")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"已刪除權限")
                            except:
                                pass

            elif msg.text in ["owner","Owner"]:
              if msg.from_ in staff:
                if staff == []:
                    cl.sendText(msg.to,"沒有權限者")
                else:
                    cl.sendText(msg.to,"權限名單讀取中...")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#--------------------------------------------------------
            elif "mid:" in msg.text:
              if msg.from_ in staff:
                mmid = msg.text.replace("mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif msg.text.lower() == 'me':
              if msg.from_ in staff:
                msg.contentType = 13
		contact = cl.getContact(msg.contentMetadata["mid"])
                msg.contentMetadata = {"mid":contact}
                cl.sendMessage(msg)


            elif "BGbyeall" in msg.text:
              if msg.from_ in admin:
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

            elif msg.text in ["url","Url"]:
              if msg.from_ in staff:
                    sendMessage(msg.to,"此群網址URL")
                    sendMessage(msg.to,"line://ti/g/" + cl.reissueGroupTicket(msg.to))
		
		
            elif "BGbot" in msg.text:
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
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
			
            elif "BGbye" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,""  +  str(ginfo.name)  + " 掰掰~")
			cl.leaveGroup(msg.to)
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                    except:
                        pass

#-----------------------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
              if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "BG戦神Bot讀取中...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))

		

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
                           cl.sendText(msg.to,"Error")
            elif ("Mid:" in msg.text):
              if msg.from_ in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"" +  key1)
				

				
            elif "Nk:" in msg.text:
              if msg.from_ in staff:
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
                                klist=[cl,ki,ki2,ki3]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"錯誤!!!!!!!!")
				
#-----------------------------------------------------------

#-----------------------------------------------------------
            elif "Bl:@" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Bl:@","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"沒有找到用戶")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"已黑單此用戶")
                            except:
                                cl.sendText(msg.to,"此用戶已是黑單")
            elif "Ubl:@" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Ubl:@","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"沒有找到用戶")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"已解除黑單")
                            except:
                                cl.sendText(msg.to,"此用戶並不是黑單")
				

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
              if msg.from_ in staff:
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
            elif "Mban:" in msg.text:
              if msg.from_ in staff:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
            elif "Munban:" in msg.text:
              if msg.from_ in staff:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = False
		cl.sendText(msg.to,"Target unLock")
#-----------------------------------------------------------

#-----------------------------------------------------------

#-----------------------------------------------------------
            elif "Test" in msg.text:
              if msg.from_ in staff:
		profile = cl.getProfile()
                text = profile.displayName + ""
                cl.sendText(msg.to, text)
                profile = ki.getProfile()
                text = profile.displayName + ""
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + ""
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + ""
                ki3.sendText(msg.to, text)

#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
              if msg.from_ in staff:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"請傳送友資黑單")
            elif msg.text in ["Unban"]:
              if msg.from_ in staff:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"請傳送友資解除黑單")

            elif msg.text in ["Bl"]:
              if msg.from_ in staff:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"目前尚無黑單")
                else:
                    cl.sendText(msg.to,"黑名單正在讀取...")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "-»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif "Banlist" in msg.text:
              if msg.from_ in staff:
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
              if msg.from_ in staff:
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
                            klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
                            pass
            elif "cancel" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
			cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"已取消邀請")

#-----------------------------------------------
            elif "Say:" in msg.text:
              if msg.from_ in staff:
				bctxt = msg.text.replace("Say:","")
                                cl.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                if op.param3 in kimid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
			ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
			wait["blacklist"][op.param2] = True


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
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
			ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
			wait["blacklist"][op.param2] = True
                        
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
                        cl.updateGroup(G)
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
                        cl.updateGroup(G)
			wait["blacklist"][op.param2] = True
                        

            except:
                pass

	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    ki3.cancelGroupInvitation(op.param1,[op.param3])
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    G = ki2.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki2.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
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
