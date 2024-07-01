# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.boost import Boost


class Libcudf(CMakePackage):
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
    version("23.12.01", sha256="ab55e0e483c4f01bf63ebe6a6c649385e0859851f0a888776366feccb738b9bf")
    version("23.12.00", sha256="30d8e8453f04a2c88cad8947d16a4616671d96c7d25dd49b2eb65773ee3eba97")
    version("23.10.02", sha256="039de4cc94a0d8e5fd276bd0847da458d83b3dc46f25faffe7411261ed51fdfd")
    version("0.15.0", sha256="2570636b72cce4c52f71e36307f51f630e2f9ea94a1abc018d40ce919ba990e4")

    depends_on("cmake@3.14:", type="build")
    depends_on("cuda@10.0:")

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants)
    depends_on("arrow+cuda+orc+parquet")
    depends_on("librmm")
    depends_on("dlpack")

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        args = []

        # args.append('-DGPU_ARCHES')
        args.append("-DUSE_NVTX=ON")
        args.append("-DBUILD_BENCHMARKS=OFF")
        args.append("-DDISABLE_DEPRICATION_WARNING=ON")
        args.append("-DPER_THREAD_DEFAULT_STREAM=OFF")
        return args
