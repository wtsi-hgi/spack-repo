# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQplexdata(RPackage):
    """Data accompanying qPLEXanalyzer package

    qPLEX-RIME and Full proteome TMT mass spectrometry datasets.
    """

    bioc = "qPLEXdata"

    version("1.26.0", commit="d03cb23c5a7dd56aa6f95a45f90241bc78fcd2a5")
    version("1.20.0", commit="a5d56e2e3bf3f45daa042023e84a7dac0e4c22fd")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-qplexanalyzer", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-msnbase", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
