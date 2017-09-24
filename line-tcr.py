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
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)

                        cl.sendText(op.param1,"測試  取消邀請ㄌ")
                    else:
                        cl.sendText(op.param1,"沒邀請拉幹你娘")
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
