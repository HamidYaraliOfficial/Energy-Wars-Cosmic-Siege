import sys
import math
import random
import time
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QSlider, QComboBox, QStackedWidget,
    QFrame, QGridLayout, QProgressBar, QDialog, QScrollArea,
    QSizePolicy,QMessageBox , QSpacerItem, QGraphicsDropShadowEffect
)
from PyQt6.QtCore import (
    Qt, QTimer, QPointF, QRectF, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QObject, QThread, QSize, pyqtProperty
)
from PyQt6.QtGui import (
    QPainter, QColor, QPen, QBrush, QFont, QFontMetrics,
    QLinearGradient, QRadialGradient, QPainterPath, QPixmap,
    QTransform, QPalette, QIcon, QPolygonF
)

# ─────────────────────────────────────────────
#  TRANSLATIONS
# ─────────────────────────────────────────────
TRANSLATIONS = {
    "en": {
        "title": "COSMIC SIEGE",
        "subtitle": "Energy Wars",
        "play": "PLAY",
        "settings": "SETTINGS",
        "quit": "QUIT",
        "back": "BACK",
        "language": "Language",
        "theme": "Theme",
        "light": "Light",
        "dark": "Dark",
        "volume": "Volume",
        "select_faction": "Select Faction",
        "soltaris": "Soltaris Union",
        "zenars": "Zenars Empire",
        "novarak": "Novarak Confederation",
        "ventari": "Ventari Domain",
        "select_missile": "Select Missile",
        "power": "Power",
        "angle": "Angle",
        "fire": "FIRE",
        "wind": "Wind",
        "gravity": "Gravity",
        "score": "Score",
        "level": "Level",
        "energy": "Energy",
        "credits": "Credits",
        "upgrade": "UPGRADE",
        "mission": "MISSION",
        "survival": "SURVIVAL",
        "sandbox": "SANDBOX",
        "game_over": "GAME OVER",
        "victory": "VICTORY!",
        "next_level": "NEXT LEVEL",
        "retry": "RETRY",
        "main_menu": "MAIN MENU",
        "pause": "PAUSE",
        "resume": "RESUME",
        "ammo": "Ammo",
        "targets": "Targets",
        "destroyed": "Destroyed",
        "wave": "Wave",
        "shop": "SHOP",
        "buy": "BUY",
        "owned": "OWNED",
        "platform_level": "Platform Lv",
        "missiles_light": "Light Missiles",
        "missiles_medium": "Medium Missiles",
        "missiles_heavy": "Heavy Missiles",
        "missiles_special": "Special Missiles",
        "missiles_smart": "Smart Missiles",
        "swift1": "Swift-1",
        "micropulse": "MicroPulse",
        "featherspark": "Feather Spark",
        "plasmaarc": "PlasmaArc M2",
        "ionjavelin": "Ion Javelin",
        "wavedart": "WaveDart",
        "titanumx": "Titanum-X",
        "hypercore": "HyperCore Crusher",
        "noxium": "Noxium Hammer",
        "starburst": "StarBurst Omega",
        "riftbreaker": "RiftBreaker",
        "tempest": "Tempest Cycler",
        "autoseeker": "AutoSeeker V9",
        "quantum": "Quantum Tracker",
        "dualphase": "DualPhase Splitter",
        "ion_storm": "Ion Storm",
        "magnetic": "Magnetic Field",
        "tutorial": "HOW TO PLAY",
        "tut1": "Drag to aim your missile",
        "tut2": "Adjust power with the slider",
        "tut3": "Destroy all enemy bases to win",
        "tut4": "Watch out for wind and gravity!",
    },
    "fa": {
        "title": "محاصره کیهانی",
        "subtitle": "جنگ‌های انرژی",
        "play": "بازی",
        "settings": "تنظیمات",
        "quit": "خروج",
        "back": "بازگشت",
        "language": "زبان",
        "theme": "تم",
        "light": "روشن",
        "dark": "تاریک",
        "volume": "صدا",
        "select_faction": "انتخاب ائتلاف",
        "soltaris": "اتحاد سولتاریس",
        "zenars": "امپراتوری زن‌ارس",
        "novarak": "کنفدراسیون نوراک",
        "ventari": "حوزه ونتاری",
        "select_missile": "انتخاب موشک",
        "power": "قدرت",
        "angle": "زاویه",
        "fire": "شلیک",
        "wind": "باد",
        "gravity": "گرانش",
        "score": "امتیاز",
        "level": "سطح",
        "energy": "انرژی",
        "credits": "اعتبار",
        "upgrade": "ارتقا",
        "mission": "مأموریت",
        "survival": "بقا",
        "sandbox": "آزمایش",
        "game_over": "بازی تمام شد",
        "victory": "پیروزی!",
        "next_level": "مرحله بعد",
        "retry": "تلاش مجدد",
        "main_menu": "منوی اصلی",
        "pause": "توقف",
        "resume": "ادامه",
        "ammo": "مهمات",
        "targets": "اهداف",
        "destroyed": "منهدم",
        "wave": "موج",
        "shop": "فروشگاه",
        "buy": "خرید",
        "owned": "دارید",
        "platform_level": "سطح سکو",
        "missiles_light": "موشک‌های سبک",
        "missiles_medium": "موشک‌های میان‌برد",
        "missiles_heavy": "موشک‌های سنگین",
        "missiles_special": "موشک‌های ویژه",
        "missiles_smart": "موشک‌های هوشمند",
        "swift1": "سوئیفت-۱",
        "micropulse": "میکروپالس",
        "featherspark": "جرقه پر",
        "plasmaarc": "پلاسما-آرک M2",
        "ionjavelin": "نیزه یونی",
        "wavedart": "دارت موجی",
        "titanumx": "تیتانیوم-X",
        "hypercore": "هایپرکور کراشر",
        "noxium": "چکش نوکسیوم",
        "starburst": "انفجار ستاره اومگا",
        "riftbreaker": "شکافنده ریفت",
        "tempest": "چرخه طوفان",
        "autoseeker": "جستجوگر خودکار V9",
        "quantum": "ردیاب کوانتومی",
        "dualphase": "تقسیم‌کننده دوفازی",
        "ion_storm": "طوفان یونی",
        "magnetic": "میدان مغناطیسی",
        "tutorial": "آموزش بازی",
        "tut1": "برای نشانه‌گیری بکشید",
        "tut2": "قدرت را با اسلایدر تنظیم کنید",
        "tut3": "همه پایگاه‌های دشمن را نابود کنید",
        "tut4": "مراقب باد و گرانش باشید!",
    },
    "zh": {
        "title": "宇宙围攻",
        "subtitle": "能量战争",
        "play": "开始游戏",
        "settings": "设置",
        "quit": "退出",
        "back": "返回",
        "language": "语言",
        "theme": "主题",
        "light": "明亮",
        "dark": "暗黑",
        "volume": "音量",
        "select_faction": "选择阵营",
        "soltaris": "索尔塔里斯联盟",
        "zenars": "泽纳斯帝国",
        "novarak": "诺瓦拉克联邦",
        "ventari": "文塔里领域",
        "select_missile": "选择导弹",
        "power": "威力",
        "angle": "角度",
        "fire": "发射",
        "wind": "风力",
        "gravity": "重力",
        "score": "分数",
        "level": "关卡",
        "energy": "能量",
        "credits": "积分",
        "upgrade": "升级",
        "mission": "任务",
        "survival": "生存",
        "sandbox": "沙盒",
        "game_over": "游戏结束",
        "victory": "胜利！",
        "next_level": "下一关",
        "retry": "重试",
        "main_menu": "主菜单",
        "pause": "暂停",
        "resume": "继续",
        "ammo": "弹药",
        "targets": "目标",
        "destroyed": "已摧毁",
        "wave": "波次",
        "shop": "商店",
        "buy": "购买",
        "owned": "已拥有",
        "platform_level": "平台等级",
        "missiles_light": "轻型导弹",
        "missiles_medium": "中程导弹",
        "missiles_heavy": "重型导弹",
        "missiles_special": "特殊导弹",
        "missiles_smart": "智能导弹",
        "swift1": "迅捷-1",
        "micropulse": "微脉冲",
        "featherspark": "羽毛火花",
        "plasmaarc": "等离子弧M2",
        "ionjavelin": "离子标枪",
        "wavedart": "波浪飞镖",
        "titanumx": "钛金-X",
        "hypercore": "超核粉碎者",
        "noxium": "诺克锤",
        "starburst": "星爆欧米伽",
        "riftbreaker": "裂缝破碎者",
        "tempest": "风暴循环者",
        "autoseeker": "自动追踪V9",
        "quantum": "量子追踪器",
        "dualphase": "双相分裂器",
        "ion_storm": "离子风暴",
        "magnetic": "磁场",
        "tutorial": "游戏教程",
        "tut1": "拖动来瞄准导弹",
        "tut2": "用滑块调整威力",
        "tut3": "摧毁所有敌方基地获胜",
        "tut4": "注意风力和重力！",
    }
}

# ─────────────────────────────────────────────
#  THEMES
# ─────────────────────────────────────────────
THEMES = {
    "dark": {
        "bg": "#0a0a1a",
        "bg2": "#0d1b2a",
        "bg3": "#1a1a3e",
        "panel": "#111133",
        "panel2": "#1a2040",
        "accent": "#00d4ff",
        "accent2": "#7b2fff",
        "accent3": "#ff6b35",
        "text": "#e8f4fd",
        "text2": "#8899bb",
        "text3": "#556688",
        "btn": "#1e3a5f",
        "btn_hover": "#2a5080",
        "btn_active": "#00d4ff",
        "border": "#2a4060",
        "border2": "#00d4ff",
        "health_bar": "#00ff88",
        "energy_bar": "#00d4ff",
        "danger": "#ff3355",
        "warning": "#ffaa00",
        "success": "#00ff88",
        "ground": "#1a3a1a",
        "sky_top": "#000510",
        "sky_bot": "#0a1a3a",
        "star": "#ffffff",
        "explosion1": "#ff6600",
        "explosion2": "#ffcc00",
        "explosion3": "#ff0044",
    },
    "light": {
        "bg": "#e8f0fe",
        "bg2": "#d0e4ff",
        "bg3": "#c0d8ff",
        "panel": "#ffffff",
        "panel2": "#f0f4ff",
        "accent": "#0066cc",
        "accent2": "#6600cc",
        "accent3": "#cc4400",
        "text": "#1a2a4a",
        "text2": "#445577",
        "text3": "#8899aa",
        "btn": "#c8deff",
        "btn_hover": "#a0c4ff",
        "btn_active": "#0066cc",
        "border": "#99bbdd",
        "border2": "#0066cc",
        "health_bar": "#00aa55",
        "energy_bar": "#0066cc",
        "danger": "#cc0033",
        "warning": "#cc8800",
        "success": "#00aa55",
        "ground": "#4a7a4a",
        "sky_top": "#87ceeb",
        "sky_bot": "#c8e8ff",
        "star": "#aabbcc",
        "explosion1": "#ff6600",
        "explosion2": "#ffcc00",
        "explosion3": "#ff0044",
    }
}

# ─────────────────────────────────────────────
#  MISSILE DATA
# ─────────────────────────────────────────────
MISSILES = {
    "swift1":     {"name_key": "swift1",     "cat": "light",   "damage": 20,  "radius": 40,  "speed": 18, "mass": 0.5, "cost": 0,   "color": "#00ffcc", "trail": "#00aa88", "special": None},
    "micropulse": {"name_key": "micropulse", "cat": "light",   "damage": 15,  "radius": 30,  "speed": 22, "mass": 0.3, "cost": 50,  "color": "#88ffff", "trail": "#44aaaa", "special": "pulse"},
    "featherspark":{"name_key":"featherspark","cat": "light",   "damage": 18,  "radius": 35,  "speed": 20, "mass": 0.4, "cost": 80,  "color": "#ffff44", "trail": "#aaaa00", "special": "spark"},
    "plasmaarc":  {"name_key": "plasmaarc",  "cat": "medium",  "damage": 45,  "radius": 70,  "speed": 14, "mass": 1.0, "cost": 120, "color": "#ff44ff", "trail": "#aa00aa", "special": "plasma"},
    "ionjavelin": {"name_key": "ionjavelin", "cat": "medium",  "damage": 40,  "radius": 60,  "speed": 16, "mass": 0.8, "cost": 150, "color": "#44aaff", "trail": "#0066cc", "special": "ion"},
    "wavedart":   {"name_key": "wavedart",   "cat": "medium",  "damage": 35,  "radius": 65,  "speed": 15, "mass": 0.9, "cost": 100, "color": "#44ffaa", "trail": "#00aa66", "special": "wave"},
    "titanumx":   {"name_key": "titanumx",   "cat": "heavy",   "damage": 90,  "radius": 120, "speed": 10, "mass": 2.5, "cost": 300, "color": "#ff8800", "trail": "#cc4400", "special": "heavy"},
    "hypercore":  {"name_key": "hypercore",  "cat": "heavy",   "damage": 110, "radius": 140, "speed": 9,  "mass": 3.0, "cost": 400, "color": "#ff4444", "trail": "#aa0000", "special": "core"},
    "noxium":     {"name_key": "noxium",     "cat": "heavy",   "damage": 100, "radius": 130, "speed": 8,  "mass": 2.8, "cost": 350, "color": "#aa44ff", "trail": "#6600cc", "special": "nox"},
    "starburst":  {"name_key": "starburst",  "cat": "special", "damage": 200, "radius": 220, "speed": 12, "mass": 2.0, "cost": 800, "color": "#ffffff", "trail": "#ffff88", "special": "starburst"},
    "riftbreaker":{"name_key": "riftbreaker","cat": "special", "damage": 150, "radius": 180, "speed": 11, "mass": 1.8, "cost": 700, "color": "#cc00ff", "trail": "#6600aa", "special": "rift"},
    "tempest":    {"name_key": "tempest",    "cat": "special", "damage": 80,  "radius": 160, "speed": 13, "mass": 1.5, "cost": 600, "color": "#00ccff", "trail": "#0088aa", "special": "tempest"},
    "autoseeker": {"name_key": "autoseeker", "cat": "smart",   "damage": 60,  "radius": 90,  "speed": 15, "mass": 1.2, "cost": 500, "color": "#ffcc00", "trail": "#aa8800", "special": "seek"},
    "quantum":    {"name_key": "quantum",    "cat": "smart",   "damage": 75,  "radius": 100, "speed": 14, "mass": 1.3, "cost": 600, "color": "#00ffff", "trail": "#00aaaa", "special": "quantum"},
    "dualphase":  {"name_key": "dualphase",  "cat": "smart",   "damage": 55,  "radius": 80,  "speed": 16, "mass": 1.1, "cost": 450, "color": "#ff88ff", "trail": "#aa44aa", "special": "dual"},
}

FACTIONS = {
    "soltaris": {"color": "#ffaa00", "color2": "#ff6600", "name_key": "soltaris"},
    "zenars":   {"color": "#00aaff", "color2": "#0044cc", "name_key": "zenars"},
    "novarak":  {"color": "#00ff88", "color2": "#00aa44", "name_key": "novarak"},
    "ventari":  {"color": "#ff44ff", "color2": "#aa00aa", "name_key": "ventari"},
}

# ─────────────────────────────────────────────
#  GAME STATE
# ─────────────────────────────────────────────
class GameState:
    def __init__(self):
        self.lang = "en"
        self.theme = "dark"
        self.faction = "soltaris"
        self.selected_missile = "swift1"
        self.power = 60
        self.angle = 45
        self.score = 0
        self.credits = 500
        self.level = 1
        self.wave = 1
        self.game_mode = "mission"
        self.platform_level = 1
        self.owned_missiles = {"swift1"}
        self.volume = 70
        self.high_score = 0

    def t(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def th(self):
        return THEMES[self.theme]

GS = GameState()

# ─────────────────────────────────────────────
#  PHYSICS ENGINE
# ─────────────────────────────────────────────
class PhysicsBody:
    def __init__(self, x, y, vx, vy, missile_key):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.missile_key = missile_key
        self.data = MISSILES[missile_key]
        self.alive = True
        self.trail = []
        self.age = 0
        self.homing_target = None
        self.split_done = False

    def update(self, dt, wind, gravity, obstacles, targets):
        if not self.alive:
            return None

        self.age += dt
        self.trail.append((self.x, self.y))
        if len(self.trail) > 30:
            self.trail.pop(0)

        special = self.data["special"]

        # Wind effect
        wind_force = wind * 0.3 / max(self.data["mass"], 0.1)
        self.vx += wind_force * dt

        # Gravity
        self.vy += gravity * dt * self.data["mass"]

        # Tempest: sinusoidal drift
        if special == "tempest":
            self.vx += math.sin(self.age * 3) * 2 * dt

        # Smart homing
        if special in ("seek", "quantum") and targets:
            nearest = min(targets, key=lambda t: math.hypot(t.x - self.x, t.y - self.y))
            dx = nearest.x - self.x
            dy = nearest.y - self.y
            dist = math.hypot(dx, dy) + 0.001
            strength = 80 if special == "quantum" else 50
            self.vx += (dx / dist) * strength * dt
            self.vy += (dy / dist) * strength * dt
            spd = math.hypot(self.vx, self.vy)
            max_spd = self.data["speed"] * 60
            if spd > max_spd:
                self.vx = self.vx / spd * max_spd
                self.vy = self.vy / spd * max_spd

        self.x += self.vx * dt
        self.y += self.vy * dt

        # Dual phase split
        if special == "dual" and not self.split_done and self.age > 0.5:
            self.split_done = True
            return "split"

        return None

class Target:
    def __init__(self, x, y, w, h, hp, faction):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.max_hp = hp
        self.faction = faction
        self.alive = True
        self.shake = 0
        self.destroyed_time = -1
        self.anim = 0.0

    def hit(self, damage):
        self.hp -= damage
        self.shake = 8
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            self.destroyed_time = time.time()

    def update(self, dt):
        self.anim += dt
        if self.shake > 0:
            self.shake -= 1

class Particle:
    def __init__(self, x, y, vx, vy, color, life, size):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.life = life
        self.max_life = life
        self.size = size
        self.alive = True

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += 200 * dt
        self.life -= dt
        if self.life <= 0:
            self.alive = False

class Explosion:
    def __init__(self, x, y, radius, missile_key):
        self.x = x
        self.y = y
        self.radius = radius
        self.max_radius = radius
        self.missile_key = missile_key
        self.age = 0.0
        self.duration = 0.6
        self.alive = True
        special = MISSILES[missile_key]["special"]
        if special == "starburst":
            self.duration = 1.2
        elif special == "rift":
            self.duration = 1.0

    def update(self, dt):
        self.age += dt
        if self.age >= self.duration:
            self.alive = False

    @property
    def progress(self):
        return min(self.age / self.duration, 1.0)

# ─────────────────────────────────────────────
#  GAME CANVAS
# ─────────────────────────────────────────────
class GameCanvas(QWidget):
    score_changed = pyqtSignal(int)
    game_over_signal = pyqtSignal(bool)  # True=victory

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 300)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMouseTracking(True)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.game_tick)
        self.timer.start(16)

        self.last_time = time.time()
        self.paused = False

        self.projectiles = []
        self.targets = []
        self.particles = []
        self.explosions = []
        self.terrain = []

        self.wind = 0.0
        self.gravity = 9.8 * 30
        self.ion_storm = False
        self.magnetic = False
        self.env_timer = 0.0

        self.drag_start = None
        self.drag_end = None
        self.is_dragging = False
        self.can_fire = True
        self.ammo = 10
        self.stars = []

        self.platform_x = 0
        self.platform_y = 0

        self.init_level()
        self.generate_stars()

    def generate_stars(self):
        self.stars = [(random.randint(0, 2000), random.randint(0, 600), random.random()) for _ in range(120)]

    def init_level(self):
        self.projectiles.clear()
        self.targets.clear()
        self.particles.clear()
        self.explosions.clear()
        self.can_fire = True
        self.ammo = 10 + GS.platform_level * 2

        w = self.width() if self.width() > 0 else 800
        h = self.height() if self.height() > 0 else 500

        self.generate_terrain(w, h)

        factions = list(FACTIONS.keys())
        factions.remove(GS.faction)

        count = 3 + GS.level
        for i in range(count):
            tx = int(w * 0.55 + i * (w * 0.12))
            ty = self.get_terrain_y(tx) - 40
            hp = 80 + GS.level * 20
            faction = factions[i % len(factions)]
            self.targets.append(Target(tx, ty, 50, 40, hp, faction))

        self.wind = random.uniform(-3, 3) * (1 + GS.level * 0.1)
        self.gravity = 9.8 * 30 * random.uniform(0.8, 1.3)
        self.ion_storm = random.random() < 0.3
        self.magnetic = random.random() < 0.2

        self.platform_x = int(w * 0.12)
        self.platform_y = self.get_terrain_y(int(w * 0.12)) - 20

    def generate_terrain(self, w, h):
        self.terrain = []
        points = 20
        base_y = h * 0.72
        for i in range(points + 1):
            x = i * w / points
            noise = math.sin(i * 0.8) * 30 + math.sin(i * 1.7) * 15 + random.uniform(-10, 10)
            y = base_y + noise
            self.terrain.append((x, y))

    def get_terrain_y(self, x):
        if not self.terrain:
            return self.height() * 0.72
        w = self.width() if self.width() > 0 else 800
        idx = x / w * (len(self.terrain) - 1)
        i = int(idx)
        i = max(0, min(i, len(self.terrain) - 2))
        frac = idx - i
        y1 = self.terrain[i][1]
        y2 = self.terrain[i + 1][1]
        return y1 + (y2 - y1) * frac

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.init_level()
        self.generate_stars()

    def game_tick(self):
        if self.paused:
            return
        now = time.time()
        dt = min(now - self.last_time, 0.05)
        self.last_time = now

        self.env_timer += dt
        if self.env_timer > 5.0:
            self.env_timer = 0
            self.wind += random.uniform(-1, 1)
            self.wind = max(-8, min(8, self.wind))

        for p in self.projectiles[:]:
            result = p.update(dt, self.wind, self.gravity, [], self.targets)
            if result == "split":
                self.spawn_split(p)

            hit_ground = p.y > self.get_terrain_y(p.x)
            hit_bounds = p.x < 0 or p.x > self.width() or p.y > self.height()

            if hit_ground or hit_bounds:
                self.explode(p)
                if p in self.projectiles:
                    self.projectiles.remove(p)
                continue

            for t in self.targets:
                if t.alive and abs(p.x - t.x) < t.w / 2 + 10 and abs(p.y - t.y) < t.h / 2 + 10:
                    self.explode(p)
                    if p in self.projectiles:
                        self.projectiles.remove(p)
                    break

        for t in self.targets:
            t.update(dt)

        for e in self.explosions[:]:
            e.update(dt)
            if not e.alive:
                self.explosions.remove(e)

        for pt in self.particles[:]:
            pt.update(dt)
            if not pt.alive:
                self.particles.remove(pt)

        if not self.projectiles and not self.can_fire:
            self.can_fire = True

        alive_targets = [t for t in self.targets if t.alive]
        if not alive_targets:
            GS.score += 100 * GS.level
            GS.credits += 50 * GS.level
            if GS.score > GS.high_score:
                GS.high_score = GS.score
            self.score_changed.emit(GS.score)
            QTimer.singleShot(1500, lambda: self.game_over_signal.emit(True))
            self.timer.stop()
            return

        if self.ammo <= 0 and not self.projectiles:
            self.game_over_signal.emit(False)
            self.timer.stop()
            return

        self.update()

    def spawn_split(self, p):
        for angle_offset in [-20, 20]:
            spd = math.hypot(p.vx, p.vy)
            base_angle = math.atan2(p.vy, p.vx)
            new_angle = base_angle + math.radians(angle_offset)
            nb = PhysicsBody(p.x, p.y,
                             math.cos(new_angle) * spd * 0.7,
                             math.sin(new_angle) * spd * 0.7,
                             p.missile_key)
            nb.split_done = True
            self.projectiles.append(nb)

    def explode(self, p):
        data = p.data
        radius = data["radius"]
        special = data["special"]

        if special == "rift":
            radius *= 1.5
        elif special == "starburst":
            radius *= 2.0

        exp = Explosion(p.x, p.y, radius, p.missile_key)
        self.explosions.append(exp)

        for t in self.targets:
            if not t.alive:
                continue
            dist = math.hypot(p.x - t.x, p.y - t.y)
            if dist < radius + t.w:
                dmg_factor = max(0, 1.0 - dist / (radius + t.w))
                dmg = data["damage"] * dmg_factor
                if self.ion_storm:
                    dmg *= 1.3
                t.hit(int(dmg))
                GS.score += int(dmg)
                self.score_changed.emit(GS.score)

        colors = [data["color"], "#ffcc00", "#ff4400", "#ffffff"]
        count = 30 if special in ("starburst", "rift") else 15
        for _ in range(count):
            angle = random.uniform(0, math.pi * 2)
            spd = random.uniform(50, 300)
            color = random.choice(colors)
            size = random.uniform(2, 8)
            life = random.uniform(0.3, 1.2)
            self.particles.append(Particle(
                p.x, p.y,
                math.cos(angle) * spd,
                math.sin(angle) * spd,
                color, life, size
            ))

        if special == "starburst":
            for _ in range(20):
                angle = random.uniform(0, math.pi * 2)
                spd = random.uniform(100, 500)
                self.particles.append(Particle(
                    p.x, p.y,
                    math.cos(angle) * spd,
                    math.sin(angle) * spd,
                    "#ffffff", random.uniform(0.5, 1.5), random.uniform(3, 10)
                ))

    def fire_missile(self):
        if not self.can_fire or self.ammo <= 0:
            return
        if GS.selected_missile not in GS.owned_missiles:
            return

        angle_rad = math.radians(GS.angle)
        spd = GS.power * 12 * (1 + (GS.platform_level - 1) * 0.15)
        vx = math.cos(angle_rad) * spd
        vy = -math.sin(angle_rad) * spd

        pb = PhysicsBody(self.platform_x, self.platform_y, vx, vy, GS.selected_missile)
        self.projectiles.append(pb)
        self.ammo -= 1
        self.can_fire = False
        QTimer.singleShot(800, lambda: setattr(self, 'can_fire', True))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start = event.position()
            self.is_dragging = True

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.drag_end = event.position()
            px, py = self.platform_x, self.platform_y
            dx = self.drag_end.x() - px
            dy = py - self.drag_end.y()
            if abs(dx) > 5 or abs(dy) > 5:
                angle = math.degrees(math.atan2(dy, dx))
                angle = max(5, min(85, angle))
                GS.angle = int(angle)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.is_dragging:
            self.is_dragging = False
            self.fire_missile()
            self.drag_start = None
            self.drag_end = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        th = GS.th()

        self._draw_sky(painter, w, h, th)
        self._draw_stars(painter, w, h, th)
        self._draw_env_effects(painter, w, h, th)
        self._draw_terrain(painter, w, h, th)
        self._draw_platform(painter, th)
        self._draw_targets(painter, th)
        self._draw_explosions(painter, th)
        self._draw_particles(painter)
        self._draw_projectiles(painter, th)
        self._draw_aim_line(painter, th)
        self._draw_hud(painter, w, h, th)

    def _draw_sky(self, painter, w, h, th):
        grad = QLinearGradient(0, 0, 0, h * 0.75)
        grad.setColorAt(0, QColor(th["sky_top"]))
        grad.setColorAt(1, QColor(th["sky_bot"]))
        painter.fillRect(0, 0, w, h, grad)

    def _draw_stars(self, painter, w, h, th):
        if GS.theme == "dark":
            for sx, sy, brightness in self.stars:
                x = int(sx % w)
                y = int(sy % (h * 0.7))
                alpha = int(100 + brightness * 155)
                c = QColor(th["star"])
                c.setAlpha(alpha)
                painter.setPen(QPen(c, 1 + brightness))
                painter.drawPoint(x, y)

    def _draw_env_effects(self, painter, w, h, th):
        t = time.time()
        if self.ion_storm:
            for i in range(5):
                x = int((t * 80 + i * w / 5) % w)
                grad = QLinearGradient(x, 0, x + 3, h * 0.7)
                c1 = QColor(th["accent"])
                c1.setAlpha(30)
                c2 = QColor(th["accent"])
                c2.setAlpha(0)
                grad.setColorAt(0, c1)
                grad.setColorAt(1, c2)
                painter.fillRect(x, 0, 3, int(h * 0.7), grad)

        if self.magnetic:
            for i in range(3):
                cx = w // 2 + int(math.sin(t + i * 2) * w * 0.2)
                cy = int(h * 0.3)
                c = QColor(th["accent2"])
                c.setAlpha(20)
                painter.setBrush(QBrush(c))
                painter.setPen(Qt.PenStyle.NoPen)
                r = 60 + i * 30
                painter.drawEllipse(cx - r, cy - r, r * 2, r * 2)

    def _draw_terrain(self, painter, w, h, th):
        if not self.terrain:
            return
        path = QPainterPath()
        path.moveTo(0, h)
        for x, y in self.terrain:
            path.lineTo(x, y)
        path.lineTo(w, h)
        path.closeSubpath()

        grad = QLinearGradient(0, h * 0.7, 0, h)
        grad.setColorAt(0, QColor(th["ground"]))
        c2 = QColor(th["ground"])
        c2 = c2.darker(150)
        grad.setColorAt(1, c2)
        painter.fillPath(path, grad)

        pen = QPen(QColor(th["accent"]), 2)
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawPath(path)

    def _draw_platform(self, painter, th):
        px, py = self.platform_x, self.platform_y
        lv = GS.platform_level
        faction = FACTIONS[GS.faction]

        base_w = 60 + lv * 8
        base_h = 20 + lv * 4

        grad = QLinearGradient(px - base_w // 2, py, px + base_w // 2, py + base_h)
        grad.setColorAt(0, QColor(faction["color"]))
        grad.setColorAt(1, QColor(faction["color2"]))
        painter.setBrush(QBrush(grad))
        painter.setPen(QPen(QColor(th["border2"]), 2))
        painter.drawRoundedRect(int(px - base_w // 2), int(py), base_w, base_h, 4, 4)

        barrel_len = 30 + lv * 5
        angle_rad = math.radians(GS.angle)
        bx = px + math.cos(angle_rad) * barrel_len
        by = py - math.sin(angle_rad) * barrel_len
        painter.setPen(QPen(QColor(faction["color"]), 5 + lv))
        painter.drawLine(int(px), int(py), int(bx), int(by))

        glow = QColor(faction["color"])
        glow.setAlpha(80)
        painter.setPen(QPen(glow, 10 + lv * 2))
        painter.drawLine(int(px), int(py), int(bx), int(by))

    def _draw_targets(self, painter, th):
        t = time.time()
        for tgt in self.targets:
            if not tgt.alive:
                continue
            faction = FACTIONS[tgt.faction]
            sx = int(tgt.shake * math.sin(t * 30)) if tgt.shake > 0 else 0

            x = int(tgt.x - tgt.w / 2) + sx
            y = int(tgt.y - tgt.h / 2)
            w = tgt.w
            h = tgt.h

            grad = QLinearGradient(x, y, x + w, y + h)
            grad.setColorAt(0, QColor(faction["color"]))
            grad.setColorAt(1, QColor(faction["color2"]))
            painter.setBrush(QBrush(grad))
            painter.setPen(QPen(QColor(th["border2"]), 2))
            painter.drawRoundedRect(x, y, w, h, 6, 6)

            pulse = abs(math.sin(tgt.anim * 2)) * 0.3 + 0.7
            glow = QColor(faction["color"])
            glow.setAlpha(int(60 * pulse))
            painter.setBrush(QBrush(glow))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(x - 4, y - 4, w + 8, h + 8, 8, 8)

            hp_ratio = tgt.hp / tgt.max_hp
            bar_w = w
            bar_h = 6
            painter.setBrush(QBrush(QColor("#333333")))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(x, y - 12, bar_w, bar_h)
            if hp_ratio > 0.5:
                bar_color = QColor(th["health_bar"])
            elif hp_ratio > 0.25:
                bar_color = QColor(th["warning"])
            else:
                bar_color = QColor(th["danger"])
            painter.setBrush(QBrush(bar_color))
            painter.drawRect(x, y - 12, int(bar_w * hp_ratio), bar_h)

            antenna_h = 15
            painter.setPen(QPen(QColor(faction["color"]), 2))
            painter.drawLine(int(tgt.x), y, int(tgt.x), y - antenna_h)
            blink = QColor(faction["color"]) if int(t * 3) % 2 == 0 else QColor(th["bg"])
            painter.setBrush(QBrush(blink))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(int(tgt.x) - 3, y - antenna_h - 3, 6, 6)

    def _draw_explosions(self, painter, th):
        for exp in self.explosions:
            p = exp.progress
            special = MISSILES[exp.missile_key]["special"]

            if special == "starburst":
                for ring in range(4):
                    r = int(exp.radius * p * (0.4 + ring * 0.2))
                    alpha = int(255 * (1 - p) * (1 - ring * 0.2))
                    colors = ["#ffffff", "#ffff88", "#ffaa00", "#ff4400"]
                    c = QColor(colors[ring])
                    c.setAlpha(alpha)
                    painter.setPen(QPen(c, 3 - ring * 0.5))
                    painter.setBrush(Qt.BrushStyle.NoBrush)
                    painter.drawEllipse(int(exp.x - r), int(exp.y - r), r * 2, r * 2)
                inner_r = int(exp.radius * 0.4 * (1 - p))
                c2 = QColor("#ffffff")
                c2.setAlpha(int(200 * (1 - p)))
                painter.setBrush(QBrush(c2))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(int(exp.x - inner_r), int(exp.y - inner_r), inner_r * 2, inner_r * 2)

            elif special == "rift":
                for i in range(6):
                    angle = i * 60 + p * 180
                    length = exp.radius * p
                    ex = exp.x + math.cos(math.radians(angle)) * length
                    ey = exp.y + math.sin(math.radians(angle)) * length
                    alpha = int(255 * (1 - p))
                    c = QColor("#cc00ff")
                    c.setAlpha(alpha)
                    painter.setPen(QPen(c, 3))
                    painter.drawLine(int(exp.x), int(exp.y), int(ex), int(ey))
                r = int(exp.radius * 0.5 * p)
                c2 = QColor("#6600aa")
                c2.setAlpha(int(150 * (1 - p)))
                painter.setBrush(QBrush(c2))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(int(exp.x - r), int(exp.y - r), r * 2, r * 2)

            else:
                r = int(exp.radius * p)
                alpha = int(200 * (1 - p))
                missile_color = MISSILES[exp.missile_key]["color"]
                c = QColor(missile_color)
                c.setAlpha(alpha)
                grad = QRadialGradient(exp.x, exp.y, r)
                c_inner = QColor("#ffffff")
                c_inner.setAlpha(alpha)
                c_outer = QColor(missile_color)
                c_outer.setAlpha(0)
                grad.setColorAt(0, c_inner)
                grad.setColorAt(0.4, c)
                grad.setColorAt(1, c_outer)
                painter.setBrush(QBrush(grad))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(int(exp.x - r), int(exp.y - r), r * 2, r * 2)

    def _draw_particles(self, painter):
        for pt in self.particles:
            alpha = int(255 * (pt.life / pt.max_life))
            c = QColor(pt.color)
            c.setAlpha(alpha)
            painter.setBrush(QBrush(c))
            painter.setPen(Qt.PenStyle.NoPen)
            s = int(pt.size * (pt.life / pt.max_life))
            if s > 0:
                painter.drawEllipse(int(pt.x - s / 2), int(pt.y - s / 2), s, s)

    def _draw_projectiles(self, painter, th):
        for p in self.projectiles:
            data = p.data
            color = QColor(data["color"])
            trail_color = QColor(data["trail"])

            for i, (tx, ty) in enumerate(p.trail):
                alpha = int(180 * i / len(p.trail))
                tc = QColor(trail_color)
                tc.setAlpha(alpha)
                size = max(1, int(4 * i / len(p.trail)))
                painter.setBrush(QBrush(tc))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(int(tx - size / 2), int(ty - size / 2), size, size)

            glow = QColor(color)
            glow.setAlpha(80)
            painter.setBrush(QBrush(glow))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(int(p.x - 10), int(p.y - 10), 20, 20)

            painter.setBrush(QBrush(color))
            painter.setPen(QPen(QColor("#ffffff"), 1))
            painter.drawEllipse(int(p.x - 5), int(p.y - 5), 10, 10)

    def _draw_aim_line(self, painter, th):
        if self.is_dragging and self.drag_end:
            px, py = self.platform_x, self.platform_y
            angle_rad = math.radians(GS.angle)
            spd = GS.power * 12
            vx = math.cos(angle_rad) * spd
            vy = -math.sin(angle_rad) * spd
            x, y = float(px), float(py)
            dt = 0.05
            painter.setPen(QPen(QColor(th["accent"]), 1, Qt.PenStyle.DotLine))
            for _ in range(40):
                nx = x + vx * dt
                ny = y + vy * dt
                vy += self.gravity * dt
                vx += self.wind * 0.3 * dt
                alpha = int(200 - _ * 5)
                c = QColor(th["accent"])
                c.setAlpha(max(0, alpha))
                painter.setPen(QPen(c, 2))
                painter.drawLine(int(x), int(y), int(nx), int(ny))
                x, y = nx, ny
                if y > self.get_terrain_y(x):
                    break

    def _draw_hud(self, painter, w, h, th):
        font = QFont("Arial", max(8, int(w * 0.012)))
        font.setBold(True)
        painter.setFont(font)

        wind_arrow = "→" if self.wind > 0 else "←"
        wind_str = f"{GS.t('wind')}: {wind_arrow} {abs(self.wind):.1f}"
        grav_str = f"{GS.t('gravity')}: {self.gravity / 30:.1f}g"
        ammo_str = f"{GS.t('ammo')}: {self.ammo}"
        score_str = f"{GS.t('score')}: {GS.score}"

        info_lines = [wind_str, grav_str, ammo_str, score_str]
        if self.ion_storm:
            info_lines.append(f"⚡ {GS.t('ion_storm')}")
        if self.magnetic:
            info_lines.append(f"🧲 {GS.t('magnetic')}")

        panel_w = int(w * 0.18)
        panel_h = len(info_lines) * int(h * 0.035) + 10
        bg = QColor(th["panel"])
        bg.setAlpha(180)
        painter.setBrush(QBrush(bg))
        painter.setPen(QPen(QColor(th["border"]), 1))
        painter.drawRoundedRect(8, 8, panel_w, panel_h, 6, 6)

        for i, line in enumerate(info_lines):
            c = QColor(th["accent"]) if i < 2 else QColor(th["text"])
            if "⚡" in line:
                c = QColor(th["warning"])
            elif "🧲" in line:
                c = QColor(th["accent2"])
            painter.setPen(c)
            painter.drawText(14, 24 + i * int(h * 0.035), line)

        alive = sum(1 for t in self.targets if t.alive)
        total = len(self.targets)
        tgt_str = f"{GS.t('targets')}: {alive}/{total}"
        painter.setPen(QColor(th["danger"]) if alive > 0 else QColor(th["success"]))
        painter.drawText(w - int(w * 0.2), 24, tgt_str)


# ─────────────────────────────────────────────
#  STYLED BUTTON
# ─────────────────────────────────────────────
class CosmicButton(QPushButton):
    def __init__(self, text, parent=None, accent=False, danger=False):
        super().__init__(text, parent)
        self.accent = accent
        self.danger = danger
        self._hovered = False
        self.setMinimumHeight(40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setFont(QFont("Arial", 11, QFont.Weight.Bold))

    def enterEvent(self, event):
        self._hovered = True
        self.update()

    def leaveEvent(self, event):
        self._hovered = False
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = GS.th()
        w, h = self.width(), self.height()

        if self.danger:
            base = QColor(th["danger"])
        elif self.accent:
            base = QColor(th["accent"])
        else:
            base = QColor(th["btn_hover"] if self._hovered else th["btn"])

        grad = QLinearGradient(0, 0, 0, h)
        grad.setColorAt(0, base.lighter(120))
        grad.setColorAt(1, base.darker(120))
        painter.setBrush(QBrush(grad))

        border_color = QColor(th["accent"] if self.accent else th["border2"])
        painter.setPen(QPen(border_color, 2))
        painter.drawRoundedRect(1, 1, w - 2, h - 2, 8, 8)

        if self._hovered:
            glow = QColor(th["accent"])
            glow.setAlpha(40)
            painter.setBrush(QBrush(glow))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(1, 1, w - 2, h - 2, 8, 8)

        painter.setPen(QColor(th["text"]))
        painter.setFont(self.font())
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text())


# ─────────────────────────────────────────────
#  PANEL WIDGET
# ─────────────────────────────────────────────
class CosmicPanel(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = GS.th()
        w, h = self.width(), self.height()
        grad = QLinearGradient(0, 0, w, h)
        grad.setColorAt(0, QColor(th["panel"]))
        grad.setColorAt(1, QColor(th["panel2"]))
        painter.setBrush(QBrush(grad))
        painter.setPen(QPen(QColor(th["border"]), 1))
        painter.drawRoundedRect(0, 0, w - 1, h - 1, 10, 10)


# ─────────────────────────────────────────────
#  MAIN MENU SCREEN
# ─────────────────────────────────────────────
class MainMenuScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._anim_t = 0.0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(16)
        self._setup_ui()

    def _tick(self):
        self._anim_t += 0.016
        self.update()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        center = QWidget()
        center.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(center)

        vl = QVBoxLayout(center)
        vl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vl.setSpacing(0)

        spacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        vl.addItem(spacer_top)

        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vl.addWidget(self.title_label)

        self.subtitle_label = QLabel()
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vl.addWidget(self.subtitle_label)

        vl.addSpacing(30)

        btn_container = QWidget()
        btn_container.setMaximumWidth(320)
        btn_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btn_layout = QVBoxLayout(btn_container)
        btn_layout.setSpacing(12)

        self.btn_play = CosmicButton(GS.t("play"), accent=True)
        self.btn_settings = CosmicButton(GS.t("settings"))
        self.btn_quit = CosmicButton(GS.t("quit"), danger=True)

        btn_layout.addWidget(self.btn_play)
        btn_layout.addWidget(self.btn_settings)
        btn_layout.addWidget(self.btn_quit)

        btn_wrapper = QHBoxLayout()
        btn_wrapper.addStretch()
        btn_wrapper.addWidget(btn_container)
        btn_wrapper.addStretch()
        vl.addLayout(btn_wrapper)

        spacer_bot = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        vl.addItem(spacer_bot)

        self._update_texts()

    def _update_texts(self):
        th = GS.th()
        title_font = QFont("Arial", 36, QFont.Weight.Bold)
        self.title_label.setFont(title_font)
        self.title_label.setText(GS.t("title"))
        self.title_label.setStyleSheet(f"color: {th['accent']}; background: transparent;")

        sub_font = QFont("Arial", 14)
        self.subtitle_label.setFont(sub_font)
        self.subtitle_label.setText(GS.t("subtitle"))
        self.subtitle_label.setStyleSheet(f"color: {th['text2']}; background: transparent;")

        self.btn_play.setText(GS.t("play"))
        self.btn_settings.setText(GS.t("settings"))
        self.btn_quit.setText(GS.t("quit"))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = GS.th()
        w, h = self.width(), self.height()

        grad = QLinearGradient(0, 0, 0, h)
        grad.setColorAt(0, QColor(th["sky_top"]))
        grad.setColorAt(1, QColor(th["sky_bot"]))
        painter.fillRect(0, 0, w, h, grad)

        if GS.theme == "dark":
            for sx, sy, brightness in getattr(self, '_stars', []):
                x = int(sx % w)
                y = int(sy % h)
                alpha = int(80 + brightness * 175)
                c = QColor(th["star"])
                c.setAlpha(alpha)
                painter.setPen(QPen(c, 1 + brightness * 0.5))
                painter.drawPoint(x, y)

        t = self._anim_t
        for i in range(6):
            angle = t * 0.3 + i * math.pi / 3
            rx = w * 0.5 + math.cos(angle) * w * 0.35
            ry = h * 0.5 + math.sin(angle) * h * 0.25
            r = 40 + i * 15
            c = QColor(th["accent"])
            c.setAlpha(15)
            painter.setBrush(QBrush(c))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(int(rx - r), int(ry - r), r * 2, r * 2)

    def showEvent(self, event):
        super().showEvent(event)
        if not hasattr(self, '_stars'):
            self._stars = [
                (random.uniform(0, self.width() or 800),
                 random.uniform(0, self.height() or 600),
                 random.random())
                for _ in range(120)
            ]
        self._update_texts()


# ─────────────────────────────────────────────
#  SETTINGS SCREEN
# ─────────────────────────────────────────────
class SettingsScreen(QWidget):
    back_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        title = QLabel(GS.t("settings"))
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        panel = CosmicPanel()
        panel_layout = QVBoxLayout(panel)
        panel_layout.setContentsMargins(30, 30, 30, 30)
        panel_layout.setSpacing(20)

        # Language
        lang_row = QHBoxLayout()
        lang_label = QLabel(GS.t("language"))
        lang_label.setFont(QFont("Arial", 12))
        lang_row.addWidget(lang_label)
        lang_row.addStretch()
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["English", "فارسی", "中文"])
        lang_map = {"en": 0, "fa": 1, "zh": 2}
        self.lang_combo.setCurrentIndex(lang_map.get(GS.lang, 0))
        self.lang_combo.currentIndexChanged.connect(self._change_lang)
        self.lang_combo.setMinimumWidth(120)
        lang_row.addWidget(self.lang_combo)
        panel_layout.addLayout(lang_row)

        # Theme
        theme_row = QHBoxLayout()
        theme_label = QLabel(GS.t("theme"))
        theme_label.setFont(QFont("Arial", 12))
        theme_row.addWidget(theme_label)
        theme_row.addStretch()
        self.theme_combo = QComboBox()
        self.theme_combo.addItems([GS.t("dark"), GS.t("light")])
        self.theme_combo.setCurrentIndex(0 if GS.theme == "dark" else 1)
        self.theme_combo.currentIndexChanged.connect(self._change_theme)
        self.theme_combo.setMinimumWidth(120)
        theme_row.addWidget(self.theme_combo)
        panel_layout.addLayout(theme_row)

        # Faction
        faction_row = QHBoxLayout()
        faction_label = QLabel(GS.t("faction"))
        faction_label.setFont(QFont("Arial", 12))
        faction_row.addWidget(faction_label)
        faction_row.addStretch()
        self.faction_combo = QComboBox()
        for fk, fv in FACTIONS.items():
            self.faction_combo.addItem(GS.t(fv["name_key"]), fk)
        keys = list(FACTIONS.keys())
        if GS.faction in keys:
            self.faction_combo.setCurrentIndex(keys.index(GS.faction))
        self.faction_combo.currentIndexChanged.connect(self._change_faction)
        self.faction_combo.setMinimumWidth(140)
        faction_row.addWidget(self.faction_combo)
        panel_layout.addLayout(faction_row)

        layout.addWidget(panel)

        btn_back = CosmicButton(GS.t("back"))
        btn_back.clicked.connect(self.back_signal.emit)
        layout.addWidget(btn_back)

        self._apply_styles()

    def _apply_styles(self):
        th = GS.th()
        self.setStyleSheet(f"QLabel {{ color: {th['text']}; background: transparent; }}"
                           f"QComboBox {{ background: {th['btn']}; color: {th['text']};"
                           f" border: 1px solid {th['border']}; border-radius: 6px; padding: 4px 8px; }}"
                           f"QComboBox::drop-down {{ border: none; }}"
                           f"QComboBox QAbstractItemView {{ background: {th['panel']}; color: {th['text']}; }}")

    def _change_lang(self, idx):
        langs = ["en", "fa", "zh"]
        GS.lang = langs[idx]
        self._apply_styles()

    def _change_theme(self, idx):
        GS.theme = "dark" if idx == 0 else "light"
        self._apply_styles()

    def _change_faction(self, idx):
        GS.faction = self.faction_combo.itemData(idx)

    def paintEvent(self, event):
        painter = QPainter(self)
        th = GS.th()
        w, h = self.width(), self.height()
        grad = QLinearGradient(0, 0, 0, h)
        grad.setColorAt(0, QColor(th["sky_top"]))
        grad.setColorAt(1, QColor(th["sky_bot"]))
        painter.fillRect(0, 0, w, h, grad)


# ─────────────────────────────────────────────
#  SHOP SCREEN
# ─────────────────────────────────────────────
class ShopScreen(QWidget):
    back_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(16)

        title = QLabel(GS.t("shop"))
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.credits_label = QLabel()
        self.credits_label.setFont(QFont("Arial", 13))
        self.credits_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.credits_label)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setStyleSheet("background: transparent;")

        container = QWidget()
        container.setStyleSheet("background: transparent;")
        grid = QGridLayout(container)
        grid.setSpacing(12)

        for i, (mk, md) in enumerate(MISSILES.items()):
            card = self._make_card(mk, md)
            grid.addWidget(card, i // 2, i % 2)

        scroll.setWidget(container)
        layout.addWidget(scroll)

        btn_back = CosmicButton(GS.t("back"))
        btn_back.clicked.connect(self.back_signal.emit)
        layout.addWidget(btn_back)

        self._update_credits()

    def _make_card(self, mk, md):
        card = CosmicPanel()
        card.setMinimumHeight(130)
        cl = QVBoxLayout(card)
        cl.setContentsMargins(12, 12, 12, 12)
        cl.setSpacing(6)

        name_lbl = QLabel(GS.t(md["name_key"]))
        name_lbl.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        color_style = f"color: {md['color']}; background: transparent;"
        name_lbl.setStyleSheet(color_style)
        cl.addWidget(name_lbl)

        info = QLabel(f"DMG: {md['damage']}  R: {md['radius']}  SPD: {md['speed']}")
        info.setFont(QFont("Arial", 9))
        th = GS.th()
        info.setStyleSheet(f"color: {th['text2']}; background: transparent;")
        cl.addWidget(info)

        special_text = md['special'].upper() if md['special'] else "—"
        special_lbl = QLabel(f"✦ {special_text}")
        special_lbl.setFont(QFont("Arial", 9))
        special_lbl.setStyleSheet(f"color: {th['accent2']}; background: transparent;")
        cl.addWidget(special_lbl)

        btn_row = QHBoxLayout()
        cost_lbl = QLabel(f"💰 {md['cost']}")
        cost_lbl.setStyleSheet(f"color: {th['warning']}; background: transparent;")
        cost_lbl.setFont(QFont("Arial", 10))
        btn_row.addWidget(cost_lbl)
        btn_row.addStretch()

        if mk in GS.owned_missiles:
            owned_lbl = QLabel(f"✓ {GS.t('owned')}")
            owned_lbl.setStyleSheet(f"color: {th['success']}; background: transparent;")
            owned_lbl.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            btn_row.addWidget(owned_lbl)
        else:
            buy_btn = CosmicButton(GS.t("buy"), accent=True)
            buy_btn.setMaximumWidth(80)
            buy_btn.setMinimumHeight(28)
            buy_btn.clicked.connect(lambda checked, k=mk, c=md["cost"]: self._buy(k, c))
            btn_row.addWidget(buy_btn)

        cl.addLayout(btn_row)
        return card

    def _buy(self, mk, cost):
        if GS.credits >= cost and mk not in GS.owned_missiles:
            GS.credits -= cost
            GS.owned_missiles.append(mk)
            self._update_credits()
            self._refresh()

    def _refresh(self):
        layout = self.layout()
        old_scroll = layout.itemAt(2).widget()
        layout.removeWidget(old_scroll)
        old_scroll.deleteLater()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setStyleSheet("background: transparent;")
        container = QWidget()
        container.setStyleSheet("background: transparent;")
        grid = QGridLayout(container)
        grid.setSpacing(12)
        for i, (mk, md) in enumerate(MISSILES.items()):
            card = self._make_card(mk, md)
            grid.addWidget(card, i // 2, i % 2)
        scroll.setWidget(container)
        layout.insertWidget(2, scroll)

    def _update_credits(self):
        th = GS.th()
        self.credits_label.setText(f"💰 {GS.t('credits')}: {GS.credits}")
        self.credits_label.setStyleSheet(f"color: {th['warning']}; background: transparent;")

    def paintEvent(self, event):
        painter = QPainter(self)
        th = GS.th()
        w, h = self.width(), self.height()
        grad = QLinearGradient(0, 0, 0, h)
        grad.setColorAt(0, QColor(th["sky_top"]))
        grad.setColorAt(1, QColor(th["sky_bot"]))
        painter.fillRect(0, 0, w, h, grad)


# ─────────────────────────────────────────────
#  GAME SCREEN WRAPPER
# ─────────────────────────────────────────────
class GameScreen(QWidget):
    back_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.canvas = GameCanvas()
        layout.addWidget(self.canvas)

        hud_bar = QWidget()
        hud_bar.setFixedHeight(44)
        hud_layout = QHBoxLayout(hud_bar)
        hud_layout.setContentsMargins(8, 4, 8, 4)
        hud_layout.setSpacing(10)

        self.score_lbl = QLabel(f"{GS.t('score')}: 0")
        self.score_lbl.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        hud_layout.addWidget(self.score_lbl)

        hud_layout.addStretch()

        self.missile_combo = QComboBox()
        for mk in GS.owned_missiles:
            self.missile_combo.addItem(GS.t(MISSILES[mk]["name_key"]), mk)
        self.missile_combo.currentIndexChanged.connect(self._change_missile)
        self.missile_combo.setMinimumWidth(140)
        hud_layout.addWidget(self.missile_combo)

        self.power_slider = QSlider(Qt.Orientation.Horizontal)
        self.power_slider.setRange(10, 100)
        self.power_slider.setValue(GS.power)
        self.power_slider.setFixedWidth(120)
        self.power_slider.valueChanged.connect(lambda v: setattr(GS, 'power', v))
        hud_layout.addWidget(QLabel(GS.t("power")))
        hud_layout.addWidget(self.power_slider)

        btn_back = CosmicButton(GS.t("back"))
        btn_back.setMaximumWidth(80)
        btn_back.setMinimumHeight(32)
        btn_back.clicked.connect(self._on_back)
        hud_layout.addWidget(btn_back)

        layout.addWidget(hud_bar)

        self.canvas.score_changed.connect(self._on_score)
        self.canvas.game_over_signal.connect(self._on_game_over)
        self._apply_styles()

    def _apply_styles(self):
        th = GS.th()
        self.setStyleSheet(
            f"QWidget {{ background: {th['bg']}; }}"
            f"QLabel {{ color: {th['text']}; background: transparent; }}"
            f"QComboBox {{ background: {th['btn']}; color: {th['text']};"
            f" border: 1px solid {th['border']}; border-radius: 5px; padding: 3px 6px; }}"
            f"QSlider::groove:horizontal {{ background: {th['border']}; height: 6px; border-radius: 3px; }}"
            f"QSlider::handle:horizontal {{ background: {th['accent']}; width: 14px; height: 14px;"
            f" margin: -4px 0; border-radius: 7px; }}"
        )

    def _change_missile(self, idx):
        mk = self.missile_combo.itemData(idx)
        if mk:
            GS.selected_missile = mk

    def _on_score(self, score):
        self.score_lbl.setText(f"{GS.t('score')}: {score}")

    def _on_back(self):
        self.canvas.timer.stop()
        self.back_signal.emit()

    def _on_game_over(self, won):
        msg = GS.t("level_complete") if won else GS.t("game_over")
        dlg = QMessageBox(self)
        dlg.setWindowTitle(GS.t("title"))
        dlg.setText(msg)
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.exec()
        if won:
            GS.level += 1
        self.back_signal.emit()

    def start_game(self):
        self.missile_combo.clear()
        for mk in GS.owned_missiles:
            self.missile_combo.addItem(GS.t(MISSILES[mk]["name_key"]), mk)
        self.canvas.init_level()
        self.canvas.timer.start(16)
        self._apply_styles()


# ─────────────────────────────────────────────
#  MAIN WINDOW
# ─────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(GS.t("title"))
        self.setMinimumSize(900, 600)
        self.resize(1100, 700)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.menu_screen = MainMenuScreen()
        self.settings_screen = SettingsScreen()
        self.shop_screen = ShopScreen()
        self.game_screen = GameScreen()

        self.stack.addWidget(self.menu_screen)      # 0
        self.stack.addWidget(self.settings_screen)  # 1
        self.stack.addWidget(self.shop_screen)      # 2
        self.stack.addWidget(self.game_screen)      # 3

        self.menu_screen.btn_play.clicked.connect(self._go_game)
        self.menu_screen.btn_settings.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.menu_screen.btn_quit.clicked.connect(self.close)

        self.settings_screen.back_signal.connect(lambda: self.stack.setCurrentIndex(0))
        self.shop_screen.back_signal.connect(lambda: self.stack.setCurrentIndex(0))
        self.game_screen.back_signal.connect(lambda: self.stack.setCurrentIndex(0))

        self.stack.setCurrentIndex(0)

    def _go_game(self):
        self.game_screen.start_game()
        self.stack.setCurrentIndex(3)


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Cosmic Siege")
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

