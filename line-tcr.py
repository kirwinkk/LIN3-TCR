# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob


cl = LINETCR.LINE()
cl.login(token="EnVFVST0YE4ULQeViJs3.2XannlnZppIccyjdoNFtaW.soaW4CPYf1dRxNSRQHncCbJd6Olm+XUJJx5/xkpvCtc=")
cl.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
admin = [mid,"ua821dbd83afa9b0d6bfa059b76567226","ua1d924caa58666ee73d0625ca036a1b1","u8dc2983d2e3183303bc466f3283d44d8","uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","u40c17f320e101b9f1abc9edaace6ed51","uef3dc2c514c550e1935b5b679dac38f6","u7a1c4338e6342bbbc33d9fa3c295b7d4","uad3b11a07372a5955ba75dc1caadeed8","u4ab4047d824385456811a2fe93c95382","u40c17f320e101b9f1abc9edaace6ed51","u8a627a2ff2ed54bcdd6c3b52f2b9691b","u96fd5925ecab120ea325511f4b53db11","ua0c6c9175efd94a9551338c72d6a7d17","u3d860a1bb50f8a536653b4940aa41bbf","u8be7a9504b9185ba75234f2f8110697b"]
staff = []
staff2 = []
staff3 = []
staff4 = []
staff5 = []
staff6 = ["uc216d8664c4e1f43772c98b1b0b8956e","ua821dbd83afa9b0d6bfa059b76567226","ubecd98a04cbf74a830b6c95b67bd6b74","u8dc2983d2e3183303bc466f3283d44d8","ua1d924caa58666ee73d0625ca036a1b1"]
bgbot = []
admsa = "uc216d8664c4e1f43772c98b1b0b8956e"
admin2 = "ubecd98a04cbf74a830b6c95b67bd6b74"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'likeOn':True,
    'commentOn':True,
    'message':"戦神Bot作者:戦神 Made In Taiwan\nhttps://line.me/R/ti/p/%40cld3625n",
    'message1':"戦神Bot作者:戦神 Made In Taiwan\nhttps://line.me/R/ti/p/%40cld3625n",
    'lang':"JP",
    'pname':{},
    'pro_name':{},  
    'linkprotect':True,
    'blacklist':{},
    'wblacklist':False,
    'dblacklist':False,
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
           if mid in op.param3:
                        cl.acceptGroupInvitation(op.param1)
		        try:
				group = cl.getGroup(op.param1)
				c = Message(to=op.param1, from_=None, text=None, contentType=13)
                	        c.contentMetadata={'mid':"u85a9b62af4ce6248cfe05324e474e226"}
				if group.invitee is not None:
                        		gInviMids = [contact.mid for contact in group.invitee]
                        		cl.cancelGroupInvitation(op.param1, gInviMids)
					a1, a2, a3, a4, a5, a6, a7, b1, b2, b3, b4, b5 = "ヾ(*´∀｀*)ﾉ", "σ(o'ω'o)", "p(^-^q)", "ψ(｀∇´)ψ", "(#ﾟДﾟ)","(´▽｀)", "p(^-^q)", "ヾ(*´∀｀*)ﾉ", "σ(o'ω'o)", "p(^-^q)", "ψ(｀∇´)ψ", "(´▽｀)"
                			omikujilist = [a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5]
					try:
						cl.sendMessage(c)
						cl.sendText(op.param1,"BOT作者:戦神↑\n" + str(len(group.invitee)) + " Done " + random.choice(omikujilist) + "")
					except:
						cl.sendMessage(c)
                        			cl.sendText(op.param1,"BOT作者:戦神↑\n" + str(len(group.invitee)) + " Done ヾ(*´∀｀*)ﾉ")
                    		else:
					a1, a2, a3, a4, a5, a6, a7, b1, b2, b3, b4, b5 = "(*｀＾´)=3", "(`皿´)", "(o｀з’*)", "ヽ(｀Д´)ﾉ", "Σ(´д｀;)","(*'A^q)", "(*´>д<)", "(>_<)", "σ(oдolll)", "( #｀Д´)", "(｀А´)", "(#ﾟДﾟ)"
                			omikujilist = [a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5]
					cl.sendMessage(c)
                        		cl.sendText(op.param1,"BOT作者:戦神↑\nNo invite " + random.choice(omikujilist) + "")
				
				
		        except:
			    pass
			cl.leaveGroup(op.param1)

           else:
		pass

#------------------------------------------------------------------------------------

        if op.type == 5:
		cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    cl.sendText(op.param1,str(wait["message"]) + "\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name + "]")

        if op.type == 59:
            print op


    except Exception as error:
        print error



def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
			try:
                                cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],"台湾戦神☆style" + "\n\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))
			except:
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],"台湾戦神☆style")
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()



def nameUpdate():
    while True:
        try:
		profile = cl.getProfile()
		fid =  cl.getAllContactIds()
		profile.statusMessage = "台湾戦神☆style\nFriend: " + str(len(fid)) + "\n\nMade in Taiwan"
		cl.updateProfile(profile)
                time.sleep(180)
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
