### opencv中一些api的理解

##### 1. quession : 视频读取时， if cv2.waitKey(1) & 0xFF == ord('q'): break的解释
```
On some systems, waitKey() may return a value that encodes more than just the ASCII keycode. 
On all systems, we can ensure that we extract just the ASCII keycode by reading the last byte from the return value like this: 
keycode = cv2.waitKey(1)
if keycode != -1: 
  keycode &= 0xFF
```  
>  waitKey(int delay)这个函数接收一个整型值，如果这个值是零，那么函数不会有返回值，如果delay大于0，那么超过delayms后，如果没有按键，那么会返回-1，如果按键那么会返回键盘值。
>  在某些系统中，返回的键盘值可能不是ASCII编码的，所以通过与运算只取字符最后一个字节。
