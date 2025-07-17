# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirintegrator(RPackage):
    """Integrating microRNA expression into signaling pathways for pathway analysis

    Tools for augmenting signaling pathways to perform pathway analysis of microRNA and mRNA expression levels.
    """

    homepage = "http://datad.github.io/mirIntegrator/"
    bioc = "mirIntegrator"

    version("1.38.0", commit="026c65f1162f5d33919ecfb1ab0f4f96b6141453")
    version("1.32.0", commit="236a2ecb6218e81cce78af85cbc39aec5c675870")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rontotools", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
