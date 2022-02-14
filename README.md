# Today I Learned 📒
- 좋은 개발자가 되기 위해 하루동안 학습한 내용이나 개발관련 경험들을 기록으로 남긴다.
- Today I Learned인데 날짜를 표시하지 않는 이유는 조급해지지 않고 꾸준하기 위함이다.
[MLP Notion](https://hphk.notion.site/hphk/Git-1-_A-22-02-09-22-02-11-3f4afeb98f784b7ead4a82f5aebd86de)을 보고 많은 도움을 얻었다.
## 나만의 작성규칙
- 해당 문서를 다시 봤을 때, 추가적인 검색의 비용이 들지 않도록 자세히 기록한다.
- 더 많은 공유를 원하는 기록은 [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f)에 포스팅한다.
- 쉴 땐 확실히 쉬고, contributions를 초록색으로 채우는 것에 집착하지 않는다.
- reference를 명시하고, 원작자가 참고를 허용하는 자료만 사용한다.
## 분류
### Git, Who RU?
- Git 기초
    - 디렉토리 만들기
        1. 'Terminal'에서 디렉토리 생성(mkdir \[폴더명])
        2. 해당 디렉토리로 이동 (cd \[폴더명])
        3. VISUALCODE 열기 (code .)
    - 기록남기기
        1. md파일 또는 txt 파일 등을 수정하여 저장하기(김멀캠 옷 입히기)
        2. git add . 또는 git add \[특정파일] (김멀캠 무대에 세우기)
        3. git commit -m " 커밋내용 " (김멀캠 사진작가에게 사진 찍히기, 커밋내용을 통해 버전확인)
    - GitHub에 연동
        1. GitHub에서 Repositories 생성
        2. git remote ~ 하는 부분 복사 후 VisualCode 에 붙여넣기
        3. git push origin master (업로드)
- Git 기초2
    - ignore
        - .gitignore 파일을 만들고 그곳에서 ignore할 파일을 추가
        - 반드시 파일 명을 ".gitignore" 이라고 해야됨 -> git에서 정한 문법
    - clone
        - clone 이란 상대방이 만든 Repositories를 그대로 복사해서 가져오는 것
        - clone은 허가가 필요하함