from typing import Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from app.summarizer import generate_summary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> list:
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Union[dict, None]:
    summary = (
        await TextSummary.filter(id=id)
        .first()
        .update(
            url=payload.url,
            summary=payload.summary,
        )
    )
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary
    return None
