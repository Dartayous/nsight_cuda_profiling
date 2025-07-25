import torch
import vector_add

# Setup test data
size = 1024
a = torch.rand(size, device='cuda')
b = torch.rand(size, device='cuda')
out = torch.empty(size, device='cuda')

# Call your custom CUDA op
vector_add.vector_add(a, b, out, size)

# Verify correctness
if torch.allclose(out, a + b):
    print("✅ Success: CUDA kernel computed vector addition correctly!")
else:
    print("❌ Mismatch: Check kernel logic.")

import os
print("✅ Script completed. PID:", os.getpid())
import sys
sys.exit(0)
