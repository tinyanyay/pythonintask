+# ������ 5. ������� 30.  
 2   +'''  
 3   +�������� ���������, ������� �� ��� ������� ��������� �������  
 4   +���������� ��� ������ �� ���� ����������� ������� �������.  
 5   +'''  
 6   +# SHEIKO R.V.  
 7   +# 10.03.2016  
 8   +  
 9   +from random import choice  
 10   +  
 11   +phrase = '�����, ����� � �����'  
 12   +  
 13   +nephews = [''.join(filter(str.isalpha, name))  
 14   +           for name in phrase.split(' ')  
 15   +           if len(name) > 2]  
 16   +  
 17   +stats = [0, 0, 0]  
 18   +  
 19   +k = 1  
 20   +while True:  
 21   +    c = choice(nephews)  
 22   +    stats[nephews.index(c)] += 1  
 23   +    k -= 1  
 24   +    if k <= 0:  
 25   +        print('\n' + c)  
 26   +        print('���������� ' + str(stats))  
 27   +        try:  
 28   +            k = int(input('��������� n ���: '))  
 29   +        except:  
 30   +            continue  
 31   +  
