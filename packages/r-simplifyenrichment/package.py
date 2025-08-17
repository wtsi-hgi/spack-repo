# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplifyenrichment(RPackage):
    """Simplify Functional Enrichment Results

    A new clustering algorithm, "binary cut", for clustering similarity matrices of functional terms is implemeted in this package. It also provides functions for visualizing, summarizing and comparing the clusterings.
    """

    homepage = "https://github.com/jokergoo/simplifyEnrichment"
    bioc = "simplifyEnrichment"

    version("2.2.0", commit="04bc7cd9f9685675c67c3c624d538d71964898f9")
    version("1.12.0", commit="32b08ebc0ac96d3099dd9016aae9aac2f2baa351")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-gosemsim", type=("build", "run"))
    depends_on("r-complexheatmap@2.7.4:", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-getoptlong", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-tm", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-slam", type=("build", "run"))
    depends_on("r-clue", type=("build", "run"))
    depends_on("r-proxyc", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-cluster@1.14.2:", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-globaloptions@0.1:", type=("build", "run"))
    depends_on("r-simona", type=("build", "run"))
