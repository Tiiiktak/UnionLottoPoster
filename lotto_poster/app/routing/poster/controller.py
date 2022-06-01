from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from .service import PosterService
import cv2

router = APIRouter(
    tags=["poster"],
    prefix="/poster",
)


@router.get("/latest")
async def get_latest_poster(date: str = 'today', ssq: bool = True, kl8: bool = True, qlc: bool = True, fc3d: bool = True):
    poster = PosterService.latest_poster(date, ssq, kl8, qlc, fc3d)
    poster_name = PosterService.poster_static(poster)
    return poster_name


@router.get("/s/{poster_name}")
async def get_poster(poster_name: str):
    img = PosterService.get_image(poster_name)
    return StreamingResponse(send_bytes_img(img), media_type="image/jpg")


def send_bytes_img(ori_img):
    byte_img = cv2.imencode(".jpg", ori_img)[1].tobytes()
    yield byte_img
