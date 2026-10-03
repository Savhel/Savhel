<div align="center">

<img src="./assets/banner.svg" alt="Savio Tsafack — Distributed Systems, Intelligent Systems & AI" width="100%" />

<br/>

<img src="https://img.shields.io/badge/Distributed%20Systems-0F172A?style=for-the-badge" />
<img src="https://img.shields.io/badge/Systems%20Engineering-111827?style=for-the-badge" />
<img src="https://img.shields.io/badge/AI%20%7C%20ML%20%7C%20DL-1D4ED8?style=for-the-badge" />
<img src="https://img.shields.io/badge/Intelligent%20Systems-4F46E5?style=for-the-badge" />
<img src="https://img.shields.io/badge/Expert%20%26%20Multi--Agent%20Systems-6D28D9?style=for-the-badge" />

</div>

# `Savio Tsafack // @Savhel`

I am a computer engineering student working at the intersection of **distributed systems, operating systems, virtualization, intelligent systems and artificial intelligence**.

My main interest is not a single framework or programming language. I am interested in **how complex computing systems manage resources, communicate, adapt, make decisions and remain observable under real constraints**.

That leads me naturally toward:

- distributed systems and datacenter engineering;
- operating systems, scheduling and concurrency;
- virtualization, hypervisors and resource isolation;
- intelligent infrastructure and autonomous orchestration;
- machine learning, deep learning and explainable AI;
- expert systems and multi-agent systems;
- signal processing, radar intelligence and embedded sensing;
- GPU computing and AI infrastructure.

---

## `01 // RESEARCH & ENGINEERING IDENTITY`

```yaml
identity:
  field: Computer Engineering

core_domains:
  - Distributed Systems
  - Systems Engineering
  - Operating Systems
  - Virtualization & Cloud Infrastructure
  - Intelligent Systems
  - Artificial Intelligence
  - Machine Learning
  - Deep Learning
  - Explainable AI
  - Expert Systems
  - Multi-Agent Systems

research_direction:
  - adaptive resource management
  - intelligent scheduling
  - distributed memory / compute
  - GPU-as-a-Service
  - AI for infrastructure
  - radar micro-Doppler classification
  - signal processing + learning
  - autonomous datacenter operations
```

---

## `02 // SYSTEMS & DISTRIBUTED COMPUTING`

### 🛰️ [Omega FusionCore / Proxmox](https://github.com/Savhel/Omega_FusionCore_Proxmox)

My strongest public systems project: a resource-management layer for a multi-node Proxmox cluster.

The project explores:

- **remote memory paging** between nodes;
- `userfaultfd`-based page recovery;
- **elastic vCPU scheduling**;
- VM migration under CPU/RAM/GPU pressure;
- cluster-wide placement and rebalancing;
- GPU proxying and remote execution;
- resource policies and admission control;
- cgroup-based I/O control;
- Ceph-backed shared storage;
- monitoring and resource telemetry.

`Linux` `Proxmox` `QEMU/KVM` `Ceph` `cgroups v2` `userfaultfd` `Python`

---

### 🌐 [ProjetReseau](https://github.com/Savhel/ProjetReseau)

Distributed and event-driven resource-management service.

`Java 21` `Spring Boot` `Kafka` `Cassandra` `Redis` `Prometheus` `Docker`

The project reflects another side of distributed systems:

- asynchronous communication;
- distributed data;
- caching;
- event-driven workflows;
- monitoring;
- state and resource management.

---

### 🧵 [Concurrent Sensor Simulation](https://github.com/Savhel/simulation_capteurs)

C++20 concurrent simulation with:

- producer threads;
- synchronized queues;
- mutexes and condition variables;
- bounded / dynamic queues;
- policy switching;
- virtual-time scheduling;
- runtime statistics.

`C++20` `Threads` `Synchronization` `Scheduling`

---

### ⚙️ OS-oriented work

I have also worked on several repositories and exercises around systems fundamentals:

- [`SimulationDePlanificationDesProcessus`](https://github.com/Savhel/SimulationDePlanificationDesProcessus)
- [`SysCall`](https://github.com/Savhel/SysCall)
- [`TraceSysCall`](https://github.com/Savhel/TraceSysCall)
- [`TP_SE`](https://github.com/Savhel/TP_SE)
- [`testMemoire`](https://github.com/Savhel/testMemoire)

These projects form part of my foundation in **processes, memory, system calls, scheduling and operating-system behavior**.

---

## `03 // DATACENTER, VIRTUALIZATION & CLOUD`

A major part of my engineering work has been around **GANDAL**, a student datacenter / cloud infrastructure project.

### Areas explored and implemented

```text
Physical nodes
    │
    ├── Virtualization
    │     ├── Proxmox VE
    │     ├── QEMU / KVM
    │     ├── XCP-ng / Xen
    │     └── Xen Orchestra
    │
    ├── Distributed Storage
    │     ├── Ceph RBD
    │     └── CephFS
    │
    ├── Networking
    │     ├── Open vSwitch
    │     ├── VLAN
    │     ├── VXLAN
    │     ├── SDN
    │     ├── pfSense
    │     └── routing / NAT / DNS
    │
    ├── Platform Services
    │     ├── Kubernetes / K3s
    │     ├── Registry
    │     ├── monitoring
    │     ├── IAM
    │     └── PaaS services
    │
    └── Intelligent Resource Layer
          ├── CPU
          ├── RAM
          ├── GPU
          ├── storage
          └── placement / migration
```

### Related research directions

- Proxmox → **XCP-ng migration strategy**
- Xen / hypervisor architecture
- OpenStack and cloud control planes
- HA and live migration
- reproducible infrastructure
- zero-touch bare-metal provisioning with PXE/iPXE
- resource profiles
- automated pool joining
- infrastructure monitoring and validation

---

## `04 // GPU COMPUTING & INTELLIGENT INFRASTRUCTURE`

I am exploring **GPU-as-a-Service** as an infrastructure problem rather than treating the GPU as a static device attached to one VM.

Research / design themes include:

- PCI passthrough;
- CUDA workers;
- CUDA MPS;
- per-job quotas;
- logical VRAM budgeting;
- priorities and queues;
- central GPU schedulers;
- API-driven job submission;
- NVML-style monitoring;
- multi-tenant accounting;
- IAM integration;
- Prometheus / Grafana observability.

The broader goal is an **intelligent resource layer** able to choose where a workload should run based on CPU, RAM, GPU, storage and system pressure.

---

## `05 // AI, ML, DEEP LEARNING & XAI`

My AI interests are connected to real systems and physical signals.

### Main directions

- classical Machine Learning;
- Deep Learning;
- NLP and sentiment analysis;
- recommendation systems;
- Explainable AI;
- intelligent decision systems;
- AI-assisted resource scheduling;
- signal classification;
- computer-assisted reasoning.

### Current / past AI workspaces

- [`AnalyseDesSentiments`](https://github.com/Savhel/AnalyseDesSentiments)
- [`Traitement-du-signal`](https://github.com/Savhel/Traitement-du-signal)

These repositories need stronger public documentation, but they belong to a broader AI path that also includes signal processing, radar classification and explainability.

---

## `06 // RADAR, SIGNAL PROCESSING & EXPLAINABLE AI`

One of my research directions is **human-presence / activity classification using radar signals**.

Pipeline studied:

```text
Radar Signal
    │
    ▼
Pre-processing
    │
    ▼
Doppler / Micro-Doppler
    │
    ▼
Spectrogram
    │
    ▼
ML / Deep Learning Classification
    │
    ▼
Explainability
    │
    ├── SHAP
    ├── Grad-CAM
    ├── Integrated Gradients
    └── Occlusion
    │
    ▼
Physical Interpretation & Validation
```

Models and methods explored include:

- SVM;
- XGBoost;
- CNN;
- CNN-LSTM;
- spectrogram-based classification;
- robustness / fidelity / stability evaluation;
- explainability grounded in physical radar phenomena.

This is one of the areas where I want to connect **signal processing + deep learning + XAI**.

---

## `07 // EXPERT SYSTEMS & MULTI-AGENT SYSTEMS`

I am also interested in **expert systems and multi-agent architectures** for supervision and autonomous infrastructure management.

In datacenter-oriented work, I have explored roles such as:

- monitoring agents;
- analyzers;
- decision agents;
- auditors;
- simulation agents;
- orchestration agents;
- resource-management agents;
- security agents.

A representative design direction combines:

`Rust` `gRPC` `mTLS / PKI` `Kubernetes / K3s` `Docker` `Proxmox`

The objective is to move from passive monitoring toward **systems that can detect, reason, decide and trigger corrective actions**.

---

## `08 // EMBEDDED SYSTEMS, IoT & INTELLIGENT SENSING`

### Harmony Gloves

A wearable / IoT research project around gesture and sign-language interaction.

Technologies and topics studied:

- ESP32 / ESP32-S3;
- flex sensors;
- MPU-6050 IMU;
- ADC acquisition;
- ESP-NOW;
- Wi-Fi / BLE;
- low-power modes;
- LiPo power management;
- digital filtering;
- EMA / IIR filtering;
- Kalman filtering;
- real-time sensor fusion;
- gesture recognition.

This project connects embedded systems, signal processing and intelligent interfaces.

---

## `09 // ALGORITHMS, OPTIMIZATION & FOUNDATIONS`

My academic work also includes:

- graph theory;
- graph algorithms;
- combinatorial optimization;
- scheduling algorithms;
- routing / network problems;
- travelling-salesman-type problems;
- transportation models;
- resource allocation;
- concurrent programming.

These topics support the algorithmic side of my work in scheduling, orchestration and intelligent systems.

---

## `10 // TECHNOLOGY MAP`

<div align="center">

### Languages

<img src="https://skillicons.dev/icons?i=python,java,cpp,c,rust,js,ts,dart&perline=8" />

### Systems / Backend / Infrastructure

<img src="https://skillicons.dev/icons?i=linux,docker,kubernetes,spring,postgres,redis,git,github&perline=8" />

<br/>

<img src="https://img.shields.io/badge/Proxmox-Virtualization-E57000?style=flat-square" />
<img src="https://img.shields.io/badge/XCP--ng-Xen-4B5563?style=flat-square" />
<img src="https://img.shields.io/badge/Ceph-Distributed%20Storage-EF5C55?style=flat-square" />
<img src="https://img.shields.io/badge/Kafka-Event%20Streaming-231F20?style=flat-square&logo=apachekafka" />
<img src="https://img.shields.io/badge/Cassandra-Distributed%20DB-1287B1?style=flat-square&logo=apachecassandra" />
<img src="https://img.shields.io/badge/Prometheus-Observability-E6522C?style=flat-square&logo=prometheus" />
<img src="https://img.shields.io/badge/Open%20vSwitch-SDN-1F2937?style=flat-square" />
<img src="https://img.shields.io/badge/CUDA-GPU%20Computing-76B900?style=flat-square&logo=nvidia&logoColor=white" />

</div>

---

## `11 // HOW MY RESEARCH CONNECTS`

```text
                ┌────────────────────┐
                │  DISTRIBUTED       │
                │  SYSTEMS           │
                └─────────┬──────────┘
                          │
            ┌─────────────┼─────────────┐
            │             │             │
            ▼             ▼             ▼
      Virtualization   Scheduling   Distributed
        / Cloud         / OS        Storage
            │             │             │
            └──────┬──────┴──────┬──────┘
                   │             │
                   ▼             ▼
             Intelligent     Observability
             Orchestration      / Security
                   │
                   ▼
        ┌───────────────────────┐
        │ AI / ML / DL / XAI   │
        └──────────┬────────────┘
                   │
          ┌────────┴──────────┐
          ▼                   ▼
   Radar / Signals      Intelligent Infra
   Classification       & Resource Control
```

The common theme is:

> **build systems that can observe, reason, decide, adapt and scale.**

---

## `12 // SELECTED PUBLIC PROJECTS`

| Project | Main theme |
|---|---|
| [Omega_FusionCore_Proxmox](https://github.com/Savhel/Omega_FusionCore_Proxmox) | Distributed resource management / virtualization |
| [ProjetReseau](https://github.com/Savhel/ProjetReseau) | Event-driven distributed services |
| [simulation_capteurs](https://github.com/Savhel/simulation_capteurs) | Concurrency and scheduling |
| [SimulationDePlanificationDesProcessus](https://github.com/Savhel/SimulationDePlanificationDesProcessus) | OS scheduling |
| [AnalyseDesSentiments](https://github.com/Savhel/AnalyseDesSentiments) | NLP / ML workspace |
| [Traitement-du-signal](https://github.com/Savhel/Traitement-du-signal) | Signal-processing workspace |
| [alanya_app](https://github.com/Savhel/alanya_app) | Secure real-time communication |

---

## `13 // CURRENT DIRECTION`

I am progressively building toward a profile centered on:

**Distributed Systems + Systems Engineering + Intelligent Infrastructure + AI/ML/DL**

with particular interest in:

- autonomous infrastructure;
- intelligent resource orchestration;
- GPU computing;
- distributed scheduling;
- explainable AI;
- signal intelligence;
- adaptive and multi-agent systems.

---

<div align="center">

### `DISTRIBUTED SYSTEMS • SYSTEMS • AI • ML • DL • XAI • INTELLIGENT SYSTEMS`

<sub>Observe. Model. Decide. Act. Adapt.</sub>

</div>
