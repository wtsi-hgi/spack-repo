# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneclassifiers(RPackage):
    """Application of gene classifiers

    This packages aims for easy accessible application of classifiers which have been published in literature using an ExpressionSet as input.
    """

    homepage = "https://doi.org/doi:10.18129/B9.bioc.geneClassifiers"
    bioc = "geneClassifiers"

    version("1.32.0", commit="28dc73df5e84b7447d767691010d10de3b6011cb")
    version("1.26.0", commit="b3a557d748a64b9927f4ce547c15c7d887012cce")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
