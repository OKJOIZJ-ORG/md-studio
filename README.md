# MD Studio

선형 HTML 세그먼트 스캐너, Shadow DOM 격리, 적응형 목차(TOC) & 스크롤스파이, 정밀 텍스트 노드 매핑 캐럿 네비게이션, 사용자 주도 양방향 차등 스크롤 동기화, 원클릭 싱크 재정렬, 대용량 문서 안정성을 지원하는 단일 파일 마크다운 에디터

- **버전**: 2.2.0
- **라이브 URL**: [https://okjoizj-org.github.io/md-studio/](https://okjoizj-org.github.io/md-studio/)

## 주요 기능
- **사용자 주도 자율 양방향 스크롤 동기화 (User-Driven Autonomy Scroll Sync)**: 사용자가 직접 조작(휠, 드래그, 터치, 타이핑)하는 창이 주도권을 갖고, 프로그래밍적 점프(TOC, 클릭 이동, 태그 점프) 시에는 스크롤 간섭을 100% 차단하여 튕김 현상 원천 박멸
- **원클릭 싱크 즉시 재정렬 (One-Click Resync Button & `Ctrl+Alt+S`)**: 어긋난 페이지나 뷰포트 중심 위치를 기준으로 에디터와 미리보기의 스크롤 맵을 1클릭으로 완벽하게 재계산 및 정합 스냅
- **도착 시점 동기화 점멸 플래시 (Arrival-Synchronized Dual Flash Jump)**: TOC/미니맵 클릭 시 부드러운 스크롤이 목적지에 완전히 안착한 순간 에디터의 `flashLine`과 미리보기의 `source-flash`를 선명하게 펄스 재생 (Emil Kowalski 애니메이션 원칙)
- **정밀 문자 단위 미리보기 ↔ 에디터 커서 매핑 (Precision Sub-Character Caret Mapping)**: 굵게, 기울임, 인라인 코드, 링크, 반복 단어, 복합 HTML, 초대형 문서 후반부에서도 클릭 지점의 텍스트 노드와 마크다운 소스 오프셋을 오차 없이 1:1 역추적
- **선형 HTML 세그먼트 스캐너 (Linear HTML Segment Scanner)**: 따옴표 안의 `>`, 중첩 태그, HTML 주석, SVG, MathML, 사용자 정의 태그를 문자 단위 상태 머신으로 해석하여 HTML 파싱 오류 및 태그 깨짐 원천 차단
- **Shadow DOM 렌더링 격리**: 미리보기 영역을 Shadow DOM으로 완전 격리하여 문서 내부의 `<style>`이나 인라인 CSS가 에디터 UI(상단바, 툴바, 상태바)를 오염시키지 않음
- **적응형 계층 목차 & 애플 글래스모피즘 팝오버 (Hierarchical TOC & Exact Scrollspy)**: H1, H2, H3 계층별 1px 헤어라인 트리와 실시간 섹션 강조, 말줄임 처리, 키보드 포커스 링을 갖춘 아크릴 팝오버 제공
- **인라인 코드 vs Fenced 코드 블록 분리**: 본문 인라인 코드는 슬림 칩 스타일로 가독성을 극대화하고, 다중행 코드 블록은 언어명 라벨과 가로 스크롤 컨테이너로 격리
- **다중 해상도 앵커링 스크롤 (Multi-Resolution Anchoring)**: 대형 블록 내부의 서브 단락/줄 단위 앵커를 세분화하여 HTML ON/OFF 및 마크다운 지문 길이 차이에도 부드러운 차등 스크롤 제공
- **대용량 문서 최적화**: 220,000자 초과 시 에디터 구문 색칠을 자동 단순화하여 렌더 및 타이핑 성능 보장
- **단일 파일 완결성 (Zero CDN)**: 외부 의존성이나 네트워크 연결 없이 독립적으로 동작하는 단일 HTML 파일
