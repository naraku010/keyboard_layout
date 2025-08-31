
# ⌨ Custom Keyboard Plate File
***
## ℹ️ 참고
> 공제 키보드에 호환되는 기판(PCB) 리스트 정리 (In Progress...)
> https://kbdlab.co.kr/index.php?mid=board_etc&document_srl=6638372
## 🛜 GMK-KEYCAP-FINDER
> GMK 키캡 찾기
> ### https://gmk-keycap-finder.vercel.app/
> 
> <img width="1524" height="836" alt="image" src="https://github.com/user-attachments/assets/bc43ccba-2e43-4cb9-8823-c8994b2105bc" />
## 🛜 기키갤 시뮬레이터
> ### https://mkg-sim.vercel.app/
>
> ![image](https://github.com/user-attachments/assets/2a3f08b6-8841-463a-88ba-cbe37a2099b0)
## 🛜 키보드 보강판 자료실
> ### https://keyboard-plate.vercel.app/
>
> <img width="1603" height="867" alt="image" src="https://github.com/user-attachments/assets/90d2aafb-48cc-42ee-b9ea-d06a4239820a" />
# 🎹 Keyboard Layout Collection

키보드 레이아웃과 플레이트 도면을 체계적으로 정리한 저장소입니다.

## 📁 프로젝트 구조

```
keyboard_layout/
├── Ai03/                    # Ai03 브랜드 키보드
│   ├── [Ai03] Andromeda/
│   ├── [Ai03] Meridian/
│   ├── [Ai03] Polaris/
│   └── [Ai03] Vega/
├── CannonKeys/              # CannonKeys 브랜드 키보드
├── Geonworks/               # Geonworks 브랜드 키보드
├── Keychron/                # Keychron 브랜드 키보드
├── Matrix/                  # Matrix 브랜드 키보드
├── Qwertykeys/              # Qwertykeys 브랜드 키보드
├── TGR/                     # TGR 브랜드 키보드
├── ...                      # 기타 브랜드들
├── convert.py               # DXF/DWG 파일 변환 스크립트
├── readme_gen.py            # README 자동 생성 스크립트
├── generate_keyboard_data.py # 키보드 데이터 JSON 생성 스크립트
├── run_all.bat              # 전체 스크립트 실행 배치 파일
├── keyboard_data.json       # 생성된 키보드 데이터
└── requirements.txt         # Python 의존성
```

## 🚀 빠른 시작

### 1. 전체 프로세스 자동 실행
```bash
# Windows에서 배치 파일 실행
run_all.bat
```

### 2. 개별 스크립트 실행
```bash
# 1. DXF/DWG 파일 변환
python convert.py

# 2. README 파일 생성
python readme_gen.py

# 3. 키보드 데이터 JSON 생성
python generate_keyboard_data.py
```

## 📊 통계 정보

- **총 브랜드 수**: 63개
- **총 키보드 수**: 756개
- **지원 파일 형식**: DXF, DWG
- **마지막 업데이트**: 자동 생성됨

## 🔧 주요 기능

### 1. 파일 변환 (`convert.py`)
- DXF/DWG 파일을 다양한 형식으로 변환
- ConvertAPI 서비스 활용

### 2. README 생성 (`readme_gen.py`)
- 프로젝트 구조를 자동으로 분석
- 마크다운 형식의 README 파일 생성
- 브랜드별 키보드 목록 자동 정리

### 3. 데이터 생성 (`generate_keyboard_data.py`)
- 로컬 디렉토리 탐색으로 DXF/DWG 파일 검색
- 브랜드별 키보드 정보 구조화
- GitHub URL과 이미지 경로 자동 생성
- JSON 형식으로 데이터 저장

## 📋 지원 브랜드

### 주요 브랜드
- **Ai03**: Andromeda, Meridian, Polaris, Vega
- **CannonKeys**: Brutal60, Chimera, Devastating TKL, Satisfaction75
- **Geonworks**: F1-88, F2-60, Frog Mini, Glare TKL
- **Keychron**: K 시리즈, Q 시리즈, V 시리즈
- **Matrix**: 3.3, 6XV, 8XV, Corsa, Navi
- **Qwertykeys**: Neo 시리즈, QK 시리즈
- **TGR**: 901-v2-me, Jane, Kohaku, Shi

### 전체 브랜드 목록
- Ai03, Archon, Baionlenja, BigStar, CannonKeys, Caryworks
- Chaosera, COX, CubStudio, Duck, ETC, Evoworks, GDK Lab
- Geonworks, Gok, GrayStudio, GRIT, Hand Engineering
- Heavy Metal Keyboards, Hiexakey, JJW, KBDFans, keebscape
- Keychron, Keycult, Keynergy, Keynetix, Kibou, KMG
- Laminar, LifeZone, Linworks, Luminkey, Machina, Matrix
- Meletrix, MM Studio, Mode Designs, Molly Studio, Monokei
- Monsgeek, Monstargear, Neson Design, Newone, Niuniu
- Novelkeys, Nuxroskb, ORI, Owlab, Qwertykeys, Rama works
- SingaKBD, Smith And Rune, Stilou Studio, Swagkey
- Syryan Industry, Teahouse, TGR, TKD, Vertex, Wind Studio
- WOB, Wuque Studio

## 📁 파일 형식

### 지원 파일
- **DXF**: AutoCAD Drawing Exchange Format
- **DWG**: AutoCAD Drawing Database
- **PNG**: 이미지 파일 (자동 생성)

### 생성 파일
- **keyboard_data.json**: 키보드 정보 데이터베이스
- **README.md**: 프로젝트 문서

## 🔗 데이터 구조

### JSON 데이터 예시
```json
{
  "brandName": "Geonworks",
  "keyboardName": "Frog Mini",
  "fileName": "FROG_MINI_ALU_PLATE.dwg",
  "filePath": "Geonworks/[Geonworks] Frog Mini/FROG_MINI_ALU_PLATE.dwg",
  "imageUrl": "https://raw.githubusercontent.com/naraku010/keyboard_layout/main/Geonworks/[Geonworks] Frog Mini/FROG_MINI_ALU_PLATE.png",
  "brandGithubUrl": "https://github.com/naraku010/keyboard_layout/tree/main/Geonworks",
  "keyboardGithubUrl": "https://github.com/naraku010/keyboard_layout/tree/main/Geonworks/[Geonworks] Frog Mini"
}
```

## 🛠️ 개발 환경

### 요구사항
- Python 3.7+
- Windows (배치 파일 실행용)

### 의존성
```
convertapi==2.0.0
```

## 📝 사용법

### 1. 데이터 업데이트
새로운 키보드 파일을 추가한 후:
```bash
run_all.bat
```

### 2. 특정 브랜드만 확인
```bash
python generate_keyboard_data.py
# 생성된 keyboard_data.json에서 원하는 브랜드 정보 확인
```

### 3. README 수동 생성
```bash
python readme_gen.py
```

## 🤝 기여하기

1. 새로운 키보드 브랜드나 모델 추가
2. 기존 파일 정보 업데이트
3. 스크립트 개선 및 버그 수정
4. 문서화 개선

## 📄 라이선스

이 프로젝트는 오픈소스입니다. 각 브랜드의 키보드 도면은 해당 브랜드의 라이선스를 따릅니다.

## 📞 문의

프로젝트에 대한 문의사항이나 제안사항이 있으시면 이슈를 생성해 주세요.

---

**마지막 업데이트**: 자동 생성됨  
**생성 스크립트**: `readme_gen.py`
