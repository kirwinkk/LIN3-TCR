# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="ElFnLZwWDCTv74XirMZ2.wjYm0VOIqBxbzkvP8voDCG.aN2lK5sPdiSmazGSVPI3QMKxFhjSELEjhijvNsbSNyk=")
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

mid = cl.getProfile().mid


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                try:
		
                    cl.acceptGroupInvitation(op.param1)
                    group = cl.getGroup(op.param1)
                    op.contentType = 13
                    op.contentMetadata = {"mid":"uc216d8664c4e1f43772c98b1b0b8956e"}
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        cl.sendText(op.param1,str(len(group.invitee)) + "人已被取消 BOT作者:戦神↓\nhttp://line.me/ti/p/4-ZKcjagH0")
			cl.sendText(op.param1,"九条騎士団∆...降臨☆")
                    else:
                        cl.sendText(op.param1,"邀請中沒人>< BOT作者:戦神↓\nhttp://line.me/ti/p/4-ZKcjagH0")
			cl.sendText(op.param1,"九条騎士団∆...降臨☆")
                    cl.leaveGroup(op.param1)
                except:
                    pass
            else:
                pass
        if op.type == 5:
                cl.sendText(op.param1,"戦神BOT作者↓\nhttp://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]")
		

    except Exception as error:
        #print error
        pass
def nameUpdate():
    while True:
        try:
                profile = cl.getProfile()
                profile.displayName = "台湾九条騎士団∆Cancel"
                cl.updateProfile(profile)
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
