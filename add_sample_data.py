#!/usr/bin/env python3
"""
سكريبت لإضافة البيانات التجريبية
Script to add sample data
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.models.medical_leave import MedicalLeave

def add_sample_data():
    """إضافة البيانات التجريبية"""
    medical_leave_model = MedicalLeave()
    
    # البيانات التجريبية
    sample_data = {
        'service_code': 'PSL54640252025',
        'identity_number': '7657865464',
        'patient_name_ar': 'علي محمد علي',
        'patient_name_en': 'Ali Mohammed Ali',
        'nationality_ar': 'السعودية',
        'nationality_en': 'Saudi Arabia',
        'workplace_ar': 'طالب جامعي',
        'workplace_en': 'University Student',
        'doctor_name_ar': 'عبدالرحمن الدوسري',
        'doctor_name_en': 'Abdulrahman Al-Daosari',
        'job_title_ar': 'طبيب عام',
        'job_title_en': 'General',
        'admission_date_gregorian': '2025-09-10',
        'admission_date_hijri': '18-03-1447',
        'discharge_date_gregorian': '2025-09-12',
        'discharge_date_hijri': '20-03-1447',
        'report_issue_date': '2025-09-12',
        'facility_name_ar': 'مستشفى الملك فيصل التخصصي ومركز الأبحاث',
        'facility_name_en': 'King Faisal Specialist Hospital and Research Centre',
        'report_time': '23:15:00',
        'duration_days': 3
    }
    
    try:
        success = medical_leave_model.create_medical_leave(sample_data)
        if success:
            print("✅ تم إضافة البيانات التجريبية بنجاح!")
            print(f"رمز الخدمة: {sample_data['service_code']}")
            print(f"رقم الهوية: {sample_data['identity_number']}")
        else:
            print("⚠️ البيانات موجودة مسبقاً أو حدث خطأ في الإضافة")
    except Exception as e:
        print(f"❌ خطأ في إضافة البيانات: {e}")

if __name__ == '__main__':
    add_sample_data()
