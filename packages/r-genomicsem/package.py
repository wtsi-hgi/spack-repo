# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGenomicsem(RPackage):
    """R-package which allows the user to fit structural equation models based on the summary statistics obtained from genome wide association studies (GWAS)."""

    homepage = "https://github.com/GenomicSEM/GenomicSEM"
    git = "https://github.com/GenomicSEM/GenomicSEM.git"

	version("2024-02-26", commit="526c998484cdfbad66eb3c87bb47ed7658d7e889")

    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-gdata", type=("build", "run"))
    depends_on("r-lavaan", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-splitstackshape", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-iterators", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-mgsub", type=("build", "run"))

    def setup_run_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")
        env.set("OMP_NUM_THREADS", "1")
        env.set("MKL_NUM_THREADS", "1")
        env.set("NUMEXPR_NUM_THREADS", "1")
        env.set("VECLIB_MAXIMUM_THREADS", "1")
