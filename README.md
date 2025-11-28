# AI-Powered-Social-Media-Content-Agent
# ✨ Creator Command Center

**An AI-Powered Social Media Content Agent built with Streamlit**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> Your AI assistant for generating social media post ideas, captions, content calendars, and maintaining brand voice consistency.

---

## 🌟 Features

### 💡 **Idea Lab**
- Generate 3-20 creative post ideas for any campaign
- Platform-specific content suggestions
- Format recommendations (Reels, Carousels, Stories, Tweets)
- Tailored to your brand voice and goals

### ✍️ **Caption Forge**
- Create 3-10 engaging caption variations
- Hook + Body + CTA structure
- Platform optimization (Instagram, LinkedIn, X, YouTube)
- Built-in emoji and hashtag suggestions

### 📅 **Content Calendar**
- Build 7, 14, or 30-day content plans
- Customizable posting frequency (3, 5, or 7 posts/week)
- Structured themes and content types
- Downloadable calendar (TXT format)

### 🧬 **Brand Voice Studio**
- Analyze existing content to identify brand voice
- Rewrite content to match your brand tone
- Maintain consistency across all platforms
- Voice characteristic breakdown

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (FREE) or Groq API key (FREE)
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/vinu3783/creator-command-center.git
cd creator-command-center
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Get FREE API Key**

Choose one:
- **Google Gemini:** https://aistudio.google.com/app/apikey
- **Groq (Recommended):** https://console.groq.com/keys

5. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📦 Dependencies
```
streamlit==1.28.0
google-generativeai  # For Google Gemini
groq                 # For Groq (Alternative)
python-dotenv==1.0.0
```

---

## 🎯 Usage

### 1. Configure Your Brand Profile

In the sidebar:
- Enter your API key
- Fill in brand details (name, platform, tone, industry)
- Add brand description and goals
- Save your profile

### 2. Generate Content

Navigate through the tabs:

**💡 Idea Lab**
```
Input: "Launching new Python course with AI assistant"
Output: 10 creative post ideas with formats
```

**✍️ Caption Forge**
```
Input: Describe your post
Output: 5-10 platform-optimized captions
```

**📅 Content Calendar**
```
Input: Duration + frequency
Output: Structured 7-30 day content plan
```

**🧬 Brand Voice Studio**
```
Input: Sample content + text to rewrite
Output: Voice analysis + rewritten content
```

---

## 🏗️ Project Structure
```
creator_command_center/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── .env.example           # Environment variables template
└── screenshots/           # App screenshots
    ├── dashboard.png
    ├── idea-lab.png
    ├── caption-forge.png
    └── calendar.png
```

---

## ⚙️ Configuration

### Using Environment Variables (Optional)

Create a `.env` file:
```env
GEMINI_API_KEY=your_key_here
# or
GROQ_API_KEY=your_key_here
```

### Model Selection

Current model: `gemini-2.5-flash` (FREE)

Available alternatives:
- `gemini-2.0-flash`
- `llama-3.3-70b-versatile` (Groq)

---

## 🎨 Features Overview

| Feature | Description | Input | Output |
|---------|-------------|-------|--------|
| **Idea Lab** | Post idea generation | Campaign focus | 10-20 ideas |
| **Caption Forge** | Caption writing | Post description | 5-10 captions |
| **Content Calendar** | Content planning | Duration + frequency | 7-30 day plan |
| **Brand Voice** | Voice analysis | Sample content | Voice profile |

---

## 💰 Cost & Limits

### Google Gemini (FREE)
- ✅ 15 requests/minute
- ✅ 1,500 requests/day
- ✅ No credit card required

### Groq (FREE - Recommended)
- ✅ 30 requests/minute
- ✅ Higher daily limits
- ✅ Faster response times

**Estimated cost per generation:** $0.00 (FREE)

---

## 🐛 Troubleshooting

### App won't start
```bash
pip install --upgrade -r requirements.txt
streamlit run app.py
```

### Rate limit error (429)
- Wait 1 minute between requests
- Switch to Groq API (higher limits)
- Or upgrade to paid tier

### API key error
- Verify key starts with `AIza...` (Gemini) or `gsk_...` (Groq)
- Check key at: https://aistudio.google.com/app/apikey
- Ensure key has proper permissions

### Blank interface
- Clear browser cache
- Try incognito/private mode
- Check terminal for errors

---

## 📚 Documentation

### Example Inputs

**Brand Profile:**
```
Name: TechFlow Solutions
Platform: Instagram
Tone: Professional
Industry: EduTech
Goals: Brand Awareness, Engagement
Description: We help students learn coding through AI-powered tutorials
```

**Idea Lab Input:**
```
Launching new Python course with 50 hands-on projects, 
live mentorship, and job guarantee. Early bird 40% off.
```

**Expected Output:**
- 10 creative post ideas
- Mix of Reels, Carousels, Stories
- Platform-specific formats

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎓 Academic Context

**Project Type:** AI Agent Development Internship Assignment  
**Technology Stack:** Python, Streamlit, Google Gemini API  
**Focus Areas:**
- AI prompt engineering
- Multi-tool agent architecture
- Modern UI/UX design
- Session state management
- API integration

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini](https://ai.google.dev/) or [Groq](https://groq.com/)
- Icons from Unicode Emoji
- Inspired by social media marketing challenges

---

## 📞 Support

For issues and questions:
- 📧 Email: vinayakagc210@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/vinu3783/AI-Powered-Social-Media-Content-Agent/issues)

---

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Image generation integration
- [ ] Analytics dashboard
- [ ] Direct social media posting
- [ ] A/B testing features
- [ ] Team collaboration tools
- [ ] Content performance tracking

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/creator-command-center?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/creator-command-center?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/creator-command-center?style=social)

---

## 🌐 Demo

**Live Demo:** [Coming Soon]



---

## 📈 Roadmap

### Version 1.0 (Current)
- ✅ Basic content generation
- ✅ Brand profile management
- ✅ Four core tools
- ✅ Modern UI

### Version 1.1 (Planned)
- [ ] Save/load sessions
- [ ] Export to multiple formats
- [ ] Template library
- [ ] Performance analytics

### Version 2.0 (Future)
- [ ] AI image generation
- [ ] Video script generator
- [ ] Multi-platform scheduling
- [ ] Team workspace

---

<div align="center">

**Made with ❤️ for content creators and marketers**

⭐ Star this repo if you find it helpful!

[Report Bug](https://github.com/vinu3783/AI-Powered-Social-Media-Content-Agent/issues) · [Request Feature](https://github.com/vinu3783/AI-Powered-Social-Media-Content-Agent/issues)

</div>

---

## 📄 Citation

If you use this project in your research or work, please cite:
```bibtex
@software{creator_command_center,
  author = {Your Name},
  title = {Creator Command Center: AI-Powered Social Media Content Agent},
  year = {2024},
  url = {https://github.com/yourusername/creator-command-center}
}
```

---

**Last Updated:** November 2024  
**Version:** 1.0.0  
**Status:** Active Development
```

---

## 📝 **Additional Files to Create:**

### **1. LICENSE (MIT License)**

Create `LICENSE` file:
```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
