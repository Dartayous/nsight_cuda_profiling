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
