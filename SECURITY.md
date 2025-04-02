Security Policy for AI_RIQA
AI_RIQA is an educational chatbot designed for scientific simulations in fields such as mathematics, ballistics, quantum physics, biology, and astronomy. As a non-commercial tool aimed at students, educators, and academic sponsors, security is a top priority to safeguard users from potential attacks and ensure a reliable experience. This policy outlines how to report vulnerabilities and our commitment to keeping the project secure.

Supported Versions
The following versions of AI_RIQA receive security updates:
Version
Supported
1.0.x
✅ Yes
< 1.0
❌ No (Pre-release)

Reporting a Vulnerability
If you discover a vulnerability in AI_RIQA, we encourage you to report it responsibly to protect the educational community. Follow these steps:
	1	Contact Us Privately:
	◦	Send an email to martinobattista@gmail.com.
	◦	Subject: “AI_RIQA Security Vulnerability Report”.
	2	Details to Include:
	◦	Project: https://github.com/TeknologyGroup/AI_RIQA.
	◦	Public Status: Indicate if the vulnerability has already been made public and, if so, where.
	◦	Description: Provide a detailed explanation, including:
	▪	Type of vulnerability (e.g., XSS, remote code execution).
	▪	Affected component (e.g., backend, frontend, OCR).
	▪	Steps to reproduce the issue.
	▪	Potential impact (e.g., user data compromise).
	◦	Evidence: If possible, attach a non-destructive proof-of-concept.
	3	Response:
	◦	You’ll receive acknowledgment within 48 hours.
	◦	Within 5 business days, we’ll update you on the next steps.
	◦	We’ll keep you informed about progress toward a fix.

Disclosure Policy
We handle vulnerability reports with a clear process:
	1	Verification: We confirm the vulnerability and identify affected versions.
	2	Analysis: We review the codebase for similar issues.
	3	Fix: We develop patches for supported versions.
	4	Release: We publish updates via GitHub Releases and updated packages (.apk, .ipa, .exe).
	5	Communication: We notify the reporter and the community when the fix is available, respecting confidentiality until the public release.
We ask that you keep the vulnerability confidential until we announce the solution.

Potential Vulnerable Areas and Security Measures
AI_RIQA uses various technologies that could be targets for attacks. Below are the main risk areas and the countermeasures implemented or recommended:
1. Backend (FastAPI)
	•	Risks:
	◦	Injection (SQL, Command): Unvalidated inputs in endpoints like /chat or /simulate.
	◦	Remote Code Execution: Python dependencies (e.g., pytesseract, matplotlib) may have use-after-free or unsafe deserialization vulnerabilities.
	•	Protections:
	◦	Input validation and sanitization using Pydantic in FastAPI.
	◦	Regular dependency updates (pip install -r requirements.txt --upgrade).
	◦	Running in an isolated environment (e.g., Docker) to limit impact.
2. Frontend (Vue.js)
	•	Risks:
	◦	Cross-Site Scripting (XSS): User-displayed messages without escaping could execute malicious scripts.
	◦	CSRF: Google authentication could be vulnerable if not secured.
	•	Protections:
	◦	Automatic data escaping with Vue.js (v-html used only with trusted data).
	◦	CSRF tokens configured in Firebase Authentication.
	◦	CSP (Content Security Policy) headers to restrict external scripts.
3. Firebase (Authentication and Hosting)
	•	Risks:
	◦	Unauthorized Access: Misconfigured Firebase security rules could expose data.
	◦	API Abuse: Exposed API keys in the frontend could be exploited.
	•	Protections:
	◦	Restrictive Firebase security rules (e.g., only authenticated users can access).
	◦	API keys proxied through the backend via FastAPI.
	◦	Access monitoring via Firebase Console.
4. OCR (pytesseract)
	•	Risks:
	◦	Code Execution: Malicious images could exploit bugs in pytesseract or pillow.
	◦	Denial of Service (DoS): Processing large files could overload the server.
	•	Protections:
	◦	File size and format limits (e.g., max 5 MB, PNG/JPG only).
	◦	OCR process sandboxing with resource restrictions (e.g., ulimit on Linux).
	◦	Updates to patched versions of pytesseract.
5. Database (SQLite/PostgreSQL)
	•	Risks:
	◦	SQL Injection: Non-parameterized queries could be exploited.
	◦	Data Exposure: Unencrypted database could leak shared results.
	•	Protections:
	◦	Exclusive use of parameterized queries.
	◦	SQLite database encryption (e.g., with SQLCipher) or SSL for PostgreSQL.
General Measures
	•	Rate Limiting: Implemented in FastAPI to prevent DoS attacks.
	•	Logging: Suspicious access logged for post-incident analysis.
	•	Education: Users encouraged to report unusual behavior.

Guidelines for Security Researchers
When exploring AI_RIQA’s security, we ask you to:
	•	Avoid compromising user data or systems.
	•	Refrain from destructive testing or DoS attacks.
	•	Do not publicly disclose vulnerabilities before our fix.
	•	Respect the project’s educational purpose, avoiding actions that undermine its integrity.

Contact
For security reports or inquiries:
	•	Email: martinobattista@gmail.com
	•	GitHub: Use the “Security Advisories” section at TeknologyGroup/AI_RIQA (contact us first for access).

Handling Duplicate CVE Reports
If GitHub flags a report as a potential duplicate of an existing CVE:
	1	We review the cited CVE(s) to confirm relevance.
	2	We update the advisory with an explanation of differences, if applicable.
	3	We re-request a CVE to ensure unique vulnerabilities are documented.

Acknowledgments
We thank all researchers who help secure AI_RIQA. While we don’t offer a bug bounty program, we’ll publicly acknowledge (with your consent) those who responsibly disclose vulnerabilities in release notes or a “Hall of Fame” section.

Why Security Matters
As an educational project, AI_RIQA aims to inspire learning and curiosity. Protecting users from attacks (e.g., code execution, data theft) is critical to maintaining trust among students, educators, and academic sponsors. Your security contributions strengthen this mission.
