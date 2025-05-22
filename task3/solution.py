def to_pairs(times: list[int]) -> list[tuple[int, int]]:
    if len(times) % 2 != 0:
        raise ValueError("Должно быть чётное число меток")
    return [(times[i], times[i+1])
            for i in range(0, len(times), 2)
            if times[i] < times[i+1]]


def crop_pairs(pairs: list[tuple[int, int]],
               start: int, end: int) -> list[tuple[int, int]]:
    res = []

    for s, e in pairs:
        s = max(s, start)
        e = min(e, end)
        if s < e:
            res.append((s, e))

    return res


def merge_pairs(pairs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not pairs:
        return []
    pairs.sort()
    merged = [list(pairs[0])]

    for s, e in pairs[1:]:
        last_s, last_e = merged[-1]
        if s <= last_e:
            merged[-1][1] = max(e, last_e)
        else:
            merged.append([s, e])

    return [tuple(p) for p in merged]


def overlap_len(a: list[tuple[int, int]], b: list[tuple[int, int]]) -> int:
    i = j = total = 0

    while i < len(a) and j < len(b):
        s = max(a[i][0], b[j][0])
        e = min(a[i][1], b[j][1])

        if s < e:
            total += e - s
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1

    return total


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals["lesson"]

    pupil_pairs = to_pairs(intervals["pupil"])
    tutor_pairs = to_pairs(intervals["tutor"])

    pupil_cropped = crop_pairs(pupil_pairs, lesson_start, lesson_end)
    tutor_cropped = crop_pairs(tutor_pairs, lesson_start, lesson_end)

    pupil_merged = merge_pairs(pupil_cropped)
    tutor_merged = merge_pairs(tutor_cropped)

    return overlap_len(pupil_merged, tutor_merged)
