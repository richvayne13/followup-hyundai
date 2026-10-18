# -*- coding: utf-8 -*-
"""
build_hyundai.py
현대자동차 전극생산운영 지원 맞춤형 심층 꼬리질문 & 방어 답변 대시보드 빌드 파이프라인.
"""

import os
import sys
import traceback

from ui_engine import render_dashboard_html, render_master_markdown
from hyundai_modules_part1 import HYUNDAI_MODULES_PART1
from hyundai_modules_part2 import HYUNDAI_MODULES_PART2

BASE_DIR = r"C:\Work\꼬리질문_현대"
RESULT_DIR = os.path.join(BASE_DIR, "result", "261018_v1.0")
LIVE_URL = "https://richvayne13.github.io/followup-hyundai/"


def main():
    try:
        os.makedirs(RESULT_DIR, exist_ok=True)
        modules = HYUNDAI_MODULES_PART1 + HYUNDAI_MODULES_PART2

        html = render_dashboard_html(
            page_title="현대자동차 전극생산운영 면접 심층 꼬리질문 & 100점 방어 답변 마스터 대시보드",
            sidebar_title="현대자동차 전극생산운영 꼬리질문",
            sidebar_subtitle="Context 전 항목 기반 심층 꼬리질문 & 방어 바이블",
            header_badge="🚗 현대자동차 배터리·전극생산운영 실전 면접 완벽 대비",
            header_title="현대자동차 전극생산운영 심층 꼬리질문 & 100점 방어 답변 대시보드",
            header_desc=(
                "<code>context/현대자동차_경력면접대비.docx</code>에 수록된 모든 경력·프로젝트(완성차 관점 지원동기, 파일럿 라인 셋업 강점, "
                "Die Shim 100:1 웜기어·LVDT 전동화, 웹게이지 미세라인 EMA·Dynamic Threshold 감지, 100만 장 Burr 이원화 Valley·1×7 Bridge Kernel 비전 엔진, "
                "IPQC 월 40시간 자동화, New-form factor 양산 셋업, 본·기·함·구 AI 프로토콜, 코터 80% 결정론 & 바인더 마이그레이션 5단계·기계 체결 토크)를 "
                "<strong>현대자동차 전극생산운영 직무 관점</strong>으로 완벽히 구조화하여 총 <strong>8개 핵심 파트 · 37개 실전 꼬리질문과 방어 답변</strong>으로 구축했습니다."
            ),
            accent_primary="#38bdf8",
            modules=modules,
            storage_prefix="followup_hyundai"
        )

        root_html = os.path.join(BASE_DIR, "index.html")
        res_html = os.path.join(RESULT_DIR, "index.html")
        for p in (root_html, res_html):
            with open(p, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"[OK] Generated {p} ({len(html):,} bytes)")

        md = render_master_markdown(
            title="현대자동차 전극생산운영 심층 꼬리질문 & 방어 답변 마스터 보고서",
            live_url=LIVE_URL,
            local_path=root_html,
            modules=modules
        )
        md_path = os.path.join(RESULT_DIR, "261018_hyundai_followup_master.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md)
        with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
            f.write(md)
        with open(os.path.join(BASE_DIR, ".nojekyll"), "w", encoding="utf-8") as f:
            f.write("\n")
        print(f"[OK] Generated {md_path}")

    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
