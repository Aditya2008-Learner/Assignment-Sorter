import os
import sys
import unittest
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.c_core.c_bridge import (
    _lib_loaded, fast_levenshtein, fast_fuzzy_similarity,
    fast_bm25_term_score, fast_batch_bm25, fast_hash_string
)
from src.backend.database import DatabaseRepo, init_db
from src.backend.scraper import PYQScraper
from src.backend.ocr_parser import NotebookParser
from src.backend.assignment_gen import AssignmentGenerator
from src.backend.grader import AssignmentGrader
from src.backend.note_maker import NoteMaker
from src.backend.quiz_engine import QuizEngine
from src.backend.rag_engine import RAGIndex
from src.backend.ai_engine import AIEngine
from src.backend.app import app
from starlette.testclient import TestClient

class TestStudyAssistantE2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()
        PYQScraper.seed_initial_pyq_papers()
        RAGIndex.get_instance().rebuild_index()
        cls.client = TestClient(app)

    def test_01_c_core_acceleration(self):
        dist = fast_levenshtein("Dijkstra", "Dijkstr")
        self.assertEqual(dist, 1)
        sim = fast_fuzzy_similarity("algorithm", "algorithm")
        self.assertAlmostEqual(sim, 1.0)
        bm25 = fast_bm25_term_score(2, 100, 100.0, 50, 5)
        self.assertGreater(bm25, 0.0)
        batch = fast_batch_bm25([2, 0, 1], [100, 50, 120], 90.0, 20, 3)
        self.assertEqual(len(batch), 3)
        self.assertEqual(batch[1], 0.0)

    def test_02_database_assignments(self):
        assignments = DatabaseRepo.get_assignments(limit=10)
        self.assertGreater(len(assignments), 0)
        first = assignments[0]
        self.assertIn("title", first)
        self.assertIn("subject", first)
        self.assertIn("college", first)

    def test_03_pyq_scraper(self):
        results = PYQScraper.search_online_pyq("Data Structures")
        self.assertGreater(len(results), 0)
        self.assertIn("title", results[0])
        self.assertIn("parsed_questions", results[0])

    def test_04_assignment_generator(self):
        gen = AssignmentGenerator.generate_assignment(
            subject="Operating Systems",
            semester="4",
            difficulty="Advanced",
            num_questions=5
        )
        self.assertIn("questions", gen)
        self.assertEqual(len(gen["questions"]), 5)
        self.assertIn("rubric", gen)

    def test_05_assignment_grader_and_hints(self):
        hint1 = AssignmentGrader.get_progressive_hint("Explain Master Theorem with T(n)=4T(n/2)+n^2", 1)
        self.assertIn("hint_text", hint1)
        
        hint3 = AssignmentGrader.get_progressive_hint("Explain Master Theorem with T(n)=4T(n/2)+n^2", 3)
        self.assertIn("hint_text", hint3)

        evaluation = AssignmentGrader.evaluate_answer(
            question_text="Derive the Master Theorem recurrence for T(n) = 4T(n/2) + n^2",
            student_answer="Here a=4, b=2. n^(log_b a) = n^2. Since f(n) = n^2, Case 2 applies: T(n) = Theta(n^2 log n).",
            total_marks=10.0,
            model_answer_summary="T(n) = Theta(n^2 log n)"
        )
        self.assertGreaterEqual(evaluation["marks_awarded"], 7.0)
        self.assertIn("rubric_breakdown", evaluation)

    def test_06_note_maker_and_flashcards(self):
        notes = NoteMaker.generate_study_notes(
            subject="Data Structures & Algorithms",
            topic="AVL Trees"
        )
        self.assertIn("flashcards", notes)
        self.assertGreater(len(notes["flashcards"]), 0)
        self.assertIn("formulas", notes)
        self.assertIn("mnemonics", notes)

    def test_07_quiz_engine_and_radar(self):
        quiz = QuizEngine.generate_quiz(
            subject="Computer Science",
            topic="Operating Systems",
            num_questions=5
        )
        self.assertEqual(len(quiz["questions"]), 5)
        
        answers = [
            {"question_id": q["id"], "selected_index": q["correct_index"]}
            for q in quiz["questions"]
        ]
        attempt = QuizEngine.grade_attempt(quiz["id"], answers, 30)
        self.assertEqual(attempt["score"], 5.0)
        self.assertEqual(attempt["percentage"], 100.0)

    def test_08_rag_and_chat(self):
        res = AIEngine.chat_rag_response("How does Dijkstra's algorithm work with negative edge weights?")
        self.assertIn("response", res)
        self.assertIn("citations", res)

    def test_09_fastapi_endpoints(self):
        resp = self.client.get("/api/system/status")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["status"], "online")
        
        resp_assign = self.client.get("/api/assignments")
        self.assertEqual(resp_assign.status_code, 200)

        resp_pyq = self.client.get("/api/pyq/search?subject=Operating%20Systems")
        self.assertEqual(resp_pyq.status_code, 200)

        resp_chat = self.client.post("/api/chat/message", json={"message": "What are ACID properties in DBMS?"})
        self.assertEqual(resp_chat.status_code, 200)
        self.assertIn("response", resp_chat.json())

if __name__ == "__main__":
    unittest.main()
