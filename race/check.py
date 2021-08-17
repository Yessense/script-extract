from os.path import join

from datasets import load_dataset

dataset = load_dataset('race', 'high')
texts = dataset['train']['article']

save_folder = '/home/yessense/PycharmProjects/ScriptExtractionForVQA/texts/Race/'
for i in range(100):
    text = texts[i * 4]
    with open(join(save_folder, f'{i}.txt'), 'w') as f:
        f.write(text)
print("Done")

"""
Статьи повторяются.
Статьи бывают списком и не сильно литературные


Course A: Understanding computers
1. A twelve-hour course for people who do not know very much about computers but need to learn about them. You can learn what computers are, what computers can do and cannot do, and how to use them.
2. Course fee: $75, from June 1 to June 28, 9~12am every Sunday.
3. Equipment fee: $10.
4. Teacher: Joseph Saunders, professor of computer science at New Urban University, with twelve years of experience in computer field.
Call 67801642 or 67801643 for more information.
Course B: Learning to speak French
1. A course with a small class of less than 20 people, twice a week. Your French level is tested in the first class. Then you can begin practicing at one of eight different skill levels. This allows you to learn at your own speed, and prepares you to learn through situations of real life with a funny and easy method.
2. Course fee: $200, from June 1 to June 25, 4~7pm every Monday and Thursday.
3. Personal tutoring fee: $100.
4. Teacher: From the first day on you can have your own personal French teacher that corrects your exercises and assists you along the course, who has successfully taught French course before.
Phone 67353019 for more information.
Course C: Learning to swim
1. A course for people who have interest in swimming. We offer morning and afternoon classes, where swimming knowledge will be taught. Then you can gain swimming skills through practicing in water.
2. Course fee: $150, from June 9 to June 29, 10am~4pm every Tuesday and Friday..
3. Personal tutoring Fee: $100
4. Teacher: Teachers from sports college and experienced swimming-loves.
Very close to the Central Park. For further information call 67432308.
"""