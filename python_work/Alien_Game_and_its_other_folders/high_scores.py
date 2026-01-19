import json
import os


class HighScores:
    """Manage persistent high scores storage and retrieval."""

    def __init__(self, filename="high_scores.json"):
        self.filepath = os.path.join(os.path.dirname(__file__), filename)
        self.scores = self._load_scores()

    def _load_scores(self):
        """Load high scores from JSON file. Return empty list if file doesn't exist."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    data = json.load(f)
                    # ensure it's a list of dicts with 'initials' and 'score' keys
                    if isinstance(data, list):
                        return sorted(data, key=lambda x: x.get('score', 0), reverse=True)[:10]
            except Exception:
                pass
        return []

    def add_score(self, initials, score):
        """Add a new score and save to file. Keep top 10."""
        self.scores.append({'initials': initials.upper(), 'score': int(score)})
        self.scores = sorted(self.scores, key=lambda x: x['score'], reverse=True)[:10]
        self._save_scores()

    def _save_scores(self):
        """Save current scores to JSON file."""
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.scores, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save high scores: {e}")

    def get_top_scores(self, limit=10):
        """Return top N scores sorted by score descending."""
        return self.scores[:limit]

    def is_high_score(self, score):
        """Check if score qualifies for high scores (top 10 or list not full)."""
        if len(self.scores) < 10:
            return True
        return score > self.scores[-1]['score']
