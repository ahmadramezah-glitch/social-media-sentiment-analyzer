# Export Features for Instagram Sentiment Analyzer

## Overview
This application now includes comprehensive export functionality that allows users to download hashtag analysis data in multiple formats.

## Export Formats

### 1. Excel Export (.xlsx)
- **Route**: `/export-excel`
- **Features**:
  - Comprehensive data including all post fields
  - Styled headers with professional formatting
  - Auto-adjusted column widths
  - Includes: Date, Caption, Sentiment, Polarity, Hashtag, Source, Likes, Comments, Media URL, Permalink, Overall Sentiment, Overall Polarity
  - Timestamped filenames

### 2. PDF Export (.pdf)
- **Route**: `/export-pdf`
- **Features**:
  - Professional report format
  - Summary statistics table
  - Detailed posts table
  - Includes: Date, Caption, Sentiment, Polarity, Hashtag, Likes, Comments
  - Timestamped filenames

### 3. Hashtag-Specific Export (.xlsx)
- **Route**: `/export-hashtag/<hashtag>`
- **Features**:
  - Export data for a specific hashtag only
  - Green-themed styling to distinguish from general exports
  - Same comprehensive data as general Excel export
  - Filename includes hashtag name

## Export Locations

### Dashboard
- Large export buttons prominently displayed
- Available when there's data to export
- Exports all available data

### Filtered Results Page
- Export buttons in the table header
- Respects current filters (date range, sentiment, etc.)
- Individual hashtag export buttons for each row

## Data Included in Exports

### Post Information
- **Basic Data**: Date, Caption, Sentiment, Polarity, Hashtag, Source
- **Engagement**: Like count, Comments count
- **Media**: Media URL, Permalink
- **Analysis**: Overall sentiment, Overall polarity

### Filtering Support
- Date range filtering
- Sentiment filtering (positive, negative, neutral)
- Hashtag filtering
- All filters are applied to exports

## Technical Implementation

### Dependencies Added
- `openpyxl==3.1.2` - For Excel file generation
- `reportlab==4.0.4` - For PDF generation

### Security
- All export routes require authentication
- Permission-based access control
- Users must have `can_view_filtered_results` permission

### File Handling
- Files generated in memory (no disk storage)
- Automatic cleanup after download
- Proper MIME types for browser handling

## Usage Instructions

1. **Navigate to Dashboard or Filtered Results**
2. **Apply desired filters** (optional)
3. **Click export button** for desired format
4. **File downloads automatically** with timestamped filename

## File Naming Convention

- **General Export**: `instagram_sentiment_analysis_YYYYMMDD_HHMMSS.xlsx/pdf`
- **Hashtag Export**: `hashtag_[hashtag]_analysis_YYYYMMDD_HHMMSS.xlsx`

## Styling Features

- **Export Buttons**: Hover effects with elevation and shadow
- **Hashtag Export Buttons**: Compact design with scale animation
- **Professional Color Scheme**: Consistent with application theme
- **Responsive Design**: Works on all screen sizes

## Future Enhancements

- CSV export option
- Custom date range selection for exports
- Batch export multiple hashtags
- Email export functionality
- Export scheduling
