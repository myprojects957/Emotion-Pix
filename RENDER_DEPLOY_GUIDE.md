# Render Deployment Guide - Fixed

## Quick Start

### Step 1: Push to GitHub
```bash
git push origin main
```

### Step 2: Configure Render

**Important**: Do NOT set "Root Directory" - leave it blank or set to `/`

**Create New Web Service on Render**:
1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: emotionix
   - **Runtime**: Python
   - **Region**: Auto (or select closest to you)
   - **Branch**: main
   - **Build Command**: `pip install --no-cache-dir -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free (or Starter+)
   - **Root Directory**: Leave BLANK (this was causing the error!)

### Step 3: Set Environment Variables

Click "Advanced" and add these environment variables:

```
SUPABASE_URL=https://kqhrkboqoxegibmbutun.supabase.co
SUPABASE_KEY=sb_publishable_1yGbsSNMrQkP10qSOMCaUQ_MdVoMet1
SECRET_KEY=30cb9ec6a2ac4e084b6353b063b2648a
FLASK_SECRET_KEY=30cb9ec6a2ac4e084b6353b063b2648a
RAPIDAPI_KEY=2040bb51dfmsh0b3d86e3a9ba373p138437jsn1c7d14412fe9
RAPIDAPI_HOST=imdb236.p.rapidapi.com
```

### Step 4: Deploy

Click "Create Web Service" - Render will start building and deploying automatically.

---

## If You Get "pip install failed" Error

The issue is usually one of these:

### Fix 1: Clear Render Cache
1. Go to your Render dashboard
2. Click your service
3. Click "Logs"
4. Look for errors with specific packages
5. If it's a build cache issue:
   - Go to "Settings" → "Environment"
   - Add a dummy variable change to force rebuild
   - Render will clear cache

### Fix 2: Root Directory Setting
⚠️ **CRITICAL**: Make sure "Root Directory" is **BLANK** or `/`

If you set a subdirectory, Render can't find requirements.txt!

### Fix 3: Check requirements.txt

Our updated requirements.txt has compatible versions:
- `opencv-python-headless==4.8.1.78` (not 4.8.0.76)
- `fastai==2.7.13` (instead of fer which had dependency issues)
- `numpy==1.26.3` (compatible with latest packages)
- Removed problematic `fer==22.4.0` package

---

## Monitoring Deployment

1. **Build Logs**: Real-time build output
2. **Deploy Logs**: Application startup logs
3. **Runtime Logs**: Live application logs

Common successful messages:
```
[2026-01-09 12:34:56] Started server process
[2026-01-09 12:34:57] Uvicorn running on http://0.0.0.0:10000
```

---

## Troubleshooting

| Error | Solution |
|-------|----------|
| `pip install failed` | Check Root Directory is blank, verify requirements.txt syntax |
| `ModuleNotFoundError` | Ensure all imports match installed package names |
| `Address already in use` | Render manages ports automatically, shouldn't happen |
| `Timeout during build` | May indicate package download issue, try rebuilding |
| `File not found .env` | .env is local-only, environment variables set in Render dashboard |

---

## After Deployment

1. **Test the app**: Click the URL at top of Render dashboard
2. **Check health**: Monitor logs in real-time
3. **Monitor usage**: Render shows CPU, memory, bandwidth usage

---

## Important Security Notes

✅ **What we fixed**:
- `.env` is now in `.gitignore` (won't be committed)
- Created `.env.example` for users to see what variables are needed
- Updated to compatible package versions

✅ **Never do this**:
- ❌ Don't commit real `.env` files with secrets
- ❌ Don't hardcode API keys in code
- ❌ Don't share API keys in documentation

✅ **Always**:
- ✅ Use Render's "Environment" tab to set secrets
- ✅ Use `.env.example` template for documentation
- ✅ Keep `.env` in `.gitignore`
- ✅ Rotate API keys regularly

---

## Still Having Issues?

1. **Clear build cache**: Stop and redeploy service
2. **Check Render status**: https://status.render.com
3. **Verify Python version**: Should be 3.11+ (set in runtime.txt)
4. **Test locally first**: `python app.py` should work on your machine

---

## Deployment Success Checklist

- [ ] GitHub repository has latest code
- [ ] Root Directory is BLANK (not set to subdirectory)
- [ ] Build Command: `pip install --no-cache-dir -r requirements.txt`
- [ ] Start Command: `gunicorn app:app`
- [ ] All environment variables set in Render dashboard
- [ ] `.env` file is NOT committed to git
- [ ] requirements.txt uses updated package versions
- [ ] runtime.txt specifies Python 3.11.7
- [ ] Procfile contains `web: gunicorn app:app`

Once all checkboxes are done, redeploy and check logs!
