from typing import List, Optional, Dict

from cocokat_com.nosql.comics import Comic
from cocokat_com.nosql.comicpanel import ComicPanel


def get_comic_by_name(name: str) -> Comic:
    comic = Comic.objects().filter(name=name).first()

    return comic


def get_comic_panels(
        comic_name: str,
        panel_start: int = None,
        panel_end: int = None) -> Dict:

    comic = Comic.objects().filter(name=comic_name).first()

    panels_dict = [panel.to_mongo().to_dict() for panel in comic.panels]

    return comic.panels


# def get_latest_releases(limit=10) -> List[Release]:
#     releases = Release.objects(). \
#         order_by("-created_date"). \
#         limit(limit). \
#         all()
#     return releases


# def get_package_count() -> int:
#     return Package.objects().count()


# def get_release_count() -> int:
#     return Release.objects().count()


# def get_package_by_id(package_id: str) -> Optional[Package]:
#     if not package_id:
#         return None

#     package_id = package_id.strip().lower()

#     package = Package.objects() \
#         .filter(id=package_id) \
#         .first()

#     return package


# def all_packages(limit: int) -> List[Package]:
#     return list(Package.objects().limit(limit))


# def get_packages_by_ids(package_ids: List[str]) -> List[Package]:
#     return list(Package.objects(id__in=package_ids))


# def get_latest_release_for_package(package_id: str) -> Optional[Release]:
#     return Release.objects(package_id=package_id).order_by('-created_date').first()
