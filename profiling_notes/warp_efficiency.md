# ⚙️ Warp Efficiency: Triton Kernel Profiling Insights

This document captures GPU-level performance results and optimization notes from profiling the `vector_add` kernel using Nsight Compute. The goal is to maximize warp occupancy, memory throughput, and reduce stall cycles for high-throughput inference.

---

## 🚀 Kernel Profile Summary

| Metric                         | Value             |
|-------------------------------|-------------------|
| GPU                           | NVIDIA RTX 4090   |
| Threads per block             | 256               |
| Shared Memory Usage           | None              |
| Registers per thread          | 28                |
| Warp Occupancy                | ~92%              |
| Memory Throughput             | 245 GB/s          |
| SM Efficiency                 | 87.5%             |

---

## 🔍 Bottleneck Breakdown

- **Stall Reason Histogram** from Nsight Compute:
  - Execution Dependency: `12%`
  - Memory Throttle (L2 latency): `8%`
  - Barrier synchronization: `<2%`

- **Warp Divergence**: Minimal — aligned memory loads, no conditional branching across threads

- **Recommendations**:
  - Tune block size for higher warp launch efficiency
  - Explore `__launch_bounds__` to control register pressure
  - Profile with varying batch sizes to isolate SM bottlenecks

---

## 🧪 Vector Add Kernel Notes

```cuda
__global__ void vector_add(const float* a, const float* b, float* c, int N) {
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  if (idx < N)
    c[idx] = a[idx] + b[idx];
}
```
### While simple, this kernel sets the foundation for occupancy and throughput analysis. Future kernels will layer shared memory, fused ops, or warp-level primitives.

---

## 🎬 Profiling Snapshots
### Visual analysis captured in assets/nsight_cuda_profiling.mp4:

- Timeline view: SM load distribution

- Memory latency heatmap

- Warp scheduling breakdown

---

## 📈 Next Optimization Targets
- Introduce shared memory for fused kernels

- Compare occupancy and latency across TensorRT precision modes (FP16 vs FP32)

- Test persistent threads vs cooperative groups for tensor workloads

---


# Warp Efficiency Notes

## 🧮 Kernel: vector_add.cu
- Threads per block: 256
- Global memory access pattern: Coalesced
- Shared memory: Not used
- Registers used: 28
- Occupancy: 92% @ SM

## 🔍 Nsight Compute Findings
- Warp stalls due to execution dependency: 12%
- Memory bottleneck identified at L2 cache under large batch sizes
- Suggested optimization:
  - Restructure input tensors to favor aligned access
  - Consider shared memory usage for larger kernels

## 🧠 Next Steps
- Tune block size for warp scheduling
- Add `__launch_bounds__` to reduce register pressure

