import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from pathlib import Path

# ----------------------------
# PAGE CONFIG & THEME TOGGLES
# ----------------------------
st.set_page_config(page_title="AR Strategy Dashboard", layout="wide")

# Simple HUD-like CSS (optional)
HUD = """
<style>
/* background */
.reportview-container .main {background-color: #0b0f17;}
.block-container {padding-top: 1rem; padding-bottom: 2rem;}
/* text */
h1, h2, h3, h4, h5, h6, p, li, span, div {color: #e6edf6;}
/* cards */
.ar-card {
  border: 1px solid #26ffe6;
  border-radius: 14px;
  padding: 16px;
  background: rgba(38,255,230,0.06);
  box-shadow: 0 0 12px rgba(38,255,230,0.15);
}
.small {font-size: 0.9rem; opacity: 0.9;}
.kpi {
  border: 1px solid #14b8a6;
  border-radius: 12px;
  padding: 14px;
  background: rgba(20,184,166,0.08);
  text-align: center;
}
.badge {
  display:inline-block;
  padding: 4px 10px;
  border: 1px solid #26ffe6;
  border-radius: 999px;
  font-size: 0.8rem; margin-bottom: 8px;
}
.caption {font-size: 0.85rem; opacity: 0.9; margin-bottom: 0.4rem;}
hr{border-top: 1px solid #1f2937;}
</style>
"""

st.markdown(HUD, unsafe_allow_html=True)

# ----------------------------
# ASSETS (optional)
# ----------------------------
ASSETS = Path("assets")
def img(path: str):
    p = ASSETS / path
    if p.exists():
        st.image(str(p), use_container_width=True)
    else:
        st.info(f"Add `{path}` to assets/ to show image.")

# ----------------------------
# SIDEBAR (Navigation & Options)
# ----------------------------
st.sidebar.title("AR Dashboard")
st.sidebar.markdown("A panel per article page (HBR, 2017)")

PANEL_TITLES = [
    "1) Cover & TL;DR",
    "2) Problem → Solution → Outcome",
    "3) What is AR? (Interface shift)",
    "4) Enhancing Human Decision-Making",
    "5) AR Capability: Visualize",
    "6) AR Capability: Instruct & Guide",
    "7) AR Capability: Interact",
    "8) AR + VR (Simulate)",
    "9) Value Creation: Product Interface",
    "10) Value Chain Impact (Pick a stage)",
    "11) C-Suite Strategy Questions",
    "12) Deploying AR (Implementation Roadmap)",
    "13) Broader Impact (Human + Machine)"
]

panel = st.sidebar.selectbox("Go to panel (page):", PANEL_TITLES, index=0)
show_all = st.sidebar.checkbox("Show all panels (scroll)", value=False)

# ----------------------------
# HELPERS: Small chart builders
# ----------------------------
def kpi_row(items):
    cols = st.columns(len(items))
    for c, (title, val, sub) in zip(cols, items):
        with c:
            st.markdown(f"<div class='kpi'><h3>{title}</h3><h2>{val}</h2><div class='small'>{sub}</div></div>", unsafe_allow_html=True)

def bar_chart(title, explanation, data, x, y, orient="h"):
    st.markdown(f"**{title}**")
    st.write(explanation)
    if orient == "h":
        fig = px.bar(data, x=x, y=y, orientation="h")
    else:
        fig = px.bar(data, x=x, y=y)
    fig.update_layout(height=380, margin=dict(l=10,r=10,t=40,b=10))
    st.plotly_chart(fig, use_container_width=True)

def line_chart(title, explanation, data, x, y, color=None):
    st.markdown(f"**{title}**")
    st.write(explanation)
    fig = px.line(data, x=x, y=y, color=color, markers=True)
    fig.update_layout(height=380, margin=dict(l=10,r=10,t=40,b=10))
    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# PANEL CONTENT
# Notes: All facts paraphrased from HBR; add source line.
# ----------------------------

def panel_1():
    st.title("Why Every Organization Needs an Augmented Reality Strategy")
    st.caption("Michael E. Porter & James E. Heppelmann, Harvard Business Review (2017):contentReference[oaicite:2]{index=2}")
    img("hud_bg.jpg")
    st.markdown("<div class='ar-card'>", unsafe_allow_html=True)
    st.subheader("TL;DR (Executive Takeaways)")
    st.markdown("""
- **AR overlays data on the real world**, closing the 2D–3D gap and lowering cognitive load.:contentReference[oaicite:3]{index=3}  
- It **boosts productivity and quality** across design, manufacturing, logistics, service, and training.:contentReference[oaicite:4]{index=4}  
- AR becomes the **human–machine interface** for smart, connected products (SCPs).:contentReference[oaicite:5]{index=5}
""")
    st.markdown("</div>", unsafe_allow_html=True)

def panel_2():
    st.header("Problem → Solution → Outcome")
    kpi_row([
        ("The Problem", "2D data vs 3D world", "High cognitive load, slower decisions:contentReference[oaicite:6]{index=6}"),
        ("The Solution", "Augmented Reality", "Contextual overlays reduce mental effort:contentReference[oaicite:7]{index=7}"),
        ("The Outcome", "Speed & Accuracy", "Faster learning, fewer errors, better safety:contentReference[oaicite:8]{index=8}")
    ])
    df = pd.DataFrame({
        "Step": ["Without AR", "With AR"],
        "Cognitive Distance (proxy)": [100, 40]
    })
    bar_chart(
        "Cognitive Distance Proxy",
        "AR places information where it’s used, which reduces 'cognitive distance' and mental effort.",
        df, x="Cognitive Distance (proxy)", y="Step"
    )

def panel_3():
    st.header("What is AR? (Interface Shift)")
    st.write("AR **transforms analytics into in-context visuals**, delivered via phones today and increasingly via hands-free smart glasses. Rising examples span consumer and industrial use-cases.:contentReference[oaicite:9]{index=9}")
    img("logo.png")
    df = pd.DataFrame({"Tech":["Mobile AR","Smart Glasses","Wearables"],"Maturity":["High","Rising","Rising"]})
    bar_chart("Delivery Modalities (qualitative maturity)",
              "Devices delivering AR experiences are shifting from handheld to hands-free, increasing usability and safety on the job.",
              df, x="Maturity", y="Tech")

def panel_4():
    st.header("Enhancing Human Decision-Making")
    st.write("Humans absorb **most information visually**. AR overlays reduce **cognitive load** by placing data exactly where action occurs—for example, **heads-up navigation** instead of glancing between road and map.:contentReference[oaicite:10]{index=10}")
    df = pd.DataFrame({"Mode":["Read manual","Watch video","AR overlay"],
                       "Relative Mental Effort":[90,70,35]})
    bar_chart("Relative mental effort across instruction modes",
              "AR minimizes translation from screen/page to real context.",
              df, x="Relative Mental Effort", y="Mode")

def panel_5():
    st.header("Capability: Visualize")
    img("ar_visualize.png")
    st.write("**Reveal the invisible**: AccuVein superimposes vein maps on skin; Bosch shows internal components with status. Result: **fewer errors and faster procedures**.:contentReference[oaicite:11]{index=11}")
    df = pd.DataFrame({"Use-case":["Vein finding (clinic)","Equipment internals"],
                       "Impact (qualitative)":["Higher first-pass success","Faster comprehension"]})
    bar_chart("Visualize: representative impacts",
              "Seeing hidden structures in context accelerates understanding and accuracy.",
              df, x="Impact (qualitative)", y="Use-case")

def panel_6():
    st.header("Capability: Instruct & Guide")
    img("ar_instruct.png")
    st.write("**Step-by-step 3D guidance** replaces 2D manuals. Boeing trainees assembling a wing section worked **35% faster** and novice first-time correctness rose **~90%**.:contentReference[oaicite:12]{index=12}")
    df = pd.DataFrame({"Metric":["Time to complete","First-time correctness"],
                       "Traditional (index)":[100,100],
                       "With AR (index)":[65,190]})
    line_chart("Training productivity & quality (index)", 
               "AR cuts time and boosts accuracy by showing each step in situ.",
               df.melt("Metric", var_name="Method", value_name="Index"),
               x="Metric", y="Index", color="Method")

def panel_7():
    st.header("Capability: Interact")
    img("ar_interact.png")
    st.write("**Virtual controls** appear directly on the product; users can point, gaze, or use voice. GE piloted **voice-driven AR** for turbine wiring and saw **~34% productivity lift**.:contentReference[oaicite:13]{index=13}")
    df = pd.DataFrame({"Control":["Physical buttons","App remote","AR virtual UI"],
                       "Usability (proxy)":[60,75,90]})
    bar_chart("Interface evolution to AR virtual controls",
              "AR collapses steps: see status, act immediately, confirm—without switching context.",
              df, x="Usability (proxy)", y="Control")

def panel_8():
    st.header("AR + VR (Simulate)")
    img("ar_vr.png")
    st.write("VR **replaces** reality to simulate hazardous/remote environments; combined with AR, teams can **practice** procedures safely (e.g., **BP**, **DHS**). Ford co-designs vehicles in a shared virtual workshop.:contentReference[oaicite:14]{index=14}")
    df = pd.DataFrame({"Dimension":["Distance","Time","Scale"],"Benefit with VR":["Co-presence","Replay/future scenarios","Engage with micro/macro"]})
    bar_chart("Where VR complements AR",
              "Simulation (VR) + in-context guidance (AR) = complete training/ops loop.",
              df, x="Benefit with VR", y="Dimension")

def panel_9():
    st.header("Value Creation: Product Interface")
    st.write("AR becomes a **software-defined user interface** on any product (e.g., ovens, cars). It’s **personalizable**, **updatable**, and can **replace physical dials**—cutting cost and enabling new UX.:contentReference[oaicite:15]{index=15}")
    df = pd.DataFrame({"Interface":["Physical dials","Embedded touchscreen","AR UI (wearables)"],
                       "Updatability (proxy)":[20,60,95]})
    bar_chart("Why AR interfaces are disruptive",
              "Software UIs evolve continuously; AR puts them on any product without adding hardware.",
              df, x="Updatability (proxy)", y="Interface")

def panel_10():
    st.header("Value Chain Impact")
    st.write("Pick a stage to see representative metrics and examples from the article.")
    stage = st.selectbox("Choose stage:", ["Product Development","Manufacturing","Logistics","Marketing & Sales","After-Sales Service","HR / Training"])

    if stage == "Product Development":
        st.write("**Volkswagen** overlays CAD on prototypes; QA becomes **5–10× faster** and more accurate.:contentReference[oaicite:16]{index=16}")
        df = pd.DataFrame({"Phase":["Design review","Fit/finish check"],"Speed index (AR vs baseline)":[500,300]})
        bar_chart("Engineering review speed index",
                  "Overlaying holograms on real prototypes makes gaps obvious.",
                  df, x="Speed index (AR vs baseline)", y="Phase")

    elif stage == "Manufacturing":
        st.write("**Newport News Shipbuilding**: inspection time cut **96%** (36h → 1.5h). AR guidance often yields **~25%+** time savings on tasks.:contentReference[oaicite:17]{index=17}")
        df = pd.DataFrame({"Task":["Inspection","Assembly"],"Time Saved (%)":[96,25]})
        bar_chart("Manufacturing time savings with AR",
                  "Big wins come from eliminating 2D-to-3D translation.",
                  df, x="Time Saved (%)", y="Task")

    elif stage == "Logistics":
        st.write("**DHL**: AR-guided picking → **+25% productivity**, fewer errors; **Intel**: **−29% picking time**, near-zero errors.:contentReference[oaicite:18]{index=18}")
        df = pd.DataFrame({"Metric":["Productivity (DHL)","+ / − Picking Time (Intel)","Error rate"],
                           "Impact":[25,-29,-90]})
        bar_chart("Warehouse picking improvements",
                  "Direction overlays and optimal routing speed up picks and reduce mistakes.",
                  df, x="Impact", y="Metric")

    elif stage == "Marketing & Sales":
        st.write("**IKEA/Wayfair/AZEK**: in-room 3D product visualization → clearer expectations, faster decisions, better satisfaction.:contentReference[oaicite:19]{index=19}")
        df = pd.DataFrame({"Outcome":["Confidence","Conversion speed","Return rate"],"Direction":["↑","↑","↓"]})
        bar_chart("Commercial outcomes with AR try-before-you-buy",
                  "Seeing size, fit, and aesthetics in context removes guesswork.",
                  df, x="Direction", y="Outcome")

    elif stage == "After-Sales Service":
        st.write("**Xerox** remote expert AR: **+67%** first-time fix, **+20%** efficiency, **−2h** per job; **Lee Company**: **$500/tech/mo** saved and ~**$20 ROI per $1**.:contentReference[oaicite:20]{index=20}")
        df = pd.DataFrame({"Metric":["First-time fix","Tech efficiency","Time per job","$ / technician / month","ROI per $1"],
                           "Impact":["+67%","+20%","−2h","$500","~$20"]})
        bar_chart("Service performance improvements",
                  "AR puts expert eyes on the problem instantly; less travel, fewer repeat visits.",
                  df, x="Impact", y="Metric")

    else:
        st.write("**DHL** uses AR for real-time onboarding and guidance, speeding seasonal ramp-ups and reducing need for trainers.:contentReference[oaicite:21]{index=21}")
        df = pd.DataFrame({"HR lever":["Onboarding speed","Trainer dependency"],"Impact":["↑","↓"]})
        bar_chart("HR impacts with AR guidance",
                  "Visual guidance reduces skill thresholds and accelerates time-to-productivity.",
                  df, x="Impact", y="HR lever")

def panel_11():
    st.header("C-Suite Strategy Questions")
    st.write("Use these as **decision tiles**. Toggle each to see prompts.")
    q1 = st.toggle("1) What AR opportunities exist in our industry, and in what sequence?")
    if q1:
        st.markdown("<div class='ar-card small'>Start with high-ROI visualizations or instructions; expand to interactive controls as hardware matures.:contentReference[oaicite:22]{index=22}</div>", unsafe_allow_html=True)
    q2 = st.toggle("2) How can AR reinforce product differentiation?")
    if q2:
        st.markdown("<div class='ar-card small'>Companion AR experiences, superior UIs, and usage telemetry to refine products.:contentReference[oaicite:23]{index=23}</div>", unsafe_allow_html=True)
    q3 = st.toggle("3) Where will AR reduce costs the most?")
    if q3:
        st.markdown("<div class='ar-card small'>Training, service, assembly, and removing physical interfaces; prioritize per strategy.:contentReference[oaicite:24]{index=24}</div>", unsafe_allow_html=True)
    q4 = st.toggle("4) Build AR in-house or partner?")
    if q4:
        st.markdown("<div class='ar-card small'>UX/UI and 3D content skills are scarce; partner early, build core strengths selectively.:contentReference[oaicite:25]{index=25}</div>", unsafe_allow_html=True)
    q5 = st.toggle("5) How will AR change stakeholder communications?")
    if q5:
        st.markdown("<div class='ar-card small'>Think beyond a new channel—AR is a new **mode** of engagement & instruction.:contentReference[oaicite:26]{index=26}</div>", unsafe_allow_html=True)

def panel_12():
    st.header("Deploying AR (Implementation Roadmap)")
    st.write("Five practical questions help you implement effectively.:contentReference[oaicite:27]{index=27}")
    items = [
        ("Dev Complexity", "Start with static visualize → move to dynamic instruction → interactive control."),
        ("3D Content", "Repurpose CAD, scan for detail, stream real-time data from SCPs/ERPs."),
        ("Environment Recognition", "Markers now; shape recognition rising—plan for it."),
        ("Hardware Path", "Phones/tablets now; **smart glasses** soon—be cross-platform ready."),
        ("Publishing Model", "Move from app-bundled to **cloud-published** AR content for scale.")
    ]
    for title, text in items:
        st.markdown(f"<div class='ar-card'><div class='badge'>{title}</div><div>{text}</div></div>", unsafe_allow_html=True)

def panel_13():
    st.header("Broader Impact (Human + Machine)")
    st.write("Humans bring dexterity, judgment, and creativity. AR is the **bridge interface** to digital knowledge and automation—**amplifying**, not replacing, people.:contentReference[oaicite:28]{index=28}")
    df = pd.DataFrame({"Capability":["Dexterity","Adaptability","Creativity","Scale & Data (Machines)"],
                       "Who excels":["Human","Human","Human","Machine"]})
    bar_chart("Complementary strengths",
              "Augmentation (not substitution) unlocks the biggest productivity gains.",
              df, x="Who excels", y="Capability")

# ----------------------------
# RENDER
# ----------------------------
PANEL_FUNCS = [
    panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7,
    panel_8, panel_9, panel_10, panel_11, panel_12, panel_13
]

if show_all:
    for f in PANEL_FUNCS:
        f()
        st.markdown("---")
else:
    idx = PANEL_TITLES.index(panel)
    PANEL_FUNCS[idx]()
