# MD Studio

선형 HTML 세그먼트 스캐너, Shadow DOM 격리, 적응형 목차(TOC) & 스크롤스파이, 정밀 텍스트 노드 매핑 캐럿 네비게이션, 대용량 문서 안정성을 지원하는 단일 파일 마크다운 에디터

- **버전**: 2.1.0
- **라이브 URL**: [https://okjoizj-org.github.io/md-studio/](https://okjoizj-org.github.io/md-studio/)

## 주요 기능
- **선형 HTML 세그먼트 스캐너 (Linear HTML Segment Scanner)**: 따옴표 안의 `>`, 중첩 태그, HTML 주석, SVG, MathML, 사용자 정의 태그를 문자 단위 상태 머신으로 해석하여 HTML 파싱 오류 및 태그 깨짐 원천 차단
- **Shadow DOM 렌더링 격리**: 미리보기 영역을 Shadow DOM으로 완전 격리하여 문서 내부의 `<style>`이나 인라인 CSS가 에디터 UI(상단바, 툴바, 상태바)를 오염시키지 않음
- **적응형 계층 목차 & 애플 글래스모피즘 팝오버 (Hierarchical TOC & Exact Scrollspy)**: H1, H2, H3 계층별 1px 헤어라인 트리와 실시간 섹션 강조, 말줄임 처리, 키보드 포커스 링을 갖춘 아크릴 팝오버 제공
- **정밀 문자 단위 미리보기 ↔ 에디터 커서 매핑 (Precision Sub-Character Caret Mapping)**: 굵게, 기울임, 인라인 코드, 링크, 반복 단어, 다국어 문맥에서 클릭 지점의 텍스트 노드와 마크다운 소스 오프셋을 오차 없이 1:1 역추적
- **인라인 코드 vs Fenced 코드 블록 분리**: 본문 인라인 코드는 슬림 칩 스타일로 가독성을 극대화하고, 다중행 코드 블록은 언어명 라벨과 가로 스크롤 컨테이너로 격리
- **도착 시점 동기화 점멸 플래시 (Arrival-Synchronized Dual Flash Jump)**: 목차/미니맵 클릭 시 스크롤 이동이 목적지에 완전히 안착하는 순간 에디터와 미리보기 양쪽에서 점멸 플래시 발동
- **구간 보간 스크롤 동기화 (Piecewise Scroll Mapping)**: 전체 높이 비율이 아닌 인접 블록 앵커 사이를 구간 보간하여 양쪽 패널의 일치도 극대화
- **대용량 문서 최적화**: 220,000자 초과 시 에디터 구문 색칠을 자동 단순화하여 렌더 및 타이핑 성능 보장
- **단일 파일 완결성 (Zero CDN)**: 외부 의존성이나 네트워크 연결 없이 독립적으로 동작하는 단일 HTML 파일
