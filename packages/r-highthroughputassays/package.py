# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighthroughputassays(RPackage):
    """Using Bioconductor with High Throughput Assays

    The workflow illustrates use of the flow cytometry packages to load, transform and visualize the flow data and gate certain populations in the dataset. The workflow loads the `flowCore`, `flowStats` and `flowWorkspace` packages and its dependencies.  It loads the ITN data with 15 samples, each of which includes, in addition to FSC and SSC, 5 fluorescence channels: CD3, CD4, CD8, CD69 and HLADR.
    """

    homepage = "https://www.bioconductor.org/help/workflows/highthroughputassays/"
    bioc = "highthroughputassays"

    version("1.32.0", commit="8ac126e68f7ac61bc5cb022ebd30d3d9cc88a2a0")
    version("1.26.0", commit="ad10d5333d77e4631f6bb2154abc06409a4c43f4")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-flowstats", type=("build", "run"))
    depends_on("r-flowworkspace", type=("build", "run"))
