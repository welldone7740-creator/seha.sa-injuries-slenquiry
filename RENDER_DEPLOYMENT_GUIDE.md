# دليل استضافة موقع صحة على Render.com
## Seha Medical System - Render.com Deployment Guide

**آخر تحديث:** 5 أكتوبر 2025  
**الإصدار:** 2.0 Final

---

## 🌐 نظرة عامة

هذا الدليل يشرح كيفية استضافة موقع صحة الطبي على **Render.com** بشكل مجاني.

**مميزات Render.com:**
- ✅ استضافة مجانية
- ✅ يدعم Flask و Python
- ✅ يدعم قواعد البيانات SQLite
- ✅ SSL مجاني (HTTPS)
- ✅ نشر تلقائي من GitHub
- ✅ سهل الاستخدام

---

## 📋 المتطلبات

1. حساب على GitHub (مجاني)
2. حساب على Render.com (مجاني)
3. ملفات المشروع (المرفقة)

---

## 🚀 الخطوة 1: إنشاء حساب GitHub

### إذا لم يكن لديك حساب:

1. افتح: https://github.com/signup
2. أدخل بريدك الإلكتروني
3. أنشئ كلمة مرور
4. اختر اسم مستخدم
5. أكمل التسجيل

---

## 📦 الخطوة 2: رفع المشروع على GitHub

### الطريقة 1: عبر واجهة GitHub (سهلة)

#### 1. إنشاء مستودع جديد:
- افتح: https://github.com/new
- **Repository name:** `seha-medical-system`
- **Description:** نظام صحة الطبي لإدارة الإجازات المرضية
- اختر: **Public** (عام)
- ✅ فعّل: **Add a README file**
- اضغط: **Create repository**

#### 2. رفع الملفات:
- اضغط على: **Add file** → **Upload files**
- اسحب جميع ملفات المشروع (من ملف ZIP)
- **⚠️ مهم:** لا ترفع مجلد `venv` أو ملفات `.db`
- اكتب رسالة: `Initial commit`
- اضغط: **Commit changes**

### الطريقة 2: عبر Git (متقدمة)

```bash
# 1. فك ضغط الملف
unzip seha_website_render.zip
cd seha_website_render

# 2. تهيئة Git
git init
git add .
git commit -m "Initial commit"

# 3. ربط بـ GitHub
git remote add origin https://github.com/YOUR_USERNAME/seha-medical-system.git
git branch -M main
git push -u origin main
```

---

## 🔧 الخطوة 3: إنشاء حساب Render

1. افتح: https://render.com/
2. اضغط: **Get Started**
3. اختر: **Sign up with GitHub**
4. امنح Render الصلاحيات المطلوبة

---

## 🌐 الخطوة 4: نشر الموقع على Render

### 1. إنشاء Web Service جديد:

- من لوحة التحكم، اضغط: **New** → **Web Service**
- اختر: **Build and deploy from a Git repository**
- اضغط: **Next**

### 2. ربط المستودع:

- ابحث عن: `seha-medical-system`
- اضغط: **Connect**

### 3. إعدادات الخدمة:

املأ الحقول التالية:

| الحقل | القيمة |
|------|--------|
| **Name** | `seha-medical-system` |
| **Region** | اختر أقرب منطقة لك |
| **Branch** | `main` |
| **Root Directory** | اتركه فارغاً |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn src.main:app` |

### 4. اختر الخطة:

- اختر: **Free** (مجاني)
- ⚠️ **ملاحظة:** الخطة المجانية تتوقف بعد 15 دقيقة من عدم الاستخدام

### 5. متغيرات البيئة (اختياري):

اضغط: **Advanced** → **Add Environment Variable**

| المفتاح | القيمة |
|---------|--------|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | أي قيمة عشوائية |

### 6. النشر:

- اضغط: **Create Web Service**
- انتظر 3-5 دقائق حتى يكتمل النشر
- ستحصل على رابط مثل: `https://seha-medical-system.onrender.com`

---

## ✅ الخطوة 5: التحقق من عمل الموقع

### 1. افتح الرابط:
```
https://YOUR-APP-NAME.onrender.com
```

### 2. اختبر الموقع:
- ✅ الصفحة الرئيسية تعمل
- ✅ نظام الاستعلام يعمل
- ✅ API يستقبل البيانات

### 3. اختبر API:
```bash
curl -X POST https://YOUR-APP-NAME.onrender.com/api/medical-leaves \
  -H "Content-Type: application/json" \
  -d '{
    "service_code": "PSL12345672025",
    "identity_number": "1234567890",
    "patient_name_ar": "أحمد محمد",
    "patient_name_en": "Ahmed Mohammed",
    "nationality_ar": "السعودية",
    "nationality_en": "Saudi Arabia",
    "workplace_ar": "موظف",
    "workplace_en": "Employee",
    "doctor_name_ar": "محمد الأحمد",
    "doctor_name_en": "Mohammed Al-Ahmad",
    "job_title_ar": "طبيب عام",
    "job_title_en": "General Practitioner",
    "admission_date_gregorian": "15-09-2025",
    "admission_date_hijri": "23-03-1447",
    "discharge_date_gregorian": "17-09-2025",
    "discharge_date_hijri": "25-03-1447",
    "report_issue_date": "17-09-2025",
    "facility_name_ar": "مستشفى الملك فهد",
    "facility_name_en": "King Fahd Hospital",
    "report_time": "10:30 AM",
    "duration_days": 3
  }'
```

---

## 🔄 الخطوة 6: تحديث رابط API في البوت

### 1. افتح ملف `config.py` في البوت:
```python
# قبل:
API_BASE_URL = 'https://3dhkilc8371w.manus.space'

# بعد:
API_BASE_URL = 'https://YOUR-APP-NAME.onrender.com'
```

### 2. احفظ الملف وأعد تشغيل البوت

---

## 📊 مراقبة الموقع

### عرض السجلات (Logs):
1. افتح لوحة تحكم Render
2. اختر خدمتك
3. اضغط على تبويب **Logs**
4. شاهد السجلات المباشرة

### عرض الإحصائيات:
- **Metrics:** استخدام الذاكرة والمعالج
- **Events:** تاريخ النشر والتحديثات

---

## 🔧 التحديثات والصيانة

### تحديث الموقع:

#### الطريقة 1: عبر GitHub (تلقائي)
1. عدّل الملفات في GitHub
2. احفظ التغييرات (Commit)
3. Render سيكتشف التغيير تلقائياً
4. سيعيد النشر تلقائياً

#### الطريقة 2: يدوياً
1. افتح لوحة تحكم Render
2. اختر خدمتك
3. اضغط: **Manual Deploy** → **Deploy latest commit**

---

## 🗄️ إدارة قاعدة البيانات

### ملاحظة مهمة:
- قاعدة البيانات SQLite **مؤقتة** على Render المجاني
- البيانات **تُحذف** عند إعادة تشغيل الخدمة
- للحفاظ على البيانات، استخدم:
  - **Render PostgreSQL** (مدفوع)
  - **Supabase** (مجاني)
  - **PlanetScale** (مجاني)

### حل بديل (للاختبار):
استخدم البيانات التجريبية في كل مرة:
```bash
python add_sample_data.py
```

---

## ⚠️ القيود على الخطة المجانية

### Render Free Plan:
- ✅ **مجاني تماماً**
- ⚠️ **يتوقف بعد 15 دقيقة** من عدم الاستخدام
- ⚠️ **يستغرق 30-60 ثانية** للتشغيل مرة أخرى
- ⚠️ **750 ساعة/شهر** فقط
- ⚠️ **قاعدة البيانات مؤقتة**

### للتغلب على التوقف:
استخدم خدمة Ping مثل:
- **UptimeRobot** (مجاني): https://uptimerobot.com/
- **Cron-job.org** (مجاني): https://cron-job.org/

---

## 🔐 الأمان

### 1. تغيير SECRET_KEY:
```python
# في main.py
app.config['SECRET_KEY'] = 'YOUR_RANDOM_SECRET_KEY_HERE'
```

### 2. إخفاء المعلومات الحساسة:
- لا ترفع ملفات `.env` على GitHub
- استخدم Environment Variables في Render

### 3. تفعيل HTTPS:
- ✅ Render يوفر HTTPS تلقائياً

---

## 🆘 استكشاف الأخطاء

### المشكلة: "Application failed to start"
**الحل:**
- تحقق من السجلات (Logs)
- تأكد من صحة `requirements.txt`
- تأكد من صحة `Start Command`

### المشكلة: "Module not found"
**الحل:**
```bash
# تأكد من وجود المكتبة في requirements.txt
pip freeze > requirements.txt
```

### المشكلة: "Database not found"
**الحل:**
- تأكد من وجود مجلد `src/database/`
- تأكد من تشغيل `db.create_all()` في `main.py`

### المشكلة: الموقع بطيء
**السبب:** الخطة المجانية توقفت
**الحل:** انتظر 30-60 ثانية للتشغيل

---

## 📝 هيكل المشروع

```
seha_website_render/
├── src/
│   ├── main.py              # الملف الرئيسي
│   ├── models/              # نماذج قاعدة البيانات
│   ├── routes/              # مسارات API
│   ├── static/              # الملفات الثابتة (HTML, CSS, JS)
│   └── database/            # قاعدة البيانات
├── requirements.txt         # المكتبات المطلوبة
├── render.yaml              # إعدادات Render (اختياري)
├── .gitignore               # ملفات يتم تجاهلها
└── README.md                # ملف التوثيق
```

---

## 🎯 الخلاصة

بعد اتباع هذه الخطوات:
- ✅ الموقع مستضاف على Render
- ✅ رابط عام للموقع
- ✅ HTTPS مفعّل
- ✅ نشر تلقائي من GitHub
- ✅ مجاني تماماً

---

## 📞 الدعم

إذا واجهت أي مشكلة:
1. راجع السجلات في Render
2. راجع قسم "استكشاف الأخطاء"
3. تحقق من صحة الملفات
4. تأكد من اتباع جميع الخطوات

---

## 🔗 روابط مفيدة

- **Render Docs:** https://render.com/docs
- **Flask Docs:** https://flask.palletsprojects.com/
- **GitHub Docs:** https://docs.github.com/

---

**تم إعداد هذا الدليل بواسطة Manus AI**  
**5 أكتوبر 2025**

**بالتوفيق! 🎉**
