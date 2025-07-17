# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowtrans(RPackage):
    """Parameter Optimization for Flow Cytometry Data Transformation

    Profile maximum likelihood estimation of parameters for flow cytometry data transformations.
    """

    bioc = "flowTrans"

    version("1.60.0", commit="0a9dedb16e582d27a1c5e74322f49be137d86048")
    version("1.54.0", commit="364b62432f2668d55ce9206b838cbd33d3be77c2")

    depends_on("r@2.11:", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-flowviz", type=("build", "run"))
    depends_on("r-flowclust", type=("build", "run"))
