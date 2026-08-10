# Design: Interview Prep Tренажёр (AQA Python + pytest)

**Date:** 2026-08-03  
**Status:** Approved in chat (sections 1–2); awaiting file review  
**Learner:** AQA, ~3y manual / ~1.5y auto; recent half-year heavy AI use → weak hands-on Python  
**Goal:** ASAP readiness for AQA interview (Python + pytest + API layers), then deeper practice

---

## 1. Problem

Repo `tbank-AQAtraining` currently holds algorithmic contest-style drills (`tasks_tbank/`), not AQA interview practice. Learner needs:

1. Pure Python without AI crutches (main weakness)
2. Pytest fluency (fixtures, parametrize, marks, conftest)
3. API test framework layers matching prior job stack (`BaseApi` + helpers + checks + Allure)
4. Pointed algorithm tasks typical for livecoding screens
5. Gate: finish current block before next; coach reviews until pass

## 2. Approach

**Interview Sprint (hybrid tracks):**

| Track | Content | Exercise format |
|-------|---------|-----------------|
| A. Python Core | utils + easy algos | Failing pytest provided → learner writes `solution.py` |
| B. AQA Craft | pytest → BaseApi → layers → Allure | Skeleton + acceptance criteria → learner writes code & tests; coach reviews |

**Week 0** optimizes for “interview in ~7 days”. Later folders deepen the same tracks.

**Anti-AI rule:** no pasting full task/tests into generative AI for solutions. Stuck protocol: ask coach (hint ladder), official docs, REPL experiments, concept search — not “solve my TASK.md”.

## 3. Repository layout

Keep `tasks_tbank/` as archive. New tree:

```
interview_prep/
  README.md
  PROGRESS.md
  resources.md
  requirements.txt          # pytest, requests, allure-pytest (week0+)
  pytest.ini
  00_week0_sprint/
    01_python_freq_dupes_reverse/
    02_python_two_sum/
    03_pytest_craft/
    04_mini_api_framework/
    05_interview_voice/
  01_python_core/           # post-week0 deepening
  02_pytest_craft/
  03_api_framework/
  04_interview_theory/
```

`tasks_tbank/` is not modified by this plan.

## 4. Week 0 blocks (strict order)

| ID | Block | Learner delivers | Done when |
|----|-------|------------------|-----------|
| 0.1 | Frequencies / duplicates / reverse | `solution.py` | All provided tests pass |
| 0.2 | Two Sum (brute + dict) | `solution.py` | Tests pass; can explain O(n) vs O(n²) |
| 0.3 | Pytest craft | Tests for a small utility: fixture, parametrize, mark | Coach review OK |
| 0.4 | Mini API framework | `BaseApi` + one API module + helper + checks + Allure steps + 2–3 tests against **jsonplaceholder.typicode.com** (httpbin optional for status/edge drills) | Tests green; layering matches prior job style |
| 0.5 | Interview voice | Written answers to 8–10 typical questions | Coach review of wording OK |

**Progress gate:** only one active block; mark complete in `PROGRESS.md` after coach sign-off.

## 5. Task file conventions

### Track A (Python) — per exercise folder

```
TASK.md           # condition, constraints, hints ladder (optional spoilers folded)
solution.py       # stubs / NotImplemented — LEARNER FILLS
test_solution.py  # provided by coach — LEARNER DOES NOT EDIT (unless asked)
```

### Track B (AQA) — per exercise folder

```
TASK.md           # acceptance criteria, required layers, public API target
src/              # skeleton packages (api, helper, checks, …)
tests/            # maybe empty or one failing smoke — LEARNER expands
conftest.py       # optional starter
```

### Review loop

1. Learner: “готово” + how to run tests  
2. Coach: run/review, list concrete fixes  
3. Repeat until pass → update `PROGRESS.md` → open next block only

## 6. Tech stack (training mirror of prior job)

Prior job reference: `e2e-api-tests-actual-dbs` — `requests` + `BaseApi`, helpers, checks, pytest fixtures, Allure, poetry/ruff optional.

Training stack (minimal Week 0):

- Python 3.12+
- pytest
- requests
- allure-pytest / allure-python-commons (from block 0.4)

No corporate secrets, no internal mocks required in Week 0. Public APIs only.

## 7. Stuck protocol (explicit)

**Allowed:** coach hints (nudge → direction → near-spoiler), docs.python.org, docs.pytest.org, REPL, concept-only web search.

**Forbidden:** paste full `TASK.md` / test file into ChatGPT/Cursor Agent asking for the solution.

**Grey:** line autocomplete OK; “generate whole function from task docstring” not OK.

## 8. External resources (also in `resources.md`)

**Structured paths**

- https://github.com/Deehlusa/cs50-python — Python → pytest → Playwright/API 60-day path  
- https://github.com/Caliquende/python-test-automation-training-projects — API + UI + CI practice  
- https://github.com/vitaliiyz/aqa_python — Playwright + pytest + POM example  

**Practice sites**

- https://exercism.org/tracks/python — Python + pytest exercises (incl. REST API kata)  
- https://docs.pytest.org/en/stable/ — primary pytest reference  
- https://httpbin.org / https://jsonplaceholder.typicode.com — public HTTP targets  

**Algo warm-up (secondary)**

- Keep using existing `tasks_tbank/` after Week 0.1–0.2 if more reps needed  
- LeetCode Easy: Two Sum, Valid Anagram, Contains Duplicate (optional)

## 9. Out of scope (Week 0)

- Playwright/Selenium UI  
- Real fintech env / DB fixtures from old job  
- Full CI/CD setup (can add post-week0)  
- JS mocker  
- Committing secrets or copying proprietary test data  

## 10. Success criteria

**After Week 0:**

- Can solve 0.1–0.2 without AI paste  
- Can explain and write fixture / parametrize / mark  
- Can sketch `BaseApi` + helper + check + Allure step verbally and in code  
- Has short spoken/written answers for common AQA interview questions  

**Ongoing:** deeper folders unlocked only after coach sign-off on prior block.

## 11. Implementation next steps

1. User approves this spec file  
2. Write implementation plan under `docs/superpowers/plans/`  
3. Scaffold `interview_prep/` + block **0.1** files only  
4. Learner starts 0.1; coach reviews until green  
5. Unlock 0.2 … sequentially  
