# 온라인 알고리즘 테스트 어플리케이션

## 1. 프로젝트 멤버 이름 및 멤버 별 담당한 파트 소개

1. 김대영 (팀장) : Frontend 수정, 보고서 작성
2. 강등원 : 어플리케이션 배포, 발표 동영상 제작
3. 권오성 : 부하 테스트, PPT 제작

## 2. 프로젝트 소개

‘온라인 알고리즘 테스트 어플리케이션’은 기존에 청도대학교에서 배포한 'OnlineJudge' 오픈소스 프로젝트를 기반으로 한국어 번역을 적용하고, 이를 쿠버네티스(Kubernetes) 환경에서 안정적으로 동작하게 만든 프로젝트입니다. 이 시스템은 사용자에게 컴퓨터 알고리즘 문제를 제시하고, 제출된 코드가 테스트 케이스를 만족하는지 확인합니다.

## 3. 프로젝트 필요성 소개

알고리즘 스터디에서 효율적으로 학습하고, 참가자들이 실력을 향상시킬 수 있도록 하기 위해 스터디 전용 알고리즘 채점 사이트가 필요합니다. 기존에는 백준이나 프로그래머스와 같은 외부 웹 서비스를 사용해 코드를 채점받아야 했는데, 이로 인해 아래와 같은 불편함이 있었습니다.

- 스터디의 필요에 맞춘 맞춤형 기능 제공이 어려워, 불필요한 문제나 기능이 포함되어 있었습니다.
- 각 스터디 참가자의 진행 상황이나 코드에 대한 피드백을 실시간으로 공유하기 어려웠습니다.

이러한 문제를 해결하기 위해, 스터디에서만 사용할 수 있는 알고리즘 채점 사이트를 제작하게 되었습니다. 이 사이트는 아래와 같은 장점을 제공합니다.

- **스터디 맞춤형 기능 제공**: 문제 등록, 코드 제출, 채점, 피드백 제공 등 스터디에 특화된 기능을 지원합니다.
- **실시간 피드백 제공**: 참가자들이 작성한 코드를 즉시 채점하고 피드백을 제공하여 빠르게 개선점을 찾고 학습할 수 있습니다.
- **경쟁 모드 지원**: 스터디 참여자들이 다양한 경쟁 모드를 선택하여 사용할 수 있습니다. ACM 모드와 OI 모드를 통해 실시간 점수 확인 및 순위 비교가 가능하며, 스터디 구성원들이 효율적으로 학습할 수 있는 환경을 제공합니다.
- **클라우드 컴퓨팅 기술을 활용한 확장성**: 클라우드 환경에서 동작하여 스터디 규모에 따라 자원을 탄력적으로 사용하고, 고가용성 시스템을 제공합니다. 이를 통해 다양한 환경에서 유연하게 시스템을 운영할 수 있어, 스터디의 효과를 극대화할 수 있습니다.

## 4. 관련 기술/논문/특허 조사 내용 소개

- **Vue.js 및 Element UI**: 프론트엔드 개발을 위해 사용된 기술입니다. Vue.js는 반응형 사용자 인터페이스를 만들기 위한 프레임워크이며, Element UI는 이를 위한 컴포넌트 라이브러리입니다.
- **Django 및 DramatIQ**: 백엔드 API 서버 개발에 사용된 기술입니다. Django는 빠르고 확장 가능한 웹 프레임워크이며, DramatIQ는 백엔드 작업 큐를 관리하기 위한 메시지 큐 시스템입니다.
- **Flask 및 Seccomp**: 채점 서버 개발에 사용된 기술입니다. Flask는 Python 기반의 마이크로 웹 프레임워크이고, Seccomp는 시스템 콜을 제한하여 보안성을 높이는 도구입니다.
- **쿠버네티스**: 컨테이너화된 애플리케이션의 배포, 확장 및 관리를 위한 오픈소스 시스템입니다. 본 프로젝트에서는 애플리케이션을 쿠버네티스 클러스터에서 실행하도록 설정했습니다.

## 5. 프로젝트 개발 결과물 소개
![프로젝트 아키텍처](https://github.com/eodudrepublic/CC-Term_Project/blob/main/presentation/architecture.png)

1. **다국어 지원**
    - Vue.js 프로젝트의 i18n 번역 파일을 수정하여 영어, 한국어, 중국어 간체, 중국어 번체를 지원하도록 했습니다. 기본 언어는 영어로 설정되어 있습니다.
2. **이미지 참고**
    - 아래 이미지는 시스템 아키텍처와 주요 구성 요소를 시각적으로 표현한 다이어그램입니다. 이를 통해 시스템의 구조와 데이터 흐름을 직관적으로 이해할 수 있습니다.
3. **경쟁 모드**
    - **ACM 모드**: ACM-ICPC 규칙을 따르며, 콘테스트 종료 후 순위가 새로 고쳐지지 않습니다.
    - **OI 모드**: 참가자의 최종 제출물에 따라 점수를 매겨 순위를 결정합니다. 실시간으로 점수를 확인하고 순위를 볼 수 있습니다.

## 6. 개발 결과물을 사용하는 방법

### 6-1. 설치 방법

1. **GitHub 레포지토리 클론**
    - 프로젝트의 GitHub 레포지토리에서 클론을 받습니다.
        
        `git clone https://github.com/your-repository/CC-Term_Project`

        `cd CC-Term_Project`
        
2. **필요한 도커 이미지를 준비**
    - 도커 이미지를 빌드하거나, Docker Hub에서 필요한 이미지를 내려받습니다.
        
        `docker pull redis:4.0-alpine`

        `docker pull postgres:10-alpine`

        `docker pull registry.cn-hongkong.aliyuncs.com/oj-image/judge:1.6.1`

        `docker pull registry.cn-hongkong.aliyuncs.com/oj-image/backend:1.6.1`
        
3. **쿠버네티스 설정 파일 준비**
    - `onlinejudge-deployment.yaml` 파일은 애플리케이션을 쿠버네티스 클러스터에 배포하기 위한 설정 파일입니다. 이 파일은 애플리케이션의 각 구성 요소(예: 데이터베이스, 캐시 서버, 백엔드, 프론트엔드 등)를 정의하고, 쿠버네티스 클러스터에서 어떻게 배포할지 지정합니다.
    - 해당 파일은 `/src/OnlineJudgeDeployk8s/onlinejudge-deployment.yaml` 경로에 있습니다.
4. **쿠버네티스 클러스터에 배포**
    - 쿠버네티스 클러스터가 준비되어 있는지 확인합니다.
    - `kubectl`을 사용하여 클러스터에 애플리케이션을 배포합니다.
        
        `kubectl apply -f onlinejudge-deployment.yaml`
        
5. **쿠버네티스 상태 확인**
    - 모든 서비스가 정상적으로 배포되었는지 확인합니다.
    
        `kubectl get pods`

        `kubectl get services`

### 6-2. 동작 방법

1. **웹 브라우저에서 접속**
    - 배포된 온라인 저지 시스템에 접속합니다. `http://<로드밸런서의 외부 IP>:<노드 포트>`로 접근합니다. 노드 포트는 `oj-backend` 서비스에 설정된 포트입니다.
    - 예를 들어, 만약 노드 포트가 30000이라면 `http://<로드밸런서의 외부 IP>:30000`로 접속합니다.
2. **사용자 계정 생성**
    - 웹 인터페이스를 통해 사용자 계정을 생성합니다.
    - 로그인 후 문제를 풀거나 새 문제를 등록할 수 있습니다.
3. **문제 풀이 및 채점**
    - 제공된 문제를 선택하고, 자신의 코드를 작성 및 제출합니다.
    - 제출된 코드는 자동으로 채점되며, 결과를 즉시 확인할 수 있습니다.
### 6-3. 시스템 관리

1. **로그 확인 및 디버깅**
    - 각 컨테이너의 로그를 확인하여 문제를 진단하고 해결합니다.
    
        `kubectl logs <pod 이름>`

2. **서비스 재시작**
    - 필요 시 서비스를 재시작하여 시스템을 갱신하거나 오류를 해결합니다.
        
        `kubectl rollout restart deployment <deployment 이름>`
        
3. **데이터 백업**
    - 데이터베이스와 기타 중요한 데이터를 주기적으로 백업하여 데이터 손실을 방지합니다.

## 7. 개발 결과물의 활용방안 소개

- **학교 전용 알고리즘 테스트 사이트**
    
    학습 및 알고리즘 수업에서 과제 제출 및 평가를 위한 전용 플랫폼으로 사용할 수 있습니다. 학생들은 학교에서 배운 내용을 기반으로 문제를 풀고, 실시간으로 피드백을 받을 수 있습니다.
    
- **알고리즘 대회 개최 및 관리**
    
    학교 주관의 알고리즘 대회 개최 시, 참가자들의 문제 풀이 및 제출을 효율적으로 관리할 수 있는 플랫폼으로 활용됩니다. 대회 모드를 통해 다양한 규칙을 설정하고, 실시간으로 순위를 집계할 수 있습니다.
    
- **커뮤니티 학습 및 협업 공간**
    
    학생들이 서로의 코드와 알고리즘을 공유하고 피드백을 주고받을 수 있는 커뮤니티 기능을 제공합니다. 이를 통해 공동 학습 및 협업의 기회를 확대하고, 학습 효과를 극대화할 수 있습니다.