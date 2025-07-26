# 🎨 Infographic Guide: GPU Kernel Profiling Pipeline (Cyberpunk Neon Edition)

*Visual storyboard inspired by Dartayous' custom CUDA kernel journey into Nsight Compute*

---

## 🟣 Title Banner

### 🔥 “Unlocking GPU Telemetry Through Nsight Compute”
*Cyberpunk-styled title bar with glowing edge, neon circuit traces, and GPU icons*

---

## 🧠 Infographic Flow Structure

Each step corresponds to a visual panel or lane in the infographic.

| # | Step Label | Description | Suggested Icon |
|---|------------|-------------|----------------|
| 1️⃣ | **Kernel Build** | Compiled `.cu` and `.cpp` into PyTorch extension | 🛠️ Chip + wrench |
| 2️⃣ | **Python Script Test** | Launched `test_vector_add.py` to verify output | 🧪 Flask + Python badge |
| 3️⃣ | **Microbenchmark** | Measured kernel time vs PyTorch native addition | ⏱️ Stopwatch |
| 4️⃣ | **Venv Launcher** | Used `.bat` script to activate `torch311` env | 💼 Terminal window |
| 5️⃣ | **Nsight Launch Config** | Ran via `cmd.exe /C run_vector_add.bat --target-processes all` | 🎯 Radar scope |
| 6️⃣ | **Unlock GPU Counters** | Registry patch to enable `PerfCounterAccess` | 🔓 Neon keyhole |
| 7️⃣ | **Nsight Telemetry Dashboard** | Full warp execution metrics + memory throughput | 📊 Warp grid graph |

---

## 🎤 Mic Drop Panel

> “I profiled my own PyTorch CUDA extension in Nsight Compute, resolved permission-level access to counters, mapped register usage and warp efficiency, and benchmarked my kernel against native ops — then made it faster.”

🟪 Glowing box with animated GPU background + Tech Noir font

---

## 👨‍💻 Author Footer Panel

**Dartayous**  
*AI Engineer & Visual Effects Technologist*  
🧠 Cyberpunk signature bar with “Reviewed by Nsight” badge (stylized hex icon)

---

This guide highlights key performance insights from our AI pipeline, including:

## 🚀 Inference Throughput
- Model: `fastapi_model` via Triton
- Batch size: 4
- Concurrency sweep: 1–8
- Peak throughput: **2,150 infer/sec**
- Avg latency: **13.4 ms**

## 🔥 CUDA Warp Efficiency
- Kernel: `vector_add`
- Nsight Compute: Warp Occupancy ~ 92%
- Memory Throughput: 245 GB/s
- Recommendations: Align memory loads and minimize divergent warps

## 🎥 .png Breakdown
Visual asset: `nsight_cuda_profiling-2-nsight_cuda_profiling.png` (in `/assets`) shows step-by-step warp profiling and timeline view from Nsight Compute.

## 📁 Assets Directory
Use assets in README, LinkedIn, or personal portfolio PDF.

---


## 🎨 Design Notes for Visual Composition

- **Palette**: Neon magenta + electric cyan on dark gradient base (black→purple)  
- **Font**: Times New Roman (body), Tech-style sans serif (headers if desired)  
- **Lines**: Glowing circuit paths connecting each step  
- **Background**: GPU schematic overlay or data grid with motion lines  
- **Layout Format**: Horizontal lanes or vertical timeline — choose based on screen/print intent

---

## 📥 Optional Assets (for designer use)

- 🖼️ Include screenshots of `Nsight Compute` dashboards (warp metrics, register usage)  
- 📁 Include code snippets from `vector_add.cpp` and `vector_add_kernel.cu`  
- 🎞️ Stylize performance graph comparing kernel speed vs native ops

---

## 🧭 Suggested Export Formats

- PNG (for LinkedIn, portfolio site)  
- SVG or PDF (for print-ready showcase or résumé inserts)  
- GitHub README.md embed (as hero graphic)

---

### 🏁 Closing Tagline

**Performance Engineered. Storytelling Delivered.**  
*By Dartayous, where GPU kernels meet cinematic impact.*

---

