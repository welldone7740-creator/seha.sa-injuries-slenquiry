# نظام صحة الطبي - الموقع الإلكتروني
## Seha Medical System - Website

**الإصدار:** 2.0 Final  
**التاريخ:** 5 أكتوبر 2025

---

## 📋 نظرة عامة

نظام صحة الطبي هو منصة إلكترونية لإدارة والاستعلام عن الإجازات المرضية.

### الميزات:
- ✅ استعلام عن الإجازات المرضية
- ✅ API لاستقبال البيانات من بوت التيليجرام
- ✅ لوحة إدارة لإدخال البيانات
- ✅ قاعدة بيانات SQLite
- ✅ واجهة عربية احترافية

---

## 🚀 التشغيل المحلي

### المتطلبات:
- Python 3.11+
- pip

### الخطوات:

```bash
# 1. تثبيت المكتبات
pip install -r requirements.txt

# 2. تشغيل التطبيق
python src/main.py
```

الموقع سيعمل على: http://localhost:5000

---

## 🌐 الاستضافة على Render.com

راجع ملف `RENDER_DEPLOYMENT_GUIDE.md` للحصول على دليل شامل.

### خطوات سريعة:

1. ارفع المشروع على GitHub
2. أنشئ حساب على Render.com
3. اربط المستودع
4. انشر الموقع

---

## 📁 هيكل المشروع

```
.
├── src/
│   ├── main.py              # الملف الرئيسي
│   ├── models/              # نماذج قاعدة البيانات
│   │   ├── user.py
│   │   └── medical_leave.py
│   ├── routes/              # مسارات API
│   │   ├── user.py
│   │   └── medical_leaves.py
│   ├── static/              # الملفات الثابتة
│   │   ├── index.html
│   │   ├── admin.html
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── database/            # قاعدة البيانات
│       └── app.db
├── requirements.txt         # المكتبات المطلوبة
├── render.yaml              # إعدادات Render
├── .gitignore               # ملفات يتم تجاهلها
└── README.md                # هذا الملف
```

---

## 🔌 API Endpoints

### 1. إضافة إجازة مرضية
```
POST /api/medical-leaves
Content-Type: application/json

{
  "service_code": "PSL12345672025",
  "identity_number": "1234567890",
  "patient_name_ar": "أحمد محمد",
  "patient_name_en": "Ahmed Mohammed",
  ...
}
```

### 2. الاستعلام عن إجازة
```
GET /api/medical-leaves/search?service_code=PSL12345672025&identity_number=1234567890
```

---

## 🗄️ قاعدة البيانات

### الجداول:

#### medical_leaves
- `id` - المعرف الفريد
- `service_code` - رمز الخدمة (PSL)
- `identity_number` - رقم الهوية
- `patient_name_ar` - اسم المريض (عربي)
- `patient_name_en` - اسم المريض (إنجليزي)
- `doctor_name_ar` - اسم الطبيب (عربي)
- `doctor_name_en` - اسم الطبيب (إنجليزي)
- `admission_date_hijri` - تاريخ الدخول (هجري)
- `discharge_date_hijri` - تاريخ الخروج (هجري)
- `duration_days` - مدة الإجازة
- وغيرها...

---

## 🔐 الأمان

- ✅ CORS مفعّل
- ✅ SECRET_KEY للجلسات
- ✅ HTTPS على Render

---

## 📞 معلومات الاتصال

**البوت:** @Sehasa_bot  
**الموقع:** https://seha-medical-system.onrender.com

---

## 📝 الترخيص

هذا المشروع مملوك لـ [اسمك/شركتك]

---

**تم التطوير بواسطة Manus AI**  
**5 أكتوبر 2025**
