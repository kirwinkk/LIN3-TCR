# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""[戦神無料代行]

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

作者:戦神
http://line.me/ti/p/4-ZKcjagH0
[Made In Taiwan]"""
KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
admsa = "u28d781fa3ba9783fd5144390352b0c24"
admin = "u28d781fa3ba9783fd5144390352b0c24"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
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
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            try:
                               cl.sendText(op.param1,"戦神代行SelfBOT[自動入群]\n作者:戦神\nhttp://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]")
                            except:
			       pass
                    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"戦神代行SelfBOT[自動入群]\n作者:戦神\nhttp://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]")
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
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
                    cl.kickoutFromGroup(op.param1, matched_list)
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
            if msg.contentType == 13:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
			if msg.contentMetadata["mid"] in wait["blacklist"]:
                             cl.sendText(msg.to,"[戦神SelfBOT代行]\n" + msg.contentMetadata["mid"])
                        else:
			     cl.sendText(msg.to,"[戦神SelfBOT代行]\n" + msg.contentMetadata["mid"])
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "[戦神SelfBOT代行]\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "[戦神SelfBOT代行]\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
		

        if op.type == 25:
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
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個性簽名]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[名字]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個性簽名]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "[戦神SelfBOT代行]\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "[戦神SelfBOT代行]\n" + msg.contentMetadata["postEndUrl"]
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
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    cl.updateGroup(group)
		    cl.sendText(msg.to,"群名:" + group.name)
		
            if msg.text == "gid":
                cl.sendText(msg.to, msg.to)
		
            if msg.text == "Gid":
                cl.sendText(msg.to, msg.to)
		
            elif msg.text in ["mid","Mid"]:
                cl.sendText(msg.to,msg.from_)


            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
		
            elif msg.text in ["Time","時刻","time","Now","now"]:
                cl.sendText(msg.to, "報時:" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S'))



            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)



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
                cl.sendText(msg.to,"[戦神SelfBOT代行]\n" + h)
		
            elif msg.text in ["Urlon","urlon"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
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
                        cl.sendText(msg.to,"網址為關閉狀態")

            elif msg.text in ["Ginfo","ginfo"]:
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
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    else:
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
                    cl.sendText(msg)

            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"[戦神SelfBOT代行]\nline://home/post?userMid=" + mid + "&postId=" + cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])


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
                cl.sendText(msg.to,"[戦神SelfBOT代行]\n" + msgs)

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
		
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    g.preventJoinByTicket = False
                    cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"0.0")
                    else:
                        cl.sendText(msg.to,"0.0")

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
                           cl.kickoutFromGroup(msg.to,[target])
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
                                cl.kickoutFromGroup(msg.to,[target])
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
                           cl.sendText(msg.to,"找不到用戶")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"已黑單此用戶")
                                except:
                                    cl.sendText(msg.to,"此用戶並不是黑單")

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
                           cl.sendText(msg.to,"找不到用戶")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"已解除黑單")
                                except:
                                    cl.sendText(msg.to,"此用戶並不是黑單")
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
                            klist=[cl]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
                            cl.sendText(msg.to,"因所踢規制無法踢人")


#-----------------------------------------------

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
#-----------------------------------------------

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




while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
