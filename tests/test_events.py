import dataclasses

import pytest

from deskpet.events import (
    AnimState,
    CommandExecuted,
    Mood,
    MoodChanged,
    PomodoroPhase,
    PomodoroStateChanged,
    SpeechBubbleRequested,
)


class TestMood:
    def test_has_expected_members(self):
        names = {m.name for m in Mood}
        assert {"IDLE", "HAPPY", "TIRED", "ALERT"} <= names


class TestAnimState:
    def test_has_expected_members(self):
        names = {s.name for s in AnimState}
        assert {"IDLE", "DRAG", "CLICK", "MOOD_HAPPY", "MOOD_TIRED", "MOOD_ALERT"} <= names


class TestPomodoroPhase:
    def test_has_expected_members(self):
        names = {p.name for p in PomodoroPhase}
        assert {"WORK", "SHORT_BREAK", "LONG_BREAK"} <= names


class TestMoodChanged:
    def test_construction(self):
        event = MoodChanged(mood=Mood.HAPPY, context="cpu_low")
        assert event.mood is Mood.HAPPY
        assert event.context == "cpu_low"

    def test_is_frozen(self):
        event = MoodChanged(mood=Mood.HAPPY, context="cpu_low")
        with pytest.raises(dataclasses.FrozenInstanceError):
            event.context = "changed"


class TestSpeechBubbleRequested:
    def test_construction(self):
        event = SpeechBubbleRequested(text="Привет!", duration_ms=3000)
        assert event.text == "Привет!"
        assert event.duration_ms == 3000

    def test_is_frozen(self):
        event = SpeechBubbleRequested(text="Привет!", duration_ms=3000)
        with pytest.raises(dataclasses.FrozenInstanceError):
            event.text = "Пока!"


class TestPomodoroStateChanged:
    def test_construction(self):
        event = PomodoroStateChanged(phase=PomodoroPhase.WORK, seconds_remaining=1500)
        assert event.phase is PomodoroPhase.WORK
        assert event.seconds_remaining == 1500

    def test_is_frozen(self):
        event = PomodoroStateChanged(phase=PomodoroPhase.WORK, seconds_remaining=1500)
        with pytest.raises(dataclasses.FrozenInstanceError):
            event.seconds_remaining = 0


class TestCommandExecuted:
    def test_construction(self):
        event = CommandExecuted(intent="start_timer", result="ok")
        assert event.intent == "start_timer"
        assert event.result == "ok"

    def test_is_frozen(self):
        event = CommandExecuted(intent="start_timer", result="ok")
        with pytest.raises(dataclasses.FrozenInstanceError):
            event.result = "changed"
