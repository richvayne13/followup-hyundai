# -*- coding: utf-8 -*-
"""
hyundai_modules_part2.py
현대자동차 전극생산운영 맞춤형 심층 꼬리질문 & 방어 답변 (PART 05 ~ PART 08)
"""

HYUNDAI_MODULES_PART2 = [
    {
        "badge": "프로젝트 4 · 인라인 IPQC 자동화 · 월 40시간 공수 100% 절감",
        "nav_title": "[프로젝트 4] 인라인 IPQC 데이터 검토 자동화 (Python/AX)",
        "title": "[프로젝트 4] 고객향 인라인 IPQC 데이터 검토 및 Lot 병합 판정 100% 자동화: 월 40시간 공수 절감, 헌팅 노이즈 제거 및 원클릭 GUI 배포",
        "context_summary": [
            "<strong>배경 및 문제점 (S/T)</strong>: 신규 모델 생산에서 고객사가 모든 Lot에 대한 인라인 검사기 Data를 요청. 사내 여러 시스템을 거쳐야 하고 헌팅(Hunting) Data를 제거해야 해서 <strong>엔지니어가 매일 2시간씩 수작업으로 데이터를 다운받고 발라내는 비효율 발생</strong>. ‘고객향 Data 송부 검토 100% 자동화(공수 100% 절감)’ 목표 설정.",
            "<strong>구현 프로세스 (Action)</strong>: ① 기존 수작업을 매뉴얼화하여 <strong>PRD(요구사항 정의서)</strong> 작성, ② 마우스 클릭과 화면 좌표를 제어해 IoT 시스템에서 데이터를 자동 다운로드하는 스크립트 구현, ③ <strong>룰 기반 헌팅 노이즈 제거 로직</strong> 및 <strong>Lot 병합 가능 여부 검토 프로그램</strong> 개발, ④ 공정능력($C_{pk}$) 그래프와 일일 품질 현황을 즉시 확인하는 <strong>HTML 대시보드</strong> 구축 및 코딩을 모르는 팀원도 원클릭으로 쓰는 <strong>직관적 GUI 환경 배포</strong>.",
            "<strong>정량적 성과 (Result)</strong>: 매일 2시간씩 소요되던 수작업을 <strong>월 40시간 이상 완전 자동화(팀 업무 공수 100% 절감)</strong>."
        ],
        "base_speech": (
            "“신규 모델 양산 당시 고객사가 모든 Lot에 대한 인라인 검사기 데이터를 요청했는데, 사내 여러 시스템에서 데이터를 다운받고 헌팅 노이즈 데이터를 수작업으로 발라내느라 엔지니어가 매일 2시간씩 단순 반복 업무에 매달리는 비효율이 있었습니다. "
            "저는 ‘고객향 데이터 송부 검토 100% 자동화’를 목표로 AI 기술을 활용해 단독 개발에 착수했습니다. "
            "먼저 기존 수작업 기준을 매뉴얼화하여 PRD를 작성한 뒤, 화면 좌표와 클릭을 제어해 IoT 시스템에서 데이터를 자동 다운로드하는 스크립트와 룰 기반 헌팅 노이즈 제거 로직을 개발했습니다. "
            "또한 공정능력 그래프와 일일 품질 현황을 한눈에 볼 수 있는 HTML 대시보드를 구축하고, 코딩을 모르는 팀원도 원클릭으로 쓸 수 있도록 직관적인 GUI 환경으로 배포하여 매일 2시간, 월 40시간의 수작업을 100% 자동화했습니다.”"
        ),
        "svg_title": "📊 [인라인 IPQC 데이터 검토 & Lot 병합 자동화 아키텍처] PRD 설계 ➔ IoT 자동 수집 ➔ 룰 기반 헌팅 제거 ➔ Cpk HTML 대시보드 & GUI 배포",
        "svg": """<svg viewBox="0 0 960 260" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="260" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <g transform="translate(20, 20)">
    <rect width="220" height="220" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="14" y="26" fill="#38bdf8" font-size="11" font-weight="800">1. 수작업 매뉴얼화 &amp; PRD</text>
    <rect x="14" y="42" width="192" height="162" rx="6" fill="#1e293b"/>
    <text x="22" y="66" fill="#fde047" font-size="8.8" font-weight="700">• 암묵지의 정량 규칙화</text>
    <text x="22" y="86" fill="#cbd5e1" font-size="8">• IoT 시스템 화면 좌표/클릭</text>
    <text x="22" y="102" fill="#cbd5e1" font-size="8">  제어로 다중 Lot 데이터</text>
    <text x="22" y="118" fill="#cbd5e1" font-size="8">  무인 자동 다운로드 구현</text>
    <text x="22" y="150" fill="#6ee7b7" font-size="8" font-weight="700">➔ 수동 조회 시간 100% 제거</text>
  </g>
  <g transform="translate(254, 20)">
    <rect width="220" height="220" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11" font-weight="800">2. 헌팅 제거 &amp; Lot 병합 로직</text>
    <rect x="14" y="42" width="192" height="162" rx="6" fill="#1e293b"/>
    <text x="22" y="66" fill="#fde047" font-size="8.8" font-weight="700">• 룰 기반 Hunting 노이즈 제거</text>
    <text x="22" y="86" fill="#cbd5e1" font-size="8">• 코팅 가감속/경계 스캔 전환 시</text>
    <text x="22" y="102" fill="#cbd5e1" font-size="8">  가짜 스파이크 자동 필터링</text>
    <text x="22" y="126" fill="#38bdf8" font-size="8.5" font-weight="700">• Lot 병합 가능 여부 자동 판정</text>
    <text x="22" y="144" fill="#94a3b8" font-size="7.8">  (합산 Cpk 및 규격 일치 검증)</text>
  </g>
  <g transform="translate(488, 20)">
    <rect width="220" height="220" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
    <text x="14" y="26" fill="#c4b5fd" font-size="11" font-weight="800">3. HTML 대시보드 &amp; GUI 배포</text>
    <rect x="14" y="42" width="192" height="162" rx="6" fill="#1e293b"/>
    <text x="22" y="66" fill="#fde047" font-size="8.8" font-weight="700">• Cpk &amp; 일일 품질 현황 시각화</text>
    <text x="22" y="86" fill="#cbd5e1" font-size="8">• 코딩 모르는 동료 엔지니어도</text>
    <text x="22" y="102" fill="#cbd5e1" font-size="8">  즉시 쓸 수 있는 원클릭 GUI</text>
    <text x="22" y="150" fill="#6ee7b7" font-size="8" font-weight="700">➔ 팀 표준 AX 툴로 정착</text>
  </g>
  <g transform="translate(722, 20)">
    <rect width="218" height="220" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="14" y="26" fill="#10b981" font-size="11" font-weight="800">4. 성과 &amp; 현대차 라인 확장</text>
    <rect x="14" y="42" width="190" height="162" rx="6" fill="#064e3b"/>
    <text x="20" y="70" fill="#fde047" font-size="10" font-weight="800">🏆 월 40시간 완전 자동화</text>
    <text x="20" y="92" fill="#ffffff" font-size="8.2">• 일 2시간 수작업 공수 100% 절감</text>
    <text x="20" y="112" fill="#a7f3d0" font-size="8">• 인력 효율이 중요한 현대차 신규</text>
    <text x="20" y="128" fill="#a7f3d0" font-size="8">  배터리 라인에서 자주검사·IPQC</text>
    <text x="20" y="144" fill="#a7f3d0" font-size="8">  모니터링 자동화 즉시 구축 가능!</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "헌팅 데이터 구분 검증",
                "question": "인라인 검사 데이터에서 '헌팅(Hunting) Data'를 룰 기반으로 제거했다고 하셨는데, 헌팅 데이터가 왜 생기며 실제 불량 데이터까지 지워버릴 위험은 어떻게 막으셨나요?",
                "intent": "데이터 정제 시 정상적인 불량 신호(Outlier)와 센서/설비 과도 구간 노이즈(Hunting)를 구분하는 도메인 기준을 묻는 질문입니다.",
                "answer": (
                    "인라인 웹게이지에서 발생하는 ‘헌팅(Hunting) 데이터’는 실제 코팅 불량이 아니라, <strong>① 코팅 시작·종료(Start/End) 가감속 구간, ② 간헐/스트라이프 코팅에서 무지부와 유지부 경계를 센서가 넘어갈 때, ③ 스플라이싱(원단 이음매) 테이프 구간 통과 시</strong> 센서가 순간적으로 튀는 가짜 스파이크입니다.<br><br>"
                    "만약 값의 크기만 보고 지우면 실제 불량까지 지워질 위험이 있기 때문에, 저는 <strong>설비 운전 상태 로그(코팅 시작/종료 미터 위치, 센서 스캔 프레임 위치, 주행 속도)를 결합한 룰(Rule)</strong>을 세웠습니다. 즉, 과도 구간 위치에서 발생한 헌팅만 정확히 트리밍하고, 정속 코팅 구간에서 발생한 스펙 이탈은 절대 삭제하지 않고 오히려 대시보드 상단에 적색 알람으로 강조 표시하도록 설계하여 데이터 신뢰성을 100% 확보했습니다."
                )
            },
            {
                "tag": "PRD 선행 작성 이유",
                "question": "코딩을 바로 시작하지 않고 '기존 수작업을 매뉴얼화하여 PRD(요구사항 정의서)를 먼저 작성했다'고 하셨는데, 혼자 개발하면서 왜 PRD부터 쓰셨나요?",
                "intent": "체계적인 소프트웨어/AX 엔지니어링 습관과 도메인 표준화 역량을 확인하는 질문입니다.",
                "answer": (
                    "엔지니어마다 수작업으로 데이터를 검토할 때 머릿속으로만 판단하던 암묵지(예: ‘앞뒤 몇 미터는 버린다’, ‘이 정도 튐은 센서 헌팅이다’)를 명문화하지 않고 코딩부터 하면, 예외 케이스가 나올 때마다 코드를 뜯어고쳐야 하고 AI를 활용할 때도 환각(Hallucination)이 발생하기 때문입니다.<br><br>"
                    "그래서 저는 먼저 수작업 프로세스의 <strong>입력 데이터 형식, 헌팅 제거 조건식, $C_{pk}$ 산출 공식, 최종 대시보드 출력 형태를 정량적인 문서(PRD)로 정의</strong>해 품질 및 생산 팀원들과 기준을 일치시켰습니다. 덕분에 개발 시행착오를 줄였을 뿐 아니라, 그 PRD 자체가 팀의 표준 데이터 검토 매뉴얼(SOP)이 되는 일석이조의 효과를 거두었습니다."
                )
            },
            {
                "tag": "Lot 병합 프로그램 검증",
                "question": "개발하신 프로그램 중에 'Lot 병합 가능 여부 검토 프로그램'도 있는데, 현장에서 왜 Lot 병합이 필요하고 어떤 기준으로 판정하나요?",
                "intent": "전극 생산운영 실무(권취 롤 길이 관리, 후공정 롤프레스/슬리팅 로스 절감)에 대한 이해도를 확인하는 질문입니다.",
                "answer": (
                    "전극 코팅 중 설비 점검이나 단선, 원단 교체 등으로 인해 기준 권취 길이(예: $3,000\\text{m}$)를 다 채우지 못한 소량 단척 롤(Short Roll)들이 발생합니다. 이를 그대로 후공정(롤프레스·슬리팅)에 넘기면 원단 교체(Mount/Unmount) 시간이 너무 많이 걸려 라인 가동률이 떨어지기 때문에, 두 롤을 이어 붙이는 <strong>Lot 병합(Merge)</strong>이 필요합니다.<br><br>"
                    "이때 아무 롤이나 합칠 수 없고 고객사 규격상 <strong>① 동일 슬러리 로트 여부, ② 두 롤의 평균 두께·로딩량 편차 이내 여부, ③ 두 롤의 데이터를 합산했을 때 전체 $C_{pk}$가 출하 기준(예: $1.33$)을 만족하는지</strong>를 계산해야 합니다. 이를 파이썬 프로그램이 전수 조합으로 자동 계산해 최적의 병합 쌍을 추천해 주도록 구현하여 단척 롤 폐기와 엔지니어 검토 시간을 동시에 줄였습니다."
                )
            },
            {
                "tag": "현대차 라인 적용 계획",
                "question": "현대차 전극생산운영 조직에 오시면 이 Python/AX 자동화 역량을 가장 먼저 어디에 적용해 보고 싶으신가요?",
                "intent": "입사 후 즉시 활용 가능한 실무 기여 포인트를 묻는 질문입니다.",
                "answer": (
                    "현대차의 신규 파일럿 및 양산 라인에서는 제한된 엔지니어 인력으로 수많은 시운전 조건(레시피)별 코팅 품질 데이터를 빠르게 비교·분석해야 합니다.<br><br>"
                    "입사 즉시 <strong>코터 인라인 계측기(웹게이지, 비전, 두께 측정기)와 건조로/장력 PLC 로그를 자동으로 취합해, 시운전 조건 변경 전후의 로딩 산포($C_{pk}$)와 에지 프로파일(Fat Edge/Sliding) 변화를 1초 만에 비교 시각화해 주는 원클릭 HTML 대시보드</strong>를 구축하겠습니다. 이를 통해 엔지니어들이 엑셀 편집에 쓰는 시간을 없애고 오직 공정 조건 최적화에만 집중할 수 있도록 만들겠습니다."
                )
            }
        ]
    },
    {
        "badge": "프로젝트 5 · New-form factor 비즈니스 · 고객 대응 & 불량 관리",
        "nav_title": "[프로젝트 5] New-form factor Biz F/up & 8D 고객 대응",
        "title": "[프로젝트 5] New-form factor(18/21/46 Series) 전극 개발~양산 Full-Cycle F/up 및 FACA·8D Report 기반 품질 사고 대응",
        "context_summary": [
            "<strong>New-form factor 전극 Biz F/up</strong>: 신규 전극 비즈니스에서 <strong>개발 단계 Spec 선정부터 샘플 생산, 시운전 기획, 설비/검사기 셋업 및 제어부 개선, 양산 수율 안정화</strong>까지 공정 엔지니어로서 전 과정 주도 (18/21/46 Series 원통형 및 간헐·스트라이프·2패턴·절연 코팅 운영).",
            "<strong>고객 기술 대응 & 불량 관리</strong>: 글로벌 고객사 Daily 미팅, Audit 및 라인투어 대응. 제품 특이점 발생 시 기술적 메커니즘 설명 및 <strong>QMS, MES, EioT, Spotfire를 활용한 원인 분석 ➔ Risk Range(위험 범위) 확인 ➔ 개선방안 수립 ➔ 유효성 검증(FACA 및 8D Report)</strong>으로 출하 승인 견인."
        ],
        "base_speech": (
            "“저는 18·21·46 시리즈 원통형 모델과 간헐·스트라이프·2패턴·절연 코팅 등 고난도 New-form factor 전극 비즈니스에서 개발 스펙 선정부터 샘플 시운전, 설비 셋업, 양산 안정화까지 전 주기를 수행했습니다. "
            "또한 고객사가 매 Lot의 인라인 데이터와 QA 측정 결과를 보고 출하 승인을 내리는 구조에서, 특이점 발생 시 물리적 메커니즘을 설명하고 QMS, MES, EioT, Spotfire로 원인 분석부터 Risk Range 확정, 개선 대책과 유효성 검증까지 담은 FACA 및 8D Report를 작성해 Daily 미팅과 Audit을 성공적으로 방어했습니다.”"
        ),
        "svg_title": "📊 [New-form factor 전극 개발~양산 셋업 & 품질 사고 대책 관리(QMS/MES/EioT/Spotfire) 4단계]",
        "svg": """<svg viewBox="0 0 960 250" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="250" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <g transform="translate(20, 20)">
    <rect width="450" height="210" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="11.5" font-weight="800">1. 고난도 코팅 라인 운영 &amp; 신제품 셋업 스펙트럼</text>
    <rect x="16" y="42" width="418" height="152" rx="6" fill="#1e293b"/>
    <text x="26" y="66" fill="#fde047" font-size="9" font-weight="700">• 폼팩터 경험: 18 / 21 / 46 Series 차세대 원통형 &amp; 파우치/각형 대응</text>
    <text x="26" y="88" fill="#cbd5e1" font-size="8.2">• 특수 코팅 공법: 간헐 코팅 / 스트라이프 코팅 / 2패턴 코팅 / 절연 코팅</text>
    <text x="26" y="110" fill="#34d399" font-size="9" font-weight="700">• 개발~양산 Full-Cycle 엔지니어링:</text>
    <text x="34" y="128" fill="#cbd5e1" font-size="8">① 개발 중 Spec 선정 ➔ ② 샘플 생산 &amp; 시운전 기획 ➔ ③ 설비/검사기 셋업</text>
    <text x="34" y="146" fill="#cbd5e1" font-size="8">➔ ④ SOP 개발 &amp; 오퍼레이터 교육(PLM) ➔ ⑤ 원재료/수율/월마감(ERP) 관리</text>
    <text x="34" y="172" fill="#6ee7b7" font-size="8" font-weight="700">➔ 현대차 신규 라인에 필요한 모든 생산운영 실무 A to Z 즉시 수행 가능!</text>
  </g>
  <g transform="translate(490, 20)">
    <rect width="450" height="210" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="11.5" font-weight="800">2. 품질 사고 대책 관리 &amp; 8D Report 대응 프로세스</text>
    <rect x="16" y="42" width="418" height="152" rx="6" fill="#1e293b"/>
    <text x="26" y="66" fill="#f87171" font-size="9" font-weight="700">① 원인 분석 &amp; Risk Range(위험 영향 범위) 확정</text>
    <text x="34" y="84" fill="#cbd5e1" font-size="8">• QMS, MES, EioT 설비 파라미터, Spotfire 다변량 분석으로 오염 구간 특정</text>
    <text x="26" y="108" fill="#fde047" font-size="9" font-weight="700">② 하드웨어/알고리즘 개선방안 수립 &amp; 유효성 검증</text>
    <text x="34" y="126" fill="#cbd5e1" font-size="8">• 전동화 개조(LVDT), 감지 로직(EMA), 비전 선별(Bridge Kernel)로 재발 방지</text>
    <text x="26" y="150" fill="#38bdf8" font-size="9" font-weight="700">③ 고객 기술 대응 (FACA / 8D Report / Daily Meeting / Audit)</text>
    <text x="34" y="168" fill="#6ee7b7" font-size="8">• 논리적 메커니즘 규명 및 데이터 검증으로 전 Lot 출하 승인 및 수율 안정화</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "46시리즈/신규 폼팩터 검증",
                "question": "18, 21시리즈뿐만 아니라 46시리즈(4680 등) New-form factor 전극도 다루셨는데, 폼팩터가 커질수록 전극 코터 공정에서 가장 관리하기 까다로워지는 변수는 무엇인가요?",
                "intent": "대형 원통형(46시리즈)이나 신규 폼팩터 코팅 시의 기술적 난점을 실제로 겪어봤는지 확인하는 질문입니다.",
                "answer": (
                    "폼팩터가 46시리즈처럼 대구경·고용량화될수록 코터 공정에서 가장 까다로워지는 것은 <strong>① 권취 길이와 코팅 폭 증가에 따른 누적 공차 및 주름·단선 제어</strong>, 그리고 <strong>② 고로딩(후막) 코팅에 따른 건조 크랙 및 바인더 마이그레이션 제어</strong>입니다.<br><br>"
                    "젤리롤 직경이 커지면서 전극 한 롤당 감기는 길이가 길어지기 때문에, 미세한 Fat Edge(에지 솟음)나 좌우 로딩 편차만 있어도 권취 시 이바리(게이지 밴드)와 슬리팅 후 캠버(Camber, 휨)로 증폭됩니다. 또한 에너지 밀도를 높이려 로딩량을 올리면 건조 열풍을 강하게 불어야 하는데 이때 바인더가 표면으로 쏠리는 마이그레이션 위험이 급증합니다. 그래서 저는 Shim Offset 전동화로 폭 누적공차를 잡고, 항률 건조 구간 온도 최적화로 후막 코팅 품질을 안정화했습니다."
                )
            },
            {
                "tag": "간헐/2패턴/절연코팅 검증",
                "question": "간헐코팅, 스트라이프코팅, 2패턴코팅, 절연코팅을 모두 운영해 보셨는데, 이 중 셋업 조건을 잡기 가장 까다로웠던 공법은 무엇이고 어떻게 관리하셨나요?",
                "intent": "경력 기술서 12번 라인의 특수 코팅 기법들에 대한 실무 노하우를 묻는 질문입니다.",
                "answer": (
                    "<strong>간헐 코팅(Intermittent Coating)과 절연 코팅(Insulating Overlay Coating)</strong>이 가장 정밀한 타이밍과 유체 제어를 요구했습니다.<br><br>"
                    "간헐 코팅은 슬러리 공급 밸브가 초당 수회씩 On/Off를 반복하며 유지부와 무지부를 교차 형성하는데, 밸브 개폐 응답성이나 다이 내부 압력 밸런스가 흔들리면 코팅 시작부(Head)가 두껍게 뭉치거나 끝단(Tail)이 길게 끌리는 테일링(Tailing) 불량이 발생해 전·후면(A/B면) 미스매치가 생깁니다. "
                    "또한 절연 코팅은 활물질 코팅층과 무지부 경계 위에 얇은 세라믹/고분자 절연층을 정확히 겹쳐 발라야 해서 코팅 폭이 수백 $\\mu\\text{m}$만 틀어져도 절연 불량이나 탭 침범이 발생합니다. 이를 해결하기 위해 앞서 말씀드린 LVDT 기반 Shim 미세조절장치와 밸브 개폐 압력 피드백 최적화를 통해 초기 셋업 Loss를 획기적으로 줄였습니다."
                )
            },
            {
                "tag": "Risk Range 산정 검증",
                "question": "품질 사고 대책 관리에서 QMS, MES, EioT, Spotfire를 활용해 'Risk Range(위험 범위)'를 확인하셨다고 했는데, 불량이 났을 때 Risk Range는 구체적으로 어떻게 좁히나요?",
                "intent": "품질 이슈 발생 시 무조건 전 물량을 폐기하지 않고 데이터로 오염 범위를 정밀 구획하는 실무 능력을 확인하는 질문입니다.",
                "answer": (
                    "품질 이슈가 발생했을 때 Risk Range를 정확히 특정하지 못하면 정상 양품 Lot까지 수억 원어치를 통째로 폐기하거나 반대로 불량이 섞여 나가는 대참사가 발생합니다.<br><br>"
                    "저는 먼저 <strong>MES와 QMS에서 원재료(슬러리 배치, Foil Lot) 이력과 작업자·설비 변경점을 역추적</strong>하고, 동시에 <strong>EioT에 기록된 코터 설비 파라미터(다이 압력, 모노펌프 유량, 오븐 온도/풍속, 웹게이지 스캔 Raw 데이터)를 Spotfire로 불러와 시계열 다변량 분석</strong>을 수행합니다. 이를 통해 파라미터가 정상 범위를 이탈한 정확한 시작 시점(Start Timestamp & 권취 미터수)과 정상 복귀 시점(End Timestamp)을 앞뒤 안전 마진까지 포함해 구획함으로써, 폐기 손실은 최소화하고 고객 유출 위험은 0%로 차단했습니다."
                )
            },
            {
                "tag": "SOP 및 오퍼레이터 교육",
                "question": "SOP 개발 및 작업자 교육(PLM), 원재료·월마감(ERP)까지 폭넓게 하셨는데, 신규 라인에서 오퍼레이터 교육 시 가장 중점을 두는 부분은 무엇인가요?",
                "intent": "생산운영 직무의 현장 관리 및 표준화 역량을 확인하는 질문입니다.",
                "answer": (
                    "신규 라인 오퍼레이터 교육에서 가장 중요한 것은 <strong>‘추상적인 지시어를 없애고 숫자와 시각적 기준으로 행동하게 만드는 것’</strong>입니다.<br><br>"
                    "예를 들어 SOP에 ‘볼트를 적당히 단단하게 조인다’거나 ‘주름이 나면 장력을 조금 줄인다’고 적어두면 작업자마다 다르게 행동해 산포가 발생합니다. 저는 슬롯 다이 조립 시 <strong>정확한 토크렌치 수치($\\text{N}\\cdot\\text{m}$)</strong>를 명시하고, 설비 이상이나 미세라인 알람 발생 시 작업자가 임의로 판단해 리셋하지 못하도록 <strong>단계별 조치 사진과 인터록 해제 기준을 1페이지 시각화된 원포인트 레슨(OPL) 및 PLM 표준 문서</strong>로 만들어 교육함으로써 교대조 간 품질 편차를 없앴습니다."
                )
            }
        ]
    },
    {
        "badge": "특화 무기 · 나만의 AI 에이전트 워크플로우 · 본기함구",
        "nav_title": "[특화 무기] 나만의 AI 에이전트 워크플로우 (본·기·함·구)",
        "title": "[특화 무기] 단순 챗봇을 넘어선 ‘AI 에이전트 워크플로우(Agentic Workflow)’: Context-Tool-Result 구조화와 본·기·함·구 파이썬 빌드업",
        "context_summary": [
            "<strong>핵심 차별점</strong>: AI를 웹 채팅창에 산발적으로 묻는 챗봇으로 쓰지 않고, 데이터 오염과 환각(Hallucination)을 제어하고 100% 재현성을 확보하는 <strong>‘에이전트 워크플로우’</strong>를 직접 구축하여 실무에 적용.",
            "<strong>프로토콜 1 — 구조화</strong>: `rules.md`를 통해 코딩 규칙과 보안 대전제를 가드레일로 고정하고, 원천 데이터인 <strong>`Context`(Read-Only)</strong>, 실행 스크립트인 <strong>`Tool`(원클릭 `run.bat`)</strong>, 산출물인 <strong>`Result`(대시보드 & 리포트)</strong> 폴더를 엄격히 분리하여 오직 신뢰할 수 있는 도메인 데이터 기반으로만 추론하도록 통제.",
            "<strong>프로토콜 2 — 점진적 파이썬 코딩 빌드업 (본·기·함·구)</strong>: 사용자·개발자·PM으로 역할을 분리해 PRD를 작성하고, ① <strong>본(本)</strong>: 문제의 본질 파악 지시, ② <strong>기(機)</strong>: 문장을 기능적 단위로 분리, ③ <strong>함(函)</strong>: 기능 단위로 함수화 및 예외 처리, ④ <strong>구(構)</strong>: 구조를 리빌딩할지 단순 덧붙일지 제시하게 하여 건물을 짓듯 코드를 완성."
        ],
        "base_speech": (
            "“네, 저는 AI를 단순 챗봇으로 쓰는 것을 넘어, 환각(Hallucination)을 제어하고 재현성을 확보하는 ‘에이전트 워크플로우(Agentic Workflow)’를 직접 구축하여 개발합니다. 웹 채팅창에 산발적으로 질의하면 데이터 오염과 환각이 발생해 실무에 적용할 수 없기 때문입니다. "
            "첫째는 ‘구조화’입니다. `rules.md`를 통해 코딩 규칙과 보안 대전제를 가드레일로 고정하고, 원천 데이터인 `Context`, 실행 스크립트인 `Tool`, 산출물인 `Result` 폴더를 엄격히 분리하여 AI가 오직 신뢰할 수 있는 도메인 데이터 기반으로만 추론하도록 통제합니다. "
            "둘째는 ‘점진적 파이썬 코딩 빌드업(본·기·함·구)’입니다. 먼저 사용자·개발자·PM으로 역할을 분리해 PRD를 작성합니다. 이후 문제의 본질을 파악하도록 지시하고(본), 문장을 기능적인 단위로 분리합니다(기). 이를 통해 기능 단위로 함수화하고(함), 구조를 리빌딩할지 단순 덧붙일지 제시하게 하여(구) 건물을 짓듯이 쪼개어 코드를 완성합니다. "
            "이러한 AI 엔지니어링 체계를 바탕으로 입사 후에도 현장 도메인 지식에 AI 에이전트를 결합하여 팀의 업무 생산성을 극대화하겠습니다.”"
        ),
        "svg_title": "📊 [나만의 AI 에이전트 엔지니어링 체계] Context-Tool-Result 데이터 무결성 격리 + 본·기·함·구 4단계 파이썬 빌드업",
        "svg": """<svg viewBox="0 0 960 250" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="250" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <g transform="translate(20, 20)">
    <rect width="450" height="210" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="11.5" font-weight="800">1. 첫째 프로토콜: 구조화 (rules.md &amp; Context-Tool-Result)</text>
    <rect x="16" y="42" width="418" height="152" rx="6" fill="#1e293b"/>
    <text x="26" y="66" fill="#fde047" font-size="9" font-weight="700">• rules.md 가드레일 고정: 코딩 규칙·보안 대전제·임의 추측 금지 강제</text>
    <text x="26" y="90" fill="#38bdf8" font-size="8.8" font-weight="700">• Context/ (원천 데이터 Read-Only): data_dict.md 선행, 원본 오염 0%</text>
    <text x="26" y="112" fill="#fbbf24" font-size="8.8" font-weight="700">• Tool/ (실행 스크립트): Result와 1:1 버전 매칭, 원클릭 run.bat 동봉</text>
    <text x="26" y="134" fill="#34d399" font-size="8.8" font-weight="700">• Result/ (산출물): PRD, 마스터 보고서, 인터랙티브 HTML 대시보드</text>
    <text x="26" y="164" fill="#6ee7b7" font-size="8">➔ 웹 채팅창의 휘발성·환각을 극복하고 100% 재현 가능한 엔지니어링 자산화!</text>
  </g>
  <g transform="translate(490, 20)">
    <rect width="450" height="210" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="11.5" font-weight="800">2. 둘째 프로토콜: 점진적 파이썬 빌드업 (본·기·함·구)</text>
    <rect x="16" y="42" width="418" height="152" rx="6" fill="#1e293b"/>
    <text x="26" y="66" fill="#38bdf8" font-size="9" font-weight="700">① 본(本): 자연어 요구사항 이면의 진짜 엔지니어링 문제 본질 파악</text>
    <text x="26" y="90" fill="#fde047" font-size="9" font-weight="700">② 기(機): 사용자·개발자·PM 역할 분리로 기능 단위 분해 &amp; PRD 작성</text>
    <text x="26" y="114" fill="#c084fc" font-size="9" font-weight="700">③ 함(函): 독립 재사용 가능한 함수 단위 모듈화 &amp; 방어적 예외 처리</text>
    <text x="26" y="138" fill="#34d399" font-size="9" font-weight="700">④ 구(構): 구조 리빌딩(Rebuilding) vs 단순 추가(Append) 검토 후 완성</text>
    <text x="26" y="166" fill="#6ee7b7" font-size="8">➔ 건물을 짓듯 단계별로 쪼개어 검증함으로써 스파게티 코드 및 오류 원천 차단</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "AI 환각 통제 검증",
                "question": "AI를 실무에 쓸 때 가장 큰 문제가 '환각(Hallucination, 거짓 정보)'인데, 본인의 워크플로우에서는 어떻게 환각을 잡나요?",
                "intent": "`context` 문서 154~160번 라인의 AI 프로토콜이 실제로 어떻게 환각을 막는지 구체적 메커니즘을 묻는 질문입니다.",
                "answer": (
                    "환각이 발생하는 근본 원인은 AI에게 도메인 제약 조건 없이 너무 추상적이고 큰 작업을 한 번에 시키기 때문입니다.<br><br>"
                    "저는 이를 두 가지 장치로 잡습니다. 첫째, 코딩에 들어가기 전 반드시 원천 데이터의 컬럼과 물리적 단위(`mm`, `μm`, `ms`), 결측치 기준을 명시한 <strong>데이터 사전(`data_dict.md`)과 입출력 스펙(`PRD.md`)을 먼저 쓰게 하여 제가 사람이 직접 승인(Gate)</strong>합니다. "
                    "둘째, <strong>‘본·기·함·구’</strong> 프로토콜을 통해 한 번에 통짜 코드를 짜게 하지 않고, 작은 기능 단위의 파이썬 함수(함, 函)로 쪼개어 단위 테스트를 거친 뒤 조립합니다. 또한 원천 데이터(`Context`)는 절대 AI가 직접 수정하지 못하고 파이썬 스크립트(`Tool`)를 통해서만 계산 결과를 내도록 격리했기 때문에 숫자 왜곡이나 환각이 끼어들 틈이 없습니다."
                )
            },
            {
                "tag": "역할 분리(PM/개발자) 검증",
                "question": "점진적 빌드업에서 '사용자·개발자·PM으로 역할을 분리하여 PRD를 작성한다'고 하셨는데, 이게 구체적으로 어떻게 진행되는 건가요?",
                "intent": "`context` 문서 159번 라인의 역할 분리 PRD 작성법을 실제로 어떻게 운용하는지 묻는 질문입니다.",
                "answer": (
                    "하나의 문제를 놓고 세 가지 관점으로 검증하는 방식입니다.<br><br>"
                    "먼저 <strong>‘현장 사용자(엔지니어/오퍼레이터)’ 관점</strong>에서는 ‘어떤 데이터를 넣었을 때 어떤 버튼 하나로 어떤 그래프가 나와야 쓰기 편한가’를 정의합니다. "
                    "다음으로 <strong>‘PM(프로젝트 매니저)’ 관점</strong>에서는 이 요구사항을 기능적 단어로 쪼개어 우선순위와 예외 상황(데이터 누락 시 처리 등)을 정리한 <strong>입출력 스펙 문서(`PRD.md`)</strong>로 구조화합니다. "
                    "마지막으로 <strong>‘개발자’ 관점</strong>에서는 승인된 PRD의 각 기능을 독립된 파이썬 함수 모듈로 구현하고 `run.bat`으로 패키징합니다. 이렇게 역할을 분리하면 현장에서 쓰기 불편한 과잉 개발이나 요구사항 누락 없이 한 번에 실무에 바로 쓸 수 있는 도구가 완성됩니다."
                )
            },
            {
                "tag": "실제 적용 사례 연결",
                "question": "이 '본·기·함·구' AI 프로토콜을 사용해서 실제로 현업에서 가장 빠르게 해결했던 프로젝트가 무엇인가요?",
                "intent": "AI 프로토콜과 앞선 실무 프로젝트(IPQC 자동화, 100만 장 비전 엔진)의 연결고리를 확인하는 질문입니다.",
                "answer": (
                    "앞서 말씀드린 <strong>‘인라인 IPQC 데이터 검토 자동화(월 40시간 절감)’와 ‘100만 장 실오라기 Burr 비전 선별 엔진(72시간 내 완수)’</strong> 모두 이 프로토콜 덕분에 단기간에 무결점으로 완성할 수 있었습니다.<br><br>"
                    "특히 100만 장 Burr 선별 당시 데드라인이 72시간밖에 없었는데, 마음이 급하다고 바로 코딩부터 한 것이 아니라 먼저 <strong>‘본(국소 음영 낙차와 세로 연속성)’</strong>과 <strong>‘기(이원화 Valley 모듈 + $1\\times 7$ Bridge Kernel 모듈 PRD)’</strong>를 명확히 정의하고 함수 단위로 쪼개어 개발했기 때문에, 중간에 Lot 간 밝기 편차 난관이 터졌을 때도 전체 코드를 갈아엎지 않고 앞단 Valley 함수만 빠르게 리빌딩(구, 構)하여 제시간에 미검률 0%를 달성할 수 있었습니다."
                )
            },
            {
                "tag": "보안 및 사내 적용성",
                "question": "현대자동차 역시 배터리 레시피와 공정 데이터 보안이 매우 엄격합니다. 외부 AI에 데이터를 올리지 않고도 이 방식을 쓸 수 있나요?",
                "intent": "사내 보안 준수 의식과 로컬 파이썬 도구화 역량을 확인하는 질문입니다.",
                "answer": (
                    "네, 보안 규정을 100% 준수하기 위해 만든 구조가 바로 `Context-Tool-Result` 분리 아키텍처입니다.<br><br>"
                    "실제 대외비 공정 수치나 레시피가 담긴 `Context` 원천 파일은 외부로 절대 반출하거나 프롬프트에 넣지 않습니다. 오직 <strong>컬럼 구조와 물리적 단위만 적힌 가상의 스키마(`data_dict.md`)와 알고리즘 수식 요구사항(`PRD.md`)만으로 사내 허용된 AI 환경에서 파이썬 코드(`Tool`)를 작성</strong>하고, 실제 데이터 처리는 사내 폐쇄망 PC의 로컬 파이썬 엔진 안에서만 실행되기 때문에 보안 사고 위험 없이 안전하게 자동화를 구축할 수 있습니다."
                )
            }
        ]
    },
    {
        "badge": "전극 공정 도메인 · 코터 80% 결정론 · 바인더 마이그레이션 · 기계요소",
        "nav_title": "[도메인 & 확장성] 코터·바인더 마이그레이션·타 공정 확장",
        "title": "[전극 공정 도메인 완전 정복] 왜 코터가 품질의 80%를 결정하는가, 타 공정(믹싱·프레스·슬리팅) 확장성, 바인더 마이그레이션 5단계 및 기계 체결 정밀도",
        "context_summary": [
            "<strong>왜 코터만 했는가 & 타 공정 확장성</strong>: 코터는 배터리 품질과 원가의 <strong>80% 이상을 결정짓는 핵심 공정</strong>. 롤프레스나 슬리팅과 달리 코터에서 발생한 <strong>로딩량 편차, 코팅폭 불균일, 건조 크랙, 바인더 마이그레이션은 후공정에서 절대 되돌릴 수 없으며</strong> 셀의 N/P Ratio 불균형과 급속충전 리튬 덴드라이트 석출로 직결됨. 5년간 전후 공정(믹싱·프레스·슬리팅)과 밀접히 협업했기에 타 공정도 즉시 수행 가능.",
            "<strong>바인더 마이그레이션 5단계 & 해결책</strong>: ① Wet 슬러리 균일 분포 ➔ ② 건조 오븐 열풍에 의한 최외곽 표면 용매 증발 ➔ ③ <strong>모세관 압력(Capillary Force)에 의한 하부 용매의 표면 상승 대류(Convective Flux)</strong> ➔ ④ 바인더 고분자의 표면 동반 상승 ➔ ⑤ 고화 임계점(Consolidation Point)에서 표면 바인더 편석 및 하부(Foil 계면) 바인더 고갈 ➔ 접착력 저하 및 미세크랙 유발. (<strong>해결: 항률 구간 온도 하향 완속 건조 유도 + 슬러리 고형분 상향</strong>).",
            "<strong>배터리 3대 공정(전극·조립·활성화), 슬러리 물성(고형분·점도·분산·그라인드게이지·입도 $D_{50}/D_{max}$), 체결 토크 정밀도</strong> 완벽 숙지."
        ],
        "base_speech": (
            "“코터가 배터리 품질과 원가의 80% 이상을 결정짓는 핵심 공정이기 때문에 지난 5년간 코터 공정을 깊이 있게 파고들었습니다. "
            "후공정인 롤프레스나 슬리팅에서 발생하는 문제는 공정 조건으로 일부 보정이 가능하지만, 코터에서 발생한 로딩량 편차, 코팅폭 불균일, 건조 크랙, 바인더 마이그레이션은 후공정에서 절대 되돌릴 수 없으며 곧바로 셀의 N/P Ratio 불균형과 급속충전 시 리튬 덴드라이트 석출로 이어집니다. "
            "저는 5년간 롤투롤 장비의 텐션, 슬롯 다이 메커니즘, 건조존의 열풍 밸런스, 무지부 주름, 그리고 토크렌치를 통한 기계적 체결 정밀도까지 모든 물리적 변수를 장악했습니다. "
            "또한 코터 문제를 풀기 위해 앞단 믹싱 물성과 뒷단 롤프레스·슬리팅 공정과 매일 협업해 왔기에 어떤 전극 공정이라도 누구보다 빠르게 안착해 성과를 낼 자신이 있습니다.”"
        ),
        "svg_title": "📊 [전극 공정 전 주기(Mixing ➔ Coating ➔ Roll Press ➔ Slitting) 상호작용 및 바인더 마이그레이션 5단계 제어 도해]",
        "svg": """<svg viewBox="0 0 960 280" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <!-- Left: Electrode 4 Processes Hub -->
  <g transform="translate(20, 20)">
    <rect width="450" height="240" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="11.5" font-weight="800">1. 전극 4대 공정 연계성: 왜 코터(Coating)가 핵심 허브인가?</text>
    <rect x="16" y="42" width="418" height="182" rx="6" fill="#1e293b"/>
    <text x="26" y="64" fill="#fde047" font-size="9" font-weight="700">① 믹싱 (Mixing) ➔ 코터 인입 물성 결정</text>
    <text x="34" y="80" fill="#cbd5e1" font-size="8">• 고형분(용매 제외 고체 비율), 점도(내부마찰저항), 분산도(그라인드게이지), 입도(D50/Dmax)</text>
    <text x="26" y="104" fill="#38bdf8" font-size="9" font-weight="700">② 코팅 (Coating) — ★ 배터리 품질·원가 80% 결정 (비가역 공정!)</text>
    <text x="34" y="120" fill="#fca5a5" font-size="8">• 로딩량 산포, 코팅폭 불균일, 건조 크랙, 바인더 마이그레이션은 후공정 보정 불가!</text>
    <text x="34" y="136" fill="#cbd5e1" font-size="8">• 텐션 제어, 슬롯 다이 Shim/체결 토크, 건조존 열풍 밸런스 통합 제어</text>
    <text x="26" y="160" fill="#34d399" font-size="9" font-weight="700">③ 압연 (Roll Pressing) &amp; ④ 슬리팅 (Slitting)</text>
    <text x="34" y="176" fill="#cbd5e1" font-size="8">• 코터의 Fat Edge ➔ 압연 시 과압연/캠버/단선 유발 | 코터 에지 불량 ➔ 슬리팅 Burr 유발</text>
    <text x="34" y="198" fill="#6ee7b7" font-size="8" font-weight="700">➔ 코터 전문가는 필연적으로 믹싱·프레스·슬리팅 전 공정의 인과관계를 통달!</text>
  </g>
  <!-- Right: Binder Migration 5 Steps -->
  <g transform="translate(490, 20)">
    <rect width="450" height="240" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">2. 바인더 마이그레이션 5단계 물리 메커니즘 &amp; 건조 솔루션</text>
    <rect x="16" y="42" width="418" height="182" rx="6" fill="#1e293b"/>
    <text x="26" y="62" fill="#e2e8f0" font-size="8.2"><tspan fill="#38bdf8" font-weight="700">1단계(초기 Wet):</tspan> 활물질·도전재·바인더(PVDF/SBR·CMC)·용매(NMP/물) 균일 분포</text>
    <text x="26" y="80" fill="#e2e8f0" font-size="8.2"><tspan fill="#38bdf8" font-weight="700">2단계(표면 증발):</tspan> 오븐 열풍/복사열 인가 시 전극 최외곽 표면부터 용매 증발 시작</text>
    <text x="26" y="98" fill="#e2e8f0" font-size="8.2"><tspan fill="#fde047" font-weight="700">3단계(모세관 대류):</tspan> 표면 빈 공간을 채우려 하부(Foil쪽) 용매가 모세관력으로 급상승</text>
    <text x="26" y="116" fill="#e2e8f0" font-size="8.2"><tspan fill="#fde047" font-weight="700">4단계(동반 상승):</tspan> 용매 흐름(Convective Flux)에 휩쓸려 바인더가 상부 표면으로 이동</text>
    <text x="26" y="134" fill="#fca5a5" font-size="8.2" font-weight="700">5단계(편석 고착): 고화 임계점 도달 시 표면 바인더 밀집(크랙) &amp; Foil 계면 고갈(박리!)</text>
    <line x1="26" y1="148" x2="418" y2="148" stroke="#475569" stroke-width="1"/>
    <text x="26" y="168" fill="#34d399" font-size="8.8" font-weight="800">✔ 현장 해결책 2가지:</text>
    <text x="34" y="186" fill="#6ee7b7" font-size="8">① <tspan fill="#ffffff" font-weight="700">항률 건조 구간 온도 하향</tspan> (표면 증발 속도 늦춰 완속 건조 유도)</text>
    <text x="34" y="204" fill="#6ee7b7" font-size="8">② <tspan fill="#ffffff" font-weight="700">슬러리 고형분(Solid Content) 상향</tspan> (증발시킬 용매 절대량 축소)</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "왜 코터만 했는가 & 타 공정 확장",
                "question": "이력서를 보면 5년간 코터 공정만 담당하셨는데, 현대차에 오셔서 믹싱이나 롤프레스, 슬리팅 같은 다른 전극 공정을 맡게 된다면 잘할 수 있겠습니까?",
                "intent": "`context` 문서 169~174번 라인('왜 코터만 했어요?', '다른 공정도 할 수 있겠어요?')을 통합 검증하는 필수 질문입니다.",
                "answer": (
                    "<strong>네, 자신 있습니다.</strong> 제가 5년간 코터 공정을 집중적으로 담당한 이유는 코터가 배터리 품질과 원가의 80% 이상을 결정짓는 가장 핵심적이고 난이도 높은 공정이기 때문입니다.<br><br>"
                    "후공정인 롤프레스나 슬리팅에서 발생하는 문제는 공정 조건으로 일부 보정이 가능하지만, 코터에서 발생한 로딩량 산포, 코팅폭 불균일, 건조 크랙, 바인더 마이그레이션은 후공정에서 절대 되돌릴 수 없습니다. "
                    "특히 코터의 문제를 해결하려면 필연적으로 <strong>앞단 믹싱의 슬러리 물성(고형분, 점도, 그라인드게이지, 입도 $D_{50}/D_{max}$)을 분석해 역제안해야 했고, 뒷단 롤프레스의 압연 연신율과 슬리팅의 Burr·캠버 문제를 함께 풀어야 했기 때문에 지난 5년간 전극 전 공정 엔지니어들과 한 팀처럼 협업</strong>해 왔습니다. 따라서 다른 전극 공정에 배치되더라도 앞서 보여드린 설비 개조와 데이터 모델링 역량으로 누구보다 빠르게 성과를 내겠습니다."
                )
            },
            {
                "tag": "바인더 마이그레이션 5단계",
                "question": "건조 공정에서 발생하는 '바인더 마이그레이션(Binder Migration)'의 발생 메커니즘을 단계별로 설명해 주시고, 현장에서 오븐 조건과 슬러리 조건을 각각 어떻게 잡아야 하는지 말씀해 주세요.",
                "intent": "`context` 문서 204~221번 라인의 바인더 마이그레이션 5단계와 항률 구간 온도 제어·고형분 관계를 정확히 물어보는 핵심 도메인 질문입니다.",
                "answer": (
                    "바인더 마이그레이션은 총 <strong>5단계 물리적 과정</strong>을 거쳐 발생합니다.<br>"
                    "1. <strong>초기 슬러리 상태</strong>: Foil 위에 도포된 젖은(Wet) 슬러리 내부에는 활물질, 도전재, 바인더(양극 PVDF, 음극 SBR/CMC), 용매(NMP 또는 물)가 균일하게 섞여 있습니다.<br>"
                    "2. <strong>건조 시작 및 표면 증발</strong>: 건조 오븐에서 열풍이나 복사열을 가하면 전극의 최외곽 표면에서부터 용매가 증발하기 시작합니다.<br>"
                    "3. <strong>모세관 압력에 의한 대류(Convective Flux)</strong>: 표면의 용매가 날아가면 빈 공간을 채우기 위해 전극 내부와 하부(Foil 쪽)에 있던 액체 용매가 <strong>모세관 현상(Capillary Force)</strong>에 의해 표면 쪽으로 강하게 빨려 올라옵니다.<br>"
                    "4. <strong>바인더의 동반 상승</strong>: 이때 용매에 용해되거나 미세 입자로 분산되어 있던 바인더 고분자가 용매의 상승 흐름에 휩쓸려 전극 상부 표면으로 함께 이동합니다.<br>"
                    "5. <strong>편석(Segregation) 고착</strong>: 고형분이 굳어지는 임계점(Consolidation Point)에 도달하면 바인더가 표면 쪽에만 빽빽하게 뭉쳐 급격한 건조 수축에 의한 <strong>미세 크랙</strong>을 유발하고, 정작 집전체(Foil)와 맞닿는 하부에는 바인더가 텅 비어버려 <strong>접착력 저하(박리)</strong>가 발생합니다.<br><br>"
                    "<strong>[현장 해결책]</strong> 오븐 건조 조건에서는 용매가 일정한 속도로 활발히 날아가는 <strong>‘항률 건조 구간(초기 Zone)’의 온도를 낮추어 표면 증발 속도를 늦추는 완속 건조</strong>를 유도해야 합니다. 또한 슬러리 물성 측면에서는 용매를 제외한 고체의 순수 무게 비율인 <strong>‘고형분(Solid Content)’을 높여</strong> 애초에 날려 보내야 할 용매의 절대량을 줄여줌으로써 모세관 상승 대류를 억제할 수 있습니다."
                )
            },
            {
                "tag": "슬러리 물성 & 계측기 검증",
                "question": "믹싱에서 넘어오는 슬러리의 품질을 확인할 때 '점도', '분산', '그라인드게이지', '입도(D50, Dmax)'를 보게 되는데 각각의 정의와 코터에서의 중요성을 설명해 주세요.",
                "intent": "`context` 문서 222~225번 라인의 슬러리 물성 용어 정의를 정확히 숙지하고 있는지 확인하는 질문입니다.",
                "answer": (
                    "• <strong>점도(Viscosity)</strong>는 유체가 흐를 때 발생하는 <strong>내부 마찰 저항</strong>으로, 슬롯 다이 토출 압력과 에지 슬라이딩(퍼짐성)을 결정짓는 핵심 지표입니다.<br>"
                    "• <strong>분산(Dispersion)</strong>은 도전재나 활물질 입자가 뭉치지 않고 용매 속에 낱개로 고르게 퍼져 있는 상태를 뜻합니다.<br>"
                    "• <strong>그라인드게이지(Grind Gauge)</strong>는 이 분산도를 현장에서 직관적으로 재는 측정기로, 깊이가 연속적으로 얕아지는 홈에 슬러리를 밀어 넣었을 때 <strong>몇 $\\mu\\text{m}$ 깊이에서 응집된 입자가 긁히거나 돌출되어 스크래치(줄무늬)가 발생하는지</strong>를 확인합니다.<br>"
                    "• <strong>입도(Particle Size Distribution)</strong>는 입자 크기의 누적 분포인데, <strong>$D_{50}$은 크기순으로 정중앙에 있는 평균 입자 크기</strong>이고, <strong>$D_{max}$는 가장 큰 덩어리의 크기</strong>입니다. 특히 $D_{max}$나 그라인드게이지 수치가 높으면 슬롯 다이 립(Lip) 간격에 덩어리가 끼어 코팅 라인 불량(미세라인/줄무늬)을 일으키므로 코터 투입 전 반드시 확인해야 합니다."
                )
            },
            {
                "tag": "기계적 체결 토크와 주름",
                "question": "기계공학 전공이 아닌데도 현장에서 기계적 정밀도에 대해 깊이 배우셨다고 했습니다. 슬롯 다이를 조립할 때 작업자의 '감'으로 볼트를 조이면 왜 코팅 품질에 문제가 생기나요?",
                "intent": "`context` 문서 179~181번 라인('느낀점 1. 기계요소: 체결토크와 미세유격, 슬롯다이 볼트와 주름')을 물어보는 질문입니다.",
                "answer": (
                    "현장에서 직접 부딪히며 <strong>‘기계적 정밀도는 결국 체결 토크와 미세 유격에서 온다’</strong>는 것을 절실히 배웠습니다.<br><br>"
                    "슬롯 다이는 스테인리스(SUS)로 된 무거운 상·하부 다이 바디 사이에 얇은 심(Shim)을 끼우고 수십 개의 볼트로 체결하는 구조입니다. 만약 이 볼트들을 작업자의 손감각에 의존해 조이면 볼트마다 체결력이 달라져 <strong>강철 다이 바디가 마이크로미터($\\mu\\text{m}$) 단위로 미세하게 뒤틀리고 폭 방향 립(Lip) 단차</strong>가 발생합니다. "
                    "이 미세한 단차가 코팅 시에는 좌우 로딩량(두께) 편차를 만들고, 결과적으로 건조 및 권취 구간에서 좌우 장력 불균형에 의한 <strong>치명적인 사선주름과 단선</strong>으로 이어진다는 것을 확인했습니다. 그래서 저는 반드시 교정된 <strong>토크렌치(Torque Wrench)를 사용해 대각선 순서로 균일한 정량 토크를 인가</strong>하도록 작업 표준을 확립했습니다."
                )
            },
            {
                "tag": "배터리 기본 원리 스피치",
                "question": "비전공자나 신입 오퍼레이터에게 '리튬이온 배터리의 동작 원리'와 '왜 전해액 대신 분리막과 외부 도선이 필요한지'를 1분 안에 쉽게 설명해 보시겠어요?",
                "intent": "`context` 문서 194~203번 라인(배터리 동작 원리 1분 스피치 및 전해액의 절연 특성)을 확인하는 기본기 질문입니다.",
                "answer": (
                    "리튬이온 배터리의 핵심 원리는 양극, 음극, 전해액, 분리막 사이에서 일어나는 <strong>리튬이온($\\text{Li}^+$)과 전자($e^-$)의 산화·환원 반응</strong>입니다.<br><br>"
                    "먼저 <strong>충전(Charging)</strong> 시에는 외부 전원의 힘으로 리튬이온이 양극에서 빠져나와 전해액을 타고 음극(흑연/실리콘) 층간으로 이동하며, 전자는 외부 도선을 따라 음극으로 이동해 높은 위치 에너지를 축적합니다. "
                    "반대로 <strong>방전(Discharging)</strong> 시에는 음극에 저장되어 있던 리튬이온이 다시 전해액을 통해 양극으로 돌아가고, 전자는 외부 도선을 타고 흐르면서 모터를 돌리는 전기 에너지를 발생시킵니다.<br><br>"
                    "여기서 <strong>전해액은 이온만 이동시킬 수 있을 뿐 자유전자가 없는 유기화합물(절연체 역할)</strong>이기 때문에 전자는 전해액을 통과하지 못하고 반드시 외부 도선으로만 흐릅니다. 즉, <strong>분리막을 통해 양·음극의 물리적 접촉에 의한 단락(Short)을 막으면서, 리튬이온은 전해액 내부로, 전자는 외부 도선으로 분리 이동시키는 연속적인 과정</strong>이 배터리 동작의 본질입니다."
                )
            }
        ]
    }
]
