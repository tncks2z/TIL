c = int(input())

for i in range(c):
    student_num, *scores = map(int,input().split())
    score_average = sum(scores)/student_num
    
    good_scores = [score for score in scores if score > score_average]
    good_student_percentage = len(good_scores)/len(scores) * 100
    
    print("{:.3f}%".format(good_student_percentage))