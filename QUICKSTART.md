# 🚀 Quick Start - Milestone 1

Get your AlOCR pipeline running in **under 5 minutes**!

---

## ⚡ TL;DR

```powershell
# 1. Activate environment
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run pipeline
python run_milestone1.py

# 4. Check results
Get-ChildItem data\validation_reports\milestone1_final_report_*.txt | Get-Content
```

---

## 📋 Prerequisites Checklist

- [x] Python 3.8+ installed
- [x] 265 images in `data/raw/aadhar_dataset/test/images/`
- [x] Virtual environment at `venv/`

---

## 🎯 Step-by-Step (5 Minutes)

### Step 1: Activate Environment (30 seconds)

```powershell
.\venv\Scripts\Activate.ps1
```

**Expected:** Your prompt shows `(venv)` prefix

### Step 2: Install Dependencies (2 minutes)

```powershell
pip install -r requirements.txt
```

**Expected:** All packages install successfully

### Step 3: Run Pipeline (15-20 minutes)

```powershell
python run_milestone1.py
```

**Expected Output:**
```
================================================================================
                    AlOCR PROJECT - MILESTONE 1
               Data Collection and Preprocessing
================================================================================

--------------------------------------------------------------------------------
  STEP 1: DATA COLLECTION AND VALIDATION
--------------------------------------------------------------------------------

Found 265 image files
Cataloging documents: 100%|█████████████████| 265/265

DATA COLLECTION COMPLETED
Total Documents: 265
Valid: 265 | Invalid: 0

--------------------------------------------------------------------------------
  STEP 2: ADVANCED IMAGE PREPROCESSING
--------------------------------------------------------------------------------

Preprocessing images: 100%|█████████████████| 265/265

IMAGE PREPROCESSING COMPLETED
Total Processed: 265
Successful: 265 | Failed: 0

--------------------------------------------------------------------------------
  STEP 3: AZURE AI DOCUMENT INTELLIGENCE PREPARATION
--------------------------------------------------------------------------------

Preparing for Azure: 100%|█████████████████| 265/265

AZURE PREPARATION COMPLETED
Azure Compatible: 265 | Rejected: 0

================================================================================
MILESTONE 1 EXECUTION SUMMARY
================================================================================
Data Collection:    ✓ Success
Preprocessing:      ✓ Success
Azure Preparation:  ✓ Success
--------------------------------------------------------------------------------
✓ MILESTONE 1 COMPLETED SUCCESSFULLY!

Final Report: data\validation_reports\milestone1_final_report_20251029_121500.txt
================================================================================
```

### Step 4: Verify Results (1 minute)

```powershell
# Check final report
Get-ChildItem data\validation_reports\milestone1_final_report_*.txt | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Get-Content

# View processed images
explorer data\preprocessed

# Check Azure-ready images
explorer data\azure_ready
```

---

## ✅ Success Indicators

**You're successful if you see:**
- ✓ "MILESTONE 1 COMPLETED SUCCESSFULLY!"
- ✓ 265 images in `data/preprocessed/`
- ✓ 265 images in `data/azure_ready/`
- ✓ 4+ files in `data/validation_reports/`
- ✓ 5+ files in `data/metadata/`

---

## 🔍 What Just Happened?

1. **Data Collection** (3 min)
   - Validated 265 Aadhaar images
   - Extracted metadata
   - Created catalog in CSV/Excel/JSON

2. **Preprocessing** (15 min)
   - Applied quality checks
   - Deskewed images
   - Removed noise
   - Applied thresholding

3. **Azure Prep** (2 min)
   - Validated Azure compatibility
   - Copied compatible images
   - Generated batch config

---

## 📊 Where Are My Results?

```
data/
├── metadata/                   📁 Catalogs & processing results
│   ├── document_catalog_*.csv  📄 All image info
│   ├── document_catalog_*.xlsx 📊 Excel version
│   └── preprocessing_results_*.csv 📄 Processing metrics
│
├── preprocessed/               📁 265 processed images
│   └── *.jpg
│
├── azure_ready/                📁 265 Azure-ready images
│   ├── *.jpg
│   └── azure_batch_config.yaml ⚙️ Batch config
│
└── validation_reports/         📁 Detailed reports
    ├── collection_report_*.txt
    ├── preprocessing_report_*.txt
    ├── azure_prep_report_*.txt
    └── milestone1_final_report_*.txt ⭐ READ THIS!
```

---

## 🎯 Next Actions

### Immediate (Now)
```powershell
# Read the final report
notepad data\validation_reports\milestone1_final_report_*.txt

# Check processing quality
notepad data\validation_reports\preprocessing_report_*.txt
```

### Short-term (This Week)
1. Review quality metrics in reports
2. Inspect sample preprocessed images
3. Set up Azure AI credentials for Milestone 2

### Long-term (Next Week)
1. Implement Milestone 2 (OCR & Verification)
2. Set up Azure AI Document Intelligence
3. Build fraud detection models

---

## ⚠️ Troubleshooting

### Problem: "Cannot activate venv"
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### Problem: "Module not found"
```powershell
pip install -r requirements.txt --force-reinstall
```

### Problem: "No images found"
```powershell
# Verify images exist
Get-ChildItem data\raw\aadhar_dataset\test\images | Measure-Object
# Should show: Count : 265
```

### Problem: Takes too long
- **Normal**: 15-20 minutes total
- **Slow**: Check CPU usage, close other apps
- **Very slow**: Edit `config/config.yaml`, reduce `denoise_strength` to 20

---

## 📚 Need More Details?

- **Full Documentation**: `README.md`
- **Detailed Guide**: `docs/MILESTONE1_EXECUTION_GUIDE.md`
- **Configuration**: `config/config.yaml`
- **Logs**: `logs/milestone1_*.log`

---

## 🎉 That's It!

**Milestone 1 Complete!**  
You now have:
- ✅ 265 validated Aadhaar images
- ✅ Comprehensive metadata
- ✅ OCR-optimized preprocessed images
- ✅ Azure-ready images
- ✅ Detailed quality reports

**Ready for Milestone 2: AI-OCR and Document Verification!** 🚀

---

## 💡 Pro Tips

1. **Always check the final report first**
   ```powershell
   Get-ChildItem data\validation_reports\milestone1_final_report_*.txt | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Get-Content
   ```

2. **Run individual steps if needed**
   ```powershell
   python scripts\data_collection.py
   python scripts\advanced_preprocessing.py
   python scripts\azure_prep.py
   ```

3. **Skip completed steps**
   ```powershell
   python run_milestone1.py --skip-collection --skip-preprocessing
   ```

4. **Backup your results**
   ```powershell
   Compress-Archive -Path data\metadata,data\validation_reports -DestinationPath milestone1_backup_$(Get-Date -Format 'yyyyMMdd').zip
   ```

---

**Happy Processing! 🎯**
