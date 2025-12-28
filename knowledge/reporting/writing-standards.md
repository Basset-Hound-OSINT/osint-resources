# Intelligence Writing Standards

This document establishes writing standards for OSINT reports and assessments, based on intelligence community best practices. Following these standards ensures clear, consistent, and professional communication of analytical findings.

---

## Reference Sources

These standards are derived from authoritative intelligence community style guides:

| Document | Description |
|----------|-------------|
| **CIA Writing Guide (2017)** | Foundational guide for intelligence writing at the Central Intelligence Agency |
| **DIA Style Manual for Intelligence Products (2016)** | Defense Intelligence Agency standards for intelligence product development |
| **ODNI Style Manual (2011-2013)** | Office of the Director of National Intelligence writing and style standards |
| **Army Intelligence Center of Excellence Writing Guide (2022)** | US Army standards for intelligence writing and reporting |
| **NSA SIGINT Style Manual (2010)** | National Security Agency signals intelligence reporting standards |
| **BLUF Writing Format** | Bottom Line Up Front methodology documentation |
| **Intelligence Writing for Academics** | Academic perspective on intelligence writing |
| **Tradecraft Primer for Structured Analytic Techniques** | CIA methodology for rigorous analysis |

See the [PDF Library Index](../references/pdf-library-index.md) for access to these source documents.

---

## 1. BLUF Writing Format

### What is BLUF?

BLUF (Bottom Line Up Front) is the foundational principle of intelligence writing. The most important information comes first, followed by supporting details.

### Why BLUF Matters

- Decision-makers are busy and may not read entire documents
- Key findings should never be buried in the middle of a report
- Readers can quickly assess relevance and importance
- Supports rapid information consumption

### BLUF Structure

```
Standard BLUF Format:

Paragraph 1: THE BOTTOM LINE
- State the key finding or assessment
- Answer the "so what?" question
- Include primary implications if space permits
- 2-4 sentences maximum

Paragraph 2-N: SUPPORTING DETAILS
- Evidence supporting the bottom line
- Analysis and reasoning
- Context and background
- Alternative views
- Sources and confidence

Final Section: IMPLICATIONS
- What this means for the reader
- Recommended actions (if requested)
```

### BLUF Examples

**Poor (Buries the Lead):**
> We examined social media activity across multiple platforms over a three-month period. Analysis included Twitter, LinkedIn, Facebook, and Instagram. Using network analysis techniques, we mapped connections between accounts. Linguistic analysis was also performed. Based on this comprehensive review, we assess that the accounts are coordinated.

**Good (BLUF Format):**
> We assess with high confidence that five social media accounts are coordinated by a single actor to spread disinformation. Network analysis reveals identical posting patterns, linguistic markers, and cross-platform amplification. This coordinated activity began in January 2024 and targets audiences interested in financial markets.

### BLUF Rules

1. **Lead with the conclusion** - Never make readers search for your main point
2. **One main idea per paragraph** - Keep paragraphs focused
3. **Most important to least important** - Structure all content in descending priority
4. **Active voice preferred** - "We assess that..." not "It is assessed that..."
5. **Concrete over abstract** - Specific findings over general observations

---

## 2. Confidence Language Standards

### Standard Probability Terms

Use these terms consistently to express likelihood:

| Term | Probability | Usage |
|------|-------------|-------|
| **Almost certainly** | 95%+ | Virtual certainty; would be surprising if wrong |
| **Very likely** | 80-95% | High probability; strong evidence supports |
| **Likely** | 60-80% | More probable than not; good evidence |
| **Roughly even chance** | 40-60% | Could go either way; balanced evidence |
| **Unlikely** | 20-40% | Less probable than not; limited evidence |
| **Very unlikely** | 5-20% | Low probability; contrary evidence exists |
| **Almost certainly not** | <5% | Near certainty of non-occurrence |

### Terms to Avoid

| Avoid | Use Instead | Reason |
|-------|-------------|--------|
| "May" | "Possibly" or specific probability | "May" is ambiguous |
| "Could" | "Might" or specific assessment | "Could" covers too broad a range |
| "Should" | Specific recommendation | Implies obligation rather than probability |
| "Believes" | "Assesses" or "Judges" | "Believes" sounds like opinion |
| "Thinks" | "Assesses" or "Judges" | Same as above |

### Confidence Levels

Separate from probability, confidence levels indicate certainty in the assessment:

| Level | Definition | Use When |
|-------|------------|----------|
| **HIGH** | Solid judgment based on high-quality information | Multiple corroborating sources; direct evidence |
| **MODERATE** | Based on credible information but not fully corroborated | Some corroboration; indirect evidence |
| **LOW** | Tentative judgment; fragmented or poorly corroborated | Limited sources; significant gaps |

### Combining Probability and Confidence

Always distinguish between:
- **How likely** something is (probability)
- **How sure** you are about that likelihood (confidence)

**Example:**
> "We assess with **MODERATE CONFIDENCE** that Subject X will **LIKELY** attempt to expand operations in the next quarter."

This means:
- There's a 60-80% chance of expansion (LIKELY)
- We have credible but not fully corroborated information supporting this (MODERATE CONFIDENCE)

---

## 3. Source Citation Formats

### Standard Source Citation

Every factual claim requires a source. Use this format:

```
In-Text Citation:
"Subject registered the domain in March 2023 (Source: WHOIS records, accessed 15 Jan 2024)."

Footnote Style:
"Subject registered the domain in March 2023.^1"

^1 WHOIS lookup, domain.com, accessed 15 January 2024. Registrar: GoDaddy.

End-of-Document Style:
See Sources section with numbered references.
```

### Source Reliability Ratings

Use the standard 6x6 system when reliability assessment is needed:

**Source Reliability (A-F):**
- A: Completely reliable - No doubt about authenticity, trustworthiness, competency
- B: Usually reliable - Minor doubt; source has been reliable in past
- C: Fairly reliable - Doubt exists but source has provided valid information
- D: Not usually reliable - Significant doubt; source has been unreliable
- E: Unreliable - Lacking in authenticity, trustworthiness, or competency
- F: Cannot be judged - No basis for evaluating reliability

**Information Validity (1-6):**
- 1: Confirmed - Confirmed by independent sources
- 2: Probably true - Logical, consistent, corroborated by other information
- 3: Possibly true - Reasonably logical, agrees with some other information
- 4: Doubtfully true - Possible but not logical; no other information
- 5: Improbable - Not logical, contradicted by other information
- 6: Cannot be judged - No basis for evaluating validity

**Combined Rating Example:**
> "B2 - Usually reliable source reporting probably true information"

### Source Categories for OSINT

| Category | Examples | Typical Reliability |
|----------|----------|---------------------|
| **Official Records** | Corporate filings, court records, government databases | High (A-B) |
| **Primary Sources** | Subject's own social media, websites, statements | High (verify authenticity) |
| **Established Media** | Major news outlets, wire services | Usually reliable (B) |
| **Secondary Sources** | Analysis, commentary, academic papers | Varies (B-D) |
| **User-Generated** | Forums, comments, social media posts | Lower (C-E) |
| **Anonymous Sources** | Tips, leaks, unverified claims | Cannot be judged alone (F) |

---

## 4. Analytical Language

### Distinguishing Facts from Judgments

**Facts** - Verifiable information with source citations:
> "The organization was incorporated in Delaware on 15 March 2020."

**Judgments** - Analytical conclusions requiring confidence language:
> "We assess that the organization likely operates as a front for money laundering."

### Signaling Judgments

Use these phrases to clearly mark analytical judgments:

- "We assess that..."
- "We judge that..."
- "Analysis indicates..."
- "Evidence suggests..."
- "This probably/likely means..."

### Avoiding Bias

**Loaded Language to Avoid:**

| Biased | Neutral Alternative |
|--------|---------------------|
| "Claimed" (implies dishonesty) | "Stated" or "Reported" |
| "Admitted" (implies guilt) | "Acknowledged" or "Confirmed" |
| "Refused to" | "Did not" or "Declined to" |
| "Only" (minimizing) | Remove or use "approximately" |
| "Failed to" | "Did not" |
| "So-called" | Use actual term or explain in context |

**Attribution:**
- Attribute statements to sources: "According to [source]..."
- Distinguish between organization statements and analyst judgments
- Note when information is self-reported

### Hedging Appropriately

Use hedges when uncertainty exists, but avoid excessive hedging:

**Under-hedged:**
> "Subject is laundering money through the shell company."

**Over-hedged:**
> "It is possible that the subject may potentially be involved in what could possibly be characterized as potential money laundering-type activities."

**Appropriately hedged:**
> "We assess with moderate confidence that the subject is likely using the shell company to launder funds."

---

## 5. Clarity and Precision

### Sentence Structure

1. **Prefer active voice**
   - Active: "The analyst reviewed the documents."
   - Passive: "The documents were reviewed." (avoid)

2. **Keep sentences concise**
   - Target: 15-20 words average
   - Maximum: 35 words
   - One idea per sentence

3. **Lead with the subject**
   - Good: "The organization operates in three countries."
   - Weak: "In three countries, operations are maintained by the organization."

### Paragraph Structure

- **One main idea per paragraph**
- **Topic sentence first** (BLUF principle applies at paragraph level)
- **3-5 sentences typically sufficient**
- **Transition between paragraphs** to maintain flow

### Word Choice

**Prefer Simple Words:**

| Complex | Simple |
|---------|--------|
| Utilize | Use |
| Facilitate | Help, enable |
| Commence | Begin, start |
| Terminate | End |
| Endeavor | Try |
| Subsequently | Then, later |
| Notwithstanding | Despite |
| Heretofore | Until now |

**Be Specific:**

| Vague | Specific |
|-------|----------|
| "Recently" | "In March 2024" or "within the past 30 days" |
| "Several" | "Four" or "between three and five" |
| "Significant" | Quantify: "a 40% increase" |
| "Large" | Quantify: "more than 10,000 followers" |
| "Soon" | "Within the next 30 days" or "by Q2 2024" |

### Numbers and Data

- **Spell out** one through nine
- **Use numerals** for 10 and above
- **Always use numerals** for: dates, measurements, percentages, money
- **Be consistent** within a document
- **Round appropriately** - don't imply false precision
  - "Approximately 1,200" not "1,247" unless precision matters

### Dates and Times

- **Standard format:** 15 January 2024 or 2024-01-15
- **Avoid ambiguous formats:** Not 01/15/24 (US) vs 15/01/24 (UK)
- **Use 24-hour time** for international clarity: 1430 hours
- **Specify time zones** when relevant: 1430 EST

---

## 6. Document Formatting

### Standard Sections

Most intelligence products should include:

1. **Header** - Classification, date, subject, preparer
2. **BLUF/Executive Summary** - Key findings upfront
3. **Key Judgments** - Main analytical conclusions
4. **Background** - Context for understanding
5. **Analysis** - Detailed supporting analysis
6. **Sources** - Documentation of information sources
7. **Confidence Assessment** - Evaluation of certainty
8. **Footer** - Distribution, next review, feedback contact

### Visual Formatting

- **Use headings liberally** - Help readers navigate
- **Bullet points for lists** - Easier to scan than prose
- **Tables for comparisons** - Present structured data clearly
- **Bold for emphasis** - Sparingly, for key terms
- **Consistent formatting** - Same style throughout

### Length Guidelines

| Product Type | Typical Length |
|--------------|----------------|
| Intelligence Brief | 1-2 pages |
| Standard Report | 3-5 pages |
| Assessment | 5-10 pages |
| Comprehensive Profile | 10-20 pages |
| Full Study | 20+ pages |

**Remember:** Length should serve the reader, not demonstrate effort.

---

## 7. Review Checklist

Before finalizing any intelligence product, verify:

### Content
- [ ] BLUF clearly states key finding in opening
- [ ] Key judgments use appropriate confidence language
- [ ] Facts and judgments are clearly distinguished
- [ ] All claims have source citations
- [ ] Alternative views are considered
- [ ] Assumptions are stated
- [ ] Gaps and limitations are acknowledged

### Language
- [ ] Active voice predominates
- [ ] Sentences are concise (average 15-20 words)
- [ ] Probability terms are used consistently
- [ ] Biased or loaded language is removed
- [ ] Jargon is explained or avoided
- [ ] Acronyms are defined on first use

### Format
- [ ] Appropriate sensitivity markings
- [ ] Clear heading structure
- [ ] Consistent formatting throughout
- [ ] Tables and bullets used effectively
- [ ] Date and preparer identified
- [ ] Page numbers included

### Accuracy
- [ ] Names spelled correctly
- [ ] Dates verified
- [ ] Numbers checked
- [ ] URLs tested (if included)
- [ ] Cross-references work

---

## 8. Common Errors to Avoid

### Analytical Errors

1. **Mirror Imaging** - Assuming others think/act as you would
2. **Anchoring** - Over-weighting initial information
3. **Confirmation Bias** - Seeking evidence that confirms existing beliefs
4. **Availability Bias** - Over-weighting readily available information
5. **Groupthink** - Conforming to team consensus without critical analysis

### Writing Errors

1. **Burying the lead** - Key finding not in first paragraph
2. **Unsourced claims** - Statements without attribution
3. **False precision** - Implying certainty that doesn't exist
4. **Ambiguous probability language** - Using "may" or "could" without clarity
5. **Opinion presented as fact** - Judgments without confidence language
6. **Passive voice overuse** - Obscuring who did what
7. **Jargon without explanation** - Assuming reader knowledge

---

## 9. Quick Reference Card

```
BLUF STRUCTURE
--------------
Lead with conclusion -> Support with evidence -> End with implications

PROBABILITY TERMS
-----------------
Almost certainly (95%+) | Very likely (80-95%) | Likely (60-80%)
Roughly even chance (40-60%)
Unlikely (20-40%) | Very unlikely (5-20%) | Almost certainly not (<5%)

CONFIDENCE LEVELS
-----------------
HIGH: Multiple corroborating sources, direct evidence
MODERATE: Credible but not fully corroborated
LOW: Limited sources, significant gaps

SIGNAL PHRASES FOR JUDGMENTS
-----------------------------
"We assess that..." | "We judge that..." | "Analysis indicates..."
"Evidence suggests..." | "This likely means..."

SOURCE RELIABILITY
------------------
A: Completely reliable | B: Usually reliable | C: Fairly reliable
D: Not usually reliable | E: Unreliable | F: Cannot judge

INFORMATION VALIDITY
--------------------
1: Confirmed | 2: Probably true | 3: Possibly true
4: Doubtful | 5: Improbable | 6: Cannot judge
```

---

## Related Documents

- [Intelligence Report Template](intelligence-report-template.md) - Standard report format
- [Assessment Template](assessment-template.md) - Assessment format with examples
- [Person of Interest Template](person-of-interest-template.md) - Individual profiles
- [Organization Profile Template](organization-profile-template.md) - Organization analysis

---

*These standards are based on the CIA Writing Guide, DIA Style Manual for Intelligence Products, ODNI Style Manual, Army Intelligence Center of Excellence Writing Guide, NSA SIGINT Style Manual, and Tradecraft Primer for Structured Analytic Techniques. See the [PDF Library Index](../references/pdf-library-index.md) for source documents.*
