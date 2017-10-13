# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="ElpcB4sko1CYXwqzi2Re.WHByzKXoh0n3ljIXSlIvBG.fqmHehYKeU6Lc3WwkwROCCxgPtB/67cBbrBds2jtWFA=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EkyeKl3OcvOKJE3uZeV4.7RWlONtZ1Buiu1pRYoIM5a.xS4I9MgobgkkvFk2rmCNlcfyPMmkYy0wjAOESdjZqbI=")
ki.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
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
    'message':"",
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


        if op.type == 25:
            msg = op.message

            if msg.text is None:
                return



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
				
            elif ("Mmk:" in msg.text):
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
				
				

				
            elif "Mnk:" in msg.text:
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
				
            elif msg.text in ["BG保護8","BGbot追加","防翻追加"]:
                        cl.acceptGroupInvitation(msg.to)
			G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
			G.preventJoinByTicket = False
                        cl.updateGroup(G)
			invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
			G.preventJoinByTicket = True
                        ki.updateGroup(G)
		        try:
                            ginfo = cl.getGroup(msg.to)
			    try:
                                gCreator = ginfo.creator.displayName
                            except:
                                gCreator = ginfo.members[0].displayName
                            cl.sendText(msg.to,"戦神公開保護V.8\n\n[禁止事項]:\n\n$[不會]被黑單[不會]被踢:\n1.禁止開啟網址\n\n$[不會]被黑單[會]被踢:\n1.禁止邀請黑單用戶\n2.禁止踢任何群內成員\n\n$[會]被黑單[會]被踢\n1.踢出機器\n\n#注意:黑單無法解除!\n\n戦神Bot作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0")
		        except:
			    cl.sendText(msg.to,"戦神公開保護V.8\n\n[禁止事項]:\n\n$[不會]被黑單[不會]被踢:\n1.禁止開啟網址\n\n$[不會]被黑單[會]被踢:\n1.禁止邀請黑單用戶\n2.禁止踢任何群內成員\n\n$[會]被黑單[會]被踢\n1.踢出機器\n\n#注意:黑單無法解除!\n\n戦神Bot作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0")

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




#-----------------------------------------------
		
	
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
