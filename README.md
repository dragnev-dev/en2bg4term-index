# en2bg4term-index

The search index behind en2bg4term dataset enrichment workflow. It pulls terms from about twenty sources (the Python glossary, MITRE CWE, MDN, IATE, Wiktionary and others) into one SQLite file with full-text search.

## Quick start

```sh
uv sync
uv run idx build --source python_glossary --source mitre_cwe
uv run idx query decorator
uv run pytest
```

To skip building, `uv run idx fetch --dest dl` downloads the latest published index.

## Using it as a library

```sh
uv add "en2bg4term-index @ git+https://github.com/dragnev-dev/en2bg4term-index@lib-v0.3.0"
```

```python
from en2bg4term_index import download_release, load_providers

index = download_release("dl")
with load_providers(index) as registry:
    hits = registry.search_all("firewall", translation="защитна стена")
```

Some sources (Wikidata, W3C, EUR-Lex, LexIT) aren't in the index and are queried live. Pass `live=False` to `load_providers` to keep everything offline. The public interface is defined in `contract.py`.

Library versions are tagged `lib-vX.Y.Z`. Data releases are tagged `index-YYYYMMDD`.

## Nightly refresh

Every night a GitHub Action (`.github/workflows/refresh.yml`) rebuilds the sources that are due and publishes a new release. If a source fails or its new data looks wrong, the previous version is kept, and an issue is opened if the problem doesn't go away on its own.

Each step is a normal `idx` command (`plan`, `shard`, `assemble`), so you can run the whole thing locally.

## Adding a source

1. Add `sources/<id>.yaml`.
2. Write `src/en2bg4term_index/ingest/<id>.py` with `fetch()` and `parse()`, and register it in `ingest/__init__.py`.
3. Add a fixture to `tests/fixtures/` so `parse()` can be tested without the network.

If you change `normalize.py`, bump `NORM_VERSION`. If you change `schema.sql`, bump `SCHEMA_VERSION` in `model.py`.
