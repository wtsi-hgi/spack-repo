# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RDemultiplex2(RPackage):
    """deMULTIplex2 is a mechanism-guided classification algorithm for multiplexed scRNA-seq data that successfully recovers many more cells across a spectrum of challenging datasets compared to existing methods. deMULTIplex2 is built on a statistical model of tag read counts derived from the physical mechanism of tag cross-contamination. Using generalized linear models and expectation-maximization, deMULTIplex2 probabilistically infers the sample identity of each cell and classifies singlets with high accuracy."""

    homepage = "https://github.com/Gartner-Lab/deMULTIplex2"
    url = "https://github.com/Gartner-Lab/deMULTIplex2/archive/refs/tags/v1.0.1.tar.gz"

    version("1.0.1", sha256="ff94d3158e403748e7247bc8ff6766de005374ea83c6554e3475d0a8fd0650fb")
    version("1.0.0", sha256="9672a3af0e7974acc464d5e82bf3d259e187f00f96f6f26d95e9789e5c2a3a43")

    depends_on("r-mass", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-shortread", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggextra", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-stringdist", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
    depends_on("r-uwot", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
