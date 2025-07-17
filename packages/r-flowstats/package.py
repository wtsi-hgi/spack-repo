# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowstats(RPackage):
    """Statistical methods for the analysis of flow cytometry data

    Methods and functionality to analyse flow data that is beyond the basic infrastructure provided by the flowCore package.
    """

    homepage = "http://www.github.com/RGLab/flowStats"
    bioc = "flowStats"

    version("4.20.0", commit="d287cda1dceed5148c43d1b8724e4175b03cd36e")
    version("4.14.1", commit="3dc62dab63308ff20d82429d711593355da6d84b")

    depends_on("r@3.0.2:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-flowcore@1.99.6:", type=("build", "run"))
    depends_on("r-flowworkspace", type=("build", "run"))
    depends_on("r-ncdfflow@2.19.5:", type=("build", "run"))
    depends_on("r-flowviz", type=("build", "run"))
    depends_on("r-fda@2.2.6:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-ks", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rrcov", type=("build", "run"))
    depends_on("r-corpcor", type=("build", "run"))
    depends_on("r-mnormt", type=("build", "run"))
    depends_on("r-clue", type=("build", "run"))
