# Collection Planning for OSINT

Collection planning is the systematic process of identifying, prioritizing, and organizing intelligence requirements to guide collection activities. This document provides a framework for OSINT collection planning based on intelligence community methodologies.

## Overview

Effective collection planning ensures:
- Resources are focused on priority requirements
- Collection activities are coordinated and efficient
- Gaps in coverage are identified and addressed
- Collection outcomes are measurable

---

## Priority Intelligence Requirements (PIRs)

### Definition

Priority Intelligence Requirements (PIRs) are the highest-priority information requirements that directly support decision-making. They represent the critical unknowns that must be answered.

### Characteristics of Good PIRs

| Characteristic | Description | Example |
|----------------|-------------|---------|
| **Specific** | Clearly defined, not vague | "Identify the beneficial owners of Company X" not "Learn about Company X" |
| **Answerable** | Can be resolved through collection | Based on available sources and methods |
| **Actionable** | Drives decisions or actions | Supports go/no-go decisions, threat response |
| **Time-bound** | Has a deadline or relevance window | "Before contract signing on [date]" |
| **Prioritized** | Ranked relative to other requirements | PIR 1, PIR 2, PIR 3 |

### PIR Development Process

```
1. Identify Decision Points
   └── What decisions will this intelligence support?

2. Define Knowledge Gaps
   └── What don't we know that we need to know?

3. Formulate Questions
   └── Convert gaps into answerable questions

4. Prioritize Requirements
   └── Rank by criticality and time-sensitivity

5. Decompose into IRs
   └── Break PIRs into specific information requirements
```

### PIR Examples

**Due Diligence Investigation:**
- PIR 1: What are the true ownership and control structures of the target entity?
- PIR 2: Are the principals involved in any criminal activity or sanctions violations?
- PIR 3: What is the financial condition and viability of the target?

**Threat Assessment:**
- PIR 1: What are the capabilities and intentions of the threat actor?
- PIR 2: What indicators suggest imminent threat activity?
- PIR 3: What vulnerabilities exist in the target environment?

**Person of Interest Investigation:**
- PIR 1: What is the subject's current location and pattern of life?
- PIR 2: Who are the subject's associates and what are those relationships?
- PIR 3: What financial resources does the subject control?

---

## Information Requirements (IRs)

### Definition

Information Requirements (IRs) are specific, discrete data points that collectively satisfy a PIR. They are the building blocks of intelligence collection.

### IR Structure

Each IR should specify:
1. **What** information is needed (the data point)
2. **About whom/what** (the target)
3. **To what level of detail** (specificity)
4. **By when** (deadline)

### Decomposing PIRs into IRs

**Example: PIR "What are the capabilities of threat actor X?"**

| IR # | Information Requirement | Collection Source |
|------|-------------------------|-------------------|
| 1.1 | Known malware families attributed to X | Threat intel databases, reports |
| 1.2 | TTPs documented for X | MITRE ATT&CK, incident reports |
| 1.3 | Infrastructure associated with X | Passive DNS, WHOIS, Shodan |
| 1.4 | Personnel associated with X | SOCMINT, leaked data |
| 1.5 | Historical operations attributed to X | News, research papers, court docs |

**Example: PIR "Who owns and controls Company Y?"**

| IR # | Information Requirement | Collection Source |
|------|-------------------------|-------------------|
| 2.1 | Registered ownership structure | Corporate registries, SEC filings |
| 2.2 | Beneficial owners | ICIJ databases, investigative reports |
| 2.3 | Board members and key officers | Annual reports, LinkedIn, news |
| 2.4 | Significant shareholders | Securities filings, proxy statements |
| 2.5 | Corporate family tree | Orbis, D&B, corporate records |

### IR Tracking Matrix

Maintain an IR tracking matrix to monitor collection progress:

| IR # | Requirement | Priority | Status | Sources Checked | Findings | Gaps |
|------|-------------|----------|--------|-----------------|----------|------|
| 1.1 | Subject DOB | High | Complete | Public records, social | 03/15/1985 | None |
| 1.2 | Subject address | High | Partial | OSINT, records | PO Box only | Physical addr needed |
| 1.3 | Associates | Medium | In Progress | SOCMINT | 3 identified | More collection needed |

---

## Source Identification and Selection

### Source Categories for OSINT

```
OSINT Source Taxonomy:
├── Public Records
│   ├── Government databases
│   ├── Court records
│   ├── Property records
│   ├── Corporate filings
│   └── Vital records
├── Media Sources
│   ├── News archives
│   ├── Broadcast media
│   ├── Podcasts
│   └── Press releases
├── Social Media
│   ├── Major platforms
│   ├── Forums and communities
│   ├── Messaging platforms
│   └── Professional networks
├── Commercial Data
│   ├── Data brokers
│   ├── Business intelligence
│   ├── Credit bureaus
│   └── Industry databases
├── Technical Sources
│   ├── Domain/DNS data
│   ├── Network infrastructure
│   ├── Code repositories
│   └── Technical documentation
├── Academic/Research
│   ├── Academic papers
│   ├── Theses and dissertations
│   ├── Conference proceedings
│   └── Patents
└── Grey Literature
    ├── Think tank reports
    ├── NGO publications
    ├── Industry reports
    └── Leaked documents
```

### Source Selection Criteria

When selecting sources, evaluate:

| Criterion | Question | Considerations |
|-----------|----------|----------------|
| **Relevance** | Does this source likely contain the needed information? | Topic coverage, subject inclusion |
| **Reliability** | Is this source trustworthy? | Track record, bias, methodology |
| **Accessibility** | Can we access this source? | Cost, authorization, technical requirements |
| **Timeliness** | Is the information current enough? | Update frequency, publication date |
| **Uniqueness** | Does this provide information not available elsewhere? | Exclusive content, unique perspective |
| **Legality** | Can we legally and ethically use this source? | Terms of service, data protection laws |

### Source Prioritization Matrix

| Source | Relevance | Reliability | Accessibility | Priority |
|--------|-----------|-------------|---------------|----------|
| SEC EDGAR | High | High | High | 1 |
| LinkedIn | High | Medium | Medium | 2 |
| News archives | Medium | Medium | High | 3 |
| Dark web forums | Medium | Low | Low | 4 |

---

## Collection Strategies for OSINT

### Strategy 1: Layered Collection

Start with the most accessible, reliable sources and progressively move to more difficult or less reliable sources.

```
Layer 1: Official Sources (Highest Reliability)
├── Government databases
├── Corporate filings
└── Official websites

Layer 2: Established Media (High Reliability)
├── Major news outlets
├── Wire services
└── Trade publications

Layer 3: Social Media (Variable Reliability)
├── Platform searches
├── Profile analysis
└── Network mapping

Layer 4: Deep Web (Lower Accessibility)
├── Subscription databases
├── Academic repositories
└── Archived content

Layer 5: Grey Sources (Lowest Reliability)
├── Forums and communities
├── Leaked data
└── Anonymous sources
```

### Strategy 2: Pivot-Based Collection

Use discovered information to identify new collection targets.

```
Initial Target → Entity Pivot → Source Expansion

Example:
Company Name → Officers identified → Personal social media → Associates → New entities
    │
    └──→ Address → Property records → Other businesses at address → Connected entities
```

### Strategy 3: Temporal Collection

Collect across time to identify patterns and changes.

```
Historical Collection:
├── Archive.org snapshots
├── Historical news
├── Old social media posts
├── Cached content
└── Document version history

Current Collection:
├── Live websites
├── Current social media
├── Recent news
└── Active databases

Prospective Collection:
├── Monitoring alerts
├── RSS feeds
├── Social media alerts
└── Website change detection
```

### Strategy 4: Multi-Modal Collection

Collect across different media types.

```
Text:
├── Written content
├── Documents
├── Transcripts
└── Chat logs

Visual:
├── Photographs
├── Videos
├── Maps
├── Infographics
└── Screenshots

Technical:
├── Code
├── Configurations
├── Metadata
├── Network data
└── Binary files

Structured Data:
├── Databases
├── Spreadsheets
├── APIs
└── Feeds
```

---

## Coverage Analysis

### Definition

Coverage analysis evaluates the extent to which collection activities have satisfied intelligence requirements and identifies gaps.

### Coverage Assessment Framework

For each PIR/IR, assess:

| Dimension | Question | Rating |
|-----------|----------|--------|
| **Completeness** | Have all aspects of the requirement been addressed? | Full / Partial / None |
| **Depth** | Is the information detailed enough? | Deep / Adequate / Shallow |
| **Breadth** | Have all relevant sources been checked? | Comprehensive / Selective / Limited |
| **Confidence** | How certain are we of the information? | High / Medium / Low |
| **Currency** | Is the information current? | Current / Dated / Stale |

### Gap Analysis

Identify and categorize collection gaps:

| Gap Type | Description | Response |
|----------|-------------|----------|
| **Source Gap** | No available source for the requirement | Alternative sources, adjust requirement |
| **Access Gap** | Source exists but cannot be accessed | Authorization, alternative access |
| **Coverage Gap** | Source checked but didn't contain information | Additional sources, refined queries |
| **Temporal Gap** | Information exists but not for required period | Archive research, witness interviews |
| **Confidence Gap** | Information exists but cannot be verified | Corroboration, source development |

### Collection Status Tracking

```
IR Collection Status:
├── GREEN: Requirement fully satisfied with high confidence
├── YELLOW: Requirement partially satisfied or moderate confidence
├── RED: Requirement unsatisfied or low confidence
└── GREY: Unable to collect (source unavailable, legal restriction)
```

### Coverage Matrix Example

| Requirement | Source 1 | Source 2 | Source 3 | Overall Status |
|-------------|----------|----------|----------|----------------|
| Subject identity | Full | Partial | N/A | GREEN |
| Current address | None | Partial | Partial | YELLOW |
| Employment history | Full | Full | Partial | GREEN |
| Criminal history | N/A | None | None | RED |
| Associates | Partial | Partial | None | YELLOW |

---

## Collection Management

### Collection Tasking

Document each collection task:

```
Collection Task Template:
┌─────────────────────────────────────────────────────┐
│ Task ID: CT-2025-001                               │
│ Requirement: IR 1.3 - Subject's current employer   │
│ Priority: High                                      │
│ Assigned: [Collector]                               │
│ Deadline: 2025-01-05                               │
│ Sources to check:                                   │
│   - LinkedIn                                        │
│   - Corporate registries                            │
│   - News articles                                   │
│   - Subject's social media                          │
│ Collection guidance:                                │
│   - Check for recent job announcements              │
│   - Look for conference appearances                 │
│   - Review corporate press releases                 │
│ OPSEC requirements: Standard (no direct contact)   │
│ Status: In Progress                                 │
└─────────────────────────────────────────────────────┘
```

### Collection Deconfliction

Avoid redundant collection and ensure coordination:
- Maintain a central collection log
- Check before tasking new collection
- Share collection findings across team
- Track which sources have been exhausted

### Collection Efficiency Metrics

Track efficiency to improve future planning:

| Metric | Calculation | Use |
|--------|-------------|-----|
| Source yield rate | Useful findings / Sources checked | Prioritize high-yield sources |
| Time to satisfaction | Hours to satisfy IR | Resource planning |
| Gap rate | Unsatisfied IRs / Total IRs | Process improvement |
| Redundancy rate | Duplicate findings / Total findings | Deconfliction improvement |

---

## Collection Plan Template

```markdown
# Collection Plan

## 1. Intelligence Problem Statement
[Clear statement of what we're trying to understand]

## 2. Priority Intelligence Requirements (PIRs)
1. [PIR 1]
2. [PIR 2]
3. [PIR 3]

## 3. Information Requirements Matrix
| PIR | IR | Specific Requirement | Priority | Deadline |
|-----|-----|---------------------|----------|----------|
| 1 | 1.1 | [Requirement] | High | [Date] |
| 1 | 1.2 | [Requirement] | Medium | [Date] |
| 2 | 2.1 | [Requirement] | High | [Date] |

## 4. Source Plan
| IR | Primary Sources | Secondary Sources | Notes |
|-----|----------------|-------------------|-------|
| 1.1 | [Sources] | [Sources] | [Notes] |
| 1.2 | [Sources] | [Sources] | [Notes] |

## 5. Collection Strategy
[Description of collection approach]

## 6. Timeline
- Phase 1: [Dates] - Initial collection
- Phase 2: [Dates] - Deep dive
- Phase 3: [Dates] - Gap filling

## 7. Resource Requirements
- Personnel: [Requirements]
- Tools: [Requirements]
- Access: [Requirements]

## 8. OPSEC Considerations
[Operational security requirements]

## 9. Legal/Ethical Boundaries
[What collection is in/out of scope]

## 10. Reporting Requirements
[How and when to report collection results]
```

---

## References

### Primary Sources (PDF Library)

- [FM 34-2 Collection Management and Synchronization Planning](../references/pdf-library-index.md)
- [FM 34-3 Intelligence Analysis](../references/pdf-library-index.md)
- [Joint Analysis Handbook](../references/pdf-library-index.md)
- [TII Online Research Framework](../references/pdf-library-index.md)

### Related Documentation

- [intelligence-cycle.md](intelligence-cycle.md) - Overall intelligence process
- [source-evaluation.md](source-evaluation.md) - Evaluating collected information
- [analysis-techniques.md](analysis-techniques.md) - Analyzing collected data

---

*Document Version: 1.0*
*Last Updated: 2025-12-28*
*Status: Active*
