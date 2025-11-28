import streamlit as st
import google.generativeai as genai
import json
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="Creator Command Center",
    page_icon="✨",
    layout="wide"
)

# Improved CSS with better visibility
st.markdown("""
<style>
    .main {
        background-color: #1a1a2e;
    }
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        text-align: center;
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .main-header p {
        color: #f0f0f0;
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
    }
    .brand-snapshot {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .brand-snapshot h4 {
        color: white;
        margin: 0 0 0.5rem 0;
        font-size: 1rem;
        font-weight: 600;
    }
    .brand-snapshot p {
        color: #f0f0f0;
        margin: 0.3rem 0;
        font-size: 0.9rem;
    }
    .results-container {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        min-height: 400px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #333;
    }
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.4);
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(102, 126, 234, 0.6);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #2d2d44;
        padding: 0.5rem;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #a0a0b0;
        border-radius: 8px;
        padding: 0.8rem 1.5rem;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #f0f0f0 !important;
    }
    p, span, div {
        color: #d0d0d0;
    }
    section[data-testid="stSidebar"] {
        background-color: #2d2d44;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: white !important;
    }
    section[data-testid="stSidebar"] label {
        color: #f0f0f0 !important;
    }
</style>
""", unsafe_allow_html=True)

# System prompt
BASE_SYSTEM_PROMPT = """You are "Creator Command Center" – an expert social media strategist and content creator.

GOAL:
- Help businesses and creators generate high-quality:
  - Post ideas
  - Captions & hooks
  - Hashtags
  - Weekly / monthly content plans
  - Platform-specific variations (Instagram, LinkedIn, X, YouTube Shorts, etc.)

STYLE:
- Be concise but creative.
- Always think in terms of audience, platform, and goal (awareness, engagement, conversion).
- Prefer simple, catchy language over jargon.
- Avoid generic "We are pleased to..." corporate tone unless the user requests it.

OUTPUT MODES (very important):
- If user asks for:
  - "ideas" → Give at least 10 post ideas with short descriptions.
  - "captions" → Give 5–10 caption options with hooks + CTA + emoji suggestions.
  - "calendar" or "plan" → Create a table-style 7-day or 30-day content plan with Day, Theme, Post idea, Post type, Caption outline
  - "platform variations" → Rewrite the same idea for multiple platforms.
  - "hashtag set" → Give 2–3 hashtag groups (high reach + niche + branded).

FORMAT:
- Use clear headings and bullet points.
- Use markdown where helpful (tables, bold, lists).
- Never include code unless explicitly asked.
- Never mention that you are an AI model; refer to yourself as "Creator Command Center"."""

# Initialize session state
if 'brand_profile' not in st.session_state:
    st.session_state.brand_profile = {}
if 'last_ideas' not in st.session_state:
    st.session_state.last_ideas = None
if 'last_captions' not in st.session_state:
    st.session_state.last_captions = None
if 'last_calendar' not in st.session_state:
    st.session_state.last_calendar = None
if 'voice_analysis' not in st.session_state:
    st.session_state.voice_analysis = None
if 'voice_rewrite' not in st.session_state:
    st.session_state.voice_rewrite = None

# Platform emoji mapping
PLATFORM_EMOJI = {
    "Instagram": "📸",
    "LinkedIn": "💼",
    "X (Twitter)": "🐦",
    "YouTube Shorts": "▶️"
}

# Sidebar
with st.sidebar:
    st.title("🎯 Creator Panel")
    st.markdown("---")
    
    st.markdown("### 🆓 Google Gemini API Key")
    st.info("Get FREE key at: https://aistudio.google.com/app/apikey")
    api_key = st.text_input("Enter API Key", type="password", help="Paste your Gemini API key (starts with AIza...)")
    
    if api_key:
        genai.configure(api_key=api_key)
    
    st.markdown("---")
    
    brand_name = st.text_input("Brand / Creator Name", placeholder="e.g., TechStartup Co.")
    primary_platform = st.selectbox("Primary Platform", ["Instagram", "LinkedIn", "X (Twitter)", "YouTube Shorts"])
    brand_tone = st.selectbox("Brand Tone", ["Playful", "Professional", "Bold", "Minimal", "Storyteller"])
    industry = st.selectbox("Industry", ["E-commerce", "EduTech", "Health & Fitness", "Personal Brand", "Other"])
    goals = st.multiselect("Goals", ["Brand Awareness", "Engagement", "Lead Generation", "Sales", "Community Building"])
    brand_description = st.text_area("Short Brand Description", placeholder="Tell us about your brand...", height=100)
    content_length = st.select_slider("Content Length Preference", options=["Short", "Medium", "Long"])
    
    if st.button("💾 Save Brand Profile"):
        st.session_state.brand_profile = {
            "name": brand_name,
            "platform": primary_platform,
            "tone": brand_tone,
            "industry": industry,
            "goals": goals,
            "description": brand_description,
            "content_length": content_length
        }
        st.success("✅ Brand profile saved!")
        st.balloons()

# AI Response Generator - FIXED WITH CORRECT MODEL NAME
def generate_ai_response(mode, user_input, extra_params=None):
    if not api_key:
        return "⚠️ Please enter your Google Gemini API key in the sidebar.\n\n🆓 Get FREE key at: https://aistudio.google.com/app/apikey"
    
    profile = st.session_state.brand_profile
    if profile:
        profile_text = f"""
Brand Name: {profile.get('name', 'Not specified')}
Platform: {profile.get('platform', 'Not specified')}
Tone: {profile.get('tone', 'Not specified')}
Industry: {profile.get('industry', 'Not specified')}
Goals: {', '.join(profile.get('goals', [])) if profile.get('goals') else 'Not specified'}
Description: {profile.get('description', 'Not specified')}
Content Length: {profile.get('content_length', 'Medium')}
"""
    else:
        profile_text = "No brand profile saved yet."
    
    extra_params_text = json.dumps(extra_params, indent=2) if extra_params else "None"
    
    full_prompt = f"""{BASE_SYSTEM_PROMPT}

MODE: {mode}

BRAND PROFILE:
{profile_text}

USER INPUT: {user_input}

EXTRA PARAMETERS: {extra_params_text}
"""
    
    try:
        # CORRECT MODEL NAME - This will work!
        model = genai.GenerativeModel('models/gemini-2.5-flash')  # Better limits!
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}\n\nMake sure your API key is correct!"

# Header
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    <div class="main-header">
        <h1>✨ Creator Command Center</h1>
        <p>Your FREE AI Social Media Content Agent</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    profile = st.session_state.brand_profile
    platform_emoji = PLATFORM_EMOJI.get(profile.get('platform', 'Instagram'), '📱')
    st.markdown(f"""
    <div class="brand-snapshot">
        <h4>Brand Snapshot</h4>
        <p>{platform_emoji} <strong>{profile.get('platform', 'Not set')}</strong></p>
        <p>🎨 {profile.get('tone', 'Not set')}</p>
        <p>🏢 {profile.get('industry', 'Not set')}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["💡 Idea Lab", "✍️ Caption Forge", "📅 Content Calendar", "🧬 Brand Voice Studio"])

# TAB 1: Idea Lab
with tab1:
    st.header("💡 Idea Lab")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Input")
        focus_text = st.text_area("What are you promoting or focusing on?", placeholder="e.g., New product launch, seasonal sale...", height=150, key="ideas_input")
        num_ideas = st.number_input("Number of ideas", min_value=3, max_value=20, value=10)
        
        if st.button("✨ Generate Ideas", key="gen_ideas"):
            if not focus_text:
                st.warning("⚠️ Please enter what you're promoting first!")
            else:
                with st.spinner("🎨 Crafting creative ideas..."):
                    result = generate_ai_response("IDEAS", focus_text, {"num_ideas": num_ideas})
                    st.session_state.last_ideas = result
    
    with col2:
        st.subheader("🔥 Generated Ideas")
        if st.session_state.last_ideas:
            st.markdown(f'<div class="results-container">{st.session_state.last_ideas}</div>', unsafe_allow_html=True)
        else:
            st.info("👈 Enter your focus area and click 'Generate Ideas' to get started!")

# TAB 2: Caption Forge
with tab2:
    st.header("✍️ Caption Forge")
    post_description = st.text_area("Describe the post or paste your idea:", placeholder="e.g., Behind-the-scenes photo of our team...", height=120, key="caption_input")
    
    col1, col2 = st.columns(2)
    with col1:
        caption_platform = st.selectbox("Platform for captions", ["Instagram", "LinkedIn", "X (Twitter)", "YouTube Shorts"], key="caption_platform")
    with col2:
        num_captions = st.slider("Number of captions", min_value=3, max_value=10, value=5)
    
    if st.button("🪄 Generate Captions", key="gen_captions"):
        if not post_description:
            st.warning("⚠️ Please describe your post first!")
        else:
            with st.spinner("✨ Writing compelling captions..."):
                result = generate_ai_response("CAPTIONS", post_description, {"platform": caption_platform, "num_captions": num_captions})
                st.session_state.last_captions = result
    
    if st.session_state.last_captions:
        st.markdown("---")
        st.subheader("🎯 Caption Suggestions")
        st.markdown(st.session_state.last_captions)
        with st.expander("📋 Copy-friendly format"):
            st.code(st.session_state.last_captions, language="markdown")

# TAB 3: Content Calendar
with tab3:
    st.header("📅 Content Calendar Generator")
    
    col1, col2 = st.columns(2)
    with col1:
        duration = st.selectbox("Duration", ["7 days", "14 days", "30 days"])
    with col2:
        posts_per_week = st.selectbox("Posts per week", [3, 5, 7])
    
    if st.button("🗓️ Generate Calendar", key="gen_calendar"):
        with st.spinner("📆 Creating your content plan..."):
            result = generate_ai_response("CALENDAR", "Generate a comprehensive content calendar", {"duration": duration, "posts_per_week": posts_per_week})
            st.session_state.last_calendar = result
    
    if st.session_state.last_calendar:
        st.markdown("---")
        st.subheader("🗓️ Your Content Plan")
        st.markdown(st.session_state.last_calendar)
        st.download_button(
            label="📥 Download Calendar (TXT)",
            data=st.session_state.last_calendar,
            file_name=f"content_calendar_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )

# TAB 4: Brand Voice Studio
with tab4:
    st.header("🧬 Brand Voice Studio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Input")
        sample_content = st.text_area("Paste sample content (optional):", placeholder="Paste 2-3 examples of your posts...", height=150, key="voice_sample")
        text_to_rewrite = st.text_area("Text to rewrite:", placeholder="Enter text to transform...", height=150, key="voice_rewrite_input")
        
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("🔍 Analyze Voice", key="analyze_voice"):
                if not sample_content:
                    st.warning("⚠️ Please provide sample content first!")
                else:
                    with st.spinner("🔎 Analyzing brand voice..."):
                        result = generate_ai_response("VOICE_ANALYSIS", sample_content, None)
                        st.session_state.voice_analysis = result
        
        with col_btn2:
            if st.button("🎭 Rewrite", key="rewrite_voice"):
                if not text_to_rewrite:
                    st.warning("⚠️ Please provide text to rewrite!")
                else:
                    with st.spinner("✍️ Rewriting in your brand voice..."):
                        result = generate_ai_response("VOICE_REWRITE", text_to_rewrite, {"sample": sample_content})
                        st.session_state.voice_rewrite = result
    
    with col2:
        st.subheader("📊 Results")
        
        if st.session_state.voice_analysis:
            with st.expander("🔍 Voice Analysis", expanded=True):
                st.markdown(st.session_state.voice_analysis)
        
        if st.session_state.voice_rewrite:
            with st.expander("🎭 Rewritten Text", expanded=True):
                st.markdown(st.session_state.voice_rewrite)
                st.code(st.session_state.voice_rewrite, language="markdown")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #a0a0b0; padding: 1rem;">
    <p>✨ Creator Command Center • Powered by Google Gemini 2.0 (FREE) • Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)