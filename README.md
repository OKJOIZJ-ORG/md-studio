# MD Studio

선형 HTML 세그먼트 스캐너, Shadow DOM 격리, 적응형 목차(TOC) & 스크롤스파이, 정밀 텍스트 노드 매핑 캐럿 네비게이션, 사용자 주도 양방향 차등 스크롤 동기화, 원클릭 싱크 재정렬, 마크다운 표-XML 태그 렉서 경계 가드를 지원하는 단일 파일 마크다운 에디터

- **버전**: 2.4.0
- **라이브 URL**: [https://okjoizj-org.github.io/md-studio/](https://okjoizj-org.github.io/md-studio/)

## 주요 기능 및 v2.4.0 업데이트
- **스크롤 최상단 천장(Ceiling) & 바닥(Floor) 경계 고정 (Boundary Clamping)**: 에디터를 최상단으로 드래그할 때 미리보기 창이 천장에 도달하지 못하던 뷰포트 오프셋 버그를 완벽히 수정 (`scrollTop <= 2 -> dst.scrollTop = 0` 및 12% 선형 블렌드)
- **HTML 렌더링 기본 활성화 (HTML Default ON)**: 실시간 아이폰 상태창, 글래스모피즘 카드, SVG 위젯이 기본적으로 완벽하게 렌더링되도록 기본 상태를 ON으로 전환
- **커스텀 XML 태그 시각 칩 상시 보장 (`isCustomXmlTag`)**: HTML 토글 상태(ON/OFF)와 무관하게 `<rp_engine>`, `<character>`, `<world>`, `<state_schema>`, `<state_logic>` 등 비표준 XML/RP 태그를 인식하여 시각 칩(`.xml-chip`)으로 100% 렌더링
- **MD Studio 사용 가이드 & 오픈소스 RP 시뮬레이션 프롬프트 분리 탑재**: 마크다운 볼드/표 오파싱을 방지하는 독립 HTML Bento Grid 가이드와 실전 오픈소스 1:1 RP 캐릭터 시뮬레이션 프롬프트(루멘 아카이브 - 아리아 벨라도나) 탑재
- **마크다운 표 & XML 태그 렉서 경계 가드 (Lexer Boundary Guard)**: 표 직후 빈 줄 없이 `</world>` 등 XML/HTML 태그가 이어질 때 표 내부 셀(`<td>`)로 흡수되던 렉서 버그 완전 수정
- **사용자 주도 자율 양방향 스크롤 동기화 (User-Driven Autonomy Scroll Sync)**: 사용자가 직접 조작(휠, 드래그, 터치, 타이핑)하는 창이 주도권을 갖고, 프로그래밍적 점프 시 스크롤 간섭 100% 차단
- **원클릭 싱크 즉시 재정렬 (One-Click Resync Button & Ctrl+Alt+S)**: 에디터와 미리보기의 스크롤 맵을 1클릭으로 완벽하게 재계산 및 정합 스냅
- **도착 시점 동기화 점멸 플래시 (Arrival-Synchronized Dual Flash Jump)**: 목적지 안착 시 에디터 `flashLine`과 미리보기 `source-flash` 선명한 펄스 재생
- **정밀 문자 단위 미리보기 ↔ 에디터 커서 매핑 (Precision Sub-Character Caret Mapping)**: 클릭 지점의 텍스트 노드와 마크다운 소스 오프셋을 오차 없이 1:1 역추적
- **Shadow DOM 렌더링 격리**: 미리보기 영역을 Shadow DOM으로 완전 격리하여 문서 내부의 `<style>`이나 인라인 CSS가 에디터 UI를 오염시키지 않음
- **적응형 계층 목차 & 애플 글래스모피즘 팝오버 (Hierarchical TOC & Exact Scrollspy)**: H1, H2, H3 계층별 1px 헤어라인 트리와 실시간 섹션 강조
- **단일 파일 완결성 (Zero CDN)**: 외부 의존성이나 네트워크 연결 없이 독립적으로 동작하는 단일 HTML 파일
