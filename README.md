#  Nsight Compute Profiling: Custom PyTorch CUDA Kernel

![Badge](https://img.shields.io/badge/Reviewed_by-Nsight_Compute-00FFFF?style=flat-square&logo=nvidia)

##  Author: Dartayous Hunter 
*AI Engineer & Visual Effects Technologist*  
*Blending low-level performance with high-level visual storytelling*

“I profiled my own PyTorch CUDA extension in Nsight Compute, resolved permission-level access to counters, mapped register usage and warp efficiency, and benchmarked my kernel against native ops — then made it faster.”
---

###  Overview

This project benchmarks and profiles a custom CUDA kernel wrapped as a PyTorch extension, using NVIDIA Nsight Compute for full GPU telemetry access. From kernel build to warp execution analysis, this pipeline unlocks performance visibility and measurable speedups — proving that GPU engineering is as cinematic as it is scientific.


---

###  Project Structure

```bash
nsight_cuda_profiling/
├── vector_add/                # PyTorch CUDA extension
│   ├── vector_add.cpp
│   ├── vector_add_kernel.cu
│   ├── setup.py
│   └── test_vector_add.py
├── run_vector_add.bat         # Launch script (activates venv)
├── profiling_notes/           # Nsight report interpretation
│   └── warp_efficiency.md
├── infographic_guide.md       # Annotated storyboard flow
└── README.md                  # You’re reading it!
```

###  Tech Stack
- Python 3.11 (torch311 virtual env)

- PyTorch (CUDA 12.1 enabled)

- Nsight Compute GUI

- C++ / CUDA kernel (.cu + .cpp)

- Bat file launcher for controlled execution

- Registry patch for counter access (PerfCounterAccess)

- Windows OS


###  Performance Highlights
-  Custom kernel: vector_add(a, b, out, size)

-  Validated with torch.allclose() in Python

-  Speedup: 4.4x faster than PyTorch native ops

-  Nsight analysis: warp execution, register pressure, memory stalls



#  Steps to Reproduce
1.) Compile extension:
```bash
python setup.py install

```

2.) Benchmark kernel:
```bash
python test_vector_add.py

```

3.) Launch in Nsight Compute:
- Executable: C:\Windows\System32\cmd.exe

- Arguments: /C run_vector_add.bat --target-processes all

- Output: vector_add_report.ncu-rep


4.) Enable GPU performance counters: Run as Admin:
```bash
reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global\PerfCounterAccess" /v Enable /t REG_DWORD /d 1 /f


```

5.) Reboot and relaunch Nsight.


---

###  Repository Hygiene

This project includes a `.gitignore` configured for Python, CUDA profiling, and modular virtual environments to keep the repository clean and focused:

###  Python Environment and Build Artifacts
__pycache__/
*.py[cod]
*.egg
*.egg-info/
dist/
build/
*.spec

###  Jupyter Notebook Checkpoints
.ipynb_checkpoints/
*-checkpoint.*

###  Nsight Compute/CUDA Profiler Files
*.ncu-rep
*.ncu-proj

###  System and IDE Artifacts
*.exe
*.dll
*.obj
*.log
*.tmp
.vscode/
*.DS_Store

###  Virtual Environments (Global or Local)
Venv/
venv/
ENV/
env/
.venv/

###  Python Egg Packaging Metadata
vector_add.egg-info/

---

### GitHub Push Workflow
```bash
# Initialize Git if you haven’t yet
git init

# Stage your project files
git add .

# Commit your changes with a descriptive message
git commit -m "Initial commit — project setup and .gitignore configured"

# Link to your GitHub repository (replace with your repo URL)
git remote add origin https://github.com/your-username/your-repo.git

# Push to main branch
git push -u origin main


```
###  Visualization Assets
See infographic_guide.md for a breakdown of the visual storyboard. Includes: Build → Benchmark → Launch → Unlock → Profile

## ✨ About the Author
Dartayous is a seasoned VFX compositing artist turned AI engineer with a passion for GPU performance and storytelling. This repository reflects a crossover journey: where cinematic precision meets CUDA kernel mastery.
