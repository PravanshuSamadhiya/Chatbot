import json
import os
from typing import Dict, List, Optional

class TornedEducationChatbot:
    def __init__(self):
        self.categories = {
            "1": "Student Support",
            "2": "Doubt Solving / Learning Help",
            "3": "Course Recommendations",
            "4": "Exam and Certification Related",
            "5": "Technical / Platform Help",
            "6": "Career Guidance",
            "7": "Motivation and Study Help"
        }
        
        self.qa_pairs = self._load_qa_pairs()
        
    def _load_qa_pairs(self) -> Dict[str, List[Dict[str, str]]]:
        """Load Q&A pairs from JSON file or use default data"""
        try:
            with open('qa_data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._get_default_qa_pairs()
    
    def _get_default_qa_pairs(self) -> Dict[str, List[Dict[str, str]]]:
        """Return default Q&A pairs if JSON file doesn't exist"""
        return {
            "Student Support": [
                {"question": "What courses are available for [subject/topic]?", 
                 "answer": "You can explore various subjects and topics by visiting the 'Categories' section on our website."},
                {"question": "Which course is best for beginners in [subject]?", 
                 "answer": "For beginners, we recommend starting with our 'Foundation Courses' available under each category."},
                {"question": "Can you suggest a learning path for [career goal]?", 
                 "answer": "You can reach out to our team by mailing on 'torned17.edu.in@gmail.com' or contact your mentor Ram on '95498 08067'."},
                {"question": "How do I enroll in a course?", 
                 "answer": "Select a category on the navbar, choose your category, and then purchase your desired course."},
                {"question": "What is the duration and cost of [course name]?", 
                 "answer": "You can view the duration and cost details on the specific course page."}
            ],
            "Doubt Solving / Learning Help": [
                {"question": "Can you explain [concept] in simple words?", 
                 "answer": "Our team of mentors is always ready to help. You can also check the concept explanation videos in your course material."},
                {"question": "I'm struggling with [topic]. Can you guide me?", 
                 "answer": "Click on the 'Quiz Practice' button on the navbar for more support."},
                {"question": "Do you have practice questions for [chapter/topic]?", 
                 "answer": "Yes! Practice questions are available in your course material and in the 'Quiz Practice' section."},
                {"question": "How can I improve in [skill/subject]?", 
                 "answer": "Click on the 'Quiz Practice' button on the navbar."},
                {"question": "Can you give me tips to study [subject] more effectively?", 
                 "answer": "Click on the 'Quiz Practice' button on the navbar."}
            ],
            "Course Recommendations": [
                {"question": "What are the top trending courses right now?", 
                 "answer": "Check out the 'Popular Courses' section under Categories."},
                {"question": "Which course should I take after completing [course]?", 
                 "answer": "You can explore the advanced level courses under the same category."},
                {"question": "Recommend a course based on my interests: [e.g., AI, Design, Finance].", 
                 "answer": "We have a variety of courses. Visit the Categories section and choose based on your interest."}
            ],
            "Exam and Certification Related": [
                {"question": "Will I get a certificate after completing the course?", 
                 "answer": "Yes! You will receive a certificate after successful completion of your course."},
                {"question": "What exams can I prepare for with your platform?", 
                 "answer": "You can prepare for exams like JEE, NEET, Olympiads, and many more."},
                {"question": "How can I download my course completion certificate?", 
                 "answer": "Our team will send your certificate to your provided email after course completion."},
                {"question": "Are there any mock tests available for [exam name]?", 
                 "answer": "Yes! Mock tests are available on our mobile app. Download here: App Link."}
            ],
            "Technical / Platform Help": [
                {"question": "How do I reset my password?", 
                 "answer": "Go to Profile > Settings > Reset Password."},
                {"question": "I'm facing issues playing videos. Can you help?", 
                 "answer": "Please clear your browser cache or use a different browser. If issue persists, contact support."},
                {"question": "How do I track my course progress?", 
                 "answer": "You can track your progress from Profile > Enrolled Courses."},
                {"question": "Can I access courses offline?", 
                 "answer": "Yes, courses can be accessed in offline mode."},
                {"question": "How can I get customer support if I face problems?", 
                 "answer": "You can mail us at 'torned17.edu.in@gmail.com' or call your mentor Ram at '95498 08067'."}
            ],
            "Career Guidance": [
                {"question": "What career options do I have after learning [skill]?", 
                 "answer": "There are multiple career options. For personalized guidance, contact your mentor."},
                {"question": "Can you suggest internships or projects to build experience?", 
                 "answer": "Our mentors can guide you for internship/project opportunities. Stay connected with your mentor."},
                {"question": "How do I create a strong resume after completing courses?", 
                 "answer": "You can follow our resume-building tips provided at the end of the course."}
            ],
            "Motivation and Study Help": [
                {"question": "How should I manage my time while studying online?", 
                 "answer": "Prepare a weekly study schedule and stick to it. Take regular short breaks for better focus."},
                {"question": "Give me a motivational quote to stay consistent today!", 
                 "answer": "Success is the sum of small efforts repeated day in and day out."},
                {"question": "Suggest a study schedule for [subject/exam].", 
                 "answer": "Divide your day into small study blocks for different subjects and keep at least 1 hour for revision."}
            ]
        }
    
    def show_categories(self) -> None:
        """Display available categories"""
        print("\n🎯 Available Categories:")
        for num, category in self.categories.items():
            print(f"{num}. {category}")
    
    def show_questions(self, category: str) -> List[Dict[str, str]]:
        """Display questions for a selected category"""
        if category not in self.categories.values():
            return []
        
        questions = self.qa_pairs.get(category, [])
        print(f"\n📚 Questions for {category}:")
        for i, qa in enumerate(questions, 1):
            print(f"{i}. {qa['question']}")
        return questions
    
    def get_answer(self, category: str, question_index: int) -> Optional[str]:
        """Get answer for selected question"""
        if category not in self.categories.values():
            return None
        
        questions = self.qa_pairs.get(category, [])
        if 1 <= question_index <= len(questions):
            return questions[question_index - 1]['answer']
        return None
    
    def handle_unknown_question(self) -> str:
        """Handle questions not in the predefined list"""
        return "Thank you for your question! Our team will get back to you. You can also reach us at torned17.edu.in@gmail.com."

def main():
    chatbot = TornedEducationChatbot()
    current_category = None
    
    print("Welcome to Torned Education Platform Assistant! 🤖")
    print("How can I help you today?")
    
    while True:
        if not current_category:
            chatbot.show_categories()
            print("\nEnter category number (or 'exit' to quit):")
            choice = input().strip().lower()
            
            if choice == 'exit':
                print("Thank you for using Torned Education Platform Assistant. Goodbye! 👋")
                break
            
            if choice in chatbot.categories:
                current_category = chatbot.categories[choice]
            else:
                print("Invalid category number. Please try again.")
                continue
        
        questions = chatbot.show_questions(current_category)
        if not questions:
            print("No questions found for this category.")
            current_category = None
            continue
        
        print("\nEnter question number (or 'back' to change category):")
        choice = input().strip().lower()
        
        if choice == 'back':
            current_category = None
            continue
        
        try:
            question_index = int(choice)
            answer = chatbot.get_answer(current_category, question_index)
            if answer:
                print(f"\nAnswer: {answer}")
            else:
                print("Invalid question number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        
        print("\nWould you like to ask another question? (yes/no)")
        if input().strip().lower() != 'yes':
            current_category = None

if __name__ == "__main__":
    main() 