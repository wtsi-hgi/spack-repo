# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCqn(RPackage):
    """Conditional quantile normalization

    A normalization tool for RNA-Seq data, implementing the conditional quantile normalization method.
    """

    bioc = "cqn"

    version("1.54.0", commit="8c4a46a4b6e55fc646cfb51174b745d59aa7f564")
    version("1.48.0", commit="0d28c4372fcc7b25c3cc7cc6596001273bee9735")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-nor1mix", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))
    depends_on("r-quantreg", type=("build", "run"))
