# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="ElpyWnrTQQHjnhAqnGN5.uEmdFcf6siszYLOn7RH6zq.h6129jw528y3MELRp9Q2udXmR1WaQRITyaBvyty+QX4=")
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

admsa = "uc216d8664c4e1f43772c98b1b0b8956e"

mid = cl.getProfile().mid
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                try:
                    cl.acceptGroupInvitation(op.param1)
                    start = time.time()
                    elapsed_time = time.time() - start
                    group = cl.getGroup(op.param1)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        cl.sendText(op.param1,"戦神已取消所有邀請(´∀｀)♡" + "\n耗費時間:%sseconds" % (elapsed_time) + "\n\n戦神BOT作者↓\nhttp://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]")
                    else:
                        cl.sendText(op.param1,"戦神發現...邀請中沒人><" + "\n耗費時間:%sseconds" % (elapsed_time) + "\n\n戦神BOT作者↓\nhttp://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]")
                    cl.leaveGroup(op.param1)
                except:
                    pass
            else:
                pass

    except Exception as error:
        #print error
        pass


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
