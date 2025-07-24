from typing import List
from uuid import UUID
from ..models.task_suggestion import TaskSuggestion
import random


# TODO: Implement the actual recommendation generation logic with ChatGPT or similar
def generate_recommendations(user_id: UUID, count: int = 3) -> List[TaskSuggestion]:
    ideas = [
        ("Organize workspace", "A clean desk improves focus."),
        ("Read a book", "Choose one you've been putting off."),
        ("Stretch every hour", "Small movements help health."),
        ("Plan your week", "Outline key tasks for the next 7 days."),
        ("Take a short walk", "Refresh your mind with a quick stroll."),
        ("Review your goals", "Reflect on your progress and next steps."),
        ("Declutter email inbox", "Archive or delete unnecessary emails."),
        ("Meditate for 5 minutes", "Calm your mind and reduce stress."),
        ("Write a journal entry", "Capture your thoughts and ideas."),
        ("Backup important files", "Keep your data safe and secure."),
        ("Call a friend or family member", "Reconnect and strengthen relationships."),
        ("Update your to-do list", "Make sure your tasks are current."),
        ("Try a new recipe", "Experiment with cooking something different."),
        ("Clean up your desktop", "Organize files and folders."),
        ("Listen to a podcast", "Learn something new or relax."),
        ("Water your plants", "Take care of your indoor greenery."),
        ("Set a new personal goal", "Challenge yourself to grow."),
        ("Practice a hobby", "Spend time on something you enjoy."),
        ("Review your finances", "Check your budget and expenses."),
        ("Organize digital photos", "Sort and backup your memories."),
    ]
    selected_ideas = random.sample(ideas, k=min(count, len(ideas)))
    return [
        TaskSuggestion(id=None, title=title, description=desc)
        for title, desc in selected_ideas
    ]
