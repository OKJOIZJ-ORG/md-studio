# MD Studio

선형 HTML 세그먼트 스캐너, Shadow DOM 격리, 1:1 동기화 목차(TOC) 미니맵 & 양방향 점멸 플래시 네비게이션, 대용량 문서 안정성을 지원하는 단일 파일 마크다운 에디터

- **버전**: 2.0.0
- **라이브 URL**: [https://okjoizj-org.github.io/md-studio/](https://okjoizj-org.github.io/md-studio/)

## 주요 기능
- **선형 HTML 세그먼트 스캐너 (Linear HTML Segment Scanner)**: 따옴표 안의 `>`, 중첩 태그, HTML 주석, SVG, MathML, 사용자 정의 태그를 문자 단위 상태 머신으로 해석하여 HTML 파싱 오류 및 태그 깨짐 원천 차단
- **Shadow DOM 렌더링 격리**: 미리보기 영역을 Shadow DOM으로 완전 격리하여 문서 내부의 `<style>`이나 인라인 CSS가 에디터 UI(상단바, 툴바, 상태바)를 오염시키지 않음
- **적응형 계층 목차 & 1:1 동기화 미니맵 (Hierarchical TOC & Exact Scrollspy)**: 대용량 헤딩에서도 창살/바코드 현상 없이 여유롭고 단정한 미니멀 스파크라인 트랙과 애플 글래스모피즘 목차 팝오버 제공
- **도착 시점 동기화 점멸 플래시 (Arrival-Synchronized Dual Flash Jump)**: 목차/미니맵 클릭 시 스크롤 이동이 목적지에 완전히 안착하는 순간 에디터와 미리보기 양쪽에서 파란색 점멸 플래시가 동시에 발동
- **구간 보간 스크롤 동기화 (Piecewise Scroll Mapping)**: 전체 높이 비율이 아닌 인접 블록 앵커 사이를 구간 보간하여 양쪽 패널의 일치도 극대화
- **대용량 문서 최적화**: 220,000자 초과 시 에디터 구문 색칠을 자동 단순화하여 렌더 및 타이핑 성능 보장
- **단일 파일 실행**: 외부 의존성이나 CDN 없이 독립적으로 동작하는 단일 HTML 파일
