# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyCudf(PythonPackage):
    """Built based on the Apache Arrow columnar memory format,
    cuDF is a GPU DataFrame library for loading, joining,
    aggregating, filtering, and otherwise manipulating data."""

    homepage = "https://rapids.ai"
    url = "https://github.com/rapidsai/cudf/archive/v0.15.0.tar.gz"

    license("Apache-2.0")
    
    version("24.06.00", sha256="3f9bbdb01b06434c14f85ff919336fd25d5ba91b70f842cec4f921328d60d4ca")
    version("24.04.01", sha256="9087bc55195b658edd4a4792525d7d913f564a15bc1fd0a62aa18f0f5be265fc")
    version("24.04.00", sha256="0da50359dbb0bc98da5be9c848838d0e680efc5cc21c7dcd82eb4c1077477bf6")
    version("24.02.02", sha256="75d780f80eae365b215d2a5bcdc906869a19b9c4eb1a90c250fcc384babc6d9c")
    version("24.02.01", sha256="af18030c040b6c55b9f65ca349a45f765739622495b396bf6fa1feb010d0da7f")
    version("24.02.00", sha256="9a61a0e3c7fd5f467027c2429ac8d28a44f0f281738f15e43976a6ced3210f73")
    version("0.15.0", sha256="2570636b72cce4c52f71e36307f51f630e2f9ea94a1abc018d40ce919ba990e4")

    # depends_on("cxx", type="build")  # generated

    build_directory = "python/cudf"

    depends_on("cmake@3.14:", type="build")
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-scikit-build-core", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-numba@0.40.0:", type=("build", "run"))
    depends_on("py-numpy@1.14.4:", type=("build", "run"))
    depends_on("py-pyarrow+cuda+orc+parquet", type=("build", "run"))
    depends_on("py-pandas@0.23.4:", type=("build", "run"))
    depends_on("cuda@10:")
    depends_on("py-cupy+cuda cuda_arch=80", type=("build", "run"))
    depends_on("py-fsspec", type=("build", "run"))

    for v in ("24.06.00", "24.04.01", "24.04.00", "24.02.02", "24.02.01", "24.02.00", "0.15.0"):
        depends_on("libcudf@" + v, when="@"+v)
        depends_on("py-rmm@" + v, when="@"+v, type=("build", "run"))

    @run_before("install")
    def cmake(self):
        cmake = which("cmake")

        build_dir = os.path.join(self.stage.source_path, "cpp", "build")

        with working_dir(build_dir, create=True):
            cmake("..")
