import os
import subprocess
import json
from sklearn.externals import joblib
import numpy as np

class CodeReviewAgent:
    def __init__(self, repo_path, pylint_config_path):
        self.repo_path = repo_path
        self.pylint_config_path = pylint_config_path
        self.model = joblib.load('review_model.pkl')

    def run_pylint(self):
        command = f'pylint --rcfile={self.pylint_config_path} {self.repo_path}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout

    def extract_features(self, pylint_output):
        errors = sum(1 for line in pylint_output.splitlines() if 'error' in line)
        warnings = sum(1 for line in pylint_output.splitlines() if 'warning' in line)
        return np.array([errors, warnings])

    def predict_review_feedback(self, features):
        prediction = self.model.predict(features.reshape(1, -1))
        return prediction[0]

    def generate_review(self):
        pylint_output = self.run_pylint()
        features = self.extract_features(pylint_output)
        feedback = self.predict_review_feedback(features)
        return pylint_output, feedback

    def save_report(self, pylint_output, feedback, report_path='review_report.txt'):
        with open(report_path, 'w') as f:
            f.write('--- Pylint Output ---
')
            f.write(pylint_output)
            f.write('

--- Feedback ---
')
            f.write(feedback)

if __name__ == "__main__":
    agent = CodeReviewAgent(repo_path='./sample_code', pylint_config_path='./pylint.rc')
    pylint_output, feedback = agent.generate_review()
    agent.save_report(pylint_output, feedback)
    print("代码评审完成，报告已保存！")
