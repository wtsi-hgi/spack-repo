# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbqn(RPackage):
    """Mean/Median-balanced quantile normalization

    Modified quantile normalization for omics or other matrix-like data distorted in location and scale.
    """

    homepage = "https://github.com/arianeschad/mbqn"
    bioc = "MBQN"

    version("2.20.0", commit="e37dde65b375f36d8916354715659e52e4114bda")
    version("2.14.0", commit="33f251535c64f9e58aac9e9e7ec330bb5ffcc284")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-limma@3.30.13:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.10:", type=("build", "run"))
    depends_on("r-preprocesscore@1.36:", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-rappdirs", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-paireddata", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
