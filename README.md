# Today I Learned 📒
* 좋은 개발자가 되기 위해 하루동안 학습한 내용이나 개발관련 경험들을 기록으로 남긴다.
* Today I Learned인데 날짜를 표시하지 않는 이유는 조급해지지 않고 꾸준하기 위함이다.
[MLP Notion](https://hphk.notion.site/hphk/Git-1-_A-22-02-09-22-02-11-3f4afeb98f784b7ead4a82f5aebd86de)을 보고 많은 도움을 얻었다.

## 나만의 작성규칙
* 해당 문서를 다시 봤을 때, 추가적인 검색의 비용이 들지 않도록 자세히 기록한다.
* 더 많은 공유를 원하는 기록은 [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f)에 포스팅한다.
* 쉴 땐 확실히 쉬고, contributions를 초록색으로 채우는 것에 집착하지 않는다.
* reference를 명시하고, 원작자가 참고를 허용하는 자료만 사용한다.

## 분류
### Git, Who RU?
* Git 기초
	* 디렉토리 만들기
		1. 'Terminal'에서 디렉토리 생성 `mkdir [폴더명]`
		2. 해당 디렉토리로 이동 `cd [폴더명]`
		3. VISUAL STUDIO CODE 열기 `code .`
	- 초기설정
		- GitHub 가입시 쓴 닉네임과 메일주소를 VISUAL STUDIO CODE에 기입
		```
		git config —global user.name “이름”
		git config —global user.email “메일 주소”
		```
		- Git에게 디렉토리에 대한 관리를 명령
		```
		git init
		```
	* 기록남기기
		1. md파일 또는 txt 파일 등을 수정하여 저장하기(김멀캠 옷 입히기)
		2. `git add .` 또는 `git add [특정파일]` (김멀캠 무대에 세우기)
		3. `git commit -m " 커밋메시지 "` (김멀캠 사진작가에게 사진 찍히기, 커밋 메시지를 통해 버전확인)
	* GitHub에 연동 및 업로드
		1. GitHub에서 New Repositories 생성
		2. `git remote ~` 하는 부분 복사 후 Visual STUDIO Code 에 붙여넣기 (고속도로 만들기)
		3. `git push origin master` (업로드)
* Git 기초2
	* ignore
		* .gitignore 파일을 만들고 그곳에서 ignore할 파일을 추가
		* 반드시 파일 명을 ".gitignore" 이라고 해야됨 -> git에서 정한 문법
	* clone, pull
		- 컴퓨터1에서 작업한 내용을 컴퓨터2로 받아올 때
		* 상대방이 만든 Repositories를 그대로 가져오고 싶을때 (허가 or 초대가 필요)
		* clone
			```
			git clone [가져오고 싶은 Repositories] [명칭할 이름]
			```
			- clone은 반드시 홈 디렉토리에서 실행할 것(나는 suchan)
		- pull
			```
			git pull origin master
			```
- Git 기초3
	- 

### DL_1
* DL은 `사람의 신경망`을 수치화를 이용해서 구현한 `인공 신경망`으로 학습하는 방법
* `XOR GATE`를 통해 컴퓨터(반도체)가 어떻게 구성되는 지를 알아보자
	* [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
* `신경망(perceptron)`은 어떻게 구성되는지 알아보자
	* 단일 Perceptron
		* [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
	* Sigmoid 함수(값들을 0~1 사이로 연결성 있게 표현)
		* 값들을 확률로 표현하기 위해 사용
	* MultiLayer의 구성
		* [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
* MNIST를 활용한 실습
	* [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
	* 시간을 단축시키기 위해, `batch`를 사용해보자