# OSINT Knowledge Base

This knowledge folder contains structured documentation for Open Source Intelligence (OSINT) methodology, techniques, tradecraft, and reference materials.

## Directory Structure

```
knowledge/
├── README.md                    # This file
├── methodology/                 # OSINT workflows and processes
├── techniques/                  # Investigation techniques
├── references/                  # Reference materials and PDF index
├── tradecraft/                  # Intelligence tradecraft
└── reporting/                   # Documentation templates
```

## Status Overview

| Directory | Status | Description |
|-----------|--------|-------------|
| methodology/ | Planned | Intelligence cycle, collection planning, analysis |
| techniques/ | Planned | Data correlation, identity resolution, attribution |
| references/ | In Progress | PDF library index, glossary |
| tradecraft/ | Planned | Analytical thinking, cognitive biases, writing standards |
| reporting/ | Planned | Report templates, assessment formats |

## Relationship to Existing Content

This knowledge folder complements the existing mdBook documentation in `../src/`:

- **mdBook (`../src/`)**: Comprehensive tool listings organized by category (3,000+ OSINT tools)
- **Knowledge (`./`)**: Methodology, tradecraft, and structured reference materials

The mdBook content is preserved intact. This knowledge folder provides:
1. Process-oriented documentation (how to conduct OSINT)
2. Tradecraft guidance (analytical techniques from intelligence community)
3. Reference materials (PDF library indexing, glossaries)

## PDF Library Integration

The `../pdfs/` folder contains 80 curated intelligence manuals and reference documents. These are indexed in [references/pdf-library-index.md](references/pdf-library-index.md) and serve as primary sources for tradecraft documentation.

## Tools Documentation

Tools documentation is intentionally deferred due to complexity:
- 3,000+ tools documented in mdBook
- Most are web-based (not traditional CLI tools)
- Require specialized three-tier documentation approach

See `../TMP.md` for details on the tools documentation strategy.

## Related Repositories

This knowledge base is part of a multi-repository ecosystem:
- `~/pwnbox` - Network penetration testing and Active Directory
- `~/webbox` - Web application security
- `~/revbox` - Reverse engineering
- `~/system_docs` - Central documentation and automation scripts
