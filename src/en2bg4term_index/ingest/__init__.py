"""Source adapters: one module per source id."""

from importlib import import_module

from en2bg4term_index.ingest.base import Adapter
from en2bg4term_index.model import Source

ADAPTERS = {
    "cncf_glossary": "en2bg4term_index.ingest.cncf_glossary:CncfGlossary",
    "ecma262": "en2bg4term_index.ingest.ecma262:Ecma262",
    "etymonline": "en2bg4term_index.ingest.etymonline:Etymonline",
    "eom": "en2bg4term_index.ingest.eom:Eom",
    "eurovoc": "en2bg4term_index.ingest.eurovoc:Eurovoc",
    "git_glossary": "en2bg4term_index.ingest.git_glossary:GitGlossary",
    "google_ml": "en2bg4term_index.ingest.google_ml:GoogleMl",
    "iate": "en2bg4term_index.ingest.iate:Iate",
    "mdn": "en2bg4term_index.ingest.mdn:Mdn",
    "mitre_cwe": "en2bg4term_index.ingest.mitre_cwe:MitreCwe",
    "nist_csrc": "en2bg4term_index.ingest.nist_csrc:NistCsrc",
    "nist_dads": "en2bg4term_index.ingest.nist_dads:NistDads",
    "owasp_cheatsheets": "en2bg4term_index.ingest.owasp_cheatsheets:OwaspCheatsheets",
    "owasp_genai": "en2bg4term_index.ingest.owasp_genai:OwaspGenai",
    "postgresql_glossary": "en2bg4term_index.ingest.postgresql_glossary:PostgresqlGlossary",
    "python_glossary": "en2bg4term_index.ingest.python_glossary:PythonGlossary",
    "rfc_editor": "en2bg4term_index.ingest.rfc_editor:RfcEditor",
    "unicode_glossary": "en2bg4term_index.ingest.unicode_glossary:UnicodeGlossary",
    "webref": "en2bg4term_index.ingest.webref:Webref",
    "wiktionary": "en2bg4term_index.ingest.wiktionary:Wiktionary",
}


def get_adapter(source: Source) -> Adapter:
    try:
        target = ADAPTERS[source.id]
    except KeyError:
        raise LookupError(f"no adapter for source {source.id!r}") from None
    module, _, name = target.partition(":")
    return getattr(import_module(module), name)(source)
