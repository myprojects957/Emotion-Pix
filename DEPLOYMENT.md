# Emotionix - Movie Recommendation App Based on Emotion Detection

## Deployment on Render

### Prerequisites
1. GitHub account with the project repository
2. Render account (https://render.com)
3. Supabase project created (for authentication)
4. RapidAPI key (for IMDB API access)

### Environment Variables to Set on Render

Add these environment variables in your Render service settings:

```
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
SECRET_KEY=your_flask_secret_key
RAPIDAPI_KEY=your_rapidapi_key
RAPIDAPI_HOST=imdb236.p.rapidapi.com
FLASK_SECRET_KEY=your_flask_secret_key
```

### Deployment Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - ready for Render"
   git push origin main
   ```

2. **Create a New Service on Render**
   - Go to https://dashboard.render.com
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Select the branch (main)

3. **Configure the Service**
   - **Name**: emotionix (or your preferred name)
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free (or upgrade as needed)

4. **Add Environment Variables**
   - Click "Advanced" or "Environment"
   - Add all the environment variables listed above

5. **Deploy**
   - Click "Create Web Service"
   - Wait for the deployment to complete (2-5 minutes)

### Verify Deployment

- Check the Render dashboard for build logs
- Visit your URL (https://your-app-name.onrender.com)
- Test the login and emotion detection features

### Notes

- Session data is stored in the filesystem. For production, consider using Redis for session management
- Movie cache uses SQLite. For production, consider migrating to PostgreSQL
- Camera access requires HTTPS (automatically provided by Render)
- Free tier apps go to sleep after 15 minutes of inactivity

### Troubleshooting

- **Build Fails**: Check requirements.txt for version compatibility
- **Runtime Issues**: Check Render logs for error messages
- **API Errors**: Verify all environment variables are set correctly
- **File Not Found**: Ensure all paths use `url_for()` for static files
