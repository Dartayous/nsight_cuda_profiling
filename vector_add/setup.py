from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension

setup(
    name="vector_add",
    ext_modules=[
        CUDAExtension(
            name="vector_add",
            sources=["vector_add.cpp", "vector_add_kernel.cu"]
        )
    ],
    cmdclass={"build_ext": BuildExtension}
)
