# Copyright 2013-2025 Lawrence Livermore National Security, LLC
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwalign(RPackage):
    """Optimal pairwise alignment interfaces and distances.

    Provides pairwiseAlignment() and stringDist() utilities via Biostrings.
    """

    # Source from Bioconductor (CRAN archive URL is 404 now)
    bioc = "pwalign"

    # Bioconductor release tarball and commit for 3.21
    version("1.4.0", commit="9842dde8e5eb474c5d04dc4f1061a9cef758c744")

    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biostrings@2.71.5:", type=("build", "run"))
