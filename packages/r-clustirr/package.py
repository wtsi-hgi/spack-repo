# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustirr(RPackage):
    """Clustering of immune receptor repertoires

    ClustIRR is a quantitative method for clustering of immune receptor repertoires (IRRs). The algorithm identifies groups of T or B cell receptors (TCRs or BCRs) with similar specificity by comparing their sequences. ClustIRR uses graphs to visualize the specificity structures of IRRs.
    """

    homepage = "https://github.com/snaketron/ClustIRR"
    bioc = "ClustIRR"

    version("1.6.0", commit="b44e4371ec776952d70d77a324396624053572d2")
    version("1.0.0", commit="739bbfffd95acbb12057c88a984941438ff1145f")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-stringdist", type=("build", "run"))
    depends_on("r-future", type=("build", "run"))
    depends_on("r-future-apply", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-visnetwork", type=("build", "run"))
