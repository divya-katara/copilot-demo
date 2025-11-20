# Theory Questions - AI Ethics and Security

## Question 11: Three Ethical Concerns of Using AI-Assisted Tools

### 1. Code Ownership and Attribution

**Concern:**  
When AI generates code, questions arise about intellectual property ownership. Who owns the code - the developer, the AI provider, or the organization? Additionally, there's an ethical obligation to properly attribute AI-generated work.

**Real-World Scenario:**  
A developer uses Copilot to generate a complex algorithm for a startup's core product. Later, they discover similar code exists in open-source projects that Copilot may have learned from.

**How to Address:**
- Always review AI-generated code for potential copyright issues
- Clearly document when AI tools were used in development
- Follow proper attribution practices in comments and documentation
- Ensure compliance with your organization's IP policies
- Use code similarity checkers to identify potential conflicts
- Example: Add comments like `// Initial implementation with Copilot assistance, reviewed and modified`

---

### 2. Bias and Discrimination in AI Suggestions

**Concern:**  
AI models are trained on existing code which may contain biases, outdated practices, or discriminatory patterns. This can perpetuate harmful stereotypes or create unfair systems.

**Real-World Scenario:**  
A developer building a hiring platform accepts Copilot suggestions that inadvertently filter candidates based on demographic factors rather than qualifications, because the training data reflected historical biases.

**How to Address:**
- Critically review all AI suggestions for potential bias
- Test algorithms with diverse datasets
- Involve diverse team members in code review
- Implement fairness checks and validation
- Regularly audit systems for discriminatory outcomes
- Example: When building recommendation systems, explicitly test for fair treatment across different user groups
- Document bias testing in your testing strategy

---

### 3. Security Vulnerabilities and Insecure Coding Practices

**Concern:**  
AI tools may suggest code with security vulnerabilities (SQL injection, XSS, hardcoded credentials) because they learn from publicly available code that may contain security flaws.

**Real-World Scenario:**  
A developer accepts a Copilot suggestion that uses string concatenation for SQL queries instead of parameterized queries, creating a SQL injection vulnerability that goes unnoticed until exploited.

**How to Address:**
- Never trust AI-generated code without security review
- Run automated security scanning tools (Snyk, SonarQube)
- Follow secure coding guidelines (OWASP Top 10)
- Implement mandatory code security reviews
- Use static analysis tools to catch vulnerabilities
- Example Implementation:
  ```python
  # ❌ Insecure - Never accept this
  query = f"SELECT * FROM users WHERE id = {user_id}"
  
  # ✅ Secure - Always validate and use parameterized queries
  query = "SELECT * FROM users WHERE id = ?"
  cursor.execute(query, (user_id,))
  ```
- Maintain a security checklist for all AI-assisted code

---

## Question 12: Security and Licensing Risks in API Integration

### Scenario: Public API Integration Code Review

**Example Copilot Suggestion for Weather API:**
```python
import requests

def get_weather(city):
    api_key = "abc123xyz789"  # ❌ RISK: Hardcoded API key
    url = f"http://api.weather.com/data?city={city}&key={api_key}"  # ❌ RISK: HTTP not HTTPS
    response = requests.get(url)
    return response.json()
```

### Security Risks Identified:

#### Risk 1: Hardcoded API Credentials
**Issue:** API key is hardcoded in source code

**Potential Impact:**
- Key exposure if code is committed to public repository
- Unauthorized API usage and cost overruns
- Data breaches if API provides sensitive information

**Mitigation Strategy:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    api_key = os.getenv('WEATHER_API_KEY')  # ✅ Load from environment
    if not api_key:
        raise ValueError("API key not configured")
    # ... rest of code
```

**Additional Measures:**
- Store keys in environment variables or secret managers (AWS Secrets Manager, Azure Key Vault)
- Use `.env` files (never commit to version control)
- Rotate API keys regularly
- Implement rate limiting to prevent abuse
- Use `.gitignore` to exclude sensitive files

---

#### Risk 2: Insecure HTTP Communication
**Issue:** Using HTTP instead of HTTPS exposes data in transit

**Potential Impact:**
- Man-in-the-middle attacks
- API key interception
- Data tampering

**Mitigation Strategy:**
```python
def get_weather(city):
    api_key = os.getenv('WEATHER_API_KEY')
    # ✅ Always use HTTPS
    url = f"https://api.weather.com/data"
    params = {'city': city, 'key': api_key}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # ✅ Check for HTTP errors
    return response.json()
```

**Additional Measures:**
- Enforce TLS/SSL certificate validation
- Set appropriate timeouts
- Implement retry logic with exponential backoff

---

#### Risk 3: Insufficient Error Handling
**Issue:** No validation or error handling

**Mitigation Strategy:**
```python
def get_weather(city):
    try:
        # Validate input
        if not city or not isinstance(city, str):
            raise ValueError("Invalid city name")
            
        api_key = os.getenv('WEATHER_API_KEY')
        if not api_key:
            raise ValueError("API key not configured")
        
        url = "https://api.weather.com/data"
        params = {'city': city, 'key': api_key}
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        # Validate response structure
        if 'temperature' not in data:
            raise ValueError("Invalid API response")
            
        return data
        
    except requests.exceptions.Timeout:
        logging.error("API request timeout")
        raise
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        raise
    except ValueError as e:
        logging.error(f"Validation error: {e}")
        raise
```

---

### Licensing Risks Identified:

#### Risk 1: Unlicensed Library Usage
**Issue:** Copilot might suggest libraries without considering licenses

**Example:**
```python
import some_proprietary_library  # ❌ May have restrictive license
```

**Mitigation Strategy:**
1. **Check Library Licenses:**
   ```bash
   pip-licenses --format=markdown > licenses.md
   ```

2. **Verify Compatibility:**
   - MIT, Apache 2.0, BSD: Generally permissive
   - GPL: Requires open-sourcing your code
   - Proprietary: May require paid license

3. **Document Dependencies:**
   ```markdown
   ## Third-Party Licenses
   - requests (Apache 2.0) - Compatible ✅
   - python-dotenv (BSD) - Compatible ✅
   ```

4. **Use Approved Libraries:**
   - Maintain a whitelist of approved libraries
   - Review new dependencies in pull requests
   - Use tools like FOSSA or Black Duck for license scanning

---

#### Risk 2: Code Snippet Copyright
**Issue:** AI might reproduce copyrighted code snippets

**Mitigation Strategy:**
- Review generated code for exact matches to known projects
- Use code similarity tools
- Prefer writing custom implementations for critical components
- When using third-party code, properly attribute and follow license terms

---

### Complete Secure Implementation Example:

```python
import os
import logging
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class WeatherAPIClient:
    """Secure Weather API client with proper error handling."""
    
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        if not self.api_key:
            raise ValueError("WEATHER_API_KEY environment variable not set")
        
        self.base_url = "https://api.weather.com/data"
        self.timeout = 10
    
    def get_weather(self, city: str) -> Optional[Dict]:
        """
        Fetch weather data for a city.
        
        Args:
            city: City name (validated)
            
        Returns:
            Weather data dictionary or None on error
            
        Raises:
            ValueError: If city is invalid
        """
        # Input validation
        if not city or not isinstance(city, str):
            raise ValueError("City name must be a non-empty string")
        
        if len(city) > 100:  # Prevent abuse
            raise ValueError("City name too long")
        
        try:
            # Make secure API request
            params = {'city': city, 'key': self.api_key}
            response = requests.get(
                self.base_url,
                params=params,
                timeout=self.timeout,
                verify=True  # Verify SSL certificate
            )
            
            # Check response status
            response.raise_for_status()
            
            # Parse and validate response
            data = response.json()
            if not self._validate_response(data):
                logger.error("Invalid response structure")
                return None
            
            return data
            
        except requests.exceptions.Timeout:
            logger.error(f"Timeout fetching weather for {city}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
            return None
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            return None
    
    def _validate_response(self, data: Dict) -> bool:
        """Validate API response structure."""
        required_fields = ['temperature', 'conditions']
        return all(field in data for field in required_fields)

# Usage
if __name__ == "__main__":
    client = WeatherAPIClient()
    weather = client.get_weather("London")
    if weather:
        print(f"Temperature: {weather['temperature']}°C")
```

---

## Summary

**Security Mitigation Checklist:**
- [ ] No hardcoded credentials
- [ ] HTTPS for all network communication
- [ ] Input validation and sanitization
- [ ] Proper error handling and logging
- [ ] Timeout and rate limiting
- [ ] SSL certificate verification

**Licensing Mitigation Checklist:**
- [ ] All dependencies have compatible licenses
- [ ] Licenses are documented
- [ ] License compliance is verified in CI/CD
- [ ] Regular license audits are conducted

By identifying and mitigating these risks, we ensure secure and compliant integration of public APIs in our projects.
