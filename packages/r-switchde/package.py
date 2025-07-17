# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwitchde(RPackage):
    """Switch-like differential expression across single-cell trajectories

    Inference and detection of switch-like differential expression across single-cell RNA-seq trajectories.
    """

    homepage = "https://github.com/kieranrcampbell/switchde"
    bioc = "switchde"

    version("1.34.0", commit="351dacea10abc18ad50c74bc4a01d26fd35bf283")
    version("1.28.0", commit="61db86f5c6637db1640b9bc793321600a31cad25")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
