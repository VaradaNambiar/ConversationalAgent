# Firestore Chat Memory Setup Guide

## What You Need to Do Before Running

### 1. Google Cloud Setup
1. **Enable Firestore**: Go to [Google Cloud Console](https://console.cloud.google.com)
2. Navigate to your project: `langchain-chatbot-3de42`
3. Enable the **Firestore API**
4. Create a **service account** with Firestore permissions
5. Download the **service account key** (JSON file)

### 2. Authentication Setup
Option A - **Service Account Key** (Recommended for development):
```bash
# Set environment variable to point to your service account key
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\service-account-key.json
```

Option B - **Application Default Credentials**:
```bash
# Install Google Cloud CLI and authenticate
gcloud auth application-default login
```

### 3. Environment Variables
Create a `.env` file in your project directory:
```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\service-account-key.json
```

### 4. Run Your Code
```bash
python tutorial_memory_in_cloud.py
```

## How It Works

### Key Differences from In-Memory Storage:

1. **Persistent Storage**: Chat history survives app restarts
2. **Scalable**: Multiple users can have separate conversations
3. **Cloud-Based**: Access from anywhere
4. **Firestore Structure**: 
   ```
   Collection: chat_sessions
   Document: session_id (e.g., "user_firestore_123")
   Fields: messages array with timestamps
   ```

### Memory Benefits:
- ✅ **Persistent**: Data survives app crashes/restarts
- ✅ **Scalable**: Handles thousands of concurrent users
- ✅ **Searchable**: Can query chat history
- ✅ **Backed up**: Google's infrastructure
- ✅ **Real-time**: Multiple clients can see updates

### Cost Considerations:
- **Firestore pricing**: Pay per read/write operation
- **Typical usage**: ~$0.18 per 100K document reads
- **Free tier**: 50K reads, 20K writes per day

## Troubleshooting

### Common Issues:

1. **Authentication Error**:
   ```
   google.auth.exceptions.DefaultCredentialsError
   ```
   **Solution**: Set `GOOGLE_APPLICATION_CREDENTIALS` or run `gcloud auth application-default login`

2. **Permission Denied**:
   ```
   google.api_core.exceptions.PermissionDenied
   ```
   **Solution**: Ensure your service account has Firestore permissions

3. **Project Not Found**:
   ```
   google.api_core.exceptions.NotFound
   ```
   **Solution**: Verify PROJECT_ID is correct and Firestore is enabled

### Useful Commands:
```bash
# Check authentication status
gcloud auth list

# Set active project
gcloud config set project langchain-chatbot-3de42

# List Firestore collections
gcloud firestore collections list
```
