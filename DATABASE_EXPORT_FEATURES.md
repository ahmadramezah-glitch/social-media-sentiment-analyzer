# Database Export Features

## Overview
The Database Viewer page now includes comprehensive export functionality that allows users to export data with hashtag filtering directly from the database interface.

## Export Features

### 1. Hashtag-Specific Export
- **Location**: Database Viewer page, right after the hashtag filter
- **Functionality**: 
  - Filter by a specific hashtag using the dropdown
  - Export only that hashtag's data
  - Available in both Excel and PDF formats

### 2. All Data Export
- **Location**: Database Viewer page, export section
- **Functionality**: Export all available data in the system
- **Available in**: Excel and PDF formats

## Export Locations

### Primary Export Buttons (Top of Page)
- **Position**: Right after the hashtag filter section
- **Dynamic**: Changes based on whether a hashtag is selected
- **Features**: 
  - Large, prominent buttons
  - Clear labeling with hashtag names
  - Professional styling with hover effects

### Quick Export Section (Bottom of Page)
- **Position**: Bottom export section
- **Features**: 
  - Smaller outline buttons
  - Quick access to all data export
  - Informational content about export capabilities

## Export Formats

### Excel Export (.xlsx)
- **Route**: `/export-database?format=excel&hashtag={hashtag}`
- **Features**:
  - Professional styling with blue headers
  - Comprehensive data including all post fields
  - Auto-adjusted column widths
  - Includes: ID, Caption, Sentiment, Polarity, Hashtag, Source, Likes, Comments, Media URL, Permalink, Overall Sentiment, Overall Polarity, Created At

### PDF Export (.pdf)
- **Route**: `/export-database?format=pdf&hashtag={hashtag}`
- **Features**:
  - Professional report format
  - Summary statistics table
  - Detailed posts table
  - Includes: ID, Caption, Sentiment, Polarity, Hashtag, Created At

## How to Use

### Step 1: Navigate to Database Viewer
- Go to the Database Viewer page
- You'll see the hashtag filter at the top

### Step 2: Choose Export Option
- **For specific hashtag**: 
  1. Select a hashtag from the dropdown
  2. Click "Apply Filter"
  3. Use the export buttons that appear below the filter

- **For all data**: 
  1. Leave hashtag filter as "All Hashtags"
  2. Use the export buttons or quick export section

### Step 3: Choose Format
- **Excel**: For data analysis, spreadsheets, further processing
- **PDF**: For reports, presentations, sharing

## File Naming Convention

### Hashtag-Specific Exports
- **Excel**: `database_export_{hashtag}_YYYYMMDD_HHMMSS.xlsx`
- **PDF**: `database_export_{hashtag}_YYYYMMDD_HHMMSS.pdf`

### All Data Exports
- **Excel**: `database_export_all_YYYYMMDD_HHMMSS.xlsx`
- **PDF**: `database_export_all_YYYYMMDD_HHMMSS.pdf`

## Technical Implementation

### New Routes Added
- `/export-database` - Main database export route
- Supports both Excel and PDF formats
- Handles hashtag filtering

### Helper Functions
- `export_database_excel()` - Excel generation with hashtag filtering
- `export_database_pdf()` - PDF generation with hashtag filtering

### Security
- Requires authentication
- Permission-based access control
- Users must have `can_view_filtered_results` permission

## Benefits

### 1. **Convenience**
- Export directly from the database viewer
- No need to navigate to other pages

### 2. **Flexibility**
- Choose specific hashtags or all data
- Multiple export formats available

### 3. **Professional Output**
- Styled Excel files with proper formatting
- Professional PDF reports with summaries

### 4. **Data Integrity**
- Exports respect current filters
- Consistent with what's displayed on screen

## Example Usage Scenarios

### Scenario 1: Marketing Team
- Filter by brand hashtag (e.g., #brandname)
- Export to Excel for sentiment analysis in external tools
- Share PDF report with stakeholders

### Scenario 2: Data Analysis
- Export all data to Excel
- Perform advanced analytics in spreadsheet software
- Create custom visualizations

### Scenario 3: Reporting
- Filter by campaign hashtag
- Generate PDF report for monthly review
- Include in presentations

## Future Enhancements

- CSV export option
- Custom date range filtering
- Batch export multiple hashtags
- Email export functionality
- Export scheduling
- Custom field selection
