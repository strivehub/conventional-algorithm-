import threading, cv2,time
#用于解决在进行图像分类或检测时，OpenCV获取的数据不是当前图像问题
#我这里是定义的双摄像头，如果是但摄像头，删除其中一个列表即可
#定义一个操作列表的类
class Stack:
    def __init__(self, stack_size):
        self.items = []   #定义列表1，用于存储图像矩阵
        self.items2 = []  #定义列表2，用于存储图像矩阵
        self.stack_size = stack_size  #最大存储图像的张数
 
    def is_empty(self):  #判断是否存在图像
        return len(self.items) == 0
 
    def pop(self):  #用于取出最新存储的图像
        return self.items.pop(),self.items2.pop()  
 
    def peek(self):  
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
 
    def size(self):  #查看目前存储图像的张数
        return [len(self.items),len(self.items2)]
    
    def push(self, item,item2):  #存储最新的图像，并删除旧图
        if self.size()[0] >= self.stack_size:  #如果数量大于预先设定的张数，就将旧的图像删除
            for i in range(self.size()[0] - self.stack_size + 1):
                self.items.remove(self.items[0])
                self.items2.remove(self.items2[0])
        self.items.append(item)
        self.items2.append(item2)

def capture_thread(frame_buffer, lock):  #开启摄像头，用于捕捉图像，我这里是双摄，如果是单摄去掉其中一个即可
    print("capture_thread start")
    vid = cv2.VideoCapture(0)
    vid2 = cv2.VideoCapture(2)
    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video")
    while True:
        return_value, frame = vid.read()
        return_value2, frame2 = vid2.read()
        if not (return_value and return_value2):
            break
        lock.acquire()
        frame_buffer.push(frame,frame2)
        lock.release()


def main(frame_buffer, lock):  #用于获取最新的图像
    if frame_buffer.size()[0] > 0:
        lock.acquire()
        frame,frame_one = frame_buffer.pop()
        lock.release()
        return frame,frame_one
    else:
        print("get video error!!")


def double_camera(frame_buffer, lock):  #显示最新图像，waitKey中的参数可根据自己需要设置，太短会导致存储速度小于获取速度，从而读取不到图像而出错
    frame_one,frame_two = main(frame_buffer, lock)
    cv2.imshow("video1",frame_one)
    cv2.imshow("video2",frame_two)
    cv2.waitKey(80)



def detect_video():  ##循环调用，显示
    frame_buffer = Stack(5)
    lock = threading.RLock()
    t1 = threading.Thread(target=capture_thread, args=(frame_buffer, lock))
    t1.start()
    time.sleep(5)
    while True:
        double_camera(frame_buffer,lock)
        



if __name__ == '__main__':
    detect_video() 
