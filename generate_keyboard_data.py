#!/usr/bin/env python3
"""
키보드 레이아웃 데이터 생성 스크립트
로컬 프로젝트 디렉토리를 탐색하여 DXF/DWG 파일 정보를 JSON으로 생성
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

def is_dxf_or_dwg(filename: str) -> bool:
    """파일이 DXF 또는 DWG인지 확인"""
    return filename.lower().endswith(('.dxf', '.dwg'))

def explore_directory(directory_path: str = ".") -> List[Dict[str, Any]]:
    """디렉토리를 재귀적으로 탐색하여 DXF/DWG 파일 찾기"""
    print(f"탐색 중: {directory_path}")
    
    plates = []
    
    try:
        for root, dirs, files in os.walk(directory_path):
            # .git 폴더는 제외
            if '.git' in root:
                continue
                
            for file in files:
                if is_dxf_or_dwg(file):
                    # 상대 경로 계산
                    rel_path = os.path.relpath(root, directory_path)
                    path_parts = rel_path.split(os.sep) if rel_path != '.' else []
                    
                    if len(path_parts) >= 1:
                        brand_name = path_parts[0]
                        keyboard_name = path_parts[1] if len(path_parts) > 1 else "Unknown"
                        
                        # 파일 경로
                        file_path = os.path.join(root, file)
                        rel_file_path = os.path.join(rel_path, file)
                        
                        # PNG 이미지 URL 생성 (GitHub raw URL)
                        png_file = file.rsplit('.', 1)[0] + '.png'
                        image_url = f"https://raw.githubusercontent.com/naraku010/keyboard_layout/main/{rel_path}/{png_file}"
                        
                        plate_data = {
                            "brandName": brand_name,
                            "keyboardName": keyboard_name,
                            "fileName": file,
                            "filePath": rel_file_path,
                            "imageUrl": image_url,
                            "brandGithubUrl": f"https://github.com/naraku010/keyboard_layout/tree/main/{brand_name}",
                            "keyboardGithubUrl": f"https://github.com/naraku010/keyboard_layout/tree/main/{rel_path}"
                        }
                        
                        plates.append(plate_data)
                        print(f"  발견: {brand_name}/{keyboard_name}/{file}")
    except Exception as e:
        print(f"디렉토리 탐색 중 오류 발생: {e}")
    
    return plates

def group_by_brands(plates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """플레이트를 브랜드별로 그룹화"""
    brand_map = {}
    
    for plate in plates:
        brand_name = plate["brandName"]
        keyboard_name = plate["keyboardName"]
        
        if brand_name not in brand_map:
            brand_map[brand_name] = {
                "name": brand_name,
                "keyboards": []
            }
        
        # 같은 키보드에 여러 도면이 있는지 확인
        existing_keyboard = next((k for k in brand_map[brand_name]["keyboards"] if k["keyboardName"] == keyboard_name), None)
        
        if existing_keyboard:
            # 기존 키보드에 도면 추가
            existing_keyboard["fileName"] += f", {plate['fileName']}"
        else:
            # 새 키보드 추가
            brand_map[brand_name]["keyboards"].append({
                "brandName": plate["brandName"],
                "keyboardName": plate["keyboardName"],
                "fileName": plate["fileName"],
                "imageUrl": plate["imageUrl"],
                "filePath": plate["filePath"],
                "brandGithubUrl": plate["brandGithubUrl"],
                "keyboardGithubUrl": plate["keyboardGithubUrl"]
            })
    
    return list(brand_map.values())

def main():
    """메인 함수"""
    print("키보드 레이아웃 데이터 생성 시작...")
    print("=" * 50)
    
    # 모든 DXF/DWG 파일 탐색
    all_plates = explore_directory()
    
    if not all_plates:
        print("DXF/DWG 파일을 찾을 수 없습니다.")
        return
    
    print(f"\n총 {len(all_plates)}개의 키보드 플레이트를 발견했습니다.")
    
    # 브랜드별로 그룹화
    brands = group_by_brands(all_plates)
    print(f"총 {len(brands)}개의 브랜드를 발견했습니다.")
    
    # 결과 데이터 구성
    result_data = {
        "plates": all_plates,
        "brands": brands,
        "generatedAt": datetime.now().isoformat() + "Z",
        "totalPlates": len(all_plates),
        "totalBrands": len(brands)
    }
    
    # JSON 파일로 저장
    output_file = "keyboard_data.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n데이터가 {output_file}에 저장되었습니다.")

    # 요약 정보 출력
    for brand in brands:
        print(f"{brand['name']}: {len(brand['keyboards'])}개 키보드")
        for keyboard in brand['keyboards']:
            print(f"  - {keyboard['keyboardName']}: {keyboard['fileName']}")

if __name__ == "__main__":
    main()
