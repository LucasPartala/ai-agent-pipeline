# Autonomous AI Lead Scoring & Dispatch Pipeline

An asynchronous Python pipeline that ingests raw business leads, evaluates high-value opportunities using LLM semantic scoring (Gemini / Claude / GPT), and dispatches qualified leads to CRM webhooks.

---

## ⚡ Architecture Flow

```
[ Raw Scraped Leads ]
         │
         ▼
[ Ingestion & Normalization ]
         │
         ▼
[ LLM Semantic Scoring Engine ] ──► (Evaluates website, rating, reviews & opportunity potential)
         │
         ▼
[ Decision Gate: Score >= 7.5 ]
      ├─── Yes ──► [ Trigger Webhook Dispatch ] ──► (Slack / WhatsApp / CRM)
      └─── No  ──► [ Archive to PostgreSQL ]
```

---

## 🛠️ Tech Stack

- **Python 3.10+ (Asyncio)**
- **LLM Prompt Engineering (Gemini / Claude / OpenAI API)**
- **Pydantic & Dataclasses** (Strict schema validation)
- **Webhooks & HTTP Dispatch**

---

## 🚀 Usage

```bash
# Clone the repository
git clone https://github.com/your-username/ai-agent-pipeline.git
cd ai-agent-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the agent pipeline
python agent.py
```
