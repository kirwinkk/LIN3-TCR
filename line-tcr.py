# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="ElVlm76pIF8zQXh2yvx0.LuypBYCpVNaalD7+KZ9xua.8CuK+u4+3BajUgt7jxYG7ucLHwGP8DrdFZlbFL4KDcU=")
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
                    start = time.time()
                    group = cl.getGroup(op.param1)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
			elapsed_time = time.time() - start
                        cl.sendText(op.param1,"已取消 " + str(len(group.invitee)) + " 人的邀請")
			cl.sendText(op.param1,"掰掰≧∇≦")
                    else:
			elapsed_time = time.time() - start
                        cl.sendText(op.param1,"咦..沒有邀請呀(ノﾟДﾟ)")
                    cl.leaveGroup(op.param1)
                except:
                    pass
            else:
                pass
        if op.type == 5:
                    cl.sendText(op.param1,"戦神代行CancelBOT\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]")

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
