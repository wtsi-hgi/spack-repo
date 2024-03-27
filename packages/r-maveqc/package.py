# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaveqc(RPackage):
    """A R package of quality control on SGE data."""

    homepage = "https://github.com/wtsi-hgi/MAVEQC"
    git = "https://github.com/wtsi-hgi/MAVEQC"

    version("0.2.5", tag="0.2.5")
    version("0.2.4", tag="0.2.4")
    version("0.2.3", tag="0.2.3")
    version("0.2.2", tag="0.2.2")

    depends_on("pandoc", type=("build", "run"))

    depends_on("r+X@4.3.2", type=("build", "run"))
    depends_on("r-configr", type=("build", "run"))
    depends_on("r-vroom@1.6.3:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ckmeans-1d-dp", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-plotly@4.10.2:", type=("build", "run"))
    depends_on("r-ggcorrplot", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-deseq2@1.38.3:", type=("build", "run"))
    depends_on("r-degreport", type=("build", "run"))
    depends_on("r-apeglm", type=("build", "run"))
    depends_on("r-see", type=("build", "run"))
    depends_on("r-ggbeeswarm@0.7.2:", type=("build", "run"))
    depends_on("r-reactable", type=("build", "run"))
    depends_on("r-htmltools@0.5.5:", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-sparkline", type=("build", "run"))
    depends_on("r-dendextend", type=("build", "run"))
