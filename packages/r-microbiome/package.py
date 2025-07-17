# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiome(RPackage):
    """Microbiome Analytics

    Utilities for microbiome analysis.
    """

    homepage = "http://microbiome.github.io/microbiome"
    bioc = "microbiome"

    version("1.30.0", commit="1d04e67141f0a7f53070e64c693aa8cf78f9c47a")
    version("1.24.0", commit="4e08c43b4872f8fa53bf052f008c57ee8bd869ca")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-phyloseq", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-compositions", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
