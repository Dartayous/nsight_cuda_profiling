#include <torch/extension.h>
#include <cuda.h>
#include <cuda_runtime.h>

__global__ void vectorAddKernel(const float* A, const float* B, float* C, int N) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < N) {
        C[idx] = A[idx] + B[idx];
    }
}

void vector_add_cuda(torch::Tensor A, torch::Tensor B, torch::Tensor C, int N) {
    const float* a_ptr = A.data_ptr<float>();
    const float* b_ptr = B.data_ptr<float>();
    float* c_ptr = C.data_ptr<float>();

    int threads = 256;
    int blocks = (N + threads - 1) / threads;

    vectorAddKernel<<<blocks, threads>>>(a_ptr, b_ptr, c_ptr, N);
}


