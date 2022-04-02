
# 문제 링크 : https://www.acmicpc.net/problem/17478

# ____ 가 ---- 인줄 알고 삽질하다가 풀이시간 오버

def solved(x):
    if x < 0:
        return
    else:
        solved(x-1)
        print('____'*x+'"재귀함수가 뭔가요?"')
        print('____'*x+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____'*x+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____'*x+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
def solved2(x):
    if x<0:
        return;
    else:
        print('____'*x+'라고 답변하였지.')
        solved2(x-1)


x = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
solved(x-1)
print('____'*x+'"재귀함수가 뭔가요?"')
print('____'*x+'"재귀함수는 자기 자신을 호출하는 함수라네"')
solved2(x)



