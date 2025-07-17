# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFedup(RPackage):
    """Fisher's Test for Enrichment and Depletion of User-Defined Pathways

    An R package that tests for enrichment and depletion of user-defined pathways using a Fisher's exact test. The method is designed for versatile pathway annotation formats (eg. gmt, txt, xlsx) to allow the user to run pathway analysis on custom annotations. This package is also integrated with Cytoscape to provide network-based pathway visualization that enhances the interpretability of the results.
    """

    homepage = "https://github.com/rosscm/fedup"
    bioc = "fedup"

    version("1.16.0", commit="e2ad7b650137c69ed96e124e99623fddd28492c7")
    version("1.10.0", commit="3fd48c2be6e04cb6410cbac9f607c15dcd2390de")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-openxlsx", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggthemes", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rcy3", type=("build", "run"))
