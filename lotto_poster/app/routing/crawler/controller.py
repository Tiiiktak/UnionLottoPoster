from fastapi import APIRouter
from typing import List
from .dto import WinningInfoDto
from .service import CrawlerService

router = APIRouter(
    tags=["crawler"],
    prefix="/crawler",
)


@router.get("/{lotto_type}")
async def get_lotto_winning_info(lotto_type: str, stages: int = 1) -> List[WinningInfoDto]:
    """
    获取中奖信息
    :param lotto_type: 彩种 {ssq: 双色球, kl8: 快乐8, fc3d: 福彩3D, qlc: 七乐彩}
    :param stages: 最近期数
    """
    infos = CrawlerService.get_winning_info(lotto_type, stages)
    infos = list(map(CrawlerService.format_winning_info, infos))
    return infos




