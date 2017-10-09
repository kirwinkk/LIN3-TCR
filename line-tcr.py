# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="ElpcB4sko1CYXwqzi2Re.WHByzKXoh0n3ljIXSlIvBG.fqmHehYKeU6Lc3WwkwROCCxgPtB/67cBbrBds2jtWFA=")
cl.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

jgs = cl.getGroupIdsJoined()
print "getGroupIdsJoined success"

helpMessage ="""=====[ℬᎶ戦神Bot]=====
--以下指令為基本功能--
[help]   查看指令
[ver]   查看版本以及說明
[Author]   作者顯示
[Mid]   顯示早就mid
[gid]   顯示群組
[Me]   顯示自己友資
--以下指令為設定用--
[contoct on/off]   友資詳情
[join on/off]   自動入群
[clock on/off]   時鐘
[Add on/off]   自動加友
[set]   確認設定
--以下指令為群組使用--
[Ginfo]   顯示群組詳情
[cancel]   取消所有邀請
[Nk:]   名字踢人
[Mk:@]   標註踢人
[Bl:@]   標註黑單
[Ban]   友資黑單
[Unban]   友資解除黑單
[Bl]   查看黑單
[Kill]   踢出黑單
[Cleanse]   踢出所有成員
--以下指令為kicker用--
[BGbot]   追加kicker
[BGbye]   kicker退出
[Test]   查看所有kicker
[Sp]   反應速度
[Url]   取得群組網址
[Urlon]   開啟群組網址
[Urloff]   關閉群組網址
[Show:]   顯示mid友資
[kick:]   踢出mid
[Invite:]   邀請mid
[Gift]   發送禮物
-以下指令為額外功用-
[TL:]   Po文
[Up]   更新時間
[point]   已讀點
[Read]   顯示已讀
[Time]   現在時間
部分指令前打[BG1/2/3]可指定kicker動作
"""
KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14]
kIL=[ki15,ki16]
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
ki12mid = ki12.getProfile().mid
ki13mid = ki13.getProfile().mid
ki14mid = ki14.getProfile().mid
ki15mid = ki15.getProfile().mid
ki16mid = ki16.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid,ki12mid,ki13mid,ki14mid,ki15mid,ki16mid]
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin = "uc216d8664c4e1f43772c98b1b0b8956e"
admin2 = "ubecd98a04cbf74a830b6c95b67bd6b74"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
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
    'cName':"ℬᎶ戦神",
    'cNames':"ℬᎶ戦神追加保護",
    'blacklist':{},
    'wblacklist':False,
    'dblacklist':False,
    'protect':True,
    'Protectguest':True,
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

        if op.type == 19:
		if op.param3 in mid:
			jgs.remove(op.param1)
		        print "jgs.remove19"
		else:
			pass
		
        if op.type == 13:
            if mid in op.param3:
                if op.param1 not in jgs:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
                        ginfo = cl.getGroup(op.param1)
			G.preventJoinByTicket = True
                        cl.updateGroup(G)
		        try:
                            ginfo = cl.getGroup(op.param1)
			    try:
                                gCreator = ginfo.creator.displayName
                            except:
                                gCreator = ginfo.members[0].displayName
                            cl.sendText(op.param1,"你好我是戦神,能愛愛嗎?")
		        except:
			    cl.sendText(op.param1,"你好我是戦神,能愛愛嗎?")
                        jgs.append(op.param1)
			print "jgs.append13"
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
	    try:
              print op.param1
              group = ki15.getGroup(op.param1)
              gInviMids = [contact.mid for contact in group.invitee]
              ki15.cancelGroupInvitation(op.param1, gInviMids)
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
        if op.type == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
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
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"><")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"><")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Bot1invite:" in msg.text:
                midd = msg.text.replace("Bot1invite:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
		

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
                        cl.sendText(msg.to,"已取消邀請")
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

            elif msg.text in ["author","Author","作者"]:
			msg.contentType = 13
                        msg.contentMetadata = {'mid': admsa}
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
                    gurl = cl.reissueGroupTicket(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                    else:
                        cl.sendText(msg.to,"line://ti/g/" + gurl)

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
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
 
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])


			

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
		

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
			pass


#-----------------------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "BG戦神Bot讀取中...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
		

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
                           klist=[cl]
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
            elif msg.text in ["tagall"]:

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

				
            elif msg.text in ["Tagall"]:

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
				
            elif msg.text in ["/bye","/Bye","戰神退出"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"確定要退出嗎?\n[y/n]")
                    if msg.text in ["Y","y"]:
                      try:
			jgs.remove(msg.to)
			print "jgs.remove"
                        cl.sendText(msg.to,""  +  str(ginfo.name)  + " 掰掰~\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
			cl.leaveGroup(msg.to)
                      except:
                        pass
                    if msg.text in ["N","n"]:
				cl.sendText(msg.to,"改變主意瞜?\nXDD")
		    else:
			pass
#-----------------------------------------------------------
            elif "#BOT登出" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

#-----------------------------------------------------------
            elif "Test" in msg.text:
                profile = cl.getProfile()
                text = profile.displayName + " 正常運作中"
                cl.sendText(msg.to, text)


#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Bl","BL","bl"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"沒有黑名單")
                else:
                    cl.sendText(msg.to,"黑名單用戶讀取中...")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"黑名單用戶:\n\n" + mc)
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
                            klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
                            pass



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


def a2():
    now2 = datetime.datetime.now()
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
                nowT = datetime.datetime.today().strftime(now2,"%H:%M")
                profile = cl.getProfile()
                profile.displayName = "戦神☆ " + nowT
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
