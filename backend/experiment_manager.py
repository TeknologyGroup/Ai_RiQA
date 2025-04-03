import uuid
from datetime import datetime
from .database import RIQA_DB

class ExperimentManager:
    def __init__(self):
        self.db = RIQA_DB()
    
    def create_experiment(self, user_id, experiment_type):
        session_id = str(uuid.uuid4())
        return {
            'session_id': session_id,
            'user_id': user_id,
            'type': experiment_type,
            'created_at': datetime.now().isoformat()
        }
    
    def save_results(self, session_id, params, results):
        self.db.save_simulation(
            user_id=results.get('user_id'),
            session_id=session_id,
            sim_type=results.get('type'),
            params=params,
            results=results
        )
    
    def get_experiment_history(self, user_id):
        with self.db._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM simulations 
                WHERE user_id = ?
                ORDER BY created_at DESC
                LIMIT 50
            ''', (user_id,))
            return cursor.fetchall()
