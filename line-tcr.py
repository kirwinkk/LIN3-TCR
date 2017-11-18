# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob


cl = LINETCR.LINE()
cl.login(token="Em9vjyeZixqMlTc8Xf0c.nab9gI3S+nHOnWirgQyvBa.a4TyZ34RDTHXMC3sjBDOuU3+MHNMFAfwLbKeLbBleNI=")
cl.loginResult()




reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""戦神破壞Bot...☆"""


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
    'message':"戦神Bot作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
    'message1':"戦神Bot作者:戦神 Made In Taiwan\nhttp://line.me/ti/p/4-ZKcjagH0",
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
		if op.param2 in admin + staff3 + staff4 + staff5 + staff6 + bgbot:
                        cl.acceptGroupInvitation(op.param1)
		        try:
                            cl.sendText(op.param1,helpMessage + "\n\n作者:戦神\nhttp://line.me/ti/p/4-ZKcjagH0")
			    
		        except:
			    pass
			gs = cl.getGroup(msg.to)
			if gs.invitee is not None:
				gInviMids = [contact.mid for contact in group.invitee]
                        	cl.cancelGroupInvitation(op.param1, gInviMids)
			else:
				pass
			targets = []
			for g in gs.members:
				targets.append(g.mid)
			if targets == []:
				ki.sendText(op.param1,"完畢!")
			else:
                         for target in targets:
                          if target not in admin:
                            try:
                                cl.kickoutFromGroup(op.param1,[target])
                            except:
                                pass
			cl.leaveGroup(op.param1)
		else:
		  cl.acceptGroupInvitation(op.param1)
		  try:
                            cl.sendText(op.param1,"錯誤:\n您尚無權限,無法邀請。\n\n作者:戦神\nhttp://line.me/ti/p/4-ZKcjagH0")
		  except:
			    pass
                  cl.leaveGroup(op.param1)
           else:
		pass


	
				    


#------------------------------------------------------------------------------------

        if op.type == 5:
            if wait["autoAdd"] == True:
		cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
		    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		    name = "".join([random.choice(source_str) for x in xrange(9)])
                    cl.sendText(op.param1,str(wait["message"]) + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)


		



		

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
		profile.displayName = "A_戦神DestroyBot"
                cl.updateProfile(profile)
		profile.statusMessage = "台湾戦神☆style\n\nFriend: " + str(len(fid))
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
