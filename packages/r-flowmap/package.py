# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowmap(RPackage):
    """Mapping cell populations in flow cytometry data for cross-sample comparisons using the Friedman-Rafsky Test

    flowMap quantifies the similarity of cell populations across multiple flow cytometry samples using a nonparametric multivariate statistical test. The method is able to map cell populations of different size, shape, and proportion across multiple flow cytometry samples. The algorithm can be incorporate in any flow cytometry work flow that requires accurat quantification of similarity between cell populations.
    """

    bioc = "flowMap"

    version("1.40.0", commit="a8a898258d0f61064b2f1e0e443e6b4734209171")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r-ade4@1.5.2:", type=("build", "run"))
    depends_on("r-doparallel@1.0.3:", type=("build", "run"))
    depends_on("r-abind@1.4:", type=("build", "run"))
    depends_on("r-reshape2@1.2.2:", type=("build", "run"))
    depends_on("r-scales@0.2.3:", type=("build", "run"))
    depends_on("r-matrix@1.1.4:", type=("build", "run"))
