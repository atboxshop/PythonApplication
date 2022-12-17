import win32com.client
import os

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
print(computer_name)
qinfo.FormatName="direct=os:" + computer_name + "\\private$\\Hello"
print(qinfo)
queue=qinfo.Open(2,0)   # Open a ref to queue
msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
msg.Label="TestMsg"
msg.Body = "Hello World From MSSQ"
msg.Send(queue)
queue.Close()
print('Already sent')
