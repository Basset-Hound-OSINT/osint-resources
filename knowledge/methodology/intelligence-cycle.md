# The Intelligence Cycle for OSINT

The intelligence cycle is a systematic process for transforming raw information into actionable intelligence. This document adapts the traditional intelligence cycle for Open Source Intelligence (OSINT) operations.

## Overview

The intelligence cycle consists of six interconnected phases:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│    ┌──────────┐     ┌────────────┐     ┌───────────┐   │
│    │Direction │ ──► │ Collection │ ──► │Processing │   │
│    │/Planning │     │            │     │           │   │
│    └──────────┘     └────────────┘     └───────────┘   │
│         ▲                                    │         │
│         │                                    ▼         │
│    ┌──────────┐     ┌────────────┐     ┌───────────┐   │
│    │ Feedback │ ◄── │Disseminat- │ ◄── │ Analysis  │   │
│    │          │     │   ion      │     │           │   │
│    └──────────┘     └────────────┘     └───────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Phase 1: Direction/Planning

### Traditional Definition

Direction establishes intelligence requirements, priorities, and the scope of collection activities. This phase translates decision-maker needs into specific intelligence requirements.

### OSINT Adaptation

In OSINT operations, direction often comes from:
- Client requirements or case intake
- Research questions or hypotheses
- Investigative leads requiring development
- Threat assessment requirements
- Due diligence scope definitions

### Key Activities

1. **Define the Intelligence Problem**
   - What decisions will this intelligence support?
   - What are the knowledge gaps?
   - What is the operational context?

2. **Establish Priority Intelligence Requirements (PIRs)**
   - Critical information needed to answer the core question
   - Time-sensitive requirements
   - See [collection-planning.md](collection-planning.md) for detailed PIR development

3. **Develop Information Requirements (IRs)**
   - Specific data points that satisfy PIRs
   - Observable indicators and signatures
   - Collection indicators

4. **Resource Allocation**
   - Available tools and platforms
   - Time constraints
   - Personnel and expertise
   - Legal and ethical boundaries

### OSINT-Specific Considerations

| Traditional Intel | OSINT Equivalent |
|-------------------|------------------|
| National security priorities | Investigation objectives |
| Commander's Critical Information Requirements (CCIRs) | Client requirements, case parameters |
| Collection assets (HUMINT, SIGINT, etc.) | OSINT sources (social media, databases, public records) |
| Classification levels | Sensitivity handling, PII considerations |

### Planning Deliverables

- [ ] Clear statement of intelligence problem
- [ ] Prioritized list of PIRs and IRs
- [ ] Collection plan with source identification
- [ ] Timeline and milestones
- [ ] Legal/ethical boundaries documented

---

## Phase 2: Collection

### Traditional Definition

Collection is the gathering of raw information from various sources using appropriate collection disciplines (HUMINT, SIGINT, IMINT, OSINT, etc.).

### OSINT Adaptation

OSINT collection leverages publicly available information from:
- **Surface Web**: Search engines, websites, news archives
- **Deep Web**: Databases, subscription services, academic repositories
- **Social Media**: Platforms, forums, messaging apps
- **Public Records**: Government databases, court records, corporate filings
- **Multimedia**: Images, videos, audio, documents
- **Technical Sources**: WHOIS, DNS, network infrastructure

### Collection Disciplines within OSINT

| Discipline | Description | Examples |
|------------|-------------|----------|
| **SOCMINT** | Social Media Intelligence | Twitter/X, Facebook, LinkedIn, Instagram |
| **GEOINT** | Geospatial Intelligence | Google Earth, Sentinel Hub, mapping platforms |
| **FININT** | Financial Intelligence | SEC filings, corporate records, sanctions lists |
| **CYBINT** | Cyber Intelligence | Shodan, VirusTotal, breach databases |
| **DOCINT** | Document Intelligence | Academic papers, leaked documents, public filings |

### Collection Best Practices

1. **Operational Security (OPSEC)**
   - Use appropriate personas and accounts
   - Employ VPNs and anonymization when needed
   - Avoid alerting targets to collection activities

2. **Documentation**
   - Preserve original sources (archive, screenshot, hash)
   - Record collection timestamps (UTC preferred)
   - Maintain chain of custody documentation
   - Log URLs and access methods

3. **Systematic Approach**
   - Work from collection plan
   - Track coverage gaps
   - Avoid redundant collection
   - Note negative findings (absence of evidence)

### Collection Techniques

```
Primary Collection Methods:
├── Passive Collection
│   ├── Search engine queries
│   ├── Website monitoring
│   ├── RSS/news aggregation
│   └── Database queries
├── Active Collection
│   ├── Account creation for access
│   ├── Direct platform queries
│   ├── API utilization
│   └── Social engineering (within legal bounds)
└── Technical Collection
    ├── DNS/WHOIS enumeration
    ├── Certificate transparency logs
    ├── Metadata extraction
    └── Infrastructure mapping
```

---

## Phase 3: Processing

### Traditional Definition

Processing converts collected information into a form suitable for analysis. This includes translation, decryption, interpretation, and organization.

### OSINT Adaptation

OSINT processing focuses on:
- **Data normalization**: Converting diverse formats to analyzable structures
- **Deduplication**: Removing redundant information
- **Enrichment**: Adding context and metadata
- **Organization**: Structuring data for analysis

### Processing Activities

1. **Format Conversion**
   - Extract text from images (OCR)
   - Transcribe audio/video content
   - Convert proprietary formats
   - Parse structured data (JSON, XML, CSV)

2. **Data Cleaning**
   - Remove duplicates
   - Standardize naming conventions
   - Normalize timestamps and locations
   - Handle encoding issues

3. **Metadata Extraction**
   - EXIF data from images
   - Document properties (author, creation date)
   - Email headers
   - File hashes

4. **Data Structuring**
   - Entity extraction (people, organizations, locations)
   - Relationship mapping
   - Timeline organization
   - Categorization and tagging

### Processing Tools and Techniques

| Task | Tools/Approaches |
|------|------------------|
| OCR | Tesseract, Google Vision, Adobe |
| Metadata | ExifTool, FOCA, Metagoofil |
| Translation | DeepL, Google Translate, native speakers |
| Data normalization | Python/Pandas, OpenRefine |
| Entity extraction | spaCy, Stanford NER, manual review |

### Quality Control

- Verify processing accuracy
- Document any data transformations
- Preserve original data alongside processed versions
- Flag uncertain interpretations

---

## Phase 4: Analysis

### Traditional Definition

Analysis is the conversion of processed information into finished intelligence through evaluation, integration, interpretation, and assessment.

### OSINT Adaptation

OSINT analysis applies structured analytic techniques to:
- Establish facts and assess reliability
- Identify patterns and relationships
- Develop hypotheses and test them
- Draw conclusions and assess confidence
- Identify intelligence gaps

### Analytic Approaches

1. **Descriptive Analysis**
   - What happened?
   - Who is involved?
   - Where and when did events occur?

2. **Explanatory Analysis**
   - Why did this happen?
   - What are the causal relationships?
   - What factors influenced outcomes?

3. **Predictive Analysis**
   - What is likely to happen next?
   - What are the indicators to monitor?
   - What scenarios are possible?

### Structured Analytic Techniques (SATs)

See [analysis-techniques.md](analysis-techniques.md) for detailed SAT guidance.

Key techniques for OSINT:
- **Analysis of Competing Hypotheses (ACH)**: Systematic hypothesis evaluation
- **Link Analysis**: Relationship mapping and network analysis
- **Timeline Analysis**: Chronological event sequencing
- **Pattern Analysis**: Identifying recurring behaviors or indicators
- **Red Team Analysis**: Adversarial perspective taking

### Analytic Standards (ICD 203)

Intelligence Community Directive 203 establishes analytic standards:
1. **Objectivity**: Analysis must be independent of political considerations
2. **Independent of political consideration**: Not shaped to support policy
3. **Timeliness**: Responsive to intelligence requirements
4. **Based on all available sources**: Integrate diverse sources
5. **Properly describe quality and reliability**: Transparent sourcing
6. **Properly express uncertainty**: Use standardized confidence language
7. **Properly distinguish between underlying intelligence and assumptions**
8. **Incorporate alternative analysis where appropriate**
9. **Demonstrate relevance and address implications**

### Source Evaluation During Analysis

See [source-evaluation.md](source-evaluation.md) for the complete evaluation framework.

Apply the Admiralty/NATO system:
- Source Reliability (A-F scale)
- Information Credibility (1-6 scale)

---

## Phase 5: Dissemination

### Traditional Definition

Dissemination is the delivery of finished intelligence to consumers in an appropriate format and through appropriate channels.

### OSINT Adaptation

OSINT dissemination considers:
- **Audience needs**: Technical vs. executive consumers
- **Format requirements**: Written reports, briefings, databases
- **Sensitivity handling**: PII, operational details, sources
- **Timeliness**: Urgent vs. scheduled delivery
- **Feedback mechanisms**: Enable consumer response

### Dissemination Products

| Product Type | Description | Audience |
|--------------|-------------|----------|
| Intelligence Summary | Brief overview of key findings | Executives, decision-makers |
| Analytical Report | Detailed analysis with sourcing | Analysts, investigators |
| Target Package | Comprehensive subject dossier | Operations, investigations |
| Indicator List | Observable signatures for monitoring | Defensive teams, watchers |
| Raw Intelligence | Minimally processed collection | Other analysts |
| Briefing | Oral presentation with visuals | Varied audiences |

### Report Components

A complete intelligence product includes:
1. **Bottom Line Up Front (BLUF)**: Key findings and implications
2. **Background**: Context and scope
3. **Analysis**: Findings with supporting evidence
4. **Source Attribution**: Reliability and credibility assessments
5. **Confidence Assessment**: Analytical confidence and gaps
6. **Implications**: What this means for the consumer
7. **Recommendations**: Suggested actions (if appropriate)

### Dissemination Considerations

- **Need to Know**: Who requires this intelligence?
- **Sensitivity**: What handling caveats apply?
- **Timeliness**: When does the consumer need it?
- **Format**: How does the consumer prefer to receive intelligence?
- **Feedback Channel**: How can consumers provide feedback?

See [../reporting/](../reporting/) for report templates and standards.

---

## Phase 6: Feedback

### Traditional Definition

Feedback is the evaluation of intelligence by consumers and the communication of their assessments back to the intelligence organization.

### OSINT Adaptation

OSINT feedback loops enable:
- Validation of intelligence accuracy
- Identification of new requirements
- Refinement of collection strategies
- Process improvement

### Feedback Mechanisms

1. **Formal Feedback**
   - Post-operation assessments
   - Customer satisfaction surveys
   - Accuracy tracking
   - Requirement validation sessions

2. **Informal Feedback**
   - Direct communication with consumers
   - Follow-up queries
   - Observed usage patterns

3. **Self-Assessment**
   - Track prediction accuracy
   - Review closed cases
   - Conduct lessons learned

### Feedback Integration

Feedback should inform:
- **Direction**: Refined intelligence requirements
- **Collection**: Adjusted source priorities
- **Processing**: Improved data handling
- **Analysis**: Enhanced techniques and rigor
- **Dissemination**: Better products and delivery

### Continuous Improvement

```
Feedback Loop Questions:
├── Was the intelligence accurate?
├── Was it timely?
├── Was it useful for decision-making?
├── What was missing?
├── What could be improved?
└── What new requirements emerged?
```

---

## OSINT Cycle Variations

### Accelerated Cycle

For time-sensitive OSINT operations:
- Compressed planning (minutes to hours)
- Parallel collection and processing
- Real-time analysis
- Immediate verbal dissemination
- Continuous feedback integration

### Research Cycle

For in-depth OSINT research:
- Extended planning with thorough scoping
- Systematic, comprehensive collection
- Rigorous processing and verification
- Deep analysis with multiple techniques
- Formal written products
- Structured feedback and validation

### Monitoring Cycle

For ongoing OSINT monitoring:
- Standing requirements
- Automated collection
- Alerting-based processing
- Exception-based analysis
- Periodic reporting
- Requirement refresh cycles

---

## References

### Primary Sources (PDF Library)

- [FM 34-1 Intelligence and Electronic Warfare Operations](../references/pdf-library-index.md) - Foundational intelligence doctrine
- [FM 2-0 Intelligence](../references/pdf-library-index.md) - Army intelligence operations
- [ICD 203 Analytic Standards](../references/pdf-library-index.md) - IC analytic standards
- [Joint Analysis Handbook](../references/pdf-library-index.md) - Multi-agency analysis guidance

### Related Documentation

- [collection-planning.md](collection-planning.md) - Detailed collection planning guidance
- [source-evaluation.md](source-evaluation.md) - Source and information assessment
- [analysis-techniques.md](analysis-techniques.md) - Structured Analytic Techniques
- [verification-methods.md](verification-methods.md) - Verification and corroboration

---

*Document Version: 1.0*
*Last Updated: 2025-12-28*
*Status: Active*
