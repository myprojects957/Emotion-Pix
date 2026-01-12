# ⚡ QUICK FIX: Invalid Supabase API Key

## 🔴 Current Error
```
Warning: SUPABASE_KEY format doesn't match expected JWT format.
Warning: Could not create Supabase client: Invalid API key
```

## ✅ Solution (3 Steps - Takes 2 Minutes)

### Step 1: Get Correct Key from Supabase (30 seconds)

1. **Open**: https://supabase.com/dashboard
2. **Click** your project: `kqhrkboqoxegibmbutun`
3. **Click**: ⚙️ **Settings** (left sidebar)
4. **Click**: **API** (in settings menu)
5. **Find**: "Project API keys" section
6. **Look for**: **"anon public"** key
7. **Click**: 📋 Copy icon next to it

**What it should look like:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtxaHJrYm9xb3hlZ2libWJ1dHVuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDAwMDAwMDAsImV4cCI6MjAwMDAwMDAwMH0.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Key characteristics:**
- ✅ Starts with `eyJ`
- ✅ About 200-300 characters long
- ✅ Labeled as "anon public" or "anon"

### Step 2: Update in Render (1 minute)

1. **Open**: https://dashboard.render.com
2. **Click**: Your **emotionpix** service
3. **Click**: **Environment** tab (left sidebar)
4. **Find**: `SUPABASE_KEY` variable
5. **Click** on it to edit
6. **Delete** the entire old value
7. **Paste** your new anon public key
8. **Click**: **Save Changes** button

**⚠️ Important:**
- No quotes needed
- No spaces before/after
- Paste exactly as copied

### Step 3: Wait for Redeploy (30 seconds)

- Render **automatically redeploys** after saving
- Wait 2-5 minutes
- Check **Logs** tab

**✅ Success looks like:**
```
Supabase client initialized successfully
```

**❌ Still failing?**
```
Warning: SUPABASE_KEY format doesn't match...
```

---

## 🔍 Verify Your Key Format

### ✅ CORRECT Format:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
- Starts with `eyJ`
- 200-300 characters
- From "anon public" section

### ❌ WRONG Formats:

**Wrong 1: Starts with `sb_publishable_`**
```
sb_publishable_1yGbsSNMrQkP10qSOMCaUQ_MdVoMet1
```
❌ This is NOT a Supabase key!

**Wrong 2: Too short**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
```
❌ Incomplete key (missing parts)

**Wrong 3: Too long (service_role)**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... (800+ chars)
```
❌ This is service_role key - DON'T use this!

---

## 🎯 Still Not Working?

### Check Render Logs:
1. Go to Render → Your Service → **Logs**
2. Look for the exact error message
3. The logs will show what's wrong

### Verify in Supabase:
1. Make sure you're in the **correct project**
2. The URL should match: `https://kqhrkboqoxegibmbutun.supabase.co`
3. Double-check you copied the **"anon public"** key (not service_role)

### Test Locally:
1. Update your `.env` file with the correct key
2. Run: `python app.py`
3. Check console output
4. If it works locally but not on Render → Render env vars are wrong

---

## 📞 Need Help?

- **Supabase Docs**: https://supabase.com/docs/guides/api
- **Render Docs**: https://render.com/docs/environment-variables
- **Check your key format**: Should start with `eyJ` and be 200-300 chars

---

## ✅ Final Checklist

- [ ] Got anon public key from Supabase (starts with `eyJ`)
- [ ] Updated `SUPABASE_KEY` in Render Environment tab
- [ ] Saved changes (auto-redeploys)
- [ ] Waited for redeploy (2-5 min)
- [ ] Checked logs for "Supabase client initialized successfully"
- [ ] Tested login/register on your app

Once all checked ✅, authentication will work! 🎉
