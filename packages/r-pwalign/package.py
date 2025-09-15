# Copyright 2013-2025 Lawrence Livermore National Security, LLC
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwalign(RPackage):
    """Optimal pairwise alignment interfaces and distances.

    Provides pairwiseAlignment() and stringDist() utilities via Biostrings.
    """

    # Source from Bioconductor (CRAN archive URL is 404 now)
    bioc = "pwalign"

    # Bioconductor release branches and commits
    version("1.4.0", commit="9842dde8e5eb474c5d04dc4f1061a9cef758c744")  # RELEASE_3_21
    version("1.2.0", commit="9d0fa610f6e1104adf60ccfbfc5982703418a258")  # RELEASE_3_20
    version("1.0.0", commit="d161c8d760cef88c43fc206703be27d8a93300fa")  # RELEASE_3_19

    # R version guards per Bioconductor series
    depends_on("r@4.4:", type=("build", "run"), when="@1.4.0:")
    depends_on("r@4.3:", type=("build", "run"), when="@1.2.0")
    depends_on("r@4.3:", type=("build", "run"), when="@1.0.0")
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    # Biostrings requirement as per DESCRIPTION across all releases
    depends_on("r-biostrings@2.71.5:", type=("build", "run"))
