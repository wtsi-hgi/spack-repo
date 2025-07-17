# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRontotools(RPackage):
    """R Onto-Tools suite

    Suite of tools for functional analysis.
    """

    bioc = "ROntoTools"

    version("2.36.0", commit="911f5f88580cd31047832935be65d6bb496308f7")
    version("2.30.0", commit="35292096b3058ff4154b8646bbc0c92dc1fed862")

    depends_on("r-graph", type=("build", "run"))
    depends_on("r-boot", type=("build", "run"))
    depends_on("r-keggrest", type=("build", "run"))
    depends_on("r-kegggraph", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
