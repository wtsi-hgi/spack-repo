# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTensorqtl(PythonPackage):
    """GPU-enabled QTL mapper for cis- and trans-QTL mapping."""

    homepage = "https://github.com/broadinstitute/tensorqtl"
    url = "https://github.com/broadinstitute/tensorqtl/archive/refs/tags/v1.0.8.tar.gz"

    license("BSD-3-Clause")

    version("1.0.8", sha256="b773034cba349cd47b95ceab6e47552ee537bce47d6c6203901a8b88e1ed6a1a")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pandas-plink", type=("build", "run"))
    depends_on("py-deprecated@1.2.6:", type=("build", "run"))
    depends_on("py-pgenlib", type=("build", "run"))
    depends_on("py-pyarrow+parquet", type=("build", "run"))
    depends_on("py-qtl", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(self.prefix.bin.tensorqtl)("--help")
