# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiscuiteerdata(RPackage):
    """Data Package for Biscuiteer

    Contains default datasets used by the Bioconductor package biscuiteer.
    """

    bioc = "biscuiteerData"

    version("1.22.0", commit="1c146768a24dc68887c13f8876f7c8dcca6c5378")
    version("1.16.0", commit="470718ce1ca01b900394010ae04338ebb782bcde")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
