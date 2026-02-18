# QA Report: AutoDocGen

**Generated:** 2026-02-18 13:57 UTC

**Persona:** indie-hacker
**Winning Stack:** Python + asyncio + Redis + Celery

## Triple-AI Review Findings

### src/main.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
⚠️ Pass 3 (Perplexity): FAIL — 5 issues
  · `await startup_tasks()` called in synchronous `main()` function without event loop, causing runtime error.
  · Celery worker started with `--without-mingle`, `--without-gossip`, `--without-heartbeat` which disables important coordination features, risking task duplication and instability.
  · Broad `except Exception` catches all errors masking specific issues; lacks targeted exception handling.

### src/config.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
⚠️ Pass 3 (Perplexity): WARN — 5 issues
  · Secrets exposed in __str__ and __repr__ methods: While github_token is masked, redis_url and celery_broker_url may contain credentials and should also be redacted
  · Missing schema validation: No validation that environment variables contain valid URLs or proper formats before storing them
  · Generic exception handling: Catching all Exception types masks specific errors and makes debugging difficult; should catch KeyError specifically

### src/api.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
✅ Pass 3 (Perplexity): Validated

### src/models.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
⚠️ Pass 3 (Perplexity): FAIL — 6 issues
  · create_user() and create_project() catch Exception which is too broad - dataclasses cannot fail instantiation with valid types, making try/except unnecessary and masking real errors
  · validate_user_data() and validate_project_data() are defined but never called in create functions, allowing invalid data to create User/Project instances
  · User/Project dataclasses lack validation; type hints provide no runtime enforcement (dataclasses don't validate types at runtime)

### src/tasks.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
⚠️ Pass 3 (Perplexity): FAIL — 10 issues
  · Tasks decorated as `@app.task` but defined as `async def` - Celery does not natively support async tasks without additional configuration (e.g., `celery[asyncio]`, eventlet/gevent)[4]
  · Missing Celery security configuration - no `task_serializer='auth'`, `accept_content=['auth']`, or `app.setup_security()` calls exposing tasks to message injection attacks[1]
  · No retry configuration - missing `max_retries`, `retry_backoff`, `autoretry_for` leading to potential infinite retries or no retries on transient failures[2][5][6]

### src/templates.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
✅ Pass 3 (Perplexity): Validated

### src/github.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
⚠️ Pass 3 (Perplexity): FAIL — 7 issues
  · Placeholder/simulated API calls instead of actual HTTP requests or PyGithub implementation - lacks real functionality
  · No rate limiting handling or API usage monitoring despite GitHub API limits
  · Broad exception catching without specific error handling for GitHub API errors (401, 403, 404, rate limits)

### src/gitlab.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
✅ Pass 3 (Perplexity): Validated

### src/utils.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
⚠️ Pass 3 (Perplexity): FAIL — 5 issues
  · Logger created with logging.getLogger(__name__) but no configuration (no handlers, level, or format set); logs may not appear or be formatted properly[3][4]
  · save_json_file catches broad Exception instead of specific IO exceptions (OSError, PermissionError), masking errors[3]
  · camel_case_to_snake_case fails on non-alphanumeric characters (e.g., 'HTTPResponse' becomes 'h_t_t_p_response' instead of 'http_response')[3]

### src/redis.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
⚠️ Pass 3 (Perplexity): FAIL — 5 issues
  · No connection pooling: Creating individual Redis connections without pooling causes overhead from repeated connection/disconnection cycles
  · Lazy connection initialization: The get(), set(), and publish() methods attempt to connect if self.client is None, but this bypasses the explicit connect() method and can cause unexpected reconnection behavior
  · Missing TTL support: The set() method lacks TTL (time-to-live) parameters, violating best practice of setting expiration times to prevent stale data accumulation

### src/parser.py
✅ Pass 2 (Secondary AI): Code reviewed and improved
⚠️ Pass 3 (Perplexity): FAIL — 6 issues
  · Incomplete AST parsing: only extracts top-level imports and functions, missing nested definitions, classes, and other constructs
  · No validation of parsed elements (e.g., dangerous imports like 'os', 'subprocess', 'exec')
  · No limits on code size or AST depth, vulnerable to DoS via stack overflow or memory exhaustion[1][4]