"""Enum'ы состояний и dataclass'ы событий шины (EventBus).

Соответствует списку сигналов из PLAN.md, раздел "Событийный поток между подсистемами".
"""

from dataclasses import dataclass
from enum import Enum


class Mood(Enum):
    """Настроение персонажа, зависящее от состояния системы (см. M3.2)."""
    IDLE = "idle"
    HAPPY = "happy"
    TIRED = "tired"
    ALERT = "alert"


class AnimState(Enum):
    """Текущий набор кадров анимации персонажа (см. SpriteAnimator, M2.3)."""
    IDLE = "idle"
    DRAG = "drag"
    CLICK = "click"
    MOOD_HAPPY = "mood_happy"
    MOOD_TIRED = "mood_tired"
    MOOD_ALERT = "mood_alert"


class PomodoroPhase(Enum):
    """Фаза конечного автомата Pomodoro (см. M2.5)."""
    IDLE = "idle"
    WORK = "work"
    SHORT_BREAK = "short_break"
    LONG_BREAK = "long_break"


# --- События (frozen dataclass'ы) --------------------------------------
#
# Каждое соответствует одному сигналу из PLAN.md. Название класса — по сигналу,
# в PascalCase. Поля — ровно те аргументы, что перечислены в скобках у сигнала.

@dataclass(frozen=True)
class MoodChanged:
    """Соответствует сигналу moodChanged(mood, context)."""
    mood: Mood
    context: str


@dataclass(frozen=True)
class SpeechBubbleRequested:
    """Соответствует сигналу speechBubbleRequested(text, duration_ms)."""
    text: str
    duration_ms: int


@dataclass(frozen=True)
class PomodoroStateChanged:
    """Соответствует сигналу pomodoroStateChanged(phase, seconds_remaining)."""
    phase: PomodoroPhase
    seconds_remaining: int


@dataclass(frozen=True)
class CommandExecuted:
    """Соответствует сигналу commandExecuted(intent, result)."""
    intent: str
    result: str
