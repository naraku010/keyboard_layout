#!/usr/bin/env python3
"""
VIA JSON 데이터 생성 스크립트
VIA JSON 파일들을 탐색하여 데이터를 JSON으로 생성
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
from urllib.parse import quote

def is_json_file(filename: str) -> bool:
    """파일이 JSON인지 확인"""
    return filename.lower().endswith('.json')

def explore_directory(directory_path: str = "C:\\Users\\user\\IdeaProjects\\via_json") -> List[Dict[str, Any]]:
    """디렉토리를 재귀적으로 탐색하여 JSON 파일 찾기"""
    print(f"탐색 중: {directory_path}")
    
    via_files = []
    
    try:
        for root, dirs, files in os.walk(directory_path):
            # .git 폴더는 제외
            if '.git' in root:
                continue
                
            for file in files:
                if is_json_file(file):
                    # 상대 경로 계산
                    rel_path = os.path.relpath(root, directory_path)
                    path_parts = rel_path.split(os.sep) if rel_path != '.' else []
                    
                    if len(path_parts) >= 1:
                        brand_name = path_parts[0]
                        keyboard_name = path_parts[1] if len(path_parts) > 1 else "Unknown"
                        
                        # 파일 경로
                        file_path = os.path.join(root, file)
                        rel_file_path = os.path.join(rel_path, file)
                        
                        # URL 인코딩 (특수문자 처리)
                        encoded_brand_name = quote(brand_name)
                        encoded_rel_path = quote(rel_path.replace(os.sep, '/'))
                        
                        via_data = {
                            "brandName": brand_name,
                            "keyboardName": keyboard_name,
                            "fileName": file,
                            "filePath": rel_file_path.replace('\\', '/'),
                            "brandGithubUrl": f"https://github.com/KBD-Type-S/via_json/tree/main/{encoded_brand_name}",
                            "keyboardGithubUrl": f"https://github.com/KBD-Type-S/via_json/tree/main/{encoded_rel_path}"
                        }
                        
                        via_files.append(via_data)
                        print(f"  발견: {brand_name}/{keyboard_name}/{file}")
    except Exception as e:
        print(f"디렉토리 탐색 중 오류 발생: {e}")
    
    return via_files

def group_by_brands(via_files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """VIA 파일들을 브랜드별로 그룹화"""
    brand_map = {}
    
    for via_file in via_files:
        brand_name = via_file["brandName"]
        keyboard_name = via_file["keyboardName"]
        
        if brand_name not in brand_map:
            brand_map[brand_name] = {
                "name": brand_name,
                "keyboards": []
            }
        
        # 같은 키보드에 여러 JSON 파일이 있는지 확인
        existing_keyboard = next((k for k in brand_map[brand_name]["keyboards"] if k["keyboardName"] == keyboard_name), None)
        
        if existing_keyboard:
            # 기존 키보드에 파일 추가
            if "files" not in existing_keyboard:
                # 첫 번째 파일을 files 배열로 변환
                first_file = {
                    "fileName": existing_keyboard["fileName"],
                    "filePath": existing_keyboard["filePath"]
                }
                
                existing_keyboard["files"] = [first_file]
                del existing_keyboard["fileName"]
                del existing_keyboard["filePath"]
            
            # 새 파일 추가
            new_file = {
                "fileName": via_file["fileName"],
                "filePath": via_file["filePath"]
            }
            
            existing_keyboard["files"].append(new_file)
        else:
            # 새 키보드 추가
            keyboard_data = {
                "brandName": via_file["brandName"],
                "keyboardName": via_file["keyboardName"],
                "fileName": via_file["fileName"],
                "filePath": via_file["filePath"],
                "brandGithubUrl": via_file["brandGithubUrl"],
                "keyboardGithubUrl": via_file["keyboardGithubUrl"]
            }
            
            brand_map[brand_name]["keyboards"].append(keyboard_data)
    
    return list(brand_map.values())

def main():
    """메인 함수"""
    print("VIA JSON 데이터 생성 시작...")
    print("=" * 50)
    
    # 모든 JSON 파일 탐색
    all_via_files = explore_directory()
    
    if not all_via_files:
        print("VIA JSON 파일을 찾을 수 없습니다.")
        return
    
    print(f"\n총 {len(all_via_files)}개의 VIA JSON 파일을 발견했습니다.")
    
    # 브랜드별로 그룹화
    brands = group_by_brands(all_via_files)
    print(f"총 {len(brands)}개의 브랜드를 발견했습니다.")
    
    # 결과 데이터 구성
    result_data = {
        "viaFiles": all_via_files,
        "brands": brands,
        "generatedAt": datetime.now().isoformat() + "Z",
        "totalViaFiles": len(all_via_files),
        "totalBrands": len(brands)
    }
    
    # JSON 파일로 저장
    output_file = "via_data.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n데이터가 {output_file}에 저장되었습니다.")

    # 요약 정보 출력
    print("\n=== 브랜드별 요약 ===")
    for brand in brands:
        keyboard_count = len(brand['keyboards'])
        # 총 파일 수 계산
        total_files = sum(
            len(kb.get('files', [])) if 'files' in kb else 1 
            for kb in brand['keyboards']
        )
        print(f"{brand['name']}: {keyboard_count}개 키보드, {total_files}개 파일")

if __name__ == "__main__":
    main()

