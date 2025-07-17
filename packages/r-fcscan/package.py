# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcscan(RPackage):
    """fcScan for detecting clusters of coordinates with user defined options

    This package is used to detect combination of genomic coordinates falling within a user defined window size along with user defined overlap between identified neighboring clusters. It can be used for genomic data where the clusters are built on a specific chromosome or specific strand. Clustering can be performed with a "greedy" option allowing thus the presence of additional sites within the allowed window size.
    """

    bioc = "fcScan"

    version("1.22.0", commit="920191b37f5df81307fb75440c10c01069e90cdd")
    version("1.16.0", commit="019508543d3295981f1a4e57effd1029341e456d")

    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
