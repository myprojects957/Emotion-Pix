# How to Fix "Invalid Supabase API key" Error

## Quick Fix Steps

### Step 1: Get Your Correct Supabase API Key

1. **Go to Supabase Dashboard**
   - Visit: https://supabase.com/dashboard
   - Sign in to your account

2. **Select Your Project**
   - Click on your project (or create a new one if needed)

3. **Navigate to API Settings**
   - Click on **Settings** (gear icon) in the left sidebar
   - Click on **API** in the settings menu

4. **Copy the Correct Key**
   - Find the **"Project API keys"** section
   - Look for **"anon public"** key
   - Click the **copy icon** next to it
   - ⚠️ **IMPORTANT**: Use the **anon public** key, NOT the **service_role** key!

### Step 2: Update in Render Dashboard

1. **Go to Render Dashboard**
   - Visit: https://dashboard.render.com
   - Sign in to your account

2. **Select Your Web Service**
   - Click on your Emotionix web service

3. **Go to Environment Tab**
   - Click on **Environment** in the left sidebar

4. **Update SUPABASE_KEY**
   - Find the `SUPABASE_KEY` variable
   - Click on it to edit
   - **Delete the old value**
   - **Paste your anon public key** from Supabase
   - Click **Save Changes**

5. **Verify SUPABASE_URL**
   - While you're there, also verify `SUPABASE_URL` is correct
   - It should look like: `https://xxxxxxxxxxxxx.supabase.co`
   - You can find this in the same Supabase API settings page

### Step 3: Redeploy

- Render will **automatically redeploy** after you save environment variables
- Or manually click **"Manual Deploy"** → **"Deploy latest commit"**
- Wait for the deployment to complete (usually 2-5 minutes)

### Step 4: Verify It Works

1. **Check Deployment Logs**
   - In Render dashboard, go to **Logs** tab
   - Look for: `Supabase client initialized successfully`
   - You should NOT see: `Invalid API key` error

2. **Test the Application**
   - Visit your app URL: `https://your-app-name.onrender.com`
   - Try to register or login
   - The error should be gone!

---

## Common Mistakes to Avoid

### ❌ Wrong: Using service_role Key
- **Don't use** the `service_role` key (it's longer, ~800+ characters)
- **Use** the `anon public` key instead (~200-300 characters)

### ❌ Wrong: Using Wrong Project
- Make sure you're copying the key from the **correct Supabase project**
- The URL and key must be from the same project

### ❌ Wrong: Extra Spaces or Characters
- When pasting, make sure there are **no extra spaces** before or after
- Don't include quotes around the key
- Copy exactly as shown in Supabase dashboard

### ❌ Wrong: Using Old/Revoked Key
- If you regenerated keys in Supabase, make sure you're using the **latest** key
- Old keys won't work after regeneration

---

## How to Identify the Correct Key

### ✅ Correct: anon public Key
- Starts with `eyJ` (JWT format)
- Usually 200-300 characters long
- Labeled as **"anon public"** or **"anon"** in Supabase dashboard
- Safe to use in client-side code

### ❌ Wrong: service_role Key
- Also starts with `eyJ`
- Usually 800+ characters long
- Labeled as **"service_role"** in Supabase dashboard
- **NEVER** use this in client-side code (security risk!)

---

## Still Having Issues?

### Check the Health Endpoint
Visit: `https://your-app-name.onrender.com/health`

This will show you:
- Whether Supabase is configured
- Whether environment variables are set
- The specific error message

### Verify Environment Variables in Render
1. Go to Render → Your Service → Environment
2. Check that both `SUPABASE_URL` and `SUPABASE_KEY` are set
3. Make sure there are no typos or extra spaces

### Check Render Logs
1. Go to Render → Your Service → Logs
2. Look for error messages during startup
3. The logs will show the exact error

### Test Locally First
1. Create a `.env` file in your project root:
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-anon-public-key
   ```
2. Run: `python app.py`
3. Check if it works locally
4. If it works locally but not on Render, the issue is with Render environment variables

---

## Need More Help?

- **Supabase Docs**: https://supabase.com/docs/guides/api
- **Render Docs**: https://render.com/docs/environment-variables
- **Check Supabase Status**: https://status.supabase.com
