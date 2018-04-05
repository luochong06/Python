# -*-coding:utf-8-*-
name = "luochong"
age = 26
pwd = "123"
count_sum = 0
##模拟账号密码登录，3允许连续错误三次
while count_sum < 3:
    input_age = int(input("请输入您的年龄:"))
    if age == input_age:
        print ("答案正确，结束")
        break
    elif age < input_age:
        print ("您输入的年龄大于实际年龄，请再次输入")
    else:
        print ("您输入的年龄小于实际年龄。。。。")
    count_sum = count_sum + 1
    # 如果错误三次提示是否继续

    if count_sum == 3:
        choose_result = input("是否继续游戏,请选择?(y|n)")
        print(choose_result)
        if choose_result == 'y' or choose_result == 'Y':
            count_sum = 0
