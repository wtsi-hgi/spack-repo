# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowdensity(RPackage):
    """Sequential Flow Cytometry Data Gating

    This package provides tools for automated sequential gating analogous to the manual gating strategy based on the density of the data.
    """

    bioc = "flowDensity"

    version("1.42.0", commit="8f7ebcf876253f35b7713883aa9d62c62fe4bb28")
    version("1.36.1", commit="e159b7d89c3e792830dd98fd9d8c928463d5febd")

    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-flowviz@1.42:", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-polyclip", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("libxml2", type=("build", "link", "run"))
