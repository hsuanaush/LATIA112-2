# 1.填表學生的性別分布
# 2.表填學生之年齡分布
# 3.每周學習時間與學業成績的關係
# 4.缺席天數與學業成績的關係
# 5.學生之空閒時間與學業成績的關係
# 6.是否有戀愛與學業成績的關係
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path='D:\學習分析\HW1\student_data.csv';
student_data=pd.read_csv(file_path)

gender_counts=student_data['sex'].value_counts()
age_counts=student_data['age'].value_counts()
avg_grade_by_stdtime = student_data.groupby('studytime')['G3'].mean().reset_index()
avg_grade_by_absences = student_data.groupby('absences')['G3'].mean().reset_index()
avg_grade_by_freetime = student_data.groupby('freetime')['G3'].mean().reset_index()
avg_grade_by_romantic = student_data.groupby('romantic')['G3'].mean().reset_index()

print("每周學習時間與學業成績的關係")
print(avg_grade_by_stdtime)
print("缺席天數與學業成績的關係")
print(avg_grade_by_absences)
print("學生之空閒時間與學業成績的關係")
print(avg_grade_by_freetime)
print('是否有戀愛與學業成績的關係')
print(avg_grade_by_romantic)
print('填表學生的性別分布')
print(gender_counts)
print('填表學生的年齡分布')
print(age_counts)

#視覺化
plt.bar(gender_counts.index, gender_counts.values)
plt.xlabel('Gender')  # 設置x軸標籤
plt.ylabel('Number')  # 設置y軸標籤
plt.title('Gender')  # 設置圖表標題
plt.xticks(list(gender_counts.keys()), ['Female', 'Male'])
plt.show()

plt.bar(age_counts.index, age_counts.values)
plt.xlabel('Age')  # 設置x軸標籤
plt.ylabel('Number')  # 設置y軸標籤
plt.title('Age')  # 設置圖表標題
plt.xticks(list(age_counts.keys()))
plt.show()

plt.bar(avg_grade_by_stdtime['studytime'], avg_grade_by_stdtime['G3'])
plt.xlabel('Study Time')  # 設置x軸標籤
plt.ylabel('Average Grade')  # 設置y軸標籤
plt.title('Study Time vs Average Grade')  # 設置圖表標題
plt.xticks(avg_grade_by_stdtime['studytime'])
plt.show()

ticks = np.arange(0, avg_grade_by_absences['absences'].max() + 1, step=5)# 從0到最大缺席天數，每5天顯示一個刻度
plt.bar(avg_grade_by_absences['absences'], avg_grade_by_absences['G3'])
plt.xlabel('Absences')  # 設置x軸標籤
plt.ylabel('Average Grade')  # 設置y軸標籤
plt.title('Absences vs Average Grade')  # 設置圖表標題
plt.xticks(ticks)
plt.show()

plt.bar(avg_grade_by_freetime['freetime'], avg_grade_by_freetime['G3'])
plt.xlabel('Free Time')  # 設置x軸標籤
plt.ylabel('Average Grade')  # 設置y軸標籤
plt.title('Free Time vs Average Grade')  # 設置圖表標題
plt.xticks(avg_grade_by_freetime['freetime'])
plt.show()

plt.bar(avg_grade_by_romantic['romantic'], avg_grade_by_romantic['G3'])
plt.xlabel('romantic')  # 設置x軸標籤
plt.ylabel('Average Grade')  # 設置y軸標籤
plt.title('Romantic vs Average Grade')  # 設置圖表標題
plt.xticks(avg_grade_by_romantic['romantic'])
plt.show()