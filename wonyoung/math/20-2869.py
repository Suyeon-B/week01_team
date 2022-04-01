# 12분 11초, 정답 이해 못함
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b, v = map(int, input().split())

print((v-b)/(a-b))