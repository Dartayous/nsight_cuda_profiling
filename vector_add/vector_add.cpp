#include <torch/extension.h>

void vector_add_cuda(torch::Tensor A, torch::Tensor B, torch::Tensor C, int N);

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("vector_add", &vector_add_cuda, "Vector add (CUDA)");
}
