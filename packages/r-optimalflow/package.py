# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalflow(RPackage):
    """optimalFlow

    Optimal-transport techniques applied to supervised flow cytometry gating.
    """

    bioc = "optimalFlow"

    version("1.20.0", commit="62702a712395c86c3aecb982a5598060128f3206")
    version("1.14.0", commit="9d31fbc718f66cacd664cf174f8b5234586a83cb")

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-optimalflowdata", type=("build", "run"))
    depends_on("r-rlang@0.4:", type=("build", "run"))
    depends_on("r-transport", type=("build", "run"))
    depends_on("r-rfast", type=("build", "run"))
    depends_on("r-robustbase", type=("build", "run"))
    depends_on("r-dbscan", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-flowmeans", type=("build", "run"))
    depends_on("r-rgl", type=("build", "run"))
    depends_on("r-ellipse", type=("build", "run"))
