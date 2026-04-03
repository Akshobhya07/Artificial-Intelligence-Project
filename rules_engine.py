class RulesEngine:
    """
    Expert system evaluating natural language text to determine
    logical test scenarios without generating test code directly.
    """
    def __init__(self):
        self.scenarios = []

    def evaluate_text(self, text):
        self.scenarios = []
        text_lower = text.lower()
        
        # Rule 1: Login / Authentication
        if 'login' in text_lower or 'authenticate' in text_lower or 'sign in' in text_lower:
            tests = [
                {"name": "test_successful_authentication", "desc": "Verify authenticating with valid credentials returns success."},
                {"name": "test_invalid_password", "desc": "Verify authenticating with an invalid password fails."},
                {"name": "test_empty_credentials", "desc": "Verify omitting required fields is handled safely."}
            ]
            if 'email' in text_lower:
                tests.append({"name": "test_invalid_email_format", "desc": "Verify providing a malformed email fails validation."})
            
            self.scenarios.append({
                "feature": "Authentication Module",
                "tests": tests
            })
            
        # Rule 2: Registration / Signup
        if 'register' in text_lower or 'sign up' in text_lower or 'signup' in text_lower:
            tests = [
                {"name": "test_successful_registration", "desc": "Verify new user can register successfully."},
                {"name": "test_duplicate_user", "desc": "Verify registration fails if user already exists."},
                {"name": "test_password_strength", "desc": "Verify weak passwords are rejected."}
            ]
            self.scenarios.append({
                "feature": "User Registration",
                "tests": tests
            })

        # Rule 3: Payment / Checkout
        if 'payment' in text_lower or 'checkout' in text_lower or 'credit card' in text_lower or 'pay' in text_lower:
            tests = [
                {"name": "test_successful_payment", "desc": "Verify payment processes successfully with valid details."},
                {"name": "test_declined_card", "desc": "Verify system handles declined cards appropriately."},
                {"name": "test_expired_card", "desc": "Verify expired cards are rejected."}
            ]
            self.scenarios.append({
                "feature": "Payment Processing",
                "tests": tests
            })
            
        # Rule 4: Data Entry / Forms 
        if 'form' in text_lower or 'submit' in text_lower or 'data entry' in text_lower:
            tests = [
                {"name": "test_submit_valid_data", "desc": "Verify submitting valid data succeeds."},
                {"name": "test_missing_required_fields", "desc": "Verify missing required fields correctly triggers an error."}
            ]
            self.scenarios.append({
                "feature": "Data Submission Form",
                "tests": tests
            })

        # Fallback Rule: If no specific keywords are detected
        if not self.scenarios:
            self.scenarios.append({
                "feature": "Generic Functional Feature",
                "tests": [
                    {"name": "test_happy_path", "desc": "Verify the primary workflow succeeds with valid inputs."},
                    {"name": "test_edge_cases", "desc": "Verify edge cases and boundary conditions are handled."},
                    {"name": "test_error_handling", "desc": "Verify exceptional states or invalid inputs are handled gracefully."}
                ]
            })

        return self.scenarios
