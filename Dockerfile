FROM agrigorev/zoomcamp-model:2025

# FROM python:3.13.5-slim-bookworm
# WORKDIR /code
# COPY pipeline_v2.bin .
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY ".python-version" "pyproject.toml" "uv.lock" "./"
RUN uv sync --locked

COPY "webservice4.py" "./"
# "pipeline_v2.bin"

EXPOSE 9697

ENTRYPOINT ["uvicorn", "webservice4:app", "--host", "0.0.0.0", "--port", "9697"]