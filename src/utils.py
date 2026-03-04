from typing import Any
from pydantic import BaseModel
from uuid import UUID
from typing import List, Union
import pandas as pd 


class Answer(BaseModel):
    """Один ответ на вопрос из датасета."""

    question_id: UUID
    answer: int | float | bool | str | list

def _parse_scalar(value: str) -> Any:
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def _parse_expected_value(answer_str: str, answer_type: str) -> Any:
    s = str(answer_str).strip()

    if answer_type == "bool":
        return s.lower() == "true"
    if answer_type == "int":
        return int(s)
    if answer_type == "float":
        return float(s)
    if answer_type == "list":
        if s.startswith("[") and s.endswith("]"):
            s = s[1:-1].strip()
        parts = [p.strip() for p in s.split(",") if p.strip()]
        return [_parse_scalar(p) for p in parts]

    return s


def _normalize(value: Any) -> str:
    """Приводит значение к нормализованной строке для сравнения."""
    s = str(value).strip()
    # Убираем trailing .0 для целых чисел, записанных как float
    if s.endswith(".0"):
        try:
            if int(float(s)) == float(s):
                s = str(int(float(s)))
        except (ValueError, OverflowError):
            pass
    return s


def validate_answers(answers: list[Answer], dataset_df: pd.DataFrame) -> dict:
    """Проверяет совпадение значения ответа (сравнение по строковому представлению)."""
    expected_by_id = (
        dataset_df.assign(question_id=dataset_df["question_id"].astype(str))
        .set_index("question_id")["answer"]
        .to_dict()
    )

    errors: list[dict[str, Any]] = []

    for idx, item in enumerate(answers):
        qid = str(item.question_id)
        expected_raw = expected_by_id.get(qid)
        if expected_raw is None:
            errors.append({"index": idx, "question_id": qid, "reason": "unknown_question_id"})
            continue

        # Сравниваем по нормализованному строковому представлению
        if _normalize(item.answer) != _normalize(expected_raw):
            errors.append({
                "index": idx,
                "question_id": qid,
                "reason": "value_mismatch",
                "expected": expected_raw,
                "actual": item.answer,
            })

    return {"ok": len(errors) == 0, "errors": errors}