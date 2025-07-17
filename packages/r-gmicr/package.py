# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmicr(RPackage):
    """Combines WGCNA and xCell readouts with bayesian network learrning to generate a Gene-Module Immune-Cell network (GMIC)

    This package uses bayesian network learning to detect relationships between Gene Modules detected by WGCNA and immune cell signatures defined by xCell. It is a hypothesis generating tool.
    """

    bioc = "GmicR"

    version("1.22.0", commit="a0ecac94125f59f362a9c3bbd07c31a30bb79142")
    version("1.16.0", commit="def961ebdd0b4695f41463a830eea7a36fcd49d1")

    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-bnlearn", type=("build", "run"))
    depends_on("r-category", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-grbase", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-grain", type=("build", "run"))
    depends_on("r-gostats", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-org-mm-eg-db", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
