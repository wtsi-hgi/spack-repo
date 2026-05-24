import os

from spack.package import *


class LightGbm(CMakePackage):
    """LightGBM is a gradient boosting framework that uses tree based
    learning algorithms."""

    homepage = "https://github.com/microsoft/LightGBM"
    url = "https://github.com/lightgbm-org/LightGBM/releases/download/v4.6.0/lightgbm-4.6.0.tar.gz"

    license("MIT")

    version("4.6.0", sha256="cb1c59720eb569389c0ba74d14f52351b573af489f230032a1c9f314f8bab7fe")
    version("4.5.0", sha256="e1cd7baf0318d4e308a26575a63a4635f08df866ad3622a9d8e3d71d9637a1ba")
    version("4.4.0", sha256="9e8a7640911481134e60987d5d1e1cd157f430c3b4b38de8d36fc55c302bc299")

    depends_on("cmake@3.18:", type="build")
    depends_on("llvm-openmp", when="%apple-clang")
    depends_on("hwloc", when="%clang")

    def cmake_args(self):
        args = [
            self.define("BUILD_CLI", False),
            self.define("BUILD_STATIC_LIB", False),
            self.define("INSTALL_HEADERS", True),
            self.define("USE_MPI", False),
            self.define("USE_GPU", False),
            self.define("USE_CUDA", False),
            self.define("USE_ROCM", False),
            self.define("USE_SWIG", False),
            self.define("USE_OPENMP", True),
        ]

        if self.spec.satisfies("%apple-clang"):
            openmp_flags = "-fopenmp=libomp"
            args.extend(
                [
                    self.define("OpenMP_C_FLAGS", openmp_flags),
                    self.define("OpenMP_C_LIB_NAMES", "libomp"),
                    self.define("OpenMP_CXX_FLAGS", openmp_flags),
                    self.define("OpenMP_CXX_LIB_NAMES", "libomp"),
                ]
            )
            clang_root = os.path.dirname(os.path.dirname(self.compiler.cc))
            args.append(
                self.define(
                    "OpenMP_libomp_LIBRARY",
                    find_libraries("libomp", root=clang_root, shared=True, recursive=True),
                )
            )

        return args

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            assert find_libraries("lib_lightgbm", root=self.prefix, shared=True, recursive=True)
