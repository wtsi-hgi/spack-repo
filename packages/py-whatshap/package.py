# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyWhatshap(PythonPackage):
    """Phases genomic variants using DNA sequencing reads."""

    homepage = "https://github.com/whatshap/whatshap"
    pypi = "whatshap/whatshap-2.8.tar.gz"

    license("MIT")

    version("2.8", sha256="073ee7946d563e0125dbce58d9fc86a7a3fae377f27859dacb398309374b2cbe")
    version("2.7", sha256="9ac6340dbd56905a1117f12c723fb2bfe52d3ecc78b9be137f58b4ed227300c7")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77.0.3:", type="build")
    depends_on("py-setuptools-scm+toml", type="build")
    depends_on("py-cython@3.0.11:3.0", type="build")

    depends_on("py-pysam@0.18.0:", type=("build", "run"))
    depends_on("py-pyfaidx@0.5.5.2:", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-biopython@1.73:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-xopen@1.2.0:", type=("build", "run"))
    depends_on("py-pulp@2:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            whatshap = Executable(self.prefix.bin.whatshap)
            whatshap("--help")
