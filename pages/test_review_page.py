# test_review_page.py

import pytest
from src.review_page import ReviewPage

@pytest.mark.usefixtures("driver")
class TestReviewPage:
    def test_search(self, driver):
        # 리뷰 페이지에서 검색 기능 테스트
        review_page = ReviewPage(driver)
        review_page.open()

        keyword = "가디건"
        review_page.search_click(keyword)

        assert review_page.get_search_results(), "검색 결과가 나오지 않음"