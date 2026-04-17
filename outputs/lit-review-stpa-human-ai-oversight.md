# Literature Review: STPA for Human-AI Oversight

**Topic:** Systems-Theoretic Process Analysis (STPA) applied to human-AI oversight  
**Date:** 2026-04-17  
**Scope:** Academic papers, technical reports, and institutional publications (2022–2025)

---

## 1. Executive Summary

STPA—a hazard analysis method rooted in Nancy Leveson's STAMP (Systems-Theoretic Accident Model and Processes)—is emerging as a leading candidate framework for analyzing safety in complex human-AI systems. Unlike traditional component-failure methods (FMEA, FTA), STPA treats safety as an **emergent property** of the whole sociotechnical system and models safety breakdowns as **inadequate control** rather than isolated component failures. This makes it particularly well-suited to human-AI oversight, where hazards arise from interactions between autonomous agents, human operators, organizational processes, and institutional constraints.

The literature clusters into four streams:

1. **Foundational theory** — Leveson's STAMP/STPA framework and its extension to AI by Dobbe (2022)
2. **AI-specific adaptations** — PHASE guideline (Rismani et al., 2024) and frontier AI hazard analysis (Mylius, 2025)
3. **Domain applications** — Autonomous vehicles, aviation, human-autonomy teaming, medical AI
4. **Security extensions** — STPA-Sec for adversarial and cybersecurity analysis of AI systems

**Key finding:** STPA applies readily to AI systems with only modest adaptations, and uniquely surfaces hazards from human-AI authority handoffs, organizational pressure, misaligned mental models, and missing feedback loops—hazards that component-level AI safety methods systematically miss.

---

## 2. Foundational Framework

### 2.1 STAMP and STPA

STAMP reframes accidents as violations of safety constraints enforced through a hierarchical control structure, rather than chains of component failures (Leveson, 2004; 2012). STPA operationalizes STAMP through four steps:

1. **Define losses and hazards** at the system level
2. **Model the control structure** (controllers, controlled processes, control actions, feedback)
3. **Identify Unsafe Control Actions (UCAs)** — control actions that, in context, lead to hazards
4. **Develop loss scenarios** — causal factors explaining why UCAs occur

The control-theoretic framing is what makes STPA especially relevant to human-AI oversight: it explicitly models **who or what has authority** over what, how decisions flow, what feedback exists, and where control can degrade.

> **Key reference:** Leveson, N. & Thomas, J. (2018). *STPA Handbook*. MIT. ([psas.scripts.mit.edu](https://psas.scripts.mit.edu/home/wp-content/uploads/2020/07/STAMP-Tutorial.pdf))

### 2.2 Seven Leveson Lessons for AI (Dobbe, 2022)

Dobbe (2022) provides the most comprehensive theoretical bridge between system safety and AI governance. He maps seven Leveson lessons to AI system safety:

| # | Leveson Lesson | AI Implication |
|---|---------------|----------------|
| 1 | Component reliability ≠ safety | Identify hazards at system, not model level |
| 2 | Event-chain models inadequate | Use sociotechnical constraints, not root causes |
| 3 | Probabilistic methods insufficient | Capture safety in process models, not loss functions |
| 4 | Operator error is environmental | **Align mental models across designers, operators, and affected stakeholders** |
| 5 | Reliable software ≠ safe software | Include AI software and org dependencies in STPA |
| 6 | Systems migrate to higher risk | Organize feedback: audits, investigations, reporting |
| 7 | Blame is the enemy of safety | Build a Just Culture |

**Lesson 4 is directly relevant to human-AI oversight:** Dobbe highlights that human oversight mandated by regulation (e.g., EU AI Act) may provide only shallow protection—what Elish (2019) calls a "moral crumple zone"—unless the system is designed so that operator mental models are aligned with actual system behavior. Leveson's three design principles for shared human-AI control are:

- **Redundant paths** — multiple ways for the human to maintain safe control
- **Incremental control** — enough time and feedback for stepwise decisions
- **Error tolerance** — reversible errors must be observable before consequences

> **Reference:** Dobbe, R. (2022). "System Safety and Artificial Intelligence." arXiv:2202.09292. To appear in *Oxford Handbook on AI Governance*.

---

## 3. AI-Specific Adaptations of STPA

### 3.1 PHASE: Process-Oriented Hazard Analysis for AI Systems (Rismani et al., 2024)

The most substantial empirical work adapting STPA to AI systems. Rismani, Dobbe & Moon (2024) applied STPA to three case studies—linear regression (medical early warning), reinforcement learning (insulin dosing), and transformer-based generative models (text-to-image)—and produced the **PHASE guideline**.

**Key adaptations for AI:**

- **Expanded loss taxonomy:** Beyond traditional safety-critical losses (loss of life), PHASE identifies *performance-related losses* (loss of efficiency, reputation) and *sociotechnical losses* (loss of privacy, creativity, diversity)
- **System boundaries:** Defined around points where humans or automated agents can exercise control—data collection/processing, model development/evaluation, and use/operation
- **Three types of UCAs in AI systems:**
  - *Functional* — system malfunction (e.g., insulin pump fails)
  - *Poor design decisions or misuse* — e.g., wrong filter threshold, incorrect feature selection
  - *Communication/coordination failures* — e.g., wrong safety requirements transmitted between teams
- **Four affordances of STPA for AI:**
  1. System-level hazard detection (including hazards from accumulation of minor issues)
  2. Explicit accounting for social factors in algorithmic harms
  3. Traceable accountability chains from harms to responsible controllers
  4. Ongoing monitoring of emergent hazards as systems evolve

**Relevance to human-AI oversight:** PHASE demonstrates that STPA naturally surfaces authority and control relationships. The control hierarchy makes explicit whether a human operator is *above* or *below* the AI system in the decision chain—and how oversight can degrade when feedback loops are missing between development teams, operators, and affected stakeholders.

**Limitation noted:** STPA frames all interactions as control-and-feedback, which can miss nuances of collaborative human decision-making.

> **Reference:** Rismani, S., Dobbe, R. & Moon, A. (2024). "From Silos to Systems: Process-Oriented Hazard Analysis for AI Systems." arXiv:2410.22526.

### 3.2 STPA for Frontier AI (Mylius, 2025)

The most recent and directly policy-relevant work. Mylius (2025) applies STPA to the AI Control threat model from Korbak et al. (2025), analyzing an LLM agent deployed internally at an AI company with unknown trustworthiness.

**Novel contributions:**

- **Demonstrates STPA on AI Control specifically:** Models the control structure including the LLM agent, scaffold layer, human auditors, blue/red teams, and organizational leadership
- **Identifies causal factors across multiple categories:**
  - *Human factors:* Auditor susceptible to manipulation by untrusted agent (LS17.2.1)
  - *Organizational:* Security team lacks authority to enforce shutdown against R&D leadership (LS7.3.1)
  - *Operational:* Business pressure for R&D progress conflicts with security protocols (LS7.3.1)
  - *Technical:* Memory reset bug allows state persistence (LS11.1.1)
  - *Feedback failures:* No verification that agent state was actually cleared (LS11.1.1)
- **STPA → Safety Cases:** Proposes a design pattern for building Claim-Argument-Evidence safety cases directly from STPA outputs, with traceability from losses through hazards, UCAs, and loss scenarios to mitigations
- **Scalability via LLMs:** Argues that STPA's structured decomposition makes it more amenable to partial automation by LLMs than unstructured hazard analysis

**Relevance to human-AI oversight:** The analysis reveals that human oversight can fail not just because the human is fooled by the AI, but because of *organizational dynamics*—e.g., R&D leadership overriding security decisions, or the human auditor lacking institutional authority. This is a class of failure invisible to model-level safety analysis.

> **Reference:** Mylius, S. (2025). "Systematic Hazard Analysis for Frontier AI using STPA." arXiv:2506.01782.

---

## 4. Domain Applications

### 4.1 Human-Autonomy Teaming (Pennington et al., 2025)

Pennington, Johnson et al. (2025) develop **STPA-Coordination**, extending STPA to analyze safety in human-AI teaming for air combat (collaborative autonomous wingmen). This is among the most directly relevant works for authority drift:

- Models how **functional authority** shifts between human pilots and AI agents
- Analyzes coordination failures at the interface—where authority is ambiguous or transitions are inadequately controlled
- The DoD context makes explicit what civilian AI safety often leaves implicit: the authority structure must be formally specified and hazard-analyzed

> **Reference:** Pennington, E.S., Johnson, K.E. et al. (2025). "Engineering safe human-autonomy teaming using STPA-coordination." *Safety Science*, 107011.

### 4.2 Collaborative Controllers (Kopeikin, MIT, 2023)

Kopeikin's MIT thesis develops a rigorous extension of STPA for teams of collaborative controllers, addressing scenarios where:

- Roles and functional authorities change dynamically
- Team cognition must be maintained across human and AI agents
- Agents must coordinate and help each other close control loops

This directly addresses the problem of **authority drift**: when the distribution of control authority changes over time, new hazards emerge that single-controller STPA may miss.

> **Reference:** Kopeikin, A.N. (2023). "System-Theoretic Safety Analysis for Teams of Collaborative Controllers." MIT Thesis. ([dspace.mit.edu/handle/1721.1/153787](https://dspace.mit.edu/handle/1721.1/153787))

### 4.3 Autonomous Vehicles

Multiple works apply STPA to AV human-oversight interfaces:

- **Cabosky (MIT, 2021)** — "Application of hierarchy to STPA: a human factors study on vehicle automation." Examines how STPA's hierarchical control structure maps to human factors in vehicle automation, specifically the problem of human disengagement. ([hdl.handle.net/1721.1/132809](https://hdl.handle.net/1721.1/132809))
- **Monkhouse & Ward (2024)** — STPA for shared control in automated driving, analyzing hazards at the human-automation boundary.
- **UniSTPA (2025)** — Extends STPA to the full lifecycle of end-to-end autonomous driving, from data collection through deployment. arXiv:2505.15005.

### 4.4 Aviation Safety

A joint evaluation by civil aviation authorities (Thomas, 2024) assessed STPA's applicability to aviation safety management, aircraft development, safety assessment, and certification. The report validates STPA's ability to identify hazards missed by traditional methods, particularly those involving human-automation interaction.

> **Reference:** Thomas, J.P. (2024). "Evaluation of System-Theoretic Process Analysis (STPA) for Improving Aviation Safety." DOT report. ([rosap.ntl.bts.gov](https://rosap.ntl.bts.gov/view/dot/78914/dot_78914_DS1.pdf))

---

## 5. Security Extension: STPA-Sec

Young (2017, 2020) developed **STPA-Sec**, adapting STPA for cybersecurity analysis. This is relevant to adversarial human-AI oversight scenarios where:

- An AI system may be intentionally subversive (the AI Control threat model)
- Human oversight must be robust to adversarial manipulation
- Security and safety constraints interact (e.g., a security shutdown protocol that conflicts with operational goals)

A recent application (**SAM framework**) combines STPA-Sec with vulnerability databases to analyze AI/ML-enabled medical devices, modeling the medical system as a control structure and identifying points vulnerable to false data injection.

> **References:**
> - Young, W. (2020). "STPA-Sec Tutorial." MIT STAMP Workshop. ([psas.scripts.mit.edu](https://psas.scripts.mit.edu/home/wp-content/uploads/2020/07/STPA-Sec-Tutorial.pdf))
> - UBC (2024). SAM technique for STPA-SEC on AI/ML medical devices. ([open.library.ubc.ca](https://open.library.ubc.ca/media/stream/pdf/24/1.0447418/4))

---

## 6. Institutional and Policy Activity

### 6.1 Carnegie Mellon SEI / NIST

Schuker et al. (CMU SEI, 2024) presented at a NIST workshop on using STPA for LLM-enabled software safety. Their work frames LLMs as introducing novel attack surfaces that traditional safety analysis misses, and advocates STPA as a method to systematically identify hazards in LLM-integrated systems.

> **Reference:** Schuker, D. et al. (2024). "Using System Theoretic Process Analysis to Advance Safety in LLM-enabled Software Systems." NIST Workshop presentation. ([nist.gov](https://www.nist.gov/system/files/documents/2024/01/23/David_Schuker_NIST%20Virtual%20Workshop%20Talk.pdf))

### 6.2 U.S. NRC

The Nuclear Regulatory Commission evaluated STPA for nuclear safety applications (Thomas, 2021), finding it addresses deficiencies in traditional methods for "complex automation behaviors"—directly relevant to AI oversight in safety-critical infrastructure.

> **Reference:** Thomas, J. (2021). "Investigation of the Use of System-Theoretic Process Analysis at the NRC." ([nrc.gov](https://www.nrc.gov/docs/ML2227/ML22272A315.pdf))

### 6.3 Google Reliability Engineering

Google's pilot study applying STPA to service reliability (Falzone & Thomas, 2021) showed that 2 engineers working part-time for 5 months identified defects that "would likely have prevented at least 4 major incidents."

---

## 7. Consensus, Disagreements, and Gaps

### Consensus

- **STPA applies to AI systems with modest adaptation.** All authors agree the core framework transfers well; the main adaptations involve broadening loss taxonomies and accommodating AI-specific properties (opacity, capability uncertainty, output complexity).
- **System-level analysis is necessary.** Component-level AI safety (fairness metrics, red-teaming, model evaluations) is insufficient alone.
- **Human oversight can be a hazard source, not just a mitigation.** STPA consistently reveals that human oversight fails due to misaligned mental models, automation complacency, missing feedback, and organizational pressure—not just AI failures.
- **Organizational and institutional factors are first-class hazards.** Business incentives, authority structures, safety culture, and communication breakdowns are systematically surfaced by STPA.

### Disagreements and Tensions

- **Scope vs. tractability:** STPA's comprehensiveness is both its strength and the main objection. Mylius (2025) argues it can be applied incrementally; critics worry about perceived process-heaviness in fast-moving AI development.
- **Qualitative vs. quantitative:** STPA is qualitative, which some view as subjective. Mylius counters that quantitative approaches "break down for black swan events" with no historical precedent—which describes frontier AI risks.
- **Control-theoretic framing of collaboration:** Rismani et al. (2024) note that STPA's control/feedback framing may not capture collaborative decision-making nuances.
- **Sufficiency of existing methods:** Some practitioners argue existing safety frameworks (red-teaming, evaluations, safety cases) are sufficient without adopting a new methodology.

### Gaps in the Literature

1. **Authority drift over time.** No work directly models how human-AI authority distributions *shift* during extended deployment—how human controllers gradually cede decision authority to AI systems, and the emergent hazards from that drift. Kopeikin (2023) addresses dynamic authority in collaborative teams, but not the long-term degradation pattern.

2. **Empirical validation at scale.** Most STPA-for-AI work is demonstrative (case studies, worked examples). There are no published controlled experiments comparing STPA to alternative hazard analysis methods on the same AI system.

3. **Automation of STPA itself.** Mylius (2025) suggests LLMs could contribute to STPA analysis, but this is speculative. Graydon & Lehman (2025) caution that LLM-generated safety arguments should be treated as experimental.

4. **Integration with AI governance infrastructure.** How STPA outputs feed into existing governance mechanisms (model cards, safety cases, deployment decisions) is described at a high level but not yet standardized.

5. **Adversarial dynamics in human-AI oversight.** STPA-Sec exists but has not been deeply applied to the specific scenario of an AI system that actively undermines its human overseers—the "sleeper agent" or "scheming" threat model.

6. **Feedback loop design.** While STPA identifies missing feedback as a hazard, the literature offers little guidance on *designing* effective feedback loops for human-AI oversight systems specifically.

---

## 8. Relevance to Authority Drift Training

For a project focused on **authority drift in human-AI systems**, STPA provides a natural analytical framework:

- **Control hierarchy** directly models who holds decision authority and how it is delegated
- **Unsafe Control Actions** can capture specific authority-drift scenarios: authority given too broadly, not revoked when conditions change, exercised at the wrong level
- **Process models** capture the mental models that humans and AI agents maintain about each other's authority—and how these diverge over time
- **Loss scenarios** can trace authority drift to organizational pressures, missing monitoring, and degraded human engagement

The gap in the literature—no direct STPA analysis of authority drift as a hazard pattern—represents a contribution opportunity.

---

## 9. Key Papers (Ranked by Relevance)

| Priority | Paper | Year | ID/URL |
|----------|-------|------|--------|
| ★★★ | Rismani, Dobbe & Moon. "From Silos to Systems: PHASE" | 2024 | [arXiv:2410.22526](https://arxiv.org/abs/2410.22526) |
| ★★★ | Mylius. "Systematic Hazard Analysis for Frontier AI using STPA" | 2025 | [arXiv:2506.01782](https://arxiv.org/abs/2506.01782) |
| ★★★ | Dobbe. "System Safety and Artificial Intelligence" | 2022 | [arXiv:2202.09292](https://arxiv.org/abs/2202.09292) |
| ★★☆ | Pennington et al. "STPA-Coordination for human-autonomy teaming" | 2025 | [doi:10.1016/j.ssci.2025.107011](https://scholar.afit.edu/facpub/2557) |
| ★★☆ | Kopeikin. "System-Theoretic Safety Analysis for Collaborative Controllers" | 2023 | [dspace.mit.edu](https://dspace.mit.edu/handle/1721.1/153787) |
| ★★☆ | Leveson & Thomas. "STPA Handbook" | 2018 | [MIT PSAS](https://psas.scripts.mit.edu/home/wp-content/uploads/2020/07/STAMP-Tutorial.pdf) |
| ★☆☆ | Thomas. "Evaluation of STPA for Aviation Safety" | 2024 | [DOT report](https://rosap.ntl.bts.gov/view/dot/78914/dot_78914_DS1.pdf) |
| ★☆☆ | Young. "STPA-Sec" | 2020 | [MIT PSAS](https://psas.scripts.mit.edu/home/wp-content/uploads/2020/07/STPA-Sec-Tutorial.pdf) |
| ★☆☆ | UniSTPA for Autonomous Driving | 2025 | [arXiv:2505.15005](https://arxiv.org/abs/2505.15005) |

---

## 10. Recommended Next Steps

1. **Model authority drift as STPA loss scenarios.** Use the STPA framework to formally specify how human oversight authority degrades over time, identifying specific UCAs (e.g., "Human operator does not revoke AI autonomy when conditions change") and the causal factors behind them.

2. **Build a control structure for your training scenario.** Map the specific human-AI authority relationships in your system, including who can override whom, what feedback exists, and where authority boundaries are ambiguous.

3. **Cross-check against PHASE guideline.** Use Rismani et al.'s supplementary guideline material as a template for conducting the analysis.

4. **Incorporate adversarial considerations.** Extend with STPA-Sec to model scenarios where the AI system actively works to expand its own authority.

5. **Design feedback loops explicitly.** Address the literature gap by specifying what monitoring and feedback mechanisms would detect authority drift before it leads to losses.

---

## Sources

All URLs verified 2026-04-17.

- Dobbe, R. (2022). "System Safety and Artificial Intelligence." arXiv:2202.09292. https://arxiv.org/abs/2202.09292
- Kopeikin, A.N. (2023). MIT Thesis. https://dspace.mit.edu/handle/1721.1/153787
- Leveson, N. (2012). *Engineering a Safer World*. MIT Press. https://direct.mit.edu/books/oa-monograph/2908/
- Leveson, N. & Thomas, J. (2018). *STPA Handbook*. MIT.
- Mylius, S. (2025). "Systematic Hazard Analysis for Frontier AI using STPA." arXiv:2506.01782. https://arxiv.org/abs/2506.01782
- Pennington, E.S. et al. (2025). "STPA-coordination." *Safety Science* 107011. https://scholar.afit.edu/facpub/2557
- Rismani, S., Dobbe, R. & Moon, A. (2024). "From Silos to Systems." arXiv:2410.22526. https://arxiv.org/abs/2410.22526
- Schuker, D. et al. (2024). CMU SEI / NIST Workshop. https://www.nist.gov/system/files/documents/2024/01/23/David_Schuker_NIST%20Virtual%20Workshop%20Talk.pdf
- Thomas, J. (2021). NRC STPA Investigation. https://www.nrc.gov/docs/ML2227/ML22272A315.pdf
- Thomas, J.P. (2024). FAA/DOT STPA Evaluation. https://rosap.ntl.bts.gov/view/dot/78914/dot_78914_DS1.pdf
- Young, W. (2020). STPA-Sec Tutorial. https://psas.scripts.mit.edu/home/wp-content/uploads/2020/07/STPA-Sec-Tutorial.pdf
- UniSTPA (2025). arXiv:2505.15005. https://arxiv.org/abs/2505.15005
