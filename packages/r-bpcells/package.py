# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpcells(RPackage):
    """Scaling Single Cell Analysis to Millions of Cells.

    Efficient operations for single cell ATAC-seq fragments and
    RNA counts matrices. Interoperable with standard file formats, and introduces
    efficient bit-packed formats that allow large storage savings and increased
    read speeds."""

    git = "https://github.com/bnprks/BPCells"

	version("0.1.0", tag="v0.1.0")

    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-scattermore", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-hexbin", type=("build", "run"))
    depends_on("hdf5", type=("build", "run"))
    depends_on("openmpi", type=("build", "run", "link"))

    def setup_build_environment(self, env):
        env.set("LD_LIBRARY_PATH", join_path(self.spec["hdf5"].prefix, "lib"))

    def setup_dependent_build_environment(self, env, spec):
        env.prepend_path("LD_LIBRARY_PATH", join_path(spec["hdf5"].prefix, "lib"))

    def setup_dependent_run_environment(self, env, spec):
        env.prepend_path("LD_LIBRARY_PATH", join_path(spec["hdf5"].prefix, "lib"))
