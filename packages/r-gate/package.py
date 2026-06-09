# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class RGate(RPackage):
    """GATE (Genetic Analysis of Time-to-Event phenotypes) is an R package with Scalable and accurate genome-wide association analysis of censored survival data in large scale biobanks using frailty models."""

    homepage = "https://github.com/weizhou0/GATE"
    url = "https://github.com/weizhou0/GATE/releases/download/v0.42/GATE_0.42.tar.gz"
    git = "https://github.com/weizhou0/GATE.git"

    version("0.45", commit="962f1028120c73e24ec34f29e02eeae3bdc3bfb3")
    version("0.42", sha256="26863cfcf6cdbace88e8b8385343fe831fd9bb86476fabb3dd941405e3f2ad8a")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-spatest", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-skat", type=("build", "run"))
    depends_on("r-metaskat", type=("build", "run"))
    depends_on("cmake", type="build")
    depends_on("xz", type="build")
    depends_on("bgen", type="build")
    depends_on("superlu", type=("build", "link"))
    depends_on("netlib-lapack", type=("build", "link", "run"))

    def patch(self):
        filter_file("# If installing within conda build ignore configure", "exit 0;", "configure", string=True)

    def setup_build_environment(self, env):
        env.set("LD_LIBRARY_PATH", self.spec["netlib-lapack"].prefix.lib)

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["netlib-lapack"].prefix.lib)
