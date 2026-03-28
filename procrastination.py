import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

# ── Setup ──────────────────────────────────────────────────────────────────────
N = 15
MAX_STEPS = 80
INTERVAL = 220  # ms between frames

arr = [random.randint(3, 50) for _ in range(N)]

# ── Color palette ──────────────────────────────────────────────────────────────
BG        = "#0d0d14"
PROC_TOP  = "#ff4060"
FAKE_TOP  = "#ffd040"
PANIC_TOP = "#40ffaa"
ACTIVE    = "#a090ff"
DONE      = "#6080ff"
TEXT_DIM  = "#555566"
TEXT_MED  = "#aaaacc"
TEXT_HI   = "#e8e4ff"

MOOD_COLORS = {
    "procrastinating": PROC_TOP,
    "fake_work":       FAKE_TOP,
    "panic":           PANIC_TOP,
    "done":            DONE,
}

MOOD_LABELS = {
    "procrastinating": "Procrastinating — doing absolutely nothing",
    "fake_work":       "Fake Work — looks busy, means nothing",
    "panic":           "Panic Mode — actually sorting now!!",
    "done":            "Sorted! Crisis averted... barely",
}

# ── Figure layout ──────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(11, 6.5), facecolor=BG)
fig.patch.set_facecolor(BG)

gs = GridSpec(3, 3, figure=fig,
              height_ratios=[0.18, 3.4, 0.55],
              hspace=0.22, wspace=0.32,
              left=0.06, right=0.97, top=0.91, bottom=0.10)

ax_prog  = fig.add_subplot(gs[0, :])
ax_bars  = fig.add_subplot(gs[1, :])
ax_steps = fig.add_subplot(gs[2, 0])
ax_swaps = fig.add_subplot(gs[2, 1])
ax_phase = fig.add_subplot(gs[2, 2])

for ax in [ax_bars, ax_prog, ax_steps, ax_swaps, ax_phase]:
    ax.set_facecolor(BG)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

# ── Title block ────────────────────────────────────────────────────────────────
fig.text(0.06, 0.978, "Procrastination Sort",
         color=TEXT_HI, fontsize=17, fontweight="bold", va="top")

fig.text(0.06, 0.930, "Why do it now… when you can do it faster later?",
         color=TEXT_HI, fontsize=9.5, fontfamily="monospace", va="top")

fig.text(0.5, 0.018,
         "Time complexity: O(n… eventually)",
         color=TEXT_HI, fontsize=10, fontstyle="italic",
         ha="center", va="bottom")

mood_text = fig.text(0.97, 0.975, "Idle",
                     color=TEXT_DIM, fontsize=10, va="top", ha="right",
                     fontfamily="monospace")

# ── Progress bar ───────────────────────────────────────────────────────────────
ax_prog.set_xlim(0, MAX_STEPS)
ax_prog.set_ylim(0, 1)
ax_prog.axvspan(0,             MAX_STEPS*0.5, color=PROC_TOP,  alpha=0.18)
ax_prog.axvspan(MAX_STEPS*0.5, MAX_STEPS*0.8, color=FAKE_TOP,  alpha=0.18)
ax_prog.axvspan(MAX_STEPS*0.8, MAX_STEPS,     color=PANIC_TOP, alpha=0.18)
prog_bar, = ax_prog.fill([0,0,0,0], [0,0,1,1], color=PROC_TOP, alpha=0.8)
ax_prog.text(MAX_STEPS*0.25, 0.5, "procrastinate", color=TEXT_DIM,
             fontsize=7, ha="center", va="center", fontfamily="monospace")
ax_prog.text(MAX_STEPS*0.65, 0.5, "fake work",     color=TEXT_DIM,
             fontsize=7, ha="center", va="center", fontfamily="monospace")
ax_prog.text(MAX_STEPS*0.9,  0.5, "panic",         color=TEXT_DIM,
             fontsize=7, ha="center", va="center", fontfamily="monospace")

# ── Bars ───────────────────────────────────────────────────────────────────────
ax_bars.set_xlim(-0.5, N - 0.5)
ax_bars.set_ylim(0, 58)

bars = [
    ax_bars.bar(i, v, color=PROC_TOP, width=0.72, linewidth=0, zorder=3)[0]
    for i, v in enumerate(arr)
]

step_label = ax_bars.text(N - 0.5, 55, "step 0",
                           color=TEXT_DIM, fontsize=9, ha="right",
                           fontfamily="monospace")
mood_label = ax_bars.text(0, 55, MOOD_LABELS["procrastinating"],
                           color=PROC_TOP, fontsize=9, ha="left")

# ── Stat panels ────────────────────────────────────────────────────────────────
def stat_panel(ax, label, init="0"):
    rect = mpatches.FancyBboxPatch((0.02, 0.05), 0.96, 0.9,
                                   boxstyle="round,pad=0.02",
                                   linewidth=0.5, edgecolor="#333355",
                                   facecolor="#13131f",
                                   transform=ax.transAxes, clip_on=False)
    ax.add_patch(rect)
    ax.text(0.5, 0.72, label, color=TEXT_DIM, fontsize=8,
            ha="center", va="center", transform=ax.transAxes,
            fontfamily="monospace")
    val = ax.text(0.5, 0.28, init, color=TEXT_HI, fontsize=22,
                  fontweight="bold", ha="center", va="center",
                  transform=ax.transAxes)
    return val

val_steps = stat_panel(ax_steps, "STEPS")
val_swaps = stat_panel(ax_swaps, "SWAPS")
val_phase = stat_panel(ax_phase, "PHASE")
val_phase.set_fontsize(13)
val_phase.set_color(TEXT_MED)
val_phase.set_text("—")

# ── Generator ──────────────────────────────────────────────────────────────────
def procrastination_sort_steps(a):
    n = len(a)
    s = 0
    while s < MAX_STEPS:
        ratio = s / MAX_STEPS
        mood = ("procrastinating" if ratio < 0.5
                else "fake_work"  if ratio < 0.8
                else "panic")
        yield list(a), -1, mood, s, False
        if mood == "procrastinating":
            s += 1
            continue
        elif mood == "fake_work":
            i, j = random.randint(0, n-2), random.randint(0, n-2)
            a[i], a[j] = a[j], a[i]
            yield list(a), i, mood, s, True
        elif mood == "panic":
            for i in range(n - 1):
                for j in range(n - 1):
                    if a[j] > a[j+1]:
                        a[j], a[j+1] = a[j+1], a[j]
                        yield list(a), j, mood, s, True
        s += 1

# ── State ──────────────────────────────────────────────────────────────────────
state = {"steps": 0, "swaps": 0}

PHASE_NAMES = {
    "procrastinating": "Avoid",
    "fake_work":       "Fake",
    "panic":           "Panic",
    "done":            "Done",
}

# ── Update ─────────────────────────────────────────────────────────────────────
def update(frame):
    values, active_idx, mood, step_num, swapped = frame

    state["steps"] += 1
    if swapped:
        state["swaps"] += 1

    color = MOOD_COLORS[mood]

    for i, (bar, v) in enumerate(zip(bars, values)):
        bar.set_height(v)
        bar.set_color(ACTIVE if i == active_idx else color)
        bar.set_linewidth(0)

    prog_bar.set_xy([[0,0],[step_num+1,0],[step_num+1,1],[0,1]])
    prog_bar.set_color(color)

    mood_label.set_text(MOOD_LABELS[mood])
    mood_label.set_color(color)
    mood_text.set_text(mood.replace("_", " ").upper())
    mood_text.set_color(color)
    step_label.set_text(f"step {state['steps']}")

    val_steps.set_text(str(state["steps"]))
    val_swaps.set_text(str(state["swaps"]))
    val_phase.set_text(PHASE_NAMES.get(mood, "—"))

# ── Animate ────────────────────────────────────────────────────────────────────
gen = procrastination_sort_steps(arr)

ani = animation.FuncAnimation(
    fig,
    update,
    frames=gen,
    interval=INTERVAL,
    blit=False,
    repeat=False,
    save_count=MAX_STEPS * 10,
    cache_frame_data=False,
)

plt.show()