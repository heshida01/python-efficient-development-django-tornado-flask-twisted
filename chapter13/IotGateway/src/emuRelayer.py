'''
Created on 2013-8-15

@author: Changlong
'''

import logging,threading,time,thread
import emuSBPS.emuReactor as emuReactor
import emuSBPS
from emuSBPS import *
from emuSBPS import ControlDevice
from Command import Authorize,BaseCommand,HeartBeat #,EventDev
logging.basicConfig(filename='example_relayer.log',level=logging.INFO,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")

def main_loop():
    time.sleep(1)
    if emuReactor.protocolActive is None:
        print "can't connect server"
        return
    
    while True:
        request=None
        try:
            command = raw_input('Enter Command: ')
            if command=="quit": break;
            request=eval(command+".C"+command+"()")
            request.protocol=emuReactor.protocolActive
        except Exception, e:
            print "unknown command :", command,e
            continue
            
        if isinstance(request, Authorize.CAuthorize):
            request.body[BaseCommand.PN_SB_CODE]="test_relayer"
            request.body[BaseCommand.PN_TERMINALTYPE]=BaseCommand.PV_ROLE_RELAYER
#        elif isinstance(request, EventDev.CEventDev):
#            request.body[BaseCommand.PN_DEVCODE]="1234"
#            request.body[BaseCommand.PN_DEVSEQ]=0
#            request.body[BaseCommand.PN_DEVVALUE]=199
            
        emuReactor.SendAndVerify(request)
        
def main():
    #thread.start_new_thread(emuReactor.Run)
    t=threading.Thread(target=main_loop)
    t.start()
    emuReactor.Run()
    

if __name__ == '__main__':
    main()
        
        
        
        
        
