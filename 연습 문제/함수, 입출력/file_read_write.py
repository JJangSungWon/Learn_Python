#파일(sample.txt)읽어서 총합과 평균구해서 파일쓰기(result.txt)
f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()