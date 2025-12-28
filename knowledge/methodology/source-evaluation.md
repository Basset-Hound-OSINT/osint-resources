# Source Evaluation for OSINT

Source evaluation is the systematic assessment of information sources and their content to determine reliability, credibility, and utility. This document provides the standard evaluation frameworks used in intelligence analysis, adapted for OSINT operations.

## Overview

Every piece of intelligence should be evaluated on two dimensions:
1. **Source Reliability**: How trustworthy is the source providing the information?
2. **Information Credibility**: How believable is the specific information itself?

These evaluations are independent; a reliable source can provide unreliable information, and an unreliable source can provide accurate information.

---

## The Admiralty/NATO Rating System

The Admiralty System (also called the NATO System) is the standard evaluation framework used by military and intelligence organizations worldwide.

### Source Reliability Scale (A-F)

| Rating | Description | Definition |
|--------|-------------|------------|
| **A** | Completely Reliable | No doubt about the source's authenticity, trustworthiness, or competency. History of complete reliability. |
| **B** | Usually Reliable | Minor doubt about the source's authenticity, trustworthiness, or competency. History of valid information most of the time. |
| **C** | Fairly Reliable | Doubt about the source's authenticity, trustworthiness, or competency, but has provided valid information in the past. |
| **D** | Not Usually Reliable | Significant doubt about the source's authenticity, trustworthiness, or competency, but has provided valid information occasionally. |
| **E** | Unreliable | Lacking in authenticity, trustworthiness, and competency. History of invalid information. |
| **F** | Cannot Be Judged | No basis for evaluating the reliability of the source. First-time source or insufficient history. |

### Information Credibility Scale (1-6)

| Rating | Description | Definition |
|--------|-------------|------------|
| **1** | Confirmed | Confirmed by other independent sources; logical in itself; consistent with other information on the subject. |
| **2** | Probably True | Not confirmed; logical in itself; consistent with other information on the subject. |
| **3** | Possibly True | Not confirmed; reasonably logical in itself; agrees with some other information on the subject. |
| **4** | Doubtfully True | Not confirmed; possible but not logical; no other information on the subject. |
| **5** | Improbable | Not confirmed; not logical in itself; contradicted by other information on the subject. |
| **6** | Cannot Be Judged | No basis for evaluating the validity of the information. |

### Combined Ratings

Ratings are expressed as letter-number combinations:

| Rating | Interpretation | Action |
|--------|----------------|--------|
| A1 | Highly reliable source, confirmed information | Use with high confidence |
| A2-B2 | Reliable source, probable information | Use with confidence, note not confirmed |
| B3-C3 | Moderate reliability, possible information | Use with caution, seek corroboration |
| C4-D4 | Limited reliability, doubtful information | Use only if corroborated |
| D5-E5 | Poor reliability, improbable information | Generally do not use |
| F6 | Cannot evaluate | Flag for further development |

### Rating Examples

| Information | Source | Source Rating | Info Rating | Combined |
|-------------|--------|---------------|-------------|----------|
| Corporate filing data | SEC EDGAR | A (official source) | 1 (official record) | A1 |
| Social media post | Known subject's verified account | B (authenticated) | 2 (unconfirmed) | B2 |
| Forum discussion | Anonymous user | F (unknown) | 3 (possible) | F3 |
| News article | Major outlet | B (established) | 2 (sourced) | B2 |
| Leaked document | Anonymous leak site | D (questionable) | 6 (unverifiable) | D6 |

---

## Source Reliability Assessment

### Evaluation Criteria

Assess source reliability based on:

```
Source Reliability Factors:
├── Authenticity
│   ├── Is the source who/what it claims to be?
│   ├── Has identity been verified?
│   └── Are credentials legitimate?
├── Trustworthiness
│   ├── Does the source have motivation to deceive?
│   ├── What biases might affect the source?
│   └── Has the source been accurate previously?
├── Competency
│   ├── Does the source have access to the information?
│   ├── Does the source have expertise in the subject?
│   └── Is the source in a position to know?
└── Track Record
    ├── How often has the source provided accurate information?
    ├── What is the source's reputation?
    └── Are there known failures or fabrications?
```

### Source Type Reliability Guidelines

| Source Type | Typical Rating | Factors Affecting Rating |
|-------------|----------------|--------------------------|
| **Official Government Sources** | A-B | Accuracy of bureaucratic process |
| **Court Records** | A-B | Legal standards for evidence |
| **Major News Outlets** | B-C | Editorial standards, sourcing practices |
| **Corporate Disclosures** | B-C | Regulatory requirements, audit quality |
| **Academic Sources** | B-C | Peer review, methodology rigor |
| **Social Media (Verified)** | B-C | Account authentication, post history |
| **Social Media (Unverified)** | D-F | No authentication, unknown history |
| **Anonymous Forums** | E-F | No identity verification |
| **Leaked Documents** | C-F | Authentication challenges, potential manipulation |

### Source Reliability Worksheet

For each source, evaluate:

| Factor | Assessment | Rating Implication |
|--------|------------|-------------------|
| **Identity confirmed?** | Yes / No / Partial | Higher if confirmed |
| **Bias or agenda?** | None / Some / Strong | Lower if biased |
| **Access to information?** | Direct / Indirect / None | Higher if direct |
| **Subject expertise?** | Expert / Knowledgeable / None | Higher if expert |
| **Previous accuracy?** | High / Mixed / Low / Unknown | Higher if accurate history |
| **Reputation?** | Excellent / Good / Poor / Unknown | Higher if good reputation |

---

## Information Credibility Assessment

### Evaluation Criteria

Assess information credibility based on:

```
Information Credibility Factors:
├── Confirmation
│   ├── Is the information confirmed by independent sources?
│   ├── How many sources confirm it?
│   └── Are confirming sources truly independent?
├── Internal Logic
│   ├── Is the information internally consistent?
│   ├── Does it make logical sense?
│   └── Are there unexplained contradictions?
├── External Consistency
│   ├── Does it fit with other known information?
│   ├── Does it contradict established facts?
│   └── Can apparent contradictions be explained?
└── Plausibility
    ├── Is the information physically possible?
    ├── Is it operationally feasible?
    └── Does it align with known patterns?
```

### Credibility Assessment Questions

| Question | Positive Indicator | Negative Indicator |
|----------|-------------------|-------------------|
| Is it confirmed? | Multiple independent sources confirm | Single source, no confirmation |
| Is it logical? | Clear cause-effect, coherent narrative | Contradictions, gaps in logic |
| Is it consistent? | Fits known facts and patterns | Contradicts established information |
| Is it specific? | Precise details, verifiable claims | Vague, non-falsifiable claims |
| Is it current? | Recent, timely information | Outdated, superseded |
| Is it complete? | Full picture, context provided | Fragmentary, missing key details |

### Information Quality Indicators

**Positive Indicators (increase credibility rating):**
- Confirmed by independent sources
- Contains verifiable specifics (dates, names, locations)
- Consistent with known facts
- Source has direct knowledge
- Documented with evidence (documents, images)
- Timely and current

**Negative Indicators (decrease credibility rating):**
- Single source, no confirmation
- Vague or non-specific
- Contradicts known facts
- Source lacks direct knowledge
- Undocumented claims
- Outdated information
- Too convenient or perfectly aligned with expectations

---

## OSINT-Specific Considerations

### Digital Source Challenges

OSINT faces unique source evaluation challenges:

| Challenge | Description | Mitigation |
|-----------|-------------|------------|
| **Anonymity** | Many online sources are anonymous | Focus on information credibility |
| **Impersonation** | Fake accounts, spoofed identities | Verify account authenticity |
| **Manipulation** | Altered images, fabricated documents | Use verification tools |
| **Ephemerality** | Content disappears, links break | Archive and document sources |
| **Volume** | Overwhelming quantity of sources | Prioritize high-reliability sources |
| **Deception** | Deliberate disinformation campaigns | Cross-reference, seek primary sources |

### Platform-Specific Evaluation

| Platform Type | Reliability Considerations | Credibility Considerations |
|---------------|---------------------------|---------------------------|
| **Social Media** | Verification status, account age, follower analysis | Post history, engagement patterns, content consistency |
| **News Sites** | Editorial standards, ownership, funding | Sourcing, corrections policy, byline attribution |
| **Government Sites** | Official domain, SSL certificates | Data currency, completeness, methodology |
| **Databases** | Provider reputation, data sourcing | Update frequency, coverage, known gaps |
| **Forums/Boards** | Moderation, community reputation | Cross-reference with other forums |
| **Dark Web** | Very low inherent reliability | Requires extensive verification |

### Evaluating User-Generated Content

For social media and other user-generated content:

```
Account Evaluation:
├── Age of account
├── Posting history and consistency
├── Follower/following ratio
├── Verification status
├── Profile completeness
├── Engagement patterns (real or bot-like?)
└── Cross-platform presence

Content Evaluation:
├── Original or reshared?
├── Metadata integrity
├── Content modifications
├── Timing and context
├── Reactions and replies
└── Spread patterns
```

### Evaluating Technical Sources

For technical OSINT (infrastructure, code, etc.):

| Source | Reliability Factors | Credibility Factors |
|--------|---------------------|---------------------|
| WHOIS data | Registry authority, data freshness | Privacy services, accuracy |
| DNS records | Authoritative server, TTL | Configuration validity |
| SSL certificates | CA trustworthiness, validation level | Certificate validity, chain |
| Code repositories | Platform legitimacy, author reputation | Commit history, code review |
| Paste sites | Generally low reliability | Verification against other sources |

---

## Digital Source Evaluation Framework

### The SIFT Method

For rapid evaluation of digital sources:

| Step | Action | Questions |
|------|--------|-----------|
| **S**top | Pause before using/sharing | Do I know this source? Should I verify? |
| **I**nvestigate the source | Research the source itself | Who is behind this? What is their reputation? |
| **F**ind better coverage | Seek additional sources | Who else is reporting this? What do experts say? |
| **T**race claims | Follow to original source | Where did this originate? What's the primary source? |

### CRAAP Test Adaptation

Originally for academic sources, adapted for OSINT:

| Criterion | Evaluation Questions |
|-----------|---------------------|
| **C**urrency | When was the information published/updated? Is it current enough for your needs? |
| **R**elevance | Does the information relate to your IRs? Who is the intended audience? |
| **A**uthority | Who is the author/publisher? What are their credentials? Is there contact information? |
| **A**ccuracy | Is the information supported by evidence? Can it be verified? Are there errors? |
| **P**urpose | Why does this information exist? Is there bias? Is it fact, opinion, or propaganda? |

### Lateral Reading

Evaluate sources by reading laterally (outside the source) rather than vertically (within the source):

1. **Leave the site**: Don't evaluate a site based only on what it says about itself
2. **Search for the source**: Look up what others say about the source
3. **Check Wikipedia**: See if Wikipedia has an article about the source
4. **Find expert views**: See what subject matter experts say about the source
5. **Check fact-checkers**: See if fact-checkers have evaluated the source

---

## Documentation and Attribution

### Recording Evaluations

Document source evaluations in your collection:

```markdown
## Source Evaluation Record

**Source**: [Name/Description]
**URL/Location**: [Where found]
**Access Date**: [Date accessed]
**Collector**: [Who collected]

### Reliability Assessment
- Rating: [A-F]
- Justification: [Why this rating]
- History: [Previous experience with source]

### Information Assessment
- Rating: [1-6]
- Justification: [Why this rating]
- Confirmation status: [Confirmed/Unconfirmed]
- Confirming sources: [List if any]

### Combined Rating: [Letter-Number]

### Notes
[Any additional context or caveats]
```

### Attribution in Reports

When using evaluated information in reports:

| Rating | Attribution Language |
|--------|---------------------|
| A1-A2 | "According to [source]..." |
| B1-B2 | "[Source] reports/indicates..." |
| B3-C2 | "[Source] suggests/claims..." |
| C3-D4 | "Unconfirmed reports indicate..." / "According to unverified sources..." |
| D5-E5 | "An unconfirmed and potentially unreliable source claims..." |
| F6 | "An unevaluated source of unknown reliability states..." |

### Confidence Language

Link source evaluation to analytical confidence:

| Source Quality | Confidence Language |
|----------------|---------------------|
| Multiple A1-B2 sources | "We assess with high confidence..." |
| Mix of A-C sources, some confirmation | "We assess with moderate confidence..." |
| Limited sources, no confirmation | "We assess with low confidence..." |
| Single source, unverifiable | "One source indicates..." (avoid confidence claim) |

---

## Practical Evaluation Workflow

### Quick Evaluation (Field)

For rapid assessment during collection:

1. **Source check**: Known/unknown? Previous experience?
2. **Logic check**: Does it make sense?
3. **Confirmation check**: Seen elsewhere?
4. **Assign provisional rating**: Best current assessment

### Full Evaluation (Processing)

For thorough assessment during processing:

1. **Research the source**: Who are they? What's their track record?
2. **Assess access and expertise**: Could they know this? Do they have expertise?
3. **Identify biases**: What interests might color the information?
4. **Test internal logic**: Is it consistent and coherent?
5. **Seek confirmation**: Find independent sources
6. **Assign final rating**: Document reasoning

### Continuous Evaluation

Update evaluations as new information emerges:
- New confirming/contradicting evidence
- Source behavior changes
- Additional context becomes available
- Original assessment proves correct/incorrect

---

## Common Evaluation Pitfalls

### Avoid These Errors

| Pitfall | Description | Mitigation |
|---------|-------------|------------|
| **Source circularity** | Multiple sources trace to single origin | Trace sources to origin |
| **Confirmation bias** | Over-rating information that confirms expectations | Actively seek disconfirming evidence |
| **Authority bias** | Over-trusting "authoritative" sources | Evaluate each claim independently |
| **Recency bias** | Over-weighting recent information | Consider historical context |
| **Vividness bias** | Over-weighting dramatic/detailed information | Assess independent of presentation |
| **Consistency inflation** | Assuming consistent = accurate | Fabricated info can be consistent |

---

## References

### Primary Sources (PDF Library)

- [FM 34-3 Intelligence Analysis](../references/pdf-library-index.md) - Intelligence analysis doctrine
- [ICD 206 Sourcing Requirements](../references/pdf-library-index.md) - IC sourcing standards
- [Psychology of Intelligence Analysis](../references/pdf-library-index.md) - Cognitive aspects of analysis
- [Critical Thinking and Intelligence Analysis](../references/pdf-library-index.md) - Analytical rigor

### Related Documentation

- [intelligence-cycle.md](intelligence-cycle.md) - Overall intelligence process
- [collection-planning.md](collection-planning.md) - Collection methodology
- [verification-methods.md](verification-methods.md) - Verification techniques
- [analysis-techniques.md](analysis-techniques.md) - Structured analytic techniques

---

*Document Version: 1.0*
*Last Updated: 2025-12-28*
*Status: Active*
