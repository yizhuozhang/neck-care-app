# 🦒 颈椎呵护助手 - 手机版使用说明

## 📱 在手机上使用

### 方法 1：直接访问（推荐）

1. **启动本地服务器**（在电脑上）：
   ```bash
   cd /Users/ian/openclaw/workspace/demo/neck-care-app
   python3 -m http.server 8080
   ```

2. **确保手机和电脑在同一 WiFi 网络**

3. **查找电脑的 IP 地址**：
   ```bash
   # Mac/Linux
   ifconfig | grep "inet "
   
   # 或在终端直接运行
   ipconfig getifaddr en0
   ```

4. **在手機瀏覽器訪問**：
   ```
   http://[电脑 IP 地址]:8080
   ```
   例如：`http://192.168.1.100:8080`

### 方法 2：部署到网络

将文件上传到任何静态网页托管服务：
- GitHub Pages
- Vercel
- Netlify
- 或任何支持 HTTPS 的服务器

---

## 📲 添加到手机主屏幕

### iPhone (Safari)
1. 用 Safari 打开网页
2. 点击底部 **分享** 按钮
3. 选择 **"添加到主屏幕"**
4. 输入名称，点击 **添加**

### Android (Chrome)
1. 用 Chrome 打开网页
2. 点击右上角 **⋮** 菜单
3. 选择 **"添加到主屏幕"**
4. 确认添加

---

## 🎯 使用提示

1. **首次使用**需允许浏览器访问摄像头
2. 将手机放在电脑屏幕旁，确保面部清晰可见
3. 当出现警告时，请起身活动颈椎
4. 建议每 30-45 分钟休息 5 分钟

---

## ⚠️ 注意事项

- 需要 HTTPS 环境才能使用摄像头（本地测试除外）
- 确保手机摄像头没有被其他应用占用
- 在光线充足的环境下使用效果更佳

---

## 🆘 常见问题

**Q: 摄像头无法启动？**
A: 检查浏览器权限设置，确保允许访问摄像头

**Q: 检测不到人脸？**
A: 调整手机角度，确保面部完整出现在画面中

**Q: 提醒太频繁/不频繁？**
A: 可在代码中调整 `staticWarningTime` 参数（默认 5 分钟）

---

## 🚀 Gunicorn/uWSGI 部署结构

项目已改为 WSGI 结构，新增文件：

- `app/__init__.py`：Flask 应用工厂
- `wsgi.py`：WSGI 入口（`app`）
- `gunicorn.conf.py`：Gunicorn 配置
- `uwsgi.ini`：uWSGI 配置
- `requirements.txt`：依赖

### 1) 安装依赖

```bash
cd /Users/izha13/Downloads/neck-care-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Gunicorn 启动

```bash
gunicorn -c gunicorn.conf.py wsgi:app
```

默认监听：`0.0.0.0:8000`

### 3) uWSGI 启动

```bash
uwsgi --ini uwsgi.ini
```

默认监听：`0.0.0.0:8000`

### 4) 路由说明

- `/` → `index.html`
- `/pacman` → `pacman.html`
- `/pacman-test` → `pacman-test.html`
- 其余静态资源（如 `pc.js`、`model/`）保持原路径可访问
