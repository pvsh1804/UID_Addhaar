# AlOCR Project - AI-Powered Aadhaar OCR and Document Verification

## 📋 Project Overview

The **AlOCR Project** is an advanced document intelligence system for Aadhaar card processing, featuring:
- Automated data collection and validation
- Advanced image preprocessing with quality assessment
- Azure AI Document Intelligence integration
- Document verification and fraud detection capabilities

---

## 🎯 Milestone 1: Data Collection and Preprocessing

### Objectives
✅ **Collect** Aadhaar documents and validate quality  
✅ **Preprocess** images for optimal OCR performance  
✅ **Extract** metadata for training and testing  
✅ **Ensure** compatibility with Azure AI Document Intelligence

### Current Status: **COMPLETED** ✓

---

## 🏗️ Project Structure

```
AlOCR_Project/
├── config/
│   └── config.yaml              # Configuration settings
├── data/
│   ├── raw/
│   │   └── aadhar_dataset/     # Raw Aadhaar images
│   ├── preprocessed/            # Processed images
│   ├── azure_ready/             # Azure-compatible images
│   ├── metadata/                # Document catalogs & metadata
│   └── validation_reports/      # Quality & validation reports
├── scripts/
│   ├── data_collection.py       # Data collection module
│   ├── advanced_preprocessing.py # Image preprocessing
│   ├── azure_prep.py            # Azure preparation
│   ├── load_images.py           # Legacy image loader
│   └── preprocess_images.py     # Legacy preprocessor
├── docs/                        # Documentation
├── logs/                        # Execution logs
├── venv/                        # Python virtual environment
├── .env.template                # Environment variables template
├── requirements.txt             # Python dependencies
├── run_milestone1.py            # Main pipeline execution
└── README.md                    # This file
```

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- Windows/Linux/macOS
- 265 Aadhaar card images (already in `data/raw/aadhar_dataset/test/images/`)

### 2. Installation

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

#### a. Review Configuration
Edit `config/config.yaml` to customize:
- Image quality thresholds
- Preprocessing techniques
- Azure AI settings

#### b. Set Up Azure Credentials (Optional for Milestone 1)
```powershell
# Copy environment template
Copy-Item .env.template .env

# Edit .env and add your Azure credentials
# AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=your_endpoint
# AZURE_DOCUMENT_INTELLIGENCE_KEY=your_key
```

### 4. Run the Complete Pipeline

```powershell
# Run all steps
python run_milestone1.py

# Or run with options
python run_milestone1.py --skip-collection    # Skip data collection
python run_milestone1.py --skip-preprocessing # Skip preprocessing
python run_milestone1.py --skip-azure        # Skip Azure prep
```

### 5. Run Individual Modules

```powershell
# Data Collection only
python scripts/data_collection.py

# Preprocessing only
python scripts/advanced_preprocessing.py

# Azure Preparation only
python scripts/azure_prep.py
```

---

## 📊 Pipeline Overview

### Step 1: Data Collection & Validation
**Module:** `scripts/data_collection.py`

**What it does:**
- Scans raw image directory for Aadhaar documents
- Validates image format, size, and dimensions
- Extracts comprehensive metadata (DPI, dimensions, file size, etc.)
- Generates document catalog (CSV, Excel, JSON)
- Creates validation reports

**Outputs:**
- `data/metadata/document_catalog_*.csv`
- `data/metadata/document_catalog_*.xlsx`
- `data/metadata/document_catalog_*.json`
- `data/validation_reports/collection_report_*.txt`

### Step 2: Advanced Preprocessing
**Module:** `scripts/advanced_preprocessing.py`

**What it does:**
- Quality assessment (blur detection, brightness check)
- Image deskewing (rotation correction)
- Noise removal using advanced algorithms
- Grayscale conversion
- Adaptive thresholding (Otsu's method)

**Techniques Applied:**
- ✓ Deskewing for rotation correction
- ✓ Grayscale conversion
- ✓ Non-local means denoising
- ✓ Otsu's adaptive thresholding
- ✓ Quality metric calculation

**Outputs:**
- `data/preprocessed/*.jpg` (processed images)
- `data/metadata/preprocessing_results_*.csv`
- `data/validation_reports/preprocessing_report_*.txt`

### Step 3: Azure AI Preparation
**Module:** `scripts/azure_prep.py`

**What it does:**
- Validates images against Azure requirements
- Checks file size (< 4 MB)
- Verifies dimensions (50x50 to 10,000x10,000 pixels)
- Confirms format compatibility
- Copies compatible images to Azure-ready directory
- Generates batch processing configuration

**Azure Requirements Met:**
- ✓ Supported formats: JPEG, PNG, BMP, TIFF
- ✓ File size < 4 MB
- ✓ Proper dimensions
- ✓ DPI recommendations

**Outputs:**
- `data/azure_ready/*.jpg` (Azure-compatible images)
- `data/azure_ready/azure_batch_config.yaml`
- `data/metadata/azure_prep_results_*.csv`
- `data/validation_reports/azure_prep_report_*.txt`

---

## 📈 Configuration Details

### Image Quality Thresholds (`config/config.yaml`)

```yaml
preprocessing:
  min_width: 600              # Minimum image width
  min_height: 400             # Minimum image height
  max_file_size_mb: 10        # Maximum file size
  blur_threshold: 100.0       # Laplacian variance threshold
  brightness_range: [30, 225] # Acceptable brightness range
  denoise_strength: 30        # Denoising strength
```

### Preprocessing Techniques

```yaml
techniques:
  grayscale: true    # Convert to grayscale
  denoise: true      # Apply noise reduction
  threshold: true    # Apply binarization
  deskew: true       # Correct rotation
  resize: false      # Resize images
```

### Azure Settings

```yaml
azure:
  max_image_size_mb: 4
  recommended_dpi: 300
  api_version: "2023-07-31"
  locale: "en-IN"
```

---

## 📝 Reports and Outputs

### Collection Report
- Total documents found and validated
- Format distribution
- Size statistics
- Validation errors

### Preprocessing Report
- Processing success rate
- Quality metrics (blur, brightness)
- Images with quality issues
- Processing statistics

### Azure Preparation Report
- Azure compatibility rate
- Rejected images and reasons
- Batch configuration details
- Next steps for Milestone 2

### Final Milestone Report
- Overall execution status
- Deliverables checklist
- Output directory summary
- Roadmap for Milestone 2

---

## 🔧 Troubleshooting

### Issue: Virtual environment not activated
```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
.\venv\Scripts\activate.bat

# Linux/macOS
source venv/bin/activate
```

### Issue: Missing dependencies
```powershell
pip install -r requirements.txt
```

### Issue: No images found
- Verify images are in `data/raw/aadhar_dataset/test/images/`
- Check supported formats: .jpg, .jpeg, .png, .bmp, .tiff

### Issue: Permission errors
- Run PowerShell as Administrator
- Check folder write permissions

### Issue: Azure credentials warning
- This is expected for Milestone 1
- Set credentials in `.env` when ready for Milestone 2

---

## 📚 Key Features

### Data Collection
- ✅ Automatic image discovery
- ✅ Multi-format support
- ✅ Comprehensive validation
- ✅ Metadata extraction
- ✅ Multiple export formats (CSV, Excel, JSON)

### Preprocessing
- ✅ Quality assessment (blur, brightness)
- ✅ Automatic deskewing
- ✅ Advanced denoising
- ✅ Adaptive thresholding
- ✅ Batch processing with progress tracking

### Azure Integration
- ✅ Azure API compatibility validation
- ✅ Automatic format conversion
- ✅ Batch configuration generation
- ✅ Credential management
- ✅ Ready for OCR processing

---

## 🎓 Technical Details

### Image Processing Pipeline

1. **Input Validation**
   - Format check
   - Size verification
   - Dimension validation
   - Corruption detection

2. **Quality Assessment**
   - Blur detection (Laplacian variance)
   - Brightness analysis
   - DPI verification

3. **Enhancement**
   - Rotation correction (deskewing)
   - Noise reduction (fastNlMeansDenoising)
   - Contrast enhancement

4. **Normalization**
   - Grayscale conversion
   - Adaptive thresholding (Otsu's method)
   - Format standardization

### Quality Metrics

- **Blur Score**: Laplacian variance > 100 (good), < 100 (blurry)
- **Brightness**: Range 30-225 (optimal for OCR)
- **Dimensions**: Minimum 600x400, Maximum 10,000x10,000
- **File Size**: 10 KB - 4 MB (Azure compatible)

---

## 🛣️ Roadmap

### ✅ Milestone 1: Data Collection and Preprocessing (COMPLETED)
- Data collection and validation
- Image preprocessing
- Azure compatibility preparation
- Comprehensive reporting

### 🔄 Milestone 2: AI-OCR and Document Verification (NEXT)
- Azure AI Document Intelligence integration
- OCR text extraction
- Field identification (Name, DOB, Aadhaar number, etc.)
- Document authenticity verification
- Fraud detection algorithms
- API endpoint development

---

## 💡 Best Practices

1. **Always review reports** after each pipeline execution
2. **Check quality metrics** before sending to Azure
3. **Backup raw data** before processing
4. **Monitor logs** in `logs/` directory for detailed execution info
5. **Update configuration** based on your dataset characteristics
6. **Test Azure credentials** before batch processing

---

## 📞 Support & Documentation

### Additional Documentation
- `docs/MILESTONE1_GUIDE.md` - Detailed Milestone 1 guide
- `docs/AZURE_SETUP.md` - Azure AI setup instructions
- `config/config.yaml` - Configuration reference

### Logs Location
- `logs/milestone1_*.log` - Full pipeline logs
- `logs/alocr_pipeline.log` - Individual module logs

### Reports Location
- `data/validation_reports/` - All validation and execution reports
- `data/metadata/` - Processed data catalogs

---

## 📄 License

This project is developed for Aadhaar document processing and OCR verification.

---

## 🎉 Achievement Summary

**Milestone 1 Deliverables:**
- ✅ 265 Aadhaar images collected and validated
- ✅ Comprehensive metadata extracted
- ✅ Advanced preprocessing pipeline implemented
- ✅ Azure AI compatibility ensured
- ✅ Detailed documentation and reports generated
- ✅ Production-ready pipeline created

**Ready for Milestone 2!** 🚀
