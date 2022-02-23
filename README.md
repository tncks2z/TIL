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
* Git 기초1
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
		2. `git add .` 또는 `git add [특정파일]` (김멀캠 무대에 세우기 -> Staging Area에 올리기)
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
	- branch
		- 하나의 프로젝트를 여러 팀원들이 자신의 이름(branch)를 만들어서, 수정하고, 공유하는 기능
		- 장점
			- branch는 사용자 독립공간을 사용하기 때문에 원본(master)을 유지할 수 있음
			- 여러 팀원들이 한 프로젝트에 참여할 때, 매우 효율적으로 관리 가능
		- 하나의 큰 줄기에 여러 잔가지(branch)를 치는 것처럼 하나의 주제에 다양한 버전을 만들 수 있음
			- 다양한 버전의 수정 가능
				- (ex. `master`는 iOS, `branch`는 /iOS15/, /iOS14/, /iOS13/ -> 각 버전 별로 수정하여 업데이트 가능 => /iOS 14.2.1/, /iOS 13.3.1/)
		- 생성
			```
			git branch <브랜치 이름>
			```
		- 조회
			```
			git branch
			```
		- 삭제
			```
			git branch -d <브랜치 이름> (병합된 branch만 삭제)
			git branch -D <브랜치 이름> (병합되지 않은 branch도 삭제 -> 웬만하면 사용X)
			```
		- 이동
			```
			git switch <브랜치 이름>
			git branch -c <브랜치 이름> (새로운 branch를 생성과 동시에 이동)
			```
		- 병합
			- branch에서 수정한 내용을 master에 반영
			- 합치고 싶어하는 branch로 이동하여 merge 사용
				- branch1에 branch2를 합치고 싶은 경우
					```
					git switch branch1
					git merge branch2
					```
				- branch2에 branch1을 합치고 싶은 경우
					```
					git switch branch2
					git merge branch1
					```
			- 병합이 완료되면 합쳐진 branch는 삭제를 한다.
				- branch1에 branch2를 합친 경우
					```
					git branch -d branch2
					```
				- branch2에 branch1을 합친 경우
					```
					git branch -d branch1
					```
	- log
		- 해당 git파일의 모든 commit을 보여줌
			- Author와 commit한 시간까지 보여줌
		- 해당 git파일의 branch가 있을 경우 branch도 같이 보여줌
		- 한줄로 간단하게 보여주기
			- 커밋 메시지만 보여줌
			```
			git log --oneline
			```
		- branch가 어디에서부터 생성 됐는지 그림으로 보여주기
			```
			git log --oneline --all --graph
			```
- Git 심화1
	- restore <파일 이름>
		- git이 관리하고 있는 파일을 수정 전으로 되돌림
		```
		git restore <파일 이름>
		```
		- 한번 restore로 되돌리면, restore 하기 전으로는 복원 불가능
	- rm --cached <파일 이름>
		- `touch <파일 이름>` 후에 `git add <파일 이름>` 한 파일의 add 상태를 취소하고 싶은 경우
		```
		touch test.txt
		git add test.txt
		git rm --cached test.txt
		```
	- restore --staged <파일 이름>
		- `git commit -m "메시지"` 한 파일의 commit 상태를 취소하고 싶은 경우
		```
		touch test.txt
		git add test.txt
		git commit -m "first commit"
		git restore --staged test.txt
		```
	
### Algorithm
- print
	- `end=` 파라미터는 최종적으로 어떤 값을 주냐
	- `sep=` 파라미터는 각각의 값들 사이사이에 어떤 값을 주냐
	- 기본적으로 `end=\n` `sep=" "` 값이 내장

- list
	- List Comprehension을 이용한 2중 for문
		- `[list(map(input().split()) for _ in range(n)`

- dictionary
	- `key`를 `hash 함수`를 통해서 `hash 테이블`에 `value`로 저장
		- 시간 복잡도는 O(1) -> O(n)이 아니기 때문에 속도가 매우 빠름
	- `[딕셔너리].get(key)`
		- 해당 key가 없을 경우, `None`을 반환
		- `[딕셔너리].get(key, " 메시지 ")`
			- 해당 key가 없을 경우, 입력한 메시지를 반환


### DL
* DL은 `사람의 신경망`을 수치화를 이용해서 구현한 `인공 신경망`으로 학습하는 방법
* `XOR GATE`를 통해 컴퓨터(반도체)가 어떻게 구성되는 지를 알아보자
	* [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
* `신경망(perceptron)`은 어떻게 구성되는지 알아보자
	* 단일 Perceptron
		* [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
	* 활성화 함수(Activation Function)
		* Sigmoid 함수(값들을 0~1 사이로 연결성 있게 표현)
		* 값들을 확률로 표현하기 위해 사용
	* MultiLayer의 구성
		* [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
	* MNIST를 활용한 실습
		* [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
		* Batch
			* epoch(전체)의 반대말
			* 데이터를 batch_size만큼 쪼개서 한번에 입력
				* (ex.`x_train`갯수가 100개, `batch_size`가 10 이라면 데이터를 10개를 한번에 train함.)
				* 코드는 [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
* Cross Entropy
	* 딥러닝의 손실(loss)함수
	* 예측값과 라벨 값의 차이(loss 값 => error 크기)를 나타냄 -> 낮을 수록 분류가 잘된 것
	* 코드는 [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
* 편미분
	* Gradient Descent(경사 하강)
		* 딥러닝의 목적함수
		* Cross Entropy(loss 값)를 낮추는 것 = 그래프의 기울기(순간 변화량)가 감소하는 것
		* 코드는 [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
	* 최적화
		* 편미분 값이 감소하는 방향으로 지속적으로 W를 업데이트 -> 기울기가 0일 때, stop
		* W = W - 학습률 * 편미분값
* 학습 알고리즘 구현
	1. `미니 배치` : 훈련 데이터 중 일부를 무작위로 batch_size만큼 가져옴.
	2. `기울기 산출` : `미니 배치`의 loss 값을 줄이기 위해 각 W 파라미터의 기울기를 구함
	3. `매개변수 갱신` : W 매개변수를 기울기 방향(줄어드는 쪽)으로 갱신
	4. 1~3단계 반복
	* 단일 신경망 클래스 학습 구현
		- [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고
	* 2층 신경망 클래스 학습 구현
		- [개인 Notion](https://www.notion.so/1ea51850579a44e389baf074f68eaf8f) 참고

