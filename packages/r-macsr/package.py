# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacsr(RPackage):
    """MACS: Model-based Analysis for ChIP-Seq

    The Model-based Analysis of ChIP-Seq (MACS) is a widely used toolkit for identifying transcript factor binding sites. This package is an R wrapper of the lastest MACS3.
    """

    bioc = "MACSr"

    version("1.16.0", commit="309d4f6ec70270334fd721b63917e0daf7485b95")
    version("1.10.0", commit="640c4c3ea3076d184b97516a678203020c858cd6")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-basilisk", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
