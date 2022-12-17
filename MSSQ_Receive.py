import win32com.client
import os

qinfo = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
print(computer_name)
qinfo.FormatName = "direct=os:" + computer_name + "\\private$\\Hello"
queue = qinfo.Open(1,0)   # Open a ref to queue to read(1)
msg = queue.Receive()
print("Label:",msg.Label)
print("Body :",msg.Body)
queue.Close()