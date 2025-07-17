# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetboost(RPackage):
    """Network Analysis Supported by Boosting

    Boosting supported network analysis for high-dimensional omics applications. This package comes bundled with the MC-UPGMA clustering package by Yaniv Loewenstein.
    """

    homepage = "https://bioconductor.org/packages/release/bioc/html/netboost.html"
    bioc = "netboost"

    version("2.16.0", commit="5f3d92417089de27dc0afb2a871b8756561ca5cd")
    version("2.10.0", commit="567817544c99a9564ea75aeeb458768a45b049dc")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-dynamictreecut", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-impute", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("perl", type=("build", "link", "run"))
    depends_on("gzip", type=("build", "link", "run"))
