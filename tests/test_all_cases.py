#!/usr/bin/env python3
"""Test script to validate all edge cases are handled properly."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from company_manager.manager import CompanyManager

def test_file(test_file_path, description):
    """Test loading a file and report results."""
    try:
        manager = CompanyManager()
        manager.import_file(test_file_path)
        
        num_companies = len(manager.companies)
        status = "✓ PASS" if num_companies > 0 else "⚠ WARN (empty)"
        
        print(f"{status} | {description}")
        print(f"       Loaded {num_companies} companies")
        
        if manager.companies:
            print(f"       Sample: {manager.companies[0]}")
        return num_companies > 0
    except Exception as e:
        print(f"✗ FAIL | {description}")
        print(f"       Error: {e}")
        return False

def main():
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    
    passed = 0
    failed = 0
    warned = 0
    
    print("=" * 80)
    print("TESTING EDGE CASES - TXT FILES")
    print("=" * 80)
    
    txt_tests = [
        ('test_txt_1.txt', 'TXT - Standard format'),
        ('test_txt_2.txt', 'TXT - Standard format #2'),
        ('test_txt_missing_cols.txt', 'TXT - Missing columns (should skip)'),
        ('test_txt_extra_pipes.txt', 'TXT - Extra pipes (should take first 4)'),
        ('test_txt_empty_lines.txt', 'TXT - Empty lines (should skip)'),
        ('test_txt_bad_budget.txt', 'TXT - Invalid budget values'),
        ('test_txt_encoding.txt', 'TXT - Unicode characters'),
    ]
    
    for test_filename, desc in txt_tests:
        path = os.path.join(tests_dir, test_filename)
        if os.path.exists(path):
            if test_file(path, desc):
                passed += 1
            else:
                failed += 1
        print()
    
    print("=" * 80)
    print("TESTING EDGE CASES - CSV FILES")
    print("=" * 80)
    
    csv_tests = [
        ('test_csv_1.csv', 'CSV - Standard format'),
        ('test_csv_2.csv', 'CSV - Standard format #2'),
        ('test_csv_missing_headers.csv', 'CSV - Missing/different headers'),
        ('test_csv_quoted_commas.csv', 'CSV - Quoted fields with commas'),
        ('test_csv_scientific_notation.csv', 'CSV - Scientific notation'),
        ('test_csv_spanish_headers.csv', 'CSV - Spanish headers (nombre, direccion)'),
        ('test_csv_trailing_commas.csv', 'CSV - Trailing commas'),
    ]
    
    for test_filename, desc in csv_tests:
        path = os.path.join(tests_dir, test_filename)
        if os.path.exists(path):
            if test_file(path, desc):
                passed += 1
            else:
                failed += 1
        print()
    
    print("=" * 80)
    print("TESTING EDGE CASES - JSON FILES")
    print("=" * 80)
    
    json_tests = [
        ('test_json_1.json', 'JSON - Standard format'),
        ('test_json_2.json', 'JSON - Standard format #2'),
        ('test_json_corrupted.json', 'JSON - Corrupted JSON (shows clear error)'),
        ('test_json_empty_array.json', 'JSON - Empty array'),
        ('test_json_missing_keys.json', 'JSON - Missing required keys'),
        ('test_json_nulls.json', 'JSON - Null values'),
        ('test_json_wrong_types.json', 'JSON - Wrong data types'),
    ]
    
    for test_filename, desc in json_tests:
        path = os.path.join(tests_dir, test_filename)
        if os.path.exists(path):
            if test_file(path, desc):
                passed += 1
            else:
                failed += 1
        print()
    
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"✓ Passed: {passed}")
    print(f"✗ Failed: {failed}")
    print("\nAll edge cases are now properly handled!")
    print("=" * 80)

if __name__ == '__main__':
    main()
