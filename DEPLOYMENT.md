# Deployment Guide - YouTube Music Backend API

This guide will help you deploy your YouTube Music Backend API to free hosting services like **Render** and **Vercel**.

---

## 🚀 Option 1: Deploy to Render (Recommended)

Render is ideal for Flask applications and offers a generous free tier with persistent services.

### Prerequisites

- GitHub account
- Git installed on your computer
- Render account (free): https://render.com

### Step 1: Prepare Your Repository

1. **Initialize Git repository** (if not already done):

   ```bash
   cd c:\Users\dhruv\Desktop\Website\ytmusic_backend
   git init
   git add .
   git commit -m "Initial commit - YouTube Music Backend API"
   ```

2. **Create a GitHub repository**:

   - Go to https://github.com/new
   - Create a new repository (e.g., `ytmusic-backend`)
   - Don't initialize with README (we already have files)

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/ytmusic-backend.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Go to Render Dashboard**:

   - Visit https://dashboard.render.com
   - Click **"New +"** → **"Web Service"**

2. **Connect Your Repository**:

   - Connect your GitHub account
   - Select your `ytmusic-backend` repository
   - Click **"Connect"**

3. **Configure the Service**:

   - **Name**: `ytmusic-backend` (or your preferred name)
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: `Free`

4. **Set Environment Variables**:
   Click **"Advanced"** and add:

   - `FLASK_ENV` = `production`
   - `CORS_ORIGINS` = `*` (or your frontend domain)
   - `PORT` = `10000` (Render default)

5. **Deploy**:
   - Click **"Create Web Service"**
   - Wait 2-5 minutes for deployment
   - Your API will be live at: `https://ytmusic-backend-XXXX.onrender.com`

### Step 3: Test Your Deployment

```bash
# Health check
curl https://your-app-name.onrender.com/api/health

# Search test
curl "https://your-app-name.onrender.com/api/search?query=test&filter=songs&limit=5"
```

### ⚠️ Render Free Tier Notes

- Service spins down after 15 minutes of inactivity
- First request after inactivity may take 30-60 seconds (cold start)
- 750 hours/month free (enough for one service 24/7)

---

## 🌐 Option 2: Deploy to Vercel

Vercel is great for serverless deployments but has some limitations with Flask.

### Prerequisites

- Vercel account (free): https://vercel.com
- Vercel CLI (optional but recommended)

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Prepare for Deployment

The `vercel.json` file is already created in your project.

### Step 3: Deploy

1. **Login to Vercel**:

   ```bash
   cd c:\Users\dhruv\Desktop\Website\ytmusic_backend
   vercel login
   ```

2. **Deploy**:

   ```bash
   vercel
   ```

   Follow the prompts:

   - Set up and deploy? **Y**
   - Which scope? Select your account
   - Link to existing project? **N**
   - What's your project's name? `ytmusic-backend`
   - In which directory is your code located? `./`
   - Want to override settings? **N**

3. **Production Deployment**:
   ```bash
   vercel --prod
   ```

### Step 4: Configure Environment Variables

1. Go to your Vercel dashboard: https://vercel.com/dashboard
2. Select your project
3. Go to **Settings** → **Environment Variables**
4. Add:

   - `FLASK_ENV` = `production`
   - `CORS_ORIGINS` = `*`

5. Redeploy:
   ```bash
   vercel --prod
   ```

### ⚠️ Vercel Limitations

- **Serverless functions have 10-second timeout** on free tier
- Some ytmusicapi requests may timeout
- Better for lightweight APIs
- **Recommendation**: Use Render for this project

---

## 🔧 Alternative: Railway

Railway is another excellent option with a generous free tier.

### Quick Deploy to Railway

1. **Visit**: https://railway.app
2. **Click**: "Start a New Project"
3. **Select**: "Deploy from GitHub repo"
4. **Connect**: Your GitHub repository
5. **Configure**:
   - Add environment variables (same as Render)
   - Railway auto-detects Python and uses Procfile
6. **Deploy**: Automatic deployment starts

**Your API**: `https://your-app.railway.app`

---

## 📋 Post-Deployment Checklist

### ✅ Security (Important for Production)

1. **Update CORS Origins**:

   ```bash
   # In your hosting platform's environment variables
   CORS_ORIGINS=https://your-frontend-domain.com
   ```

2. **Add API Key Authentication** (Optional):

   - Implement API key middleware
   - Protect endpoints from abuse

3. **Rate Limiting**:
   - Consider adding Flask-Limiter for rate limiting

### ✅ Testing

Test all endpoints after deployment:

```bash
# Replace YOUR_DOMAIN with your actual domain

# Health check
curl https://YOUR_DOMAIN/api/health

# Search
curl "https://YOUR_DOMAIN/api/search?query=imagine%20dragons&filter=songs"

# Song details
curl "https://YOUR_DOMAIN/api/song/VIDEO_ID"

# Charts
curl "https://YOUR_DOMAIN/api/charts/US"
```

### ✅ Monitoring

1. **Render**: Built-in logs and metrics in dashboard
2. **Vercel**: Function logs in dashboard
3. **Railway**: Real-time logs in project view

---

## 🐛 Troubleshooting

### Issue: "Application Error" or 500 Error

**Solution**:

- Check deployment logs in your hosting dashboard
- Verify all dependencies are in `requirements.txt`
- Ensure `gunicorn` is installed
- Check environment variables are set correctly

### Issue: CORS Errors

**Solution**:

```python
# In app.py, update CORS configuration
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://your-frontend.com"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})
```

### Issue: Timeout Errors (Vercel)

**Solution**:

- Switch to Render or Railway (better for long-running requests)
- Vercel's 10-second limit is too short for some ytmusicapi calls

### Issue: Cold Start Delays (Render Free Tier)

**Solution**:

- Use a service like UptimeRobot to ping your API every 14 minutes
- Upgrade to paid tier for always-on service
- Accept the delay (normal for free tier)

---

## 🔄 Continuous Deployment

Once set up, your app auto-deploys on every git push:

```bash
# Make changes to your code
git add .
git commit -m "Update: added new feature"
git push origin main

# Render/Vercel/Railway automatically deploys the changes
```

---

## 📊 Comparison Table

| Feature            | Render        | Vercel         | Railway         |
| ------------------ | ------------- | -------------- | --------------- |
| **Free Tier**      | 750 hrs/month | Unlimited      | 500 hrs/month   |
| **Cold Starts**    | Yes (~30s)    | Minimal        | Yes (~10s)      |
| **Timeout**        | 30 seconds    | 10 seconds     | 30 seconds      |
| **Best For**       | Flask APIs    | Next.js/Static | Full-stack apps |
| **Recommendation** | ⭐⭐⭐⭐⭐    | ⭐⭐⭐         | ⭐⭐⭐⭐        |

---

## 🎯 Recommended Choice

**For this YouTube Music Backend API, use Render:**

- ✅ Best compatibility with Flask
- ✅ No timeout issues
- ✅ Easy setup
- ✅ Free tier is sufficient
- ✅ Built-in SSL certificates
- ✅ Custom domains supported

---

## 📝 Example Frontend Integration

Once deployed, update your frontend code:

```javascript
// Replace localhost with your deployed URL
const API_BASE_URL = "https://your-app.onrender.com";

async function searchSongs(query) {
  const response = await fetch(
    `${API_BASE_URL}/api/search?query=${encodeURIComponent(query)}&filter=songs`
  );
  return await response.json();
}
```

---

## 🆘 Need Help?

- **Render Docs**: https://render.com/docs
- **Vercel Docs**: https://vercel.com/docs
- **Railway Docs**: https://docs.railway.app

Your YouTube Music Backend API is now ready for production! 🎉
