def appearance(intervals):

    def segments_to_tuple(list):
        return [(list[n], list[n+1]) for n in range(0, len(list), 2)]

    lesson = segments_to_tuple(intervals['lesson'])
    tutor = segments_to_tuple(intervals['tutor'])
    pupil = segments_to_tuple(intervals['pupil'])



    def get_time_segments(glob, mini):
        res = []
        for start_glob, end_glob in glob:
            for start_mini, end_mini in mini:
                if (end_mini < start_glob) or (start_mini > end_glob):
                    continue
                else:
                    if res != []:
                        s, e = res[-1]
                        if e > end_mini:
                            res = modify_union
                    else:
                        tpl = (max(start_mini, start_glob), min(end_mini, end_glob))
                        res.append(tpl)
        return res

    lesson_tutor = get_time_segments(lesson, tutor)
    lesson_tutor_pupil = get_time_segments(lesson_tutor, pupil)

    return sum([lesson_tutor_pupil[n+1] - lesson_tutor_pupil[n] for n in range(0, len(lesson_tutor_pupil), 2)])

tests = [
    # {'data': {'lesson': [1594663200, 1594666800],
    #          'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    #          'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    #  'answer': 3117
    # },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    # {'data': {'lesson': [1594692000, 1594695600],
    #          'pupil': [1594692033, 1594696347],
    #          'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    # 'answer': 3565
    # },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
