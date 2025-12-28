# Analysis Techniques for OSINT

Structured Analytic Techniques (SATs) are systematic methods designed to improve the quality of analysis by making reasoning transparent, challenging assumptions, and reducing cognitive biases. This document covers the primary analytical techniques used in intelligence analysis, adapted for OSINT operations.

## Overview

Analysis is the process of transforming raw information into finished intelligence through:
- Evaluation of evidence
- Integration of multiple sources
- Interpretation of meaning
- Development of judgments
- Assessment of confidence

Structured techniques provide rigor and transparency to this process.

---

## Categories of Analytic Techniques

```
Structured Analytic Techniques:
├── Diagnostic Techniques
│   ├── Key Assumptions Check
│   ├── Quality of Information Check
│   ├── Indicators and Signposts
│   └── Analysis of Competing Hypotheses (ACH)
├── Contrarian Techniques
│   ├── Devil's Advocacy
│   ├── Red Team Analysis
│   ├── "What If?" Analysis
│   └── High-Impact/Low-Probability Analysis
├── Imaginative Techniques
│   ├── Brainstorming
│   ├── Structured Brainstorming
│   ├── Scenario Analysis
│   └── Indicators Generation
└── Data Organization Techniques
    ├── Link Analysis
    ├── Timeline Analysis
    ├── Pattern Analysis
    ├── Matrix Analysis
    └── Geospatial Analysis
```

---

## Diagnostic Techniques

### Key Assumptions Check

**Purpose**: Identify and evaluate the assumptions underlying analysis.

**When to Use**:
- At the start of major analytical efforts
- When analysis may be influenced by implicit assumptions
- When previous judgments need reassessment

**Process**:

1. **List all assumptions**
   - What are we taking for granted?
   - What conditions must be true for our analysis to be valid?

2. **Categorize assumptions**
   - Evidentiary (based on evidence)
   - Logical (based on reasoning)
   - Contextual (based on background knowledge)

3. **Evaluate each assumption**

| Assumption | Evidence For | Evidence Against | Confidence | If Wrong, Impact |
|------------|--------------|------------------|------------|------------------|
| [Assumption 1] | [Evidence] | [Evidence] | High/Med/Low | High/Med/Low |
| [Assumption 2] | [Evidence] | [Evidence] | High/Med/Low | High/Med/Low |

4. **Challenge high-impact, low-confidence assumptions**
   - Seek additional evidence
   - Consider alternatives
   - Adjust conclusions if necessary

**Example (OSINT Context)**:
- Assumption: "The social media account belongs to the target"
- Evidence For: Name match, location match, friend connections
- Evidence Against: Common name, no verified badge
- Impact if Wrong: High - entire analysis could be about wrong person

### Quality of Information Check

**Purpose**: Systematically evaluate the quality of underlying information before drawing conclusions.

**Process**:

1. **Inventory sources**
   - List all sources used in analysis
   - Categorize by type and origin

2. **Evaluate each source** (see [source-evaluation.md](source-evaluation.md))
   - Source reliability (A-F)
   - Information credibility (1-6)

3. **Assess overall information quality**

| Factor | Assessment | Implications |
|--------|------------|--------------|
| Source diversity | Single/Few/Many sources | More diversity = higher confidence |
| Source independence | Related/Independent | Independent better for confirmation |
| Information recency | Current/Dated/Stale | Currency affects validity |
| Information specificity | Vague/General/Specific | Specific = more verifiable |
| Gaps | What's missing | Identify collection needs |

4. **Adjust confidence accordingly**
   - Limited sources = lower confidence
   - Unconfirmed information = hedged conclusions

### Indicators and Signposts

**Purpose**: Identify observable events or conditions that would indicate a change in situation or validate/invalidate hypotheses.

**When to Use**:
- Monitoring ongoing situations
- Tracking threat development
- Validating predictive analysis

**Process**:

1. **Define possible outcomes or scenarios**
   - What futures are we monitoring for?
   - What hypotheses need testing?

2. **Identify indicators for each scenario**

| Scenario | Indicator | Source | Observation Method |
|----------|-----------|--------|-------------------|
| Company preparing IPO | SEC S-1 filing | SEC EDGAR | Monitoring |
| Subject relocating | Address change, property sale | Public records | Periodic check |
| Threat actor active | New infrastructure registration | Passive DNS | Automated alerting |

3. **Weight indicators**
   - Leading indicators (early warning)
   - Confirming indicators (validation)
   - Unique indicators (discriminating)

4. **Establish monitoring process**
   - Assign responsibility
   - Set check frequency
   - Define trigger thresholds

---

## Analysis of Competing Hypotheses (ACH)

ACH is the cornerstone structured technique for evaluating multiple explanations against evidence.

### Purpose

- Systematically evaluate multiple hypotheses
- Reduce confirmation bias
- Identify diagnostic evidence
- Increase analytical rigor

### When to Use

- Multiple possible explanations exist
- Stakes are high
- Confirmation bias is a concern
- Transparency is required

### The ACH Process

**Step 1: Identify Hypotheses**

Generate all reasonable hypotheses, including:
- Most likely explanation
- Alternative explanations
- Unlikely but possible explanations
- Deception or denial scenarios

**Step 2: List Evidence**

Compile all relevant evidence:
- Confirmed facts
- Reports and claims
- Assumptions
- Logical deductions
- Absence of evidence (where something should exist if hypothesis is true)

**Step 3: Build the Matrix**

Create a matrix with hypotheses as columns and evidence as rows:

| Evidence | H1: Natural Causes | H2: Deliberate Action | H3: Third Party |
|----------|-------------------|----------------------|-----------------|
| E1: [Evidence item] | CC (Confirms) | II (Inconsistent) | N/A |
| E2: [Evidence item] | C (Consistent) | CC (Confirms) | C (Consistent) |
| E3: [Evidence item] | II (Inconsistent) | CC (Confirms) | C (Consistent) |

**Evidence Codes**:
- **CC** = Strongly confirms (very diagnostic for this hypothesis)
- **C** = Consistent (supports but doesn't prove)
- **N/A** = Not applicable or neutral
- **I** = Inconsistent (weighs against)
- **II** = Strongly inconsistent (if true, hypothesis very unlikely)

**Step 4: Evaluate Hypotheses**

Focus on disconfirmation, not confirmation:
- Which hypotheses have the most inconsistent evidence?
- Which survive the most tests?
- What evidence would disprove each hypothesis?

**Step 5: Assess Sensitivity**

Consider:
- What if key evidence is wrong?
- What if key evidence is deception?
- How would new evidence change the assessment?

**Step 6: Draw Conclusions**

- State which hypothesis(es) best fit the evidence
- Explain why alternatives are less likely
- Identify what would change the assessment
- Express appropriate confidence

### ACH Example (OSINT Investigation)

**Scenario**: Investigating whether a company is a legitimate business or a front operation.

**Hypotheses**:
- H1: Legitimate operating business
- H2: Shell company (inactive front)
- H3: Active front for money laundering
- H4: Legitimate but failing business

**Evidence Matrix**:

| Evidence | H1: Legit | H2: Shell | H3: Money Front | H4: Failing |
|----------|-----------|-----------|-----------------|-------------|
| E1: Minimal online presence | I | CC | C | C |
| E2: Registered at virtual office | I | CC | CC | N/A |
| E3: Officers in multiple shells | II | CC | CC | I |
| E4: Some verifiable transactions | C | I | C | C |
| E5: No employee LinkedIn profiles | I | CC | C | C |
| E6: Recent regulatory filings | C | I | C | C |
| E7: Website recently created | I | C | C | N/A |

**Analysis**: H1 (legitimate operating business) has the most inconsistent evidence. H2 (shell company) and H3 (money front) are most consistent. Recommend further investigation to distinguish between H2 and H3.

### ACH Best Practices

1. **Include unlikely hypotheses**: Don't prematurely eliminate possibilities
2. **Focus on disconfirmation**: Look for evidence that disproves, not proves
3. **Weight evidence carefully**: Not all evidence is equally diagnostic
4. **Document reasoning**: Make the process transparent
5. **Revisit regularly**: Update as new evidence emerges
6. **Be honest about gaps**: Acknowledge what you don't know

---

## Link Analysis

Link analysis maps relationships between entities to understand networks, identify key nodes, and discover hidden connections.

### Purpose

- Visualize relationships and networks
- Identify central or influential entities
- Discover non-obvious connections
- Understand organizational structures

### Entity Types

| Entity Type | Symbol | Examples |
|-------------|--------|----------|
| Person | Circle/Node | Individuals, subjects |
| Organization | Rectangle | Companies, agencies |
| Location | Diamond | Addresses, facilities |
| Account | Hexagon | Bank accounts, usernames |
| Communication | Triangle | Phone numbers, emails |
| Event | Pentagon | Meetings, transactions |

### Relationship Types

| Relationship | Notation | Meaning |
|--------------|----------|---------|
| Direct | Solid line | Confirmed direct connection |
| Indirect | Dashed line | Inferred or weak connection |
| Hierarchical | Arrow | Direction of authority/influence |
| Financial | Double line | Money flow |
| Communication | Wavy line | Information exchange |
| Temporal | Dotted line | Historical connection (no longer active) |

### Link Analysis Process

1. **Entity Extraction**
   - Identify all relevant entities from collected information
   - Standardize naming (resolve aliases, alternate spellings)
   - Categorize entities by type

2. **Relationship Identification**
   - Document all known relationships
   - Note relationship type and strength
   - Record source for each link

3. **Network Construction**
   - Build visual network diagram
   - Position entities meaningfully
   - Apply consistent visual conventions

4. **Network Analysis**

| Metric | Meaning | Significance |
|--------|---------|--------------|
| Degree centrality | Number of connections | Hub or broker role |
| Betweenness centrality | Lies on paths between others | Gatekeeper role |
| Closeness centrality | Average distance to all others | Access to network |
| Clustering coefficient | Connection among neighbors | Tightness of subgroups |

5. **Interpretation**
   - Who are the key players?
   - What subgroups exist?
   - Where are the gaps or vulnerabilities?
   - What's the structure (hierarchy, cell, network)?

### Link Analysis Tools

- **i2 Analyst's Notebook**: Industry standard
- **Maltego**: OSINT-focused
- **Gephi**: Open-source network analysis
- **yEd**: Free diagramming
- **Neo4j**: Graph database

---

## Timeline Analysis

Timeline analysis organizes events chronologically to understand sequences, patterns, and causation.

### Purpose

- Establish sequence of events
- Identify patterns and cycles
- Discover temporal relationships
- Support or refute narratives

### Timeline Construction

1. **Collect temporal data**
   - Extract all dated events from sources
   - Note date precision (exact time, date, month, year)
   - Record source for each event

2. **Normalize timestamps**
   - Convert to consistent timezone (UTC recommended)
   - Handle ambiguous dates
   - Note uncertainties

3. **Build timeline**

| Date/Time | Event | Entities Involved | Source | Confidence |
|-----------|-------|-------------------|--------|------------|
| 2024-03-15 09:23 UTC | Domain registration | Company X | WHOIS | High |
| 2024-03-15 | Website launched | Company X | Archive.org | Medium |
| 2024-03-20 | First social post | Account @company_x | Twitter | High |

4. **Analyze patterns**
   - Cause-effect relationships
   - Suspicious timing
   - Gaps in activity
   - Parallel activities

### Timeline Visualization

```
Timeline Format Options:
├── Linear timeline
│   └── Events on horizontal or vertical axis
├── Gantt-style
│   └── Duration-based events
├── Swimlane
│   └── Multiple parallel tracks by entity
└── Calendar view
    └── Events mapped to calendar
```

### Temporal Pattern Analysis

| Pattern | Indicators | Significance |
|---------|------------|--------------|
| Burst activity | Sudden increase in events | Response to trigger |
| Regular cycles | Periodic events | Routine or scheduled activity |
| Synchronization | Coordinated timing | Collaboration or common cause |
| Gaps | Absence of activity | Dormancy, obstruction, or data gaps |
| Acceleration | Increasing frequency | Escalation or approaching deadline |

---

## Pattern Analysis

Pattern analysis identifies recurring behaviors, characteristics, or events to develop profiles and predictions.

### Types of Patterns

1. **Behavioral Patterns**
   - Operating hours and habits
   - Communication patterns
   - Travel patterns
   - Financial patterns

2. **Technical Patterns**
   - Infrastructure reuse
   - Tool and technique signatures
   - Code patterns
   - Configuration patterns

3. **Organizational Patterns**
   - Structure and hierarchy
   - Decision-making patterns
   - Recruitment patterns
   - Operational patterns

### Pattern Analysis Process

1. **Data Collection**
   - Gather sufficient data points (more is better)
   - Ensure consistent data quality
   - Document collection methodology

2. **Pattern Identification**
   - Look for regularities
   - Use statistical methods where appropriate
   - Consider multiple pattern types

3. **Pattern Validation**
   - Test against additional data
   - Consider alternative explanations
   - Assess pattern significance

4. **Pattern Application**
   - Predict future behavior
   - Identify anomalies
   - Guide collection priorities

### Pattern Matching for Attribution

| Pattern Element | Example | Analytical Use |
|-----------------|---------|----------------|
| Writing style | Word choice, syntax patterns | Author identification |
| Technical signatures | IP ranges, malware families | Infrastructure attribution |
| Operational timing | Activity hours, holiday patterns | Geographic location |
| Tactical choices | Target selection, methods | Actor profiling |

---

## Hypothesis Generation and Testing

### Generating Hypotheses

**Structured Brainstorming**:
1. Define the analytical question
2. Generate hypotheses individually (avoid groupthink)
3. Combine and refine as a group
4. Categorize hypotheses (likely, alternative, unlikely)

**Techniques**:
- **Simple Brainstorming**: Free generation of ideas
- **Nominal Group Technique**: Individual then group
- **Starbursting**: Question-based generation (who, what, when, where, why, how)

### Hypothesis Requirements

Good hypotheses are:
- **Specific**: Clear enough to test
- **Falsifiable**: Can be disproven with evidence
- **Mutually exclusive**: Clearly different from alternatives
- **Collectively exhaustive**: Cover reasonable possibilities

### Testing Hypotheses

| Test Type | Method | Outcome |
|-----------|--------|---------|
| Consistency test | Compare hypothesis with evidence | Consistent/Inconsistent |
| Prediction test | Derive expected observations, seek them | Found/Not found |
| Disconfirmation test | Seek evidence that would disprove | Found (hypothesis weakened) / Not found |
| Comparative test | Evaluate against competing hypotheses | Most/less supported |

### Documenting Hypothesis Testing

```markdown
## Hypothesis Testing Record

**Hypothesis**: [Statement]

**Evidence For**:
- [Evidence 1 with source and assessment]
- [Evidence 2 with source and assessment]

**Evidence Against**:
- [Evidence 1 with source and assessment]

**Predicted Evidence (if true)**:
- [Prediction 1]: [Found/Not found]
- [Prediction 2]: [Found/Not found]

**Disconfirming Evidence (would disprove)**:
- [Potential disconfirmer]: [Present/Absent]

**Assessment**: [Supported/Weakened/Inconclusive]
**Confidence**: [High/Medium/Low]
```

---

## Contrarian Techniques

### Devil's Advocacy

**Purpose**: Challenge prevailing analysis by systematically arguing the opposite position.

**Process**:
1. Identify the prevailing view or leading hypothesis
2. Assign analyst(s) to argue against it
3. Develop the strongest possible counter-argument
4. Present and debate
5. Assess whether prevailing view survives challenge

### Red Team Analysis

**Purpose**: Analyze from the adversary's or target's perspective.

**Applications**:
- How would the adversary see this situation?
- What would the adversary do next?
- How would the adversary exploit our vulnerabilities?
- What does the adversary know about us?

**Process**:
1. Develop adversary profile (capabilities, intentions, constraints)
2. Adopt adversary's perspective fully
3. Analyze situation as adversary would
4. Generate adversary courses of action
5. Return to own perspective and assess implications

### "What If?" Analysis

**Purpose**: Explore alternative scenarios and their implications.

**Process**:
1. Identify key assumptions or conditions
2. Ask "What if [assumption/condition] were different?"
3. Trace implications of the change
4. Assess likelihood and impact
5. Identify indicators that would signal the change

---

## Applying SATs to OSINT

### Technique Selection Guide

| Situation | Recommended Techniques |
|-----------|------------------------|
| Starting an investigation | Key Assumptions Check, Brainstorming |
| Multiple possible explanations | ACH, Hypothesis Testing |
| Understanding relationships | Link Analysis |
| Reconstructing events | Timeline Analysis |
| Monitoring a situation | Indicators and Signposts |
| High-stakes assessment | ACH, Devil's Advocacy, Red Team |
| Predictive analysis | Scenario Analysis, Indicators |
| Attribution | Pattern Analysis, ACH |

### Integration with OSINT Workflow

1. **Collection Phase**: Use brainstorming to identify sources
2. **Processing Phase**: Use timelines and link analysis to organize
3. **Analysis Phase**: Apply SATs appropriate to analytical question
4. **Reporting Phase**: Document methodology and reasoning

---

## References

### Primary Sources (PDF Library)

- [A Tradecraft Primer: Structured Analytic Techniques](../references/pdf-library-index.md) - Core SAT reference
- [Psychology of Intelligence Analysis](../references/pdf-library-index.md) - Cognitive foundations
- [Critical Thinking and Intelligence Analysis](../references/pdf-library-index.md) - Analytical rigor
- [Criminal Intelligence for Analysts](../references/pdf-library-index.md) - Law enforcement applications
- [Joint Analysis Handbook](../references/pdf-library-index.md) - Multi-agency techniques

### Related Documentation

- [intelligence-cycle.md](intelligence-cycle.md) - Overall intelligence process
- [source-evaluation.md](source-evaluation.md) - Evaluating sources and information
- [verification-methods.md](verification-methods.md) - Verifying analytical findings
- [../tradecraft/](../tradecraft/) - Cognitive bias awareness

---

*Document Version: 1.0*
*Last Updated: 2025-12-28*
*Status: Active*
