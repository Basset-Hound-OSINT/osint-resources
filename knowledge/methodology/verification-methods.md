# Verification Methods for OSINT

Verification is the process of confirming the accuracy, authenticity, and reliability of information. This document provides systematic methods for verifying OSINT findings, with particular emphasis on digital content verification.

## Overview

Verification serves multiple purposes:
- Confirm accuracy before acting on intelligence
- Detect manipulation, fabrication, or deception
- Build confidence in analytical judgments
- Meet evidentiary or reporting standards
- Protect against disinformation

---

## Core Verification Principles

### The Three C's of Verification

| Principle | Description | Questions |
|-----------|-------------|-----------|
| **Corroboration** | Multiple independent sources confirm | How many sources? Are they truly independent? |
| **Consistency** | Information aligns with known facts | Does it fit the broader picture? Any contradictions? |
| **Credibility** | Information is plausible and logical | Could this be true? Does it make sense? |

### Levels of Verification

| Level | Description | Requirements |
|-------|-------------|--------------|
| **Unverified** | Single source, no confirmation | Flag as unverified |
| **Partially Verified** | Some corroboration, some gaps | Note what is/isn't verified |
| **Verified** | Multiple independent sources confirm key facts | Document verification path |
| **Confirmed** | Primary source documentation or direct evidence | Highest confidence |

---

## Cross-Referencing Techniques

### Source Triangulation

Confirm information using three or more independent sources:

```
Source Triangulation:
├── Primary Source
│   └── Original document, direct witness
├── Secondary Source 1
│   └── Independent report, different origin
└── Secondary Source 2
    └── Another independent source

Requirement: Sources must be truly independent
(not citing each other or common source)
```

### Independence Assessment

Before counting sources as corroborating, verify independence:

| Check | Question | Red Flag |
|-------|----------|----------|
| Origin tracing | Where did each source get this information? | Sources trace to common origin |
| Timing | When did each source report? | All appeared simultaneously |
| Wording | Is the language identical? | Copy-paste or direct quotation |
| Perspective | Do sources have different vantage points? | Same perspective or affiliation |

### Cross-Reference Matrix

Document cross-referencing systematically:

| Claim | Source 1 | Source 2 | Source 3 | Assessment |
|-------|----------|----------|----------|------------|
| Subject DOB: 1985-03-15 | Public records (A1) | Social media (B2) | N/A | Verified |
| Subject employed at X | LinkedIn (B2) | Company website (B2) | News article (C3) | Verified |
| Subject owns property at Y | Property records (A1) | N/A | N/A | Single source |

---

## Corroboration Standards

### Minimum Standards by Use Case

| Use Case | Minimum Corroboration | Rationale |
|----------|----------------------|-----------|
| Informal intelligence | Single source acceptable (with caveats) | Speed over certainty |
| Formal assessment | Two independent sources | Balance of rigor and practicality |
| Accusatory findings | Three+ independent sources | Higher standard for serious claims |
| Legal/evidentiary | Primary documentation or testimony | Courtroom standards |
| Publication | Subject matter expert review | Reputational protection |

### Corroboration Quality Factors

Not all corroboration is equal:

| Factor | Stronger | Weaker |
|--------|----------|--------|
| Source independence | Truly separate origins | Common ultimate source |
| Source type diversity | Different types (records, media, social) | Same type |
| Source reliability | High-reliability sources | Low-reliability sources |
| Detail agreement | Specific details match | Only general facts match |
| Timing | Near-contemporaneous | Significant time gaps |

### Documenting Corroboration

```markdown
## Corroboration Record

**Claim**: [Statement being verified]

**Primary Source**:
- Source: [Description]
- Rating: [Admiralty rating]
- Details provided: [Specific information]

**Corroborating Source 1**:
- Source: [Description]
- Rating: [Admiralty rating]
- Independence verified: [Yes/No and how]
- Details confirmed: [Specific information]

**Corroborating Source 2**:
- Source: [Description]
- Rating: [Admiralty rating]
- Independence verified: [Yes/No and how]
- Details confirmed: [Specific information]

**Discrepancies**: [Any differences between sources]
**Resolution**: [How discrepancies were resolved]
**Verification Status**: [Verified/Partially verified/Unverified]
```

---

## Fact-Checking Workflows

### Basic Fact-Check Process

```
1. Identify the Claim
   └── What specific assertion needs verification?

2. Trace to Source
   └── Where does this claim originate?

3. Evaluate the Source
   └── Apply source evaluation framework

4. Seek Corroboration
   └── Find independent confirming sources

5. Check for Contradiction
   └── Look for disconfirming evidence

6. Assess and Document
   └── Record verification status and confidence
```

### Claim Deconstruction

Break complex claims into verifiable components:

**Original Claim**: "John Smith, former CIA officer, published a book in 2020 revealing secret operations."

| Component | Verification Method | Status |
|-----------|---------------------|--------|
| Person named John Smith exists | Identity verification | Verified |
| John Smith was CIA officer | Official records, media, biography | Partially verified |
| Published a book | Publisher records, ISBN lookup | Verified |
| Published in 2020 | Publication date records | Verified |
| Book reveals secret operations | Content review | Subjective claim |

### Red Flags Checklist

Watch for indicators of false or manipulated information:

| Category | Red Flags |
|----------|-----------|
| **Source** | Anonymous, no track record, known for unreliability |
| **Origin** | Cannot trace to original source, circular references |
| **Timing** | Conveniently timed, appeared suddenly everywhere |
| **Content** | Too good to be true, confirms biases perfectly |
| **Details** | Vague on specifics, verifiable details wrong |
| **Spread** | Amplified by suspicious accounts, coordinated sharing |
| **Response** | Official denial with specifics, expert debunking |

---

## Digital Content Verification

### Image Verification

#### Authenticity Checks

| Check | Method | Tools |
|-------|--------|-------|
| **Reverse image search** | Find original and variations | Google Images, TinEye, Yandex |
| **Metadata analysis** | Extract EXIF data | ExifTool, Jeffrey's EXIF Viewer |
| **Manipulation detection** | Analyze for editing | FotoForensics, Forensically |
| **Consistency analysis** | Check lighting, shadows, perspective | Manual visual inspection |
| **Context verification** | Match image to claimed context | Cross-reference with known images |

#### Image Verification Workflow

```
1. Save Original
   └── Preserve unmodified copy with hash

2. Reverse Image Search
   ├── Google Images
   ├── TinEye
   ├── Yandex Images
   └── Bing Visual Search
   Result: Find original source, prior uses

3. Metadata Extraction
   └── ExifTool or online extractors
   Result: Camera, date, location, editing software

4. Manipulation Analysis
   ├── Error Level Analysis (ELA)
   ├── Clone detection
   └── Metadata consistency
   Result: Signs of editing

5. Visual Consistency
   ├── Lighting direction
   ├── Shadow analysis
   ├── Perspective/scale
   └── Edge analysis
   Result: Physical plausibility

6. Context Verification
   └── Match to claimed time, location, event
   Result: Context accuracy
```

#### Common Image Manipulation Types

| Type | Description | Detection Method |
|------|-------------|------------------|
| Cropping | Removing context | Reverse search for full image |
| Splicing | Combining images | ELA, edge analysis |
| Cloning | Duplicating elements | Clone detection tools |
| Retouching | Altering details | ELA, metadata |
| AI generation | Synthetic images | AI detection tools, artifacts |
| Recontextualization | Old image, new claim | Reverse search, metadata date |

### Video Verification

#### Authentication Checks

| Check | Method | Notes |
|-------|--------|-------|
| **Reverse video search** | Find original | InVID, YouTube search |
| **Keyframe extraction** | Analyze still frames | InVID, ffmpeg |
| **Metadata analysis** | Extract video metadata | MediaInfo, ffprobe |
| **Audio analysis** | Check audio track | Separate analysis |
| **Temporal analysis** | Check for edits/jumps | Frame-by-frame review |
| **Context verification** | Match claimed context | Cross-reference |

#### Video Verification Tools

- **InVID Verification Plugin**: Browser extension for video analysis
- **YouTube DataViewer**: Amnesty International tool
- **ffmpeg**: Command-line video analysis
- **MediaInfo**: Metadata extraction

#### Video Red Flags

| Indicator | Possible Issue |
|-----------|----------------|
| Sudden frame jumps | Editing, removal of content |
| Audio/video mismatch | Dubbed audio, manipulation |
| Inconsistent quality | Spliced from multiple sources |
| No metadata | Stripped intentionally |
| Compressed heavily | Multiple re-encodings, degradation |

### Document Verification

#### Document Authentication

| Check | Method | Purpose |
|-------|--------|---------|
| **Format analysis** | Check document structure | Detect recreation |
| **Metadata extraction** | Author, dates, software | Verify provenance |
| **Typography analysis** | Fonts, spacing, alignment | Detect anachronisms |
| **Content verification** | Verify named facts | Internal consistency |
| **Signature/seal analysis** | Compare to known authentic | Detect forgery |
| **Paper/printing analysis** | Physical examination | For physical documents |

#### Document Metadata

| Metadata Field | Verification Use |
|----------------|------------------|
| Author | Who created the document |
| Creation date | When originally created |
| Modification date | When last changed |
| Software | What application created it |
| Company | Organization metadata |
| Revision count | How many times edited |

#### PDF-Specific Checks

```
PDF Verification:
├── Extract and compare metadata
│   └── pdfinfo, ExifTool
├── Check for embedded objects
│   └── Hidden content, scripts
├── Analyze fonts
│   └── Consistent with claimed date?
├── Compare to official formats
│   └── Does formatting match known authentic documents?
└── Verify digital signatures
    └── Certificate validity
```

---

## Geolocation Verification

### Purpose

Confirm that images or videos were taken at the claimed location.

### Geolocation Techniques

#### 1. Metadata-Based

- Extract GPS coordinates from EXIF data
- Verify coordinates match claimed location
- Note: Often stripped from shared images

#### 2. Visual Feature Matching

| Feature Type | Examples | Verification Method |
|--------------|----------|---------------------|
| Landmarks | Buildings, monuments, signs | Match to satellite/street view |
| Infrastructure | Roads, bridges, power lines | Match to maps |
| Natural features | Mountains, rivers, vegetation | Match to terrain |
| Signage | Language, style, content | Regional identification |
| Vehicles | License plates, vehicle types | Regional identification |
| Sky | Sun position, shadows | Time/location calculation |

#### 3. Shadow Analysis

Use shadows to determine:
- Time of day (shadow length and direction)
- Approximate latitude (with date)
- Verify against claimed time

Tools: SunCalc, Shadow Calculator

#### 4. Satellite Imagery Comparison

1. Identify potential location
2. Find satellite imagery of that location
3. Compare features visible in image
4. Account for temporal changes

Platforms: Google Earth, Sentinel Hub, Planet Labs, Maxar

### Geolocation Workflow

```
1. Initial Assessment
   ├── What location is claimed?
   ├── What visible features can be identified?
   └── Is there metadata with coordinates?

2. Feature Identification
   ├── List all identifiable features
   ├── Prioritize unique/distinctive features
   └── Note feature relationships (relative positions)

3. Hypothesis Generation
   ├── Based on features, what locations are possible?
   └── Use context clues to narrow region

4. Verification
   ├── Search for candidate locations
   ├── Compare imagery (satellite, street view)
   ├── Verify feature alignment
   └── Check for temporal consistency

5. Confirmation
   ├── Multiple features match
   ├── Relative positions correct
   └── No contradicting evidence
```

### Chronolocation

Determine when an image was taken:

| Method | Data Used | Precision |
|--------|-----------|-----------|
| Metadata | EXIF date/time | Exact (if not manipulated) |
| Shadow analysis | Shadow length/direction | Hour of day |
| Weather correlation | Visible weather conditions | Match to weather records |
| Seasonal indicators | Vegetation, snow, daylight | Season |
| Event markers | Datable events in image | Date of event |
| Construction/development | Building state | Before/after construction date |

---

## Social Media Verification

### Account Authentication

| Check | Method | Purpose |
|-------|--------|---------|
| Verification status | Platform verification badge | Official identity confirmation |
| Account age | Creation date | Established vs. new account |
| Posting history | Pattern analysis | Consistent behavior |
| Follower analysis | Quality of followers | Bot networks vs. real |
| Cross-platform presence | Same identity elsewhere | Identity consistency |
| Bio verification | Check claimed credentials | Verify stated identity |

### Content Verification

| Check | Method | Purpose |
|-------|--------|---------|
| Original vs. shared | Trace to original post | Find primary source |
| Timestamp verification | Compare to event timeline | Temporal consistency |
| Location claims | Geolocation techniques | Verify claimed location |
| Image/video verification | Digital forensics | Detect manipulation |
| Quote verification | Find original statement | Accuracy of attribution |

### Viral Content Verification

For rapidly spreading content:

1. **Find the origin**: When/where was it first posted?
2. **Analyze spread pattern**: Organic or coordinated?
3. **Check debunking**: Have fact-checkers addressed it?
4. **Verify key claims**: Apply standard verification
5. **Assess motive**: Who benefits from this spreading?

---

## Verification Documentation

### Verification Record Template

```markdown
## Verification Record

**Item**: [Description of content being verified]
**Source**: [Where obtained]
**Claimed context**: [What is claimed about the content]
**Date of verification**: [Date]
**Analyst**: [Who verified]

### Verification Steps Performed

1. [Step]: [Result]
2. [Step]: [Result]
3. [Step]: [Result]

### Findings

**Authenticity**: [Authentic / Modified / Fabricated / Unknown]
**Context accuracy**: [Accurate / Misleading / False / Unknown]
**Confidence**: [High / Medium / Low]

### Evidence

- [Evidence item 1]
- [Evidence item 2]

### Discrepancies or Concerns

- [Issue 1]
- [Issue 2]

### Conclusion

[Summary of verification findings]
```

### Archival for Verification

Preserve evidence for verification:

| What to Preserve | How | Why |
|------------------|-----|-----|
| Original file | Download, do not screenshot | Preserve metadata |
| URL | Copy full URL | Citation |
| Screenshot | Full page with URL visible | Backup if removed |
| Hash | SHA-256 of original file | Prove authenticity |
| Timestamp | Record access time (UTC) | Temporal record |
| Archive link | Archive.org, archive.today | Permanent reference |

---

## Verification Resources and Tools

### General Verification

| Tool | Purpose | URL |
|------|---------|-----|
| InVID WeVerify | Video/image verification | Browser extension |
| Google Fact Check Tools | Search fact-checks | factchecktools.google.com |
| Snopes | Fact-checking database | snopes.com |
| Full Fact | Fact-checking (UK) | fullfact.org |

### Image Verification

| Tool | Purpose | URL |
|------|---------|-----|
| TinEye | Reverse image search | tineye.com |
| Google Images | Reverse image search | images.google.com |
| Yandex Images | Reverse image search | yandex.com/images |
| FotoForensics | Image forensics | fotoforensics.com |
| Forensically | Image forensics | 29a.ch/photo-forensics |
| ExifTool | Metadata extraction | exiftool.org |

### Video Verification

| Tool | Purpose | URL |
|------|---------|-----|
| InVID | Video analysis | invid-project.eu |
| YouTube DataViewer | YouTube metadata | citizenevidence.amnestyusa.org |
| Downsub | Extract video subtitles | downsub.com |

### Geolocation

| Tool | Purpose | URL |
|------|---------|-----|
| Google Earth Pro | Satellite imagery | earth.google.com |
| Google Street View | Ground-level imagery | maps.google.com |
| SunCalc | Sun position/shadows | suncalc.org |
| Sentinel Hub | Satellite imagery | sentinel-hub.com |
| Wikimapia | Crowdsourced maps | wikimapia.org |

### Archive and Preservation

| Tool | Purpose | URL |
|------|---------|-----|
| Archive.org | Web archive | archive.org |
| Archive.today | Web archive | archive.today |
| Hunchly | OSINT capture | hunch.ly |
| SingleFile | Page archiving | Extension |

---

## Common Verification Challenges

### Challenge: Source Circularity

**Problem**: Multiple sources trace to a single origin.

**Solution**:
- Trace each source back to origin
- Map the citation/sharing network
- Find truly independent sources
- Adjust confidence accordingly

### Challenge: Coordinated Amplification

**Problem**: Disinformation amplified by coordinated networks.

**Solution**:
- Analyze account networks spreading content
- Check for bot indicators
- Trace to original source
- Verify content independently of spread

### Challenge: Deepfakes and AI Content

**Problem**: AI-generated or manipulated content increasingly sophisticated.

**Solution**:
- Use AI detection tools
- Look for visual artifacts
- Verify through non-visual means
- Corroborate with reliable sources

### Challenge: Stripped Metadata

**Problem**: Metadata removed by platforms or intentionally.

**Solution**:
- Use visual verification techniques
- Seek original source with metadata
- Apply multiple verification methods
- Document metadata absence

---

## References

### Primary Sources (PDF Library)

- [TII Online Research Framework](../references/pdf-library-index.md) - Verification workflows
- [TII Online Investigators Checklist](../references/pdf-library-index.md) - Practical verification steps
- [Critical Thinking and Intelligence Analysis](../references/pdf-library-index.md) - Analytical rigor
- [ICD 206 Sourcing Requirements](../references/pdf-library-index.md) - Sourcing standards

### Related Documentation

- [source-evaluation.md](source-evaluation.md) - Source reliability assessment
- [analysis-techniques.md](analysis-techniques.md) - ACH and hypothesis testing
- [collection-planning.md](collection-planning.md) - Collection for verification

### External Resources

- Bellingcat Online Investigation Toolkit
- First Draft Verification Handbook
- Amnesty International Digital Verification Corps

---

*Document Version: 1.0*
*Last Updated: 2025-12-28*
*Status: Active*
