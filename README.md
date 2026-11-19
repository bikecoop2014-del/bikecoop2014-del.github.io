# 자전거문화사회적협동조합 (바이쿱) 홈페이지

바이쿱(자전거문화사회적협동조합)의 임시 공식 홈페이지입니다. GitHub Pages로 서비스됩니다.

- 주소: https://bikecoop2014-del.github.io/
- 구성: 단일 `index.html` (Tailwind CSS CDN + Vanilla JS), `logo.svg` / `logo.png`

## 페이지 구성

| 구역 | 내용 |
|---|---|
| 히어로 | 조합 로고, 슬로건 "자전거면 충분하다!!", 누적 교육 37만 명 |
| 조합소개 | 생태적 전환 · 지역 공동체 · 안전한 교육 |
| 연혁·성과 | 2014 설립인가 → 2020 행안부 장관상 → 2022 사회적기업 인증 → 2026 노원구 어린이교통공원 수탁(2027~2029) |
| 주요사업 | 찾아가는 자전거 안전교육 / 국토종주 투어 / 사회연대경제 우선구매 |
| 공식채널 | 네이버 스마트스토어(바이크프렌즈 사이클아카데미) · 인스타그램 @bikecoop2014 · 네이버 블로그 |
| 능력고사 | 자전거 안전지식 6문항, 합격 시 수료증 인쇄(PDF 저장) — 날짜는 접속일 기준 |
| 교육신청 | 오늘 기준 달력, 신청서 작성 후 전화 확인 안내 |

## 수정 방법

`index.html`을 직접 고쳐 `main` 브랜치에 커밋·푸시하면 1~2분 안에 반영됩니다.

```bash
git clone https://github.com/bikecoop2014-del/bikecoop2014-del.github.io.git
# index.html 수정 후
git commit -am "내용 수정" && git push
```

## 남은 작업

- 교육 신청 내역 저장: Google Apps Script 웹앱을 만들어 `SCRIPT_URL` 상수에 주소를 넣으면 자동 기록됩니다.
- 도메인 연결: `bikecoop.or.kr`을 연결할 때는 저장소에 `CNAME` 파일(`bikecoop.or.kr`)을 추가하고 도메인 DNS를 설정합니다.
