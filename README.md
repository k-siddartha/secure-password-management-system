# 🔐 Secure Password Management System – Deployment & Demo

> **A two-part portfolio project:**  
> 1. **Deployment** of a production-grade password manager (Vaultwarden) with MFA, RBAC, and secure remote access.  
> 2. **Custom Python scripts** demonstrating my understanding of bcrypt, AES-256, and TOTP-based MFA.

---

## 📌 Overview

This repository documents the **complete setup** of a self-hosted, enterprise-ready password management system, including:

- ✅ AES-256 encryption (end-to-end)
- ✅ Multi-Factor Authentication (TOTP)
- ✅ Role-Based Access Control (Admin vs User)
- ✅ Encrypted backups & disaster recovery
- ✅ Cross-platform access via Cloudflare Tunnel
- ✅ Monitoring & audit logging

Additionally, I wrote **custom Python code** to prove I understand *how* these security features work under the hood.

---

## 🧪 Custom Security Implementations (My Code)

To demonstrate that I don't just *configure* security tools — but understand the underlying cryptography — I wrote a Python script that implements:

| Concept | Implementation |
|---------|----------------|
| **Password Hashing** | bcrypt with unique salts |
| **Symmetric Encryption** | AES-256 (via Fernet) |
| **Multi-Factor Authentication** | TOTP (RFC 6238) |

📁 **File:** [`src/security_demo.py`](src/security_demo.py)

### Run my custom demo:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the demo
python src/security_demo.py
