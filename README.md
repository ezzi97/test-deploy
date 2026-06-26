# Test Deploy — Monorepo Demo

A minimal monorepo demonstrating:
- **GitHub** — code versioning & CI
- **Vercel** — static frontend hosting
- **Railway** — serverless API (FastAPI)

## Structure

```
├── frontend/          → Deployed on Vercel
│   ├── index.html
│   ├── style.css
│   └── vercel.json
├── api/               → Deployed on Railway
│   ├── main.py        (FastAPI)
│   └── requirements.txt
└── .github/workflows/
    └── ci.yml         → GitHub Actions CI
```

## Endpoints (API)

- `GET /health` — health check with version + timestamp
- `GET /` — root info
- `GET /docs` — auto-generated Swagger docs

## Deploy

Push to `main` — both Vercel and Railway auto-deploy via GitHub integration.
