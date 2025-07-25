import torch
import vector_add
import time

size = 100_000_000  # Large tensor for meaningful timing
a = torch.rand(size, device='cuda')
b = torch.rand(size, device='cuda')
out = torch.empty(size, device='cuda')

# Warm up CUDA context
for _ in range(5):
    vector_add.vector_add(a, b, out, size)
    _ = a + b

# Benchmark Custom CUDA Kernel
torch.cuda.synchronize()
start = time.time()
vector_add.vector_add(a, b, out, size)
torch.cuda.synchronize()
custom_duration = time.time() - start

# Benchmark PyTorch Native
torch.cuda.synchronize()
start = time.time()
c = a + b
torch.cuda.synchronize()
native_duration = time.time() - start

# Results
print(f"🧠 Custom kernel time: {custom_duration * 1000:.3f} ms")
print(f"🚀 PyTorch native time: {native_duration * 1000:.3f} ms")

speedup = native_duration / custom_duration if custom_duration else float('inf')
print(f"⚖️ Speedup factor: {speedup:.2f}x")
