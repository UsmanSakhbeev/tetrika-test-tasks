import csv
from unittest.mock import Mock, patch

from task2 import solution


def _fake_api_batch(titles, cmcontinue=None):
    data = {
        "batchcomplete": True,
        "query": {
            "categorymembers": [
                {"pageid": i, "ns": 0, "title": title}
                for i, title in enumerate(titles, start=1)
            ]
        },
    }
    if cmcontinue:
        data["continue"] = {"cmcontinue": cmcontinue, "continue": "-||"}
    return data


def test_fetch_single_batch():
    titles = ["Акула", "бобр", "Варан"]
    with patch("task2.solution.requests.Session.get") as get:
        mock_resp = Mock(json=lambda: _fake_api_batch(titles))
        mock_resp.raise_for_status = lambda: None
        get.return_value = mock_resp

        counts = solution.fetch_category_members(solution.CATEGORY)

    assert counts == {"А": 1, "Б": 1, "В": 1}


def test_fetch_multiple_batches():
    with patch("task2.solution.requests.Session.get") as get:
        get.side_effect = [
            Mock(
                json=lambda: _fake_api_batch(["Акула"], cmcontinue="cont-1"),
                raise_for_status=lambda: None,
            ),
            Mock(
                json=lambda: _fake_api_batch(["Белка"], cmcontinue="cont-2"),
                raise_for_status=lambda: None,
            ),
            Mock(
                json=lambda: _fake_api_batch(["Варан"]),
                raise_for_status=lambda: None,
            ),
        ]

        counts = solution.fetch_category_members(solution.CATEGORY)

    assert counts == {"А": 1, "Б": 1, "В": 1}


def test_write_csv(tmp_path):
    counts = {"А": 2, "В": 1}
    csv_path = tmp_path / "beasts.csv"

    solution.write_csv(counts, path=csv_path)

    with csv_path.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == ["А", "2"]
    assert rows[1] == ["Б", "0"]
    assert rows[2] == ["В", "1"]

    assert len(rows) == len(solution.ALPHABET)
