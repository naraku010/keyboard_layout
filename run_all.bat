@echo off
echo ========================================
echo 키보드 레이아웃 데이터 생성 시작
echo ========================================
echo.

echo 1. converter.py 실행 중...
python converter.py
if %errorlevel% neq 0 (
    echo 오류: convert.py 실행 실패
    pause
    exit /b 1
)
echo convert.py 완료
echo.

echo 2. readme_gen.py 실행 중...
python readme_gen.py
if %errorlevel% neq 0 (
    echo 오류: readme_gen.py 실행 실패
    pause
    exit /b 1
)
echo readme_gen.py 완료
echo.

echo 3. generate_keyboard_data.py 실행 중...
python generate_keyboard_data.py
if %errorlevel% neq 0 (
    echo 오류: generate_keyboard_data.py 실행 실패
    pause
    exit /b 1
)
echo generate_keyboard_data.py 완료
echo.

echo 4. generate_via_data.py 실행 중...
python generate_via_data.py
if %errorlevel% neq 0 (
    echo 오류: generate_via_data.py 실행 실패
    pause
    exit /b 1
)
echo generate_via_data.py 완료
echo.

echo ========================================
echo 모든 스크립트 실행 완료!
echo ========================================
echo.
echo 생성된 파일들:
echo - keyboard_data.json
echo - README.md (업데이트됨)
echo.
pause
